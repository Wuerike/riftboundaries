import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from semantic_contracts import DEFAULT_QUALITY_POLICY, load_contract_bundle


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
CONTRACTS_DIR = SCRIPT_DIR / "contracts"

DEFAULT_CARDS = PROJECT_ROOT / "data" / "processed" / "cards" / "normalized" / "cards_normalized.json"
DEFAULT_FACTS = PROJECT_ROOT / "data" / "processed" / "cards" / "semantic" / "cards_semantic_facts.jsonl"
DEFAULT_SCHEMA = CONTRACTS_DIR / "semantic_facts_schema.json"
DEFAULT_GOLDEN_REPORT = PROJECT_ROOT / "data" / "processed" / "cards" / "semantic" / "cards_semantic_golden_report.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "processed" / "cards" / "semantic" / "cards_semantic_audit_report.json"
DEFAULT_MARKDOWN = PROJECT_ROOT / "data" / "processed" / "cards" / "semantic" / "cards_semantic_audit_report.md"


def repo_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


TEXT_SOURCE_FIELDS = ("rules_lines", "effect_lines")
REPORT_LIMIT = 80


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            row["_line_number"] = line_number
            rows.append(row)
    return rows


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def normalize_text(value: str) -> str:
    return " ".join(value.casefold().split())


def line_has_optional_governor(value: str, optional_governors: list[str]) -> bool:
    return bool(any(needle in value.casefold() for needle in optional_governors))


def load_card_lines(cards: list[dict[str, Any]]) -> dict[tuple[str, str, int], str]:
    lines = {}
    for card in cards:
        for source_field in TEXT_SOURCE_FIELDS:
            for index, line in enumerate(card.get(source_field, []) or []):
                lines[(card["play_id"], source_field, index)] = line
    return lines


def load_card_ids(cards: list[dict[str, Any]]) -> set[str]:
    return {card["play_id"] for card in cards}


def nested_values(payload: Any, key: str) -> list[Any]:
    values = []
    if isinstance(payload, dict):
        for item_key, item_value in payload.items():
            if item_key == key:
                values.append(item_value)
            values.extend(nested_values(item_value, key))
    elif isinstance(payload, list):
        for item in payload:
            values.extend(nested_values(item, key))
    return values


def event_ids_from_fact(fact: dict[str, Any]) -> list[str]:
    event_ids = []
    for event in nested_values(fact.get("payload", {}), "event"):
        if isinstance(event, dict) and isinstance(event.get("id"), str):
            event_ids.append(event["id"])
        elif isinstance(event, str):
            event_ids.append(event)
    event = fact.get("payload", {}).get("event")
    if isinstance(event, dict) and isinstance(event.get("id"), str):
        event_ids.append(event["id"])
    return sorted(set(event_ids))


def output_ids_from_fact(fact: dict[str, Any]) -> list[str]:
    output_ids = []
    for output in fact.get("payload", {}).get("outputs", []) or []:
        if isinstance(output, dict) and isinstance(output.get("id"), str):
            output_ids.append(output["id"])
    return sorted(set(output_ids))


def fact_signature(fact: dict[str, Any]) -> str:
    source = fact.get("source_ref", {})
    return json.dumps(
        {
            "play_id": fact.get("play_id"),
            "source_field": source.get("source_field"),
            "line_index": source.get("line_index"),
            "semantic_role": fact.get("semantic_role"),
            "fact_type": fact.get("fact_type"),
            "predicate": fact.get("predicate"),
            "evidence": normalize_text(str(fact.get("evidence", ""))),
            "payload": fact.get("payload"),
        },
        ensure_ascii=False,
        sort_keys=True,
    )


def add_issue(issues: list[dict[str, Any]], severity: str, code: str, fact: dict[str, Any], detail: str) -> None:
    issues.append(
        {
            "severity": severity,
            "code": code,
            "line_number": fact.get("_line_number"),
            "fact_id": fact.get("fact_id"),
            "play_id": fact.get("play_id"),
            "card_name": fact.get("card_name"),
            "detail": detail,
        }
    )


def audit_facts(
    cards: list[dict[str, Any]],
    facts: list[dict[str, Any]],
    schema: dict[str, Any],
    ontology: dict[str, Any],
    golden_report: dict[str, Any] | None,
    quality_policy: dict[str, Any],
) -> dict[str, Any]:
    card_ids = load_card_ids(cards)
    card_lines = load_card_lines(cards)
    required = set(schema.get("semantic_fact_record", {}).get("required", []))
    roles = set(ontology.get("semantic_roles", schema.get("semantic_roles", [])))
    fact_types = set(ontology.get("fact_types", schema.get("fact_types", [])))
    canonical_actions = set(ontology.get("actions", schema.get("canonical_action_ids", [])))
    canonical_events = set(ontology.get("events", schema.get("canonical_event_ids", [])))
    canonical_outputs = set(ontology.get("outputs", schema.get("canonical_output_ids", [])))
    optional_governors = quality_policy.get("optional_governors", [])
    relation_event_ignore = set(quality_policy.get("relation_event_ignore", []))
    effect_predicates_as_trigger = set(quality_policy.get("effect_predicates_as_trigger", []))
    relational_keywords = quality_policy.get("relational_keywords", [])

    issues: list[dict[str, Any]] = []
    fact_signatures = Counter(fact_signature(fact) for fact in facts)
    fact_ids = Counter(str(fact.get("fact_id")) for fact in facts)
    text_line_keys_with_facts = set()
    relational_text_line_keys_with_facts = set()
    produced_events = Counter()
    observed_events = Counter()
    output_ids = Counter()
    facts_by_card = Counter()
    facts_by_source_line = Counter()
    fact_rows_by_source_line: dict[tuple[str, str, int], list[dict[str, Any]]] = defaultdict(list)
    relational_clause_groups_by_source_line: dict[tuple[str, str, int], set[str]] = defaultdict(set)
    web_uses = Counter()
    role_payload_issues = Counter()

    for fact in facts:
        payload = fact.get("payload", {})
        role = fact.get("semantic_role")
        fact_type = fact.get("fact_type")
        predicate = fact.get("predicate")
        facts_by_card[fact.get("play_id")] += 1
        missing_required = sorted(required - set(fact))
        if missing_required:
            add_issue(issues, "error", "missing_required_fields", fact, ", ".join(missing_required))

        if fact.get("schema_version") != schema.get("version"):
            add_issue(issues, "error", "schema_version_mismatch", fact, str(fact.get("schema_version")))

        if fact_ids[str(fact.get("fact_id"))] > 1:
            add_issue(issues, "error", "duplicate_fact_id", fact, str(fact.get("fact_id")))

        if fact.get("play_id") not in card_ids:
            add_issue(issues, "error", "unknown_play_id", fact, str(fact.get("play_id")))

        if fact.get("semantic_role") not in roles:
            add_issue(issues, "error", "unknown_semantic_role", fact, str(fact.get("semantic_role")))

        if fact.get("fact_type") not in fact_types:
            add_issue(issues, "error", "unknown_fact_type", fact, str(fact.get("fact_type")))

        if fact.get("predicate") not in canonical_actions:
            add_issue(issues, "warning", "unknown_predicate", fact, str(fact.get("predicate")))

        confidence = fact.get("confidence")
        if not isinstance(confidence, (int, float)) or confidence < 0 or confidence > 1:
            add_issue(issues, "error", "invalid_confidence", fact, str(confidence))
        elif confidence < 0.7:
            add_issue(issues, "warning", "low_confidence", fact, str(confidence))

        source_ref = fact.get("source_ref", {})
        source_field = source_ref.get("source_field")
        line_index = source_ref.get("line_index")
        if source_field in TEXT_SOURCE_FIELDS:
            key = (fact.get("play_id"), source_field, line_index)
            text_line_keys_with_facts.add(key)
            facts_by_source_line[key] += 1
            source_line = card_lines.get(key)
            if source_line is None:
                add_issue(issues, "error", "invalid_source_ref", fact, str(key))
            else:
                evidence = str(fact.get("evidence", ""))
                if normalize_text(evidence) not in normalize_text(source_line):
                    add_issue(issues, "error", "evidence_not_in_source_line", fact, evidence)
                if source_ref.get("line_text") != source_line:
                    add_issue(issues, "warning", "source_line_text_mismatch", fact, str(key))
                if fact.get("semantic_role") != "identity_or_descriptor":
                    relational_text_line_keys_with_facts.add(key)
                    relational_clause_groups_by_source_line[key].add(str(fact.get("clause_group_id")))
                    if (
                        role in {"payoff_output", "event_produced", "state_or_modifier", "cost_or_requirement"}
                        and line_has_optional_governor(source_line, optional_governors)
                        and payload.get("modality") != "optional"
                    ):
                        add_issue(issues, "warning", "optional_line_without_optional_modality", fact, str(key))
                        role_payload_issues["optional_line_without_optional_modality"] += 1
                fact_rows_by_source_line[key].append(fact)
        elif source_field != "official_field":
            add_issue(issues, "error", "unknown_source_field", fact, str(source_field))

        if fact_signatures[fact_signature(fact)] > 1:
            add_issue(issues, "warning", "duplicate_fact_signature", fact, "same semantic signature appears more than once")

        for event_id in event_ids_from_fact(fact):
            if event_id not in canonical_events:
                add_issue(issues, "warning", "unknown_event_id", fact, event_id)
            if fact.get("semantic_role") == "trigger_observed":
                observed_events[event_id] += 1
            elif fact.get("semantic_role") == "event_produced":
                produced_events[event_id] += 1
            elif fact.get("fact_type") == "token_creation":
                produced_events[event_id] += 1

        for output_id in output_ids_from_fact(fact):
            output_ids[output_id] += 1
            if output_id not in canonical_outputs:
                add_issue(issues, "info", "unknown_output_id", fact, output_id)

        for use in fact.get("web_uses", []) or []:
            web_uses[use] += 1

        if role == "trigger_observed" and not payload.get("event"):
            add_issue(issues, "error", "trigger_without_event", fact, "trigger_observed requires payload.event")
            role_payload_issues["trigger_without_event"] += 1
        if role == "event_produced" and not payload.get("event"):
            add_issue(issues, "error", "producer_without_event", fact, "event_produced requires payload.event")
            role_payload_issues["producer_without_event"] += 1
        if predicate == "observe_event" and role != "trigger_observed":
            add_issue(issues, "error", "observe_event_wrong_role", fact, role)
            role_payload_issues["observe_event_wrong_role"] += 1
        if predicate in effect_predicates_as_trigger and role == "trigger_observed":
            add_issue(issues, "error", "effect_predicate_as_trigger", fact, predicate)
            role_payload_issues["effect_predicate_as_trigger"] += 1
        if role == "payoff_output" and fact_type != "damage" and not payload.get("outputs") and not payload.get("amounts"):
            add_issue(issues, "warning", "payoff_without_output", fact, "payoff_output should expose outputs or amounts")
            role_payload_issues["payoff_without_output"] += 1
        if role == "cost_or_requirement" and not payload.get("costs") and not payload.get("conditions"):
            add_issue(issues, "warning", "cost_without_costs", fact, "cost_or_requirement should expose costs or conditions")
            role_payload_issues["cost_without_costs"] += 1
        if fact_type in {"damage", "stat_change"} and not payload.get("amounts") and not payload.get("multiplier"):
            add_issue(issues, "warning", "numeric_fact_without_amount", fact, fact_type)
            role_payload_issues["numeric_fact_without_amount"] += 1

    for key, groups in relational_clause_groups_by_source_line.items():
        if len(groups) <= 1:
            continue
        fact = fact_rows_by_source_line[key][0]
        add_issue(
            issues,
            "warning",
            "multiple_relational_clause_groups_on_line",
            fact,
            ", ".join(sorted(groups)),
        )
        role_payload_issues["multiple_relational_clause_groups_on_line"] += 1

    all_text_line_keys = set(card_lines)
    uncovered_lines = [
        {
            "play_id": play_id,
            "source_field": source_field,
            "line_index": line_index,
            "line": card_lines[(play_id, source_field, line_index)],
        }
        for play_id, source_field, line_index in sorted(all_text_line_keys - text_line_keys_with_facts)
    ]
    uncovered_relational_lines = [
        row
        for row in uncovered_lines
        if any(keyword in row["line"].casefold() for keyword in relational_keywords)
    ]

    produced_without_observers = {
        event_id: count
        for event_id, count in produced_events.items()
        if event_id not in observed_events and event_id not in relation_event_ignore
    }
    observed_without_producers = {
        event_id: count
        for event_id, count in observed_events.items()
        if event_id not in produced_events and event_id not in relation_event_ignore
    }

    issue_counts = Counter(issue["severity"] for issue in issues)
    issue_code_counts = Counter(issue["code"] for issue in issues)
    facts_by_source_kind = Counter(
        fact.get("extractor", {}).get("source_kind", "unknown")
        if isinstance(fact.get("extractor"), dict)
        else "legacy_string"
        for fact in facts
    )
    contract_rules = Counter(
        fact.get("extractor", {}).get("rule_id")
        for fact in facts
        if isinstance(fact.get("extractor"), dict)
        and fact.get("extractor", {}).get("source_kind") == "contract_rule"
    )

    return {
        "version": schema.get("version"),
        "inputs": {
            "cards": repo_path(DEFAULT_CARDS),
            "facts": repo_path(DEFAULT_FACTS),
            "schema": repo_path(DEFAULT_SCHEMA),
            "ontology": repo_path(CONTRACTS_DIR / "semantic_ontology.json"),
            "golden_report": repo_path(DEFAULT_GOLDEN_REPORT),
            "quality_policy": repo_path(DEFAULT_QUALITY_POLICY),
        },
        "summary": {
            "card_count": len(cards),
            "fact_count": len(facts),
            "cards_with_facts": len([play_id for play_id in facts_by_card if play_id]),
            "text_line_count": len(all_text_line_keys),
            "text_lines_with_facts": len(text_line_keys_with_facts),
            "text_lines_without_facts": len(uncovered_lines),
            "text_line_fact_coverage": round(len(text_line_keys_with_facts) / len(all_text_line_keys), 4)
            if all_text_line_keys
            else 1.0,
            "error_count": issue_counts.get("error", 0),
            "warning_count": issue_counts.get("warning", 0),
            "info_count": issue_counts.get("info", 0),
            "golden_pass": bool(golden_report and golden_report.get("summary", {}).get("pass")),
            "legacy_rule_count": sum(
                1
                for fact in facts
                if isinstance(fact.get("extractor"), dict)
                and fact.get("extractor", {}).get("source_kind") == "legacy_rule"
            ),
        },
        "issue_counts": dict(issue_code_counts.most_common()),
        "facts_by_source_kind": dict(facts_by_source_kind.most_common()),
        "top_contract_rules": dict(contract_rules.most_common(40)),
        "contract_rule_coverage": {
            "contract_rule_count": facts_by_source_kind.get("contract_rule", 0),
            "legacy_rule_count": facts_by_source_kind.get("legacy_rule", 0),
            "contract_share": round(facts_by_source_kind.get("contract_rule", 0) / len(facts), 4) if facts else 0.0,
        },
        "issues": sorted(
            issues,
            key=lambda issue: (
                {"error": 0, "warning": 1, "info": 2}.get(issue["severity"], 9),
                issue["code"],
                issue.get("line_number") or 0,
            ),
        )[:REPORT_LIMIT],
        "coverage": {
            "top_uncovered_text_lines": uncovered_lines[:REPORT_LIMIT],
            "top_uncovered_relational_text_lines": uncovered_relational_lines[:REPORT_LIMIT],
            "top_fact_dense_lines": [
                {
                    "play_id": key[0],
                    "source_field": key[1],
                    "line_index": key[2],
                    "fact_count": count,
                    "line": card_lines.get(key),
                }
                for key, count in facts_by_source_line.most_common(30)
            ],
        },
        "relations_readiness": {
            "produced_events": dict(produced_events.most_common()),
            "observed_events": dict(observed_events.most_common()),
            "output_ids": dict(output_ids.most_common()),
            "web_uses": dict(web_uses.most_common()),
            "role_payload_issues": dict(role_payload_issues.most_common()),
            "relational_text_lines_with_facts": len(relational_text_line_keys_with_facts),
            "relational_text_lines_without_facts": len(uncovered_relational_lines),
            "produced_events_without_observers": produced_without_observers,
            "observed_events_without_producers": observed_without_producers,
        },
    }


def markdown_table(rows: list[dict[str, Any]], columns: list[tuple[str, str]]) -> list[str]:
    lines = []
    lines.append("| " + " | ".join(label for label, _key in columns) + " |")
    lines.append("| " + " | ".join("---" for _label, _key in columns) + " |")
    for row in rows:
        values = []
        for _label, key in columns:
            value = row.get(key, "")
            values.append(str(value).replace("\n", " ").replace("|", "\\|"))
        lines.append("| " + " | ".join(values) + " |")
    return lines


def markdown_report(payload: dict[str, Any]) -> str:
    summary = payload["summary"]
    lines = [
        "# Cards Semantic Audit Report",
        "",
        "Audit for `data/processed/cards/semantic/cards_semantic_facts.jsonl`.",
        "",
        "## Summary",
        "",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## Issue Counts", ""])
    if payload["issue_counts"]:
        for code, count in payload["issue_counts"].items():
            lines.append(f"- {code}: {count}")
    else:
        lines.append("- none")

    lines.extend(["", "## Extraction Provenance", ""])
    for key, value in payload.get("facts_by_source_kind", {}).items():
        lines.append(f"- {key}: {value}")
    if payload.get("top_contract_rules"):
        lines.extend(["", "### Top Contract Rules", ""])
        for key, value in payload["top_contract_rules"].items():
            lines.append(f"- {key}: {value}")

    lines.extend(["", "## Top Issues", ""])
    if payload["issues"]:
        lines.extend(
            markdown_table(
                payload["issues"][:30],
                [
                    ("Severity", "severity"),
                    ("Code", "code"),
                    ("Card", "card_name"),
                    ("Fact", "fact_id"),
                    ("Detail", "detail"),
                ],
            )
        )
    else:
        lines.append("No issues found.")

    readiness = payload["relations_readiness"]
    lines.extend(["", "## Relation Readiness", ""])
    lines.append(f"- produced event ids: {len(readiness['produced_events'])}")
    lines.append(f"- observed event ids: {len(readiness['observed_events'])}")
    lines.append(f"- output ids: {len(readiness['output_ids'])}")
    lines.append(f"- relational text lines with facts: {readiness['relational_text_lines_with_facts']}")
    lines.append(f"- relational text lines without facts: {readiness['relational_text_lines_without_facts']}")
    lines.append(f"- produced events without observers: {len(readiness['produced_events_without_observers'])}")
    lines.append(f"- observed events without producers: {len(readiness['observed_events_without_producers'])}")

    lines.extend(["", "### Web Uses", ""])
    if readiness["web_uses"]:
        for use, count in readiness["web_uses"].items():
            lines.append(f"- {use}: {count}")
    else:
        lines.append("- none")

    lines.extend(["", "### Role Payload Issues", ""])
    if readiness["role_payload_issues"]:
        for code, count in readiness["role_payload_issues"].items():
            lines.append(f"- {code}: {count}")
    else:
        lines.append("- none")

    lines.extend(["", "### Produced Events Without Observers", ""])
    if readiness["produced_events_without_observers"]:
        for event_id, count in readiness["produced_events_without_observers"].items():
            lines.append(f"- {event_id}: {count}")
    else:
        lines.append("- none")

    lines.extend(["", "### Observed Events Without Producers", ""])
    if readiness["observed_events_without_producers"]:
        for event_id, count in readiness["observed_events_without_producers"].items():
            lines.append(f"- {event_id}: {count}")
    else:
        lines.append("- none")

    lines.extend(["", "## Top Uncovered Text Lines", ""])
    uncovered = payload["coverage"]["top_uncovered_text_lines"][:40]
    if uncovered:
        lines.extend(
            markdown_table(
                uncovered,
                [("Card", "play_id"), ("Source", "source_field"), ("Line", "line_index"), ("Text", "line")],
            )
        )
    else:
        lines.append("No uncovered text lines.")

    lines.extend(["", "## Top Uncovered Relational Text Lines", ""])
    uncovered_relational = payload["coverage"]["top_uncovered_relational_text_lines"][:40]
    if uncovered_relational:
        lines.extend(
            markdown_table(
                uncovered_relational,
                [("Card", "play_id"), ("Source", "source_field"), ("Line", "line_index"), ("Text", "line")],
            )
        )
    else:
        lines.append("No uncovered relational text lines.")

    return "\n".join(lines) + "\n"


def write_markdown(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(markdown_report(payload), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit semantic facts.")
    parser.add_argument("--cards", type=Path, default=DEFAULT_CARDS)
    parser.add_argument("--facts", type=Path, default=DEFAULT_FACTS)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--golden-report", type=Path, default=DEFAULT_GOLDEN_REPORT)
    parser.add_argument("--quality-policy", type=Path, default=DEFAULT_QUALITY_POLICY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MARKDOWN)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cards = read_json(args.cards)
    facts = read_jsonl(args.facts)
    schema = read_json(args.schema)
    golden_report = read_json(args.golden_report) if args.golden_report.exists() else None
    contracts = load_contract_bundle(CONTRACTS_DIR)
    quality_policy = contracts["quality_policy"] if args.quality_policy == DEFAULT_QUALITY_POLICY else read_json(args.quality_policy)
    report = audit_facts(cards, facts, schema, contracts["ontology"], golden_report, quality_policy)
    write_json(args.output, report)
    write_markdown(args.markdown, report)
    print(f"Wrote semantic audit JSON to {args.output}")
    print(f"Wrote semantic audit Markdown to {args.markdown}")
    print(
        "Semantic audit: "
        f"{report['summary']['error_count']} errors, "
        f"{report['summary']['warning_count']} warnings, "
        f"{report['summary']['text_line_fact_coverage']} text coverage"
    )


if __name__ == "__main__":
    main()
