import argparse
import hashlib
import html
import json
import re
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = PROJECT_ROOT / "data" / "raw" / "cards.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "processed" / "cards" / "normalized" / "cards_normalized.json"

WHITESPACE_RE = re.compile(r"[ \t\r\f\v]+")
SLUG_RE = re.compile(r"[^a-z0-9]+")


def compact_text(value: str) -> str:
    return WHITESPACE_RE.sub(" ", value).strip()


def compact_lines(lines: list[str]) -> list[str]:
    return [line for line in (compact_text(line) for line in lines) if line]


def simple_entity(value: Any) -> dict[str, Any] | None:
    if not isinstance(value, dict):
        return None

    normalized: dict[str, Any] = {}
    if "id" in value:
        normalized["id"] = value["id"]
    if "label" in value:
        normalized["name"] = value["label"]

    icon = value.get("icon")
    if isinstance(icon, dict) and icon.get("url"):
        normalized["icon_url"] = icon["url"]

    return normalized or None


def value_entity(container: Any) -> dict[str, Any] | None:
    if not isinstance(container, dict):
        return None
    return simple_entity(container.get("value"))


def values_entities(container: Any, key: str = "values") -> list[dict[str, Any]]:
    if not isinstance(container, dict):
        return []
    values = container.get(key)
    if not isinstance(values, list):
        return []
    return [entity for entity in (simple_entity(value) for value in values) if entity]


def ids(entities: list[dict[str, Any]]) -> list[Any]:
    return [entity["id"] for entity in entities if "id" in entity]


def unique_preserving_order(values: list[Any]) -> list[Any]:
    unique: list[Any] = []
    seen: set[str] = set()
    for value in values:
        marker = json.dumps(value, ensure_ascii=False, sort_keys=True)
        if marker in seen:
            continue
        seen.add(marker)
        unique.append(value)
    return unique


def slugify(value: str) -> str:
    slug = SLUG_RE.sub("-", value.lower()).strip("-")
    return slug or "unknown-card"


def stable_hash(value: Any, length: int = 8) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha1(payload.encode("utf-8")).hexdigest()[:length]


def numeric_value(container: Any) -> int | float | None:
    if not isinstance(container, dict):
        return None
    value = container.get("value")
    if not isinstance(value, dict):
        return None

    raw = value.get("id", value.get("label"))
    if raw is None:
        return None

    if isinstance(raw, (int, float)):
        return raw

    text = str(raw).replace("+", "").strip()
    try:
        return int(text)
    except ValueError:
        try:
            return float(text)
        except ValueError:
            return None


def rich_text_body(container: Any) -> str:
    if not isinstance(container, dict):
        return ""
    rich_text = container.get("richText")
    if not isinstance(rich_text, dict):
        return ""
    body = rich_text.get("body")
    return body if isinstance(body, str) else ""


def html_to_lines(markup: str) -> list[str]:
    if not markup:
        return []

    soup = BeautifulSoup(markup, "html.parser")
    for br in soup.find_all("br"):
        br.replace_with("\n")

    text = soup.get_text("\n")
    text = html.unescape(text)
    return compact_lines(text.splitlines())


def image_data(container: Any) -> dict[str, Any] | None:
    if not isinstance(container, dict):
        return None

    normalized: dict[str, Any] = {}
    for key in ["provider", "type", "url", "mimeType", "accessibilityText"]:
        if key in container:
            target_key = "mime_type" if key == "mimeType" else "accessibility_text" if key == "accessibilityText" else key
            normalized[target_key] = container[key]

    dimensions = container.get("dimensions")
    if isinstance(dimensions, dict):
        normalized["dimensions"] = {
            "height": dimensions.get("height"),
            "width": dimensions.get("width"),
            "aspect_ratio": dimensions.get("aspectRatio"),
        }

    colors = container.get("colors")
    if isinstance(colors, dict):
        normalized["colors"] = colors

    return normalized or None


def normalize_card(card: dict[str, Any], index: int, source_path: Path) -> dict[str, Any]:
    rules_html = rich_text_body(card.get("text"))
    rules_lines = html_to_lines(rules_html)
    effect_html = rich_text_body(card.get("effect"))
    effect_lines = html_to_lines(effect_html)

    domains = values_entities(card.get("domain"))
    card_types = values_entities(card.get("cardType"), "type")
    supertypes = values_entities(card.get("cardType"), "superType")
    illustrators = values_entities(card.get("illustrator"))

    try:
        source_ref = source_path.resolve().relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        source_ref = source_path.as_posix()

    normalized: dict[str, Any] = {
        "printing_id": card.get("id"),
        "name": card.get("name"),
        "collector_number": card.get("collectorNumber"),
        "public_code": card.get("publicCode"),
        "set": value_entity(card.get("set")),
        "domains": domains,
        "domain_ids": ids(domains),
        "rarity": value_entity(card.get("rarity")),
        "card_types": card_types,
        "card_type_ids": ids(card_types),
        "supertypes": supertypes,
        "supertype_ids": ids(supertypes),
        "tags": card.get("tags", {}).get("tags", []) if isinstance(card.get("tags"), dict) else [],
        "energy": numeric_value(card.get("energy")),
        "might": numeric_value(card.get("might")),
        "power": numeric_value(card.get("power")),
        "might_bonus": numeric_value(card.get("mightBonus")),
        "orientation": card.get("orientation"),
        "rules_html": rules_html,
        "rules_text": " ".join(rules_lines),
        "rules_lines": rules_lines,
        "effect_html": effect_html,
        "effect_text": " ".join(effect_lines),
        "effect_lines": effect_lines,
        "image": image_data(card.get("cardImage")),
        "illustrators": illustrators,
        "illustrator_ids": ids(illustrators),
        "raw_ref": {
            "source": source_ref,
            "index": index,
        },
    }

    return normalized


def printing_key(card: dict[str, Any]) -> tuple[Any, Any]:
    return (card.get("printing_id"), card.get("public_code"))


def merge_duplicate_printings(cards: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: dict[tuple[Any, Any], dict[str, Any]] = {}

    for card in cards:
        key = printing_key(card)
        if key not in merged:
            copied = dict(card)
            copied["raw_refs"] = [copied.pop("raw_ref")]
            merged[key] = copied
            continue

        merged[key]["raw_refs"].append(card["raw_ref"])

    return list(merged.values())


def rarity_id(card: dict[str, Any]) -> str | None:
    rarity = card.get("rarity")
    if not isinstance(rarity, dict):
        return None
    value = rarity.get("id")
    return str(value) if value is not None else None


def canonical_printing(cards: list[dict[str, Any]]) -> dict[str, Any]:
    def sort_key(card: dict[str, Any]) -> tuple[int, int, str]:
        is_showcase = 1 if rarity_id(card) == "showcase" else 0
        text_len = len(card.get("rules_text") or "") + len(card.get("effect_text") or "")
        return (
            is_showcase,
            -text_len,
            str(card.get("public_code") or card.get("printing_id") or ""),
        )

    return sorted(cards, key=sort_key)[0]


def richest_printing(cards: list[dict[str, Any]]) -> dict[str, Any]:
    def sort_key(card: dict[str, Any]) -> tuple[int, str]:
        text_len = len(card.get("rules_text") or "") + len(card.get("effect_text") or "")
        return (-text_len, str(card.get("public_code") or card.get("printing_id") or ""))

    return sorted(cards, key=sort_key)[0]


def rule_variants(cards: list[dict[str, Any]]) -> list[dict[str, Any]]:
    variants: list[dict[str, Any]] = []
    seen: dict[tuple[str, str], dict[str, Any]] = {}

    for card in cards:
        key = (card.get("rules_text") or "", card.get("effect_text") or "")
        if key not in seen:
            seen[key] = {
                "rules_text": card.get("rules_text") or "",
                "rules_lines": card.get("rules_lines") or [],
                "effect_text": card.get("effect_text") or "",
                "effect_lines": card.get("effect_lines") or [],
                "printing_ids": [],
                "public_codes": [],
            }
            variants.append(seen[key])

        seen[key]["printing_ids"].append(card.get("printing_id"))
        seen[key]["public_codes"].append(card.get("public_code"))

    return variants


def printing_variant(card: dict[str, Any]) -> dict[str, Any]:
    return {
        "printing_id": card.get("printing_id"),
        "collector_number": card.get("collector_number"),
        "public_code": card.get("public_code"),
        "set": card.get("set"),
        "rarity": card.get("rarity"),
        "orientation": card.get("orientation"),
        "image": card.get("image"),
        "illustrators": card.get("illustrators", []),
        "illustrator_ids": card.get("illustrator_ids", []),
        "raw_refs": card.get("raw_refs", []),
    }


def gameplay_signature(card: dict[str, Any]) -> dict[str, Any]:
    return {
        "name": card.get("name"),
        "domain_ids": sorted(card.get("domain_ids", [])),
        "card_type_ids": sorted(card.get("card_type_ids", [])),
        "supertype_ids": sorted(card.get("supertype_ids", [])),
        "energy": card.get("energy"),
        "might": card.get("might"),
        "power": card.get("power"),
        "might_bonus": card.get("might_bonus"),
    }


def gameplay_group_key(card: dict[str, Any]) -> str:
    return json.dumps(
        gameplay_signature(card),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def group_card_printings(cards: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = {}
    for card in cards:
        groups.setdefault(gameplay_group_key(card), []).append(card)

    normalized_groups: list[dict[str, Any]] = []

    for group_key in sorted(groups):
        printings = merge_duplicate_printings(groups[group_key])
        canonical = canonical_printing(printings)
        richest = richest_printing(printings)
        variants = rule_variants(printings)
        signature = gameplay_signature(richest)
        name = richest.get("name") or ""

        sets = unique_preserving_order([printing["set"] for printing in printings if printing.get("set")])
        rarities = unique_preserving_order(
            [printing["rarity"] for printing in printings if printing.get("rarity")]
        )

        normalized_groups.append(
            {
                "play_id": f"play:{slugify(name)}:{stable_hash(signature)}",
                "name": name,
                "signature": signature,
                "canonical_printing_id": canonical.get("printing_id"),
                "printing_ids": [printing.get("printing_id") for printing in printings],
                "collector_numbers": [printing.get("collector_number") for printing in printings],
                "public_codes": [printing.get("public_code") for printing in printings],
                "sets": sets,
                "set_ids": ids(sets),
                "rarities": rarities,
                "rarity_ids": ids(rarities),
                "domains": richest.get("domains", []),
                "domain_ids": richest.get("domain_ids", []),
                "card_types": richest.get("card_types", []),
                "card_type_ids": richest.get("card_type_ids", []),
                "supertypes": richest.get("supertypes", []),
                "supertype_ids": richest.get("supertype_ids", []),
                "tags": richest.get("tags", []),
                "energy": richest.get("energy"),
                "might": richest.get("might"),
                "power": richest.get("power"),
                "might_bonus": richest.get("might_bonus"),
                "rules_html": richest.get("rules_html"),
                "rules_text": richest.get("rules_text"),
                "rules_lines": richest.get("rules_lines", []),
                "effect_html": richest.get("effect_html"),
                "effect_text": richest.get("effect_text"),
                "effect_lines": richest.get("effect_lines", []),
                "rule_variants": variants if len(variants) > 1 else [],
                "printings": [printing_variant(printing) for printing in printings],
            }
        )

    return normalized_groups


def normalize_cards(input_path: Path, output_path: Path) -> list[dict[str, Any]]:
    cards = json.loads(input_path.read_text(encoding="utf-8"))
    if not isinstance(cards, list):
        raise ValueError(f"Expected a list of cards in {input_path}")

    normalized_printings = [
        normalize_card(card, index, input_path) for index, card in enumerate(cards)
    ]
    normalized_cards = group_card_printings(normalized_printings)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(normalized_cards, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return normalized_cards


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Normalize the official Riftbound cards JSON into a flatter processed dataset."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Input raw cards JSON path.")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output normalized cards JSON path.",
    )
    args = parser.parse_args()

    cards = normalize_cards(args.input, args.output)
    print(f"[OK] normalized cards: {len(cards)}")
    print(f"[OK] output: {args.output}")


if __name__ == "__main__":
    main()
