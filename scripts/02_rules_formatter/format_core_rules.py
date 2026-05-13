import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import pdfplumber


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = PROJECT_ROOT / "data" / "raw" / "core-rules-20260330.pdf"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "data" / "processed" / "rules"

RULE_START_RE = re.compile(r"^(?P<id>\d{3}(?:\.(?:\d+|[a-z]))*)\.\s*(?P<text>.*)$")
WHITESPACE_RE = re.compile(r"\s+")


@dataclass
class Rule:
    id: str
    text: str
    page_start: int
    page_end: int
    parent_id: str | None
    section_id: str
    section_title: str | None
    source: str


def clean_line(line: str) -> str:
    line = line.strip()
    line = WHITESPACE_RE.sub(" ", line)
    return line


def should_skip_line(line: str) -> bool:
    return line in {"Riftbound Core Rules"} or line.startswith("Last Updated:")


def parent_rule_id(rule_id: str) -> str | None:
    parts = rule_id.split(".")
    if len(parts) == 1:
        return None
    return ".".join(parts[:-1])


def is_heading_like(rule: Rule) -> bool:
    if "." in rule.id:
        return False
    if len(rule.text) > 90:
        return False
    sentence_endings = (".", "!", "?", ".)", '."')
    return not rule.text.endswith(sentence_endings)


def extract_page_lines(pdf_path: Path) -> list[tuple[int, str]]:
    page_lines: list[tuple[int, str]] = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_index, page in enumerate(pdf.pages, start=1):
            text = page.extract_text(x_tolerance=1, y_tolerance=3) or ""
            for raw_line in text.splitlines():
                line = clean_line(raw_line)
                if not line or should_skip_line(line):
                    continue
                page_lines.append((page_index, line))
    return page_lines


def parse_rules(page_lines: Iterable[tuple[int, str]], source_name: str) -> list[Rule]:
    rules: list[Rule] = []
    current_id: str | None = None
    current_text_parts: list[str] = []
    current_page_start: int | None = None
    current_page_end: int | None = None

    def flush_current() -> None:
        nonlocal current_id, current_text_parts, current_page_start, current_page_end
        if current_id is None or current_page_start is None or current_page_end is None:
            return
        text = clean_line(" ".join(current_text_parts))
        rules.append(
            Rule(
                id=current_id,
                text=text,
                page_start=current_page_start,
                page_end=current_page_end,
                parent_id=parent_rule_id(current_id),
                section_id=current_id.split(".")[0],
                section_title=None,
                source=source_name,
            )
        )
        current_id = None
        current_text_parts = []
        current_page_start = None
        current_page_end = None

    for page_number, line in page_lines:
        match = RULE_START_RE.match(line)
        if match:
            flush_current()
            current_id = match.group("id")
            current_text_parts = [match.group("text")]
            current_page_start = page_number
            current_page_end = page_number
            continue

        if current_id is not None:
            current_text_parts.append(line)
            current_page_end = page_number

    flush_current()
    attach_section_titles(rules)
    return rules


def attach_section_titles(rules: list[Rule]) -> None:
    section_titles: dict[str, str] = {}
    for rule in rules:
        if is_heading_like(rule):
            section_titles[rule.id] = rule.text

    active_title_by_section: dict[str, str] = {}
    for rule in rules:
        if rule.id in section_titles:
            active_title_by_section[rule.section_id] = section_titles[rule.id]
        rule.section_title = active_title_by_section.get(rule.section_id)


def rules_to_markdown(rules: list[Rule], title: str, source_name: str) -> str:
    lines = [
        f"# {title}",
        "",
        f"Source: `{source_name}`",
        "",
    ]

    for rule in rules:
        escaped_text = rule.text.replace("\n", " ").strip()
        if is_heading_like(rule):
            lines.extend([f"## {rule.id}. {escaped_text}", ""])
            continue

        lines.extend(
            [
                f'<a id="rule-{rule.id.replace(".", "-")}"></a>',
                f"**{rule.id}.** {escaped_text}",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def make_chunks(rules: list[Rule], source_name: str, max_chars: int) -> list[dict]:
    chunks: list[dict] = []
    active_rules: list[Rule] = []
    active_text_parts: list[str] = []
    active_len = 0

    def flush() -> None:
        nonlocal active_rules, active_text_parts, active_len
        if not active_rules:
            return
        first_id = active_rules[0].id
        last_id = active_rules[-1].id
        chunks.append(
            {
                "chunk_id": f"core-rules:{first_id}-{last_id}",
                "source": source_name,
                "rule_ids": [rule.id for rule in active_rules],
                "page_start": min(rule.page_start for rule in active_rules),
                "page_end": max(rule.page_end for rule in active_rules),
                "section_ids": sorted({rule.section_id for rule in active_rules}),
                "section_titles": sorted(
                    {rule.section_title for rule in active_rules if rule.section_title}
                ),
                "text": "\n".join(active_text_parts),
            }
        )
        active_rules = []
        active_text_parts = []
        active_len = 0

    for rule in rules:
        rule_text = f"{rule.id}. {rule.text}"
        if active_rules and active_len + len(rule_text) + 1 > max_chars:
            flush()
        active_rules.append(rule)
        active_text_parts.append(rule_text)
        active_len += len(rule_text) + 1

    flush()
    return chunks


def write_json(path: Path, payload: object) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_jsonl(path: Path, rows: Iterable[dict]) -> None:
    with path.open("w", encoding="utf-8") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")


def format_rules(pdf_path: Path, output_dir: Path, max_chunk_chars: int) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    page_lines = extract_page_lines(pdf_path)
    rules = parse_rules(page_lines, pdf_path.name)
    chunks = make_chunks(rules, pdf_path.name, max_chunk_chars)

    md_path = output_dir / "core-rules.md"
    json_path = output_dir / "core-rules.json"
    jsonl_path = output_dir / "core-rules.chunks.jsonl"

    md_path.write_text(
        rules_to_markdown(rules, "Riftbound Core Rules", pdf_path.name),
        encoding="utf-8",
    )
    write_json(
        json_path,
        {
            "source": pdf_path.name,
            "rule_count": len(rules),
            "rules": [asdict(rule) for rule in rules],
        },
    )
    write_jsonl(jsonl_path, chunks)

    return {
        "markdown": md_path,
        "json": json_path,
        "jsonl": jsonl_path,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert the Riftbound core rules PDF into Markdown, JSON, and JSONL chunks."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Input PDF path.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory where processed rule files will be written.",
    )
    parser.add_argument(
        "--max-chunk-chars",
        type=int,
        default=2400,
        help="Approximate maximum size for each JSONL chunk.",
    )
    args = parser.parse_args()

    outputs = format_rules(args.input, args.output_dir, args.max_chunk_chars)
    for label, path in outputs.items():
        print(f"[OK] {label}: {path}")


if __name__ == "__main__":
    main()
