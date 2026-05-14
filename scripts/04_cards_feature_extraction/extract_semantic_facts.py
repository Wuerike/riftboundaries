import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from semantic_contracts import DEFAULT_EXTRACTION_RULES, DEFAULT_ONTOLOGY, load_contract_bundle


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
CONTRACTS_DIR = SCRIPT_DIR / "contracts"

DEFAULT_CARDS = PROJECT_ROOT / "data" / "processed" / "cards" / "normalized" / "cards_normalized.json"
DEFAULT_INVENTORY = PROJECT_ROOT / "data" / "processed" / "cards" / "inventory" / "cards_text_inventory.json"
DEFAULT_TAXONOMY = CONTRACTS_DIR / "feature_relation_taxonomy.json"
DEFAULT_ALIGNMENT = PROJECT_ROOT / "data" / "processed" / "cards" / "inventory" / "cards_taxonomy_alignment.json"
DEFAULT_SCHEMA = CONTRACTS_DIR / "semantic_facts_schema.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "processed" / "cards" / "semantic" / "cards_semantic_facts.jsonl"
DEFAULT_REPORT = PROJECT_ROOT / "data" / "processed" / "cards" / "semantic" / "cards_semantic_facts_report.json"


def repo_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


SCHEMA_VERSION = "2026-05-12"
EXTRACTOR_VERSION = "semantic_facts"
NON_GRANTED_BRACKET_ACTION_KEYWORDS = {"stun"}
UNBRACKETED_INTRINSIC_KEYWORDS = {
    "ambush",
    "assault",
    "deathknell",
    "deflect",
    "ganking",
    "hidden",
    "reaction",
    "shield",
    "tank",
    "temporary",
    "weaponmaster",
}

TEXT_SOURCE_FIELDS = ("rules_lines", "effect_lines")
BRACKET_TOKEN_RE = re.compile(r"\[([^\]]+)\]")
RB_SYMBOL_RE = re.compile(r":rb_[a-z0-9_]+:", re.I)
ENERGY_SYMBOL_RE = re.compile(r":rb_energy_(?P<amount>\d+):", re.I)
RUNE_SYMBOL_RE = re.compile(r":rb_rune_(?P<domain>[a-z]+):", re.I)
ADD_RESOURCE_SYMBOL_RE = re.compile(r":rb_(?:energy_\d+|rune_[a-z]+):|\bEnergy\b", re.I)
NUMBER_RE = re.compile(r"\b\d+\b")
RUNE_DOMAINS = ("body", "calm", "chaos", "fury", "mind", "order")

WORD_NUMBERS = {
    "a": 1,
    "an": 1,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
}

TRIGGER_PATTERNS: list[tuple[str, re.Pattern[str], list[str], dict[str, Any]]] = [
    ("self_played", re.compile(r"\bWhen you play (?:me|this|it)\b", re.I), ["self_played"], {"subject": "self"}),
    ("self_dies", re.compile(r"\bWhen (?:I|this|me) die?s?\b", re.I), ["self_dies"], {"subject": "self"}),
    ("friendly_unit_dies", re.compile(r"\bWhen (?:a|one or more|another|a buffed)?\s*(?:non-[A-Za-z]+\s+)?friendly units? dies?\b", re.I), ["friendly_unit_dies"], {"subject": "friendly_unit"}),
    ("your_unit_dies", re.compile(r"\bWhen (?:another\s+)?(?:non-[A-Za-z]+\s+)?unit you control dies?\b", re.I), ["friendly_unit_dies"], {"subject": "friendly_unit"}),
    ("enemy_unit_dies", re.compile(r"\bWhen one or more enemy units die\b", re.I), ["enemy_unit_dies"], {"subject": "enemy_unit", "amount": "one_or_more"}),
    ("self_conquers_or_holds", re.compile(r"\bWhen I conquer or hold\b", re.I), ["self_conquers", "self_holds"], {"subject": "self"}),
    ("self_conquers", re.compile(r"\bWhen I conquer\b", re.I), ["self_conquers"], {"subject": "self"}),
    ("self_holds", re.compile(r"\bWhen I hold\b", re.I), ["self_holds"], {"subject": "self"}),
    ("battlefield_conquered", re.compile(r"\bWhen you conquer here\b", re.I), ["battlefield_conquered"], {"subject": "you"}),
    ("battlefield_held", re.compile(r"\bWhen you hold here\b", re.I), ["battlefield_held"], {"subject": "you"}),
    ("self_attacks_or_defends", re.compile(r"\bWhen I attack or defend\b", re.I), ["self_attacks", "self_defends"], {"subject": "self"}),
    ("self_attacks", re.compile(r"\bWhen I attack\b(?!\s+or\s+defend)", re.I), ["self_attacks"], {"subject": "self"}),
    ("self_moves", re.compile(r"\bWhen I move(?: to a battlefield)?\b", re.I), ["self_moves"], {"subject": "self"}),
    ("self_leaves_board", re.compile(r"\bWhen this leaves the board\b", re.I), ["self_leaves_board"], {"subject": "self"}),
    ("rune_recycled", re.compile(r"\bWhen you recycle a rune\b", re.I), ["rune_recycled"], {"subject": "you"}),
    ("card_recycled", re.compile(r"\bWhen you recycle one or more cards?(?: to your Main Deck)?\b", re.I), ["card_recycled"], {"subject": "you"}),
    ("unit_stunned", re.compile(r"\bWhen you stun one or more enemy units?\b", re.I), ["unit_stunned"], {"subject": "enemy_unit", "amount": "one_or_more"}),
    ("unit_buffed", re.compile(r"\bWhen you buff a friendly unit\b", re.I), ["unit_buffed"], {"subject": "friendly_unit"}),
    ("spell_played", re.compile(r"\bWhen (?:a player|you) plays? a spell\b", re.I), ["spell_played"], {"subject": "player"}),
    ("unit_played", re.compile(r"\bWhen (?:a player|you) plays? (?:a|\[Mighty\]) unit\b", re.I), ["unit_played"], {"subject": "unit"}),
    ("mighty_becomes", re.compile(r"\bWhen one of your units becomes \[Mighty\]\b", re.I), ["unit_becomes_mighty"], {"subject": "friendly_unit"}),
]

STATIC_CONDITION_PATTERNS: list[tuple[str, re.Pattern[str], str]] = [
    ("control_this_battlefield", re.compile(r"\bWhile you control this battlefield\b", re.I), "you_control_this_battlefield"),
    ("while_attacker", re.compile(r"\bwhile (?:I'?m|it's|this is) an attacker\b", re.I), "while_attacker"),
    ("while_defender", re.compile(r"\bwhile (?:I'?m|it's|this is) a defender\b", re.I), "while_defender"),
]


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip()).casefold()


def slug(value: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", value).strip("_").lower()
    return cleaned or "unknown"


def keyword_ids_from_text(value: str) -> list[str]:
    keywords = []
    for token in BRACKET_TOKEN_RE.findall(value):
        token = token.strip()
        if not token or token in {">", "<"}:
            continue
        keyword_id = slug(re.sub(r"\s+\d+$", "", token))
        if keyword_id == "add":
            continue
        keywords.append(keyword_id)
    return sorted(set(keywords))


def is_angle_marker(token: str) -> bool:
    return bool(token) and all(character in {"<", ">"} for character in token.strip())


def normalize_target(raw: Any) -> dict[str, Any]:
    if not isinstance(raw, str):
        return {}
    cleaned = normalize_text(raw)
    target: dict[str, Any] = {"raw": raw.strip()}
    if not cleaned:
        return target

    self_target_text = re.sub(r"\bthis (?:turn|combat|round)\b", "", cleaned)
    if re.search(r"\b(?:me|myself|this|it|i)\b|\bmy cost\b", self_target_text):
        target.update({"kind": "card", "scope": "self"})
    if re.search(r"\bunits?\b", cleaned):
        target["kind"] = "unit"
    if re.search(r"\bgears?\b", cleaned):
        if target.get("kind") and target["kind"] != "gear":
            target["kinds"] = sorted({target["kind"], "gear"})
            target.pop("kind", None)
        else:
            target["kind"] = "gear"
    if re.search(r"\bspells?\b", cleaned):
        if target.get("kind") and target["kind"] != "spell":
            target["kinds"] = sorted({target["kind"], "spell"})
            target.pop("kind", None)
        else:
            target["kind"] = "spell"
    if re.search(r"\bcards?\b", cleaned) and "kind" not in target and "kinds" not in target:
        target["kind"] = "card"

    if "friendly" in cleaned:
        target["controller"] = "friendly"
    elif re.search(r"\b(?:your|you control|you play)\b", cleaned):
        target["controller"] = "you"
    elif "enemy" in cleaned:
        target["controller"] = "opponent"
        target.setdefault("scope", "enemy")
    elif "opponent" in cleaned:
        target["controller"] = "opponent"

    if "named tag" in cleaned:
        target["qualifier"] = "named_tag"
    if "buffed" in cleaned:
        target["qualifier"] = "buffed" if "qualifier" not in target else f"{target['qualifier']},buffed"
    if "token" in cleaned:
        target["token_state"] = "token"
    if "non-token" in cleaned:
        target["exclude"] = ["token"]
    if "here" in cleaned:
        target["location"] = "here"
    elif "my battlefield" in cleaned:
        target["location"] = "my_battlefield"
    elif "at a battlefield" in cleaned or "at battlefields" in cleaned:
        target["location"] = "battlefield"
    elif "base" in cleaned:
        target["location"] = "base"
    if "open battlefield" in cleaned:
        target["location_state"] = "open"
    if "occupied battlefield" in cleaned:
        target["location_state"] = "occupied"

    return target


def normalize_destination(raw: Any) -> dict[str, Any] | None:
    if not isinstance(raw, str) or not raw.strip():
        return None
    cleaned = normalize_text(raw)
    destination: dict[str, Any] = {"raw": raw.strip()}
    if "open battlefield" in cleaned:
        destination.update({"zone": "battlefield", "state": "open"})
    elif "occupied battlefield" in cleaned:
        destination.update({"zone": "battlefield", "state": "occupied"})
    elif "battlefield" in cleaned:
        destination["zone"] = "battlefield"
    elif "base" in cleaned:
        destination["zone"] = "base"
    elif "hand" in cleaned:
        destination["zone"] = "hand"
    elif re.search(r"\bhere\b", cleaned):
        destination["location"] = "here"
    elif "location" in cleaned:
        destination["zone"] = "location"
    if "enemy" in cleaned:
        destination["controller"] = "opponent"
    if "friendly" in cleaned or "your" in cleaned:
        destination["controller"] = "you"
    return destination


def normalize_payload(payload: dict[str, Any]) -> dict[str, Any]:
    payload = dict(payload)
    target = payload.get("target")
    if isinstance(target, dict) and isinstance(target.get("raw"), str):
        normalized = normalize_target(target["raw"])
        normalized.update({key: value for key, value in target.items() if key != "raw"})
        payload["target"] = normalized
    location = payload.get("location")
    if isinstance(location, str) and location.strip():
        payload["destination"] = normalize_destination(location)
    destination = payload.get("destination")
    if isinstance(destination, dict) and isinstance(destination.get("raw"), str):
        normalized_destination = normalize_destination(destination["raw"]) or {}
        normalized_destination.update({key: value for key, value in destination.items() if key != "raw"})
        payload["destination"] = normalized_destination
    return payload


def line_clause_group_id(play_id: str, source_field: str, line_index: int) -> str:
    return f"clause:{play_id}:{source_field}:{line_index}:ability"


def line_has_optional_governor(line: str) -> bool:
    return bool(
        re.search(
            r"\b(?:you may|they may|each player may|may pay|may exhaust|may discard|may kill|may play|may reveal)\b",
            line,
            re.I,
        )
    )


def payload_with_line_modality(
    line: str,
    payload: dict[str, Any],
    default: str = "required",
    evidence: str | None = None,
) -> dict[str, Any]:
    if "modality" in payload:
        return payload
    payload = dict(payload)
    context = evidence or line
    if evidence:
        line_norm = normalize_text(line)
        evidence_norm = normalize_text(evidence)
        start = line_norm.find(evidence_norm)
        if start >= 0:
            prior = line_norm[max(0, start - 90) : start]
            sentence_start = max(prior.rfind("."), prior.rfind(";"))
            if sentence_start >= 0:
                prior = prior[sentence_start + 1 :]
            context = f"{prior} {evidence_norm}"
    payload["modality"] = "optional" if line_has_optional_governor(context) else default
    return payload


def word_number(value: str | None) -> int | None:
    if value is None:
        return None
    value = value.strip().casefold()
    if value.isdigit():
        return int(value)
    return WORD_NUMBERS.get(value)


def card_snapshot(card: dict[str, Any]) -> dict[str, Any]:
    return {
        "domain_ids": card.get("domain_ids", []),
        "card_type_ids": card.get("card_type_ids", []),
        "energy": card.get("energy"),
        "might": card.get("might"),
        "power": card.get("power"),
        "tags": [tag.get("name") if isinstance(tag, dict) else tag for tag in card.get("tags", [])],
    }


def load_inventory_line_units(inventory: dict[str, Any]) -> dict[tuple[str, str, int], list[dict[str, Any]]]:
    units_by_source: dict[tuple[str, str, int], list[dict[str, Any]]] = defaultdict(list)
    for unit_index, unit in enumerate(inventory.get("text_units", [])):
        compact_unit = {
            "unit_index": unit_index,
            "unit_text": unit.get("unit_text"),
            "normalized_unit": unit.get("normalized_unit"),
            "parameterized_unit": unit.get("parameterized_unit"),
            "candidate_families": unit.get("candidate_families", []),
        }
        for example in unit.get("examples", []):
            for card in example.get("example_cards", []):
                key = (card.get("play_id", ""), card.get("source_field", ""), card.get("line_index", -1))
                if key[0] and key[1] and key[2] >= 0:
                    units_by_source[key].append(compact_unit)
    return units_by_source


def matching_inventory_unit(
    units_by_source: dict[tuple[str, str, int], list[dict[str, Any]]],
    play_id: str,
    source_field: str,
    line_index: int | None,
    evidence: str,
) -> dict[str, Any] | None:
    if line_index is None:
        return None
    units = units_by_source.get((play_id, source_field, line_index), [])
    evidence_norm = normalize_text(evidence)
    for unit in units:
        unit_text = str(unit.get("unit_text") or "")
        if normalize_text(unit_text) in evidence_norm or evidence_norm in normalize_text(unit_text):
            return unit
    return units[0] if units else None


def web_uses_for(semantic_role: str, fact_type: str) -> list[str]:
    uses = {"similarity"}
    if semantic_role == "event_produced":
        uses.update({"enables", "deck_synergy"})
    if semantic_role == "trigger_observed":
        uses.update({"enabled_by", "filters", "deck_synergy"})
    if semantic_role == "payoff_output":
        uses.update({"enables", "filters", "deck_synergy"})
    if semantic_role == "cost_or_requirement":
        uses.update({"filters", "deck_synergy"})
    if semantic_role == "restriction_or_permission":
        uses.update({"filters"})
    if semantic_role == "state_or_modifier":
        uses.update({"enables", "filters", "deck_synergy"})
    if semantic_role in {"targeting_or_scope", "identity_or_descriptor"}:
        uses.update({"filters"})
    if fact_type in {"token_creation", "resource_change", "entry_state", "static_modifier"}:
        uses.update({"enables", "deck_synergy"})
    return sorted(uses)


def regex_flags(rule: dict[str, Any]) -> int:
    flags = 0
    for flag in rule.get("flags", []) or []:
        if flag == "IGNORECASE":
            flags |= re.I
    return flags


def compile_extraction_rules(contract: dict[str, Any]) -> list[dict[str, Any]]:
    rules = []
    for section in ("trigger_rules", "condition_rules", "cost_rules", "effect_rules", "reminder_rules"):
        for rule in contract.get(section, []) or []:
            compiled = dict(rule)
            compiled["_section"] = section
            compiled["_pattern"] = re.compile(rule["pattern"], regex_flags(rule))
            rules.append(compiled)
    return rules


def rule_evidence(rule: dict[str, Any], match: re.Match[str]) -> str:
    evidence = match.group(0)
    if rule.get("rule_id") == "counter_spell":
        evidence = re.split(r"\s+and\s+give\b", evidence, maxsplit=1, flags=re.I)[0]
    trim = rule.get("evidence_trim")
    if isinstance(trim, str) and trim:
        evidence = evidence.rstrip(trim)
    return evidence.strip()


def transform_value(value: Any, transform: str | None) -> Any:
    if value is None:
        return None
    if isinstance(value, str) and transform in {"int", "word_number", "strip", "slug"}:
        value = value.strip()
    if transform == "int":
        return int(value)
    if transform == "word_number":
        return word_number(str(value))
    if transform == "strip":
        return str(value).strip()
    if transform == "casefold":
        return str(value).casefold()
    if transform == "slug":
        return slug(str(value))
    return value


def format_template(template: str, match: re.Match[str]) -> str:
    def replace(token: re.Match[str]) -> str:
        value = match.groupdict().get(token.group("name"))
        if value is None:
            return ""
        return str(transform_value(value, token.group("transform")))

    return re.sub(r"\{(?P<name>[A-Za-z_][A-Za-z0-9_]*)(?::(?P<transform>[A-Za-z_]+))?\}", replace, template)


def resolve_template(value: Any, match: re.Match[str]) -> Any:
    if isinstance(value, list):
        return [resolve_template(item, match) for item in value]
    if not isinstance(value, dict):
        return value
    if "$group" in value:
        group_value = match.groupdict().get(str(value["$group"]))
        if group_value in {None, ""}:
            return value.get("default")
        return transform_value(group_value, value.get("transform"))
    if "$format" in value:
        return format_template(str(value["$format"]), match)
    if "$if_match_contains" in value:
        needle = str(value["$if_match_contains"]).casefold()
        branch = "then" if needle in match.group(0).casefold() else "else"
        return resolve_template(value.get(branch), match)
    return {key: resolve_template(item, match) for key, item in value.items()}


class FactBuilder:
    def __init__(self, units_by_source: dict[tuple[str, str, int], list[dict[str, Any]]]) -> None:
        self.units_by_source = units_by_source
        self.ordinal_by_key: Counter[tuple[str, str, int | None, str, str]] = Counter()

    def next_fact_id(
        self,
        play_id: str,
        source_field: str,
        line_index: int | None,
        semantic_role: str,
        predicate: str,
    ) -> str:
        key = (play_id, source_field, line_index, semantic_role, predicate)
        ordinal = self.ordinal_by_key[key]
        self.ordinal_by_key[key] += 1
        line_part = "official" if line_index is None else str(line_index)
        return f"fact:{play_id}:{source_field}:{line_part}:{slug(semantic_role)}:{slug(predicate)}:{ordinal}"

    def fact(
        self,
        card: dict[str, Any],
        *,
        source_field: str,
        line_index: int | None,
        line_text: str,
        evidence: str,
        clause_group_id: str,
        semantic_role: str,
        fact_type: str,
        predicate: str,
        payload: dict[str, Any],
        confidence: float = 0.86,
        rule_id: str = "generic",
        rule_version: int | None = None,
        source_kind: str = "legacy_rule",
        contract: str | None = None,
        secondary_roles: list[str] | None = None,
        notes: str | None = None,
    ) -> dict[str, Any]:
        payload = normalize_payload(payload)
        payload = payload_with_attached_context(card, source_field, payload)
        inventory_unit = matching_inventory_unit(
            self.units_by_source,
            card["play_id"],
            source_field,
            line_index,
            evidence,
        )
        source_ref = {
            "source_field": source_field,
            "line_index": line_index,
            "unit_index": inventory_unit.get("unit_index") if inventory_unit else None,
            "line_text": line_text,
            "unit_text": inventory_unit.get("unit_text") if inventory_unit else evidence,
            "normalized_unit": inventory_unit.get("normalized_unit") if inventory_unit else normalize_text(evidence),
            "parameterized_unit": inventory_unit.get("parameterized_unit") if inventory_unit else normalize_text(evidence),
            "inventory_families": inventory_unit.get("candidate_families") if inventory_unit else [],
        }
        row = {
            "schema_version": SCHEMA_VERSION,
            "fact_id": self.next_fact_id(card["play_id"], source_field, line_index, semantic_role, predicate),
            "play_id": card["play_id"],
            "card_name": card["name"],
            "card_snapshot": card_snapshot(card),
            "source_ref": source_ref,
            "clause_group_id": clause_group_id,
            "semantic_role": semantic_role,
            "fact_type": fact_type,
            "predicate": predicate,
            "payload": payload,
            "web_uses": web_uses_for(semantic_role, fact_type),
            "evidence": evidence.strip(),
            "extractor": {
                "id": EXTRACTOR_VERSION,
                "source_kind": source_kind,
                "contract": contract,
                "rule_id": rule_id,
                "rule_version": rule_version,
            },
            "confidence": confidence,
        }
        if secondary_roles:
            row["secondary_roles"] = secondary_roles
        if notes:
            row["notes"] = notes
        return row


def payload_with_attached_context(card: dict[str, Any], source_field: str, payload: dict[str, Any]) -> dict[str, Any]:
    card_types = {str(item).casefold() for item in card.get("card_type_ids", []) or []}
    tag_names = {
        str(tag.get("name") if isinstance(tag, dict) else tag).casefold()
        for tag in card.get("tags", []) or []
    }
    if source_field != "effect_lines" or not ({"gear", "equipment"} & (card_types | tag_names)):
        return payload
    payload = dict(payload)
    payload.setdefault("activation_context", "attached")
    payload.setdefault("inactive_until_attached", True)
    payload.setdefault("applies_to", "top_most_card")
    return payload


def contract_fact(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    fact_spec: dict[str, Any],
    evidence: str,
    payload: dict[str, Any],
) -> dict[str, Any]:
    modality = fact_spec.get("modality")
    if modality == "line_optional":
        payload = payload_with_line_modality(line, payload, evidence=evidence)
    elif isinstance(modality, str):
        payload = payload_with_line_modality(line, payload, default=modality, evidence=evidence)
    return builder.fact(
        card,
        source_field=source_field,
        line_index=line_index,
        line_text=line,
        evidence=evidence,
        clause_group_id=line_clause_group_id(card["play_id"], source_field, line_index),
        semantic_role=fact_spec["semantic_role"],
        fact_type=fact_spec["fact_type"],
        predicate=fact_spec["predicate"],
        payload=payload,
        confidence=float(rule.get("confidence", 0.86)),
        rule_id=rule["rule_id"],
        rule_version=rule.get("rule_version"),
        source_kind="contract_rule",
        contract="semantic_extraction_rules",
    )


def build_template_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    evidence = rule_evidence(rule, match)
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            fact_spec,
            evidence,
            resolve_template(fact_spec.get("payload", {}), match),
        )
        for fact_spec in rule.get("facts", [])
    ]


def build_trigger_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    evidence = rule_evidence(rule, match)
    defaults = dict(rule.get("event_defaults", {}) or {})
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "trigger_observed", "fact_type": "event_trigger", "predicate": "observe_event"},
            evidence,
            {"event": {"id": event_id, **defaults}, "modality": "required"},
        )
        for event_id in rule.get("events", []) or []
    ]


def build_condition_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "restriction_or_permission", "fact_type": "restriction", "predicate": "require"},
            rule_evidence(rule, match),
            {"conditions": [{"state": rule["condition_id"]}], "duration": "while"},
        )
    ]


def build_additional_cost_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    verb = match.group("verb").casefold()
    body = match.group("body")
    costs: list[dict[str, Any]] = []
    if verb == "spend" and (amount := re.search(r"(?P<amount>\d+) XP", body, re.I)):
        costs.append({"resource": "xp", "amount": int(amount.group("amount"))})
    elif verb == "pay":
        costs.extend(symbol_costs(body))
    elif verb == "kill":
        costs.append({"action": "kill", "object": body.strip(), "event": "unit_dies"})
    else:
        costs.append({"action": verb, "object": body.strip()})
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "cost_or_requirement", "fact_type": "additional_cost", "predicate": verb},
            rule_evidence(rule, match),
            {"costs": costs, "modality": "optional", "conditions": [{"applies_to": "play_self"}]},
        )
    ]


def build_activation_cost_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    split = activation_split(line)
    if not split:
        return []
    cost_text, _effect_text = split
    costs = parse_non_symbol_costs(cost_text)
    if not costs:
        return []
    evidence = activation_cost_evidence(cost_text)
    is_repeat_cost = "[repeat]" in cost_text.casefold()
    fact_type = "additional_cost" if is_repeat_cost else "activated_ability_cost"
    payload = {"costs": costs}
    if is_repeat_cost:
        payload.update({"modality": "optional", "conditions": [{"applies_to": "repeat_effect"}], "repeat": True})
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "cost_or_requirement", "fact_type": fact_type, "predicate": "pay", "modality": "line_optional"},
            evidence,
            payload,
        )
    ]


def build_token_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "payoff_output", "fact_type": "token_creation", "predicate": "play_token", "modality": "line_optional"},
            rule_evidence(rule, match),
            token_payload(match, line),
        )
    ]


def draw_payload(match: re.Match[str]) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "outputs": [{"id": "card_drawn", "action": "draw", "object": "card"}],
        "amounts": [{"value": int(match.group("amount")), "unit": "card"}],
    }
    per = match.groupdict().get("per")
    if per:
        normalized_per = re.sub(r"^(?:other\s+|of\s+)+", "", per.strip(), flags=re.I)
        payload["scaling"] = {"per": normalized_per}
    return payload


def build_draw_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "payoff_output", "fact_type": "card_flow", "predicate": "draw", "modality": "line_optional"},
            rule_evidence(rule, match),
            draw_payload(match),
        )
    ]


def build_counter_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    raw_object = match.group("object").casefold()
    tail = re.split(r"\s+and\s+give\b", match.group("tail"), maxsplit=1, flags=re.I)[0]
    target_kind = "spell_or_ability" if "ability" in raw_object else "spell"
    target: dict[str, Any] = {"kind": target_kind}
    if "enemy" in raw_object:
        target["controller"] = "opponent"
    if "costs no more" in tail.casefold():
        target["cost_limit"] = tail.strip()
    if "unless" in tail.casefold():
        target["condition"] = tail.strip()
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "event_produced", "fact_type": "produced_event", "predicate": "counter", "modality": "line_optional"},
            rule_evidence(rule, match),
            {
                "event": {"id": "spell_countered", "produced": True},
                "target": target,
                "outputs": [{"id": "spell_countered", "action": "counter", "object": target_kind}],
                "polarity": "prevention",
            },
        )
    ]


def clean_control_target(raw: str) -> str:
    target = raw.strip()
    target = re.split(r"\s*,", target, maxsplit=1)[0].strip()
    target = re.split(
        r"\s+and\s+(?:exhaust|recall|ready|move|kill|return)\b",
        target,
        maxsplit=1,
        flags=re.I,
    )[0].strip()
    target = re.sub(r"\s+at end of turn\b.*$", "", target, flags=re.I).strip()
    return target


def control_change_target(raw: str, line: str) -> dict[str, Any]:
    target = normalize_target(raw)
    target_norm = normalize_text(raw)
    line_norm = normalize_text(line)
    pronoun_refers_to_enemy_unit = target_norm in {"it", "that unit"} and "enemy unit" in line_norm
    if "spell" in target_norm:
        target["kind"] = "spell"
    elif "unit" in target_norm or pronoun_refers_to_enemy_unit:
        target["kind"] = "unit"
    if "enemy" in target_norm or pronoun_refers_to_enemy_unit:
        target["controller"] = "opponent"
        target.setdefault("scope", "enemy")
    if "at a battlefield" in target_norm or (pronoun_refers_to_enemy_unit and "at a battlefield" in line_norm):
        target["location"] = "battlefield"
    if target.get("kind") != "card" and target.get("scope") == "self":
        target.pop("scope", None)
    return target


def build_control_change_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    verb = match.group("verb").casefold()
    target_raw = clean_control_target(match.group("target"))
    if not target_raw:
        return []
    action = "lose_control" if verb == "lose" else "gain_control"
    output_id = "control_lost" if verb == "lose" else "control_gained"
    target = control_change_target(target_raw, line)
    payload: dict[str, Any] = {
        "event": {"id": "control_changed", "produced": True},
        "target": target,
        "outputs": [{"id": output_id, "action": action, "object": target.get("kind") or "card"}],
        "polarity": "lose" if verb == "lose" else "gain",
    }
    if "end of turn" in match.group(0).casefold():
        payload["timing"] = "end_of_turn"
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "event_produced", "fact_type": "control_change", "predicate": action, "modality": "line_optional"},
            f"{match.group('verb')} control of {target_raw}",
            payload,
        )
    ]


def resource_from_symbol(symbol: str) -> dict[str, Any]:
    if symbol.casefold() == "energy":
        return {"resource": "energy", "amount": 1, "symbol": symbol}
    if match := ENERGY_SYMBOL_RE.fullmatch(symbol):
        return {"resource": "energy", "amount": int(match.group("amount")), "symbol": symbol}
    if match := RUNE_SYMBOL_RE.fullmatch(symbol):
        domain = normalize_rune_domain(match.group("domain"))
        return {"resource": "rune", "domain": domain, "amount": 1, "symbol": symbol}
    return {"resource": "unknown", "symbol": symbol}


def normalize_rune_domain(domain: Any) -> str:
    value = str(domain or "").casefold()
    return "any" if value in {"rainbow", "any"} else value


def add_resource_payload(symbols_text: str, amount_text: str | None) -> dict[str, Any]:
    symbols = [match.group(0) for match in ADD_RESOURCE_SYMBOL_RE.finditer(symbols_text)]
    if not symbols:
        symbols = [symbols_text.strip()]

    amount_key = amount_text.casefold() if isinstance(amount_text, str) else None
    resources_by_key: dict[tuple[str | None, str | None], dict[str, Any]] = {}
    resource_order: list[tuple[str | None, str | None]] = []
    raw_resources = []

    for symbol in symbols:
        resource = resource_from_symbol(symbol)
        amount_value: int | str | None = word_number(amount_text) if amount_text else resource.get("amount")
        if amount_key == "that much":
            amount_value = "variable"
        if amount_key == "an additional":
            amount_value = resource.get("amount")

        resource = dict(resource)
        resource["amount"] = amount_value
        if amount_key == "an additional":
            resource["additional"] = True
        raw_resources.append(resource)

        key = (resource.get("resource"), resource.get("domain"))
        if key not in resources_by_key:
            amount = {"unit": resource.get("resource"), "value": amount_value}
            if resource.get("domain"):
                amount["domain"] = resource["domain"]
            if amount_key == "an additional":
                amount["additional"] = True
            resources_by_key[key] = amount
            resource_order.append(key)
            continue

        existing = resources_by_key[key]
        existing_value = existing.get("value")
        if existing_value == "variable" or amount_value == "variable":
            existing["value"] = "variable"
        elif isinstance(existing_value, int) and isinstance(amount_value, int):
            existing["value"] = existing_value + amount_value

    amounts = [resources_by_key[key] for key in resource_order]
    payload: dict[str, Any] = {
        "outputs": [
            {
                "id": "resource_added",
                "action": "add_resource",
                "object": "resource" if len(amounts) > 1 else amounts[0].get("unit"),
            }
        ],
        "amounts": amounts,
    }
    if amount_key == "an additional":
        payload["additional"] = True

    if len(amounts) == 1:
        resource = dict(raw_resources[0])
        resource["amount"] = amounts[0].get("value")
        payload["resource"] = resource
    else:
        payload["resources"] = raw_resources
    return payload


def build_add_resource_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    symbols_text = match.groupdict().get("symbols") or match.group("symbol")
    amount_text = match.group("amount")
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "payoff_output", "fact_type": "resource_change", "predicate": "add_resource", "modality": "line_optional"},
            rule_evidence(rule, match),
            add_resource_payload(symbols_text, amount_text),
        )
    ]


def resource_payment_costs(cost_text: str) -> list[dict[str, Any]]:
    text = cost_text.strip()
    if match := re.fullmatch(r"(?:(?P<amount>any amount of|\d+)\s+)?Energy", text, re.I):
        amount_text = (match.group("amount") or "1").casefold().strip()
        return [{"resource": "energy", "amount": "variable" if amount_text == "any amount of" else int(amount_text)}]
    if match := re.fullmatch(r"(?:(?P<amount>any amount of|\d+)\s+)?(?P<symbol>:rb_rune_(?P<domain>[a-z]+):)", text, re.I):
        amount_text = (match.group("amount") or "1").casefold().strip()
        return [
            {
                "resource": "rune",
                "domain": normalize_rune_domain(match.group("domain")),
                "amount": "variable" if amount_text == "any amount of" else int(amount_text),
                "symbol": match.group("symbol"),
            }
        ]
    return symbol_costs(text)


def action_from_pay_effect(effect_text: str) -> str:
    text = normalize_text(effect_text)
    if text.startswith("[add]"):
        return "add_resource"
    if text.startswith("score"):
        return "score"
    if text.startswith("deal"):
        return "damage"
    if text.startswith("heal"):
        return "heal"
    if text.startswith("[buff]"):
        return "buff"
    return "effect"


def payer_from_pay_match(match: re.Match[str]) -> dict[str, str] | None:
    payer = match.groupdict().get("payer")
    if not payer:
        return None
    normalized_payer = normalize_text(payer)
    if normalized_payer in {"its controller", "that unit's controller"}:
        return {"kind": "controller", "scope": "affected_object", "raw": payer}
    if normalized_payer == "you":
        return {"kind": "player", "scope": "you", "raw": payer}
    if normalized_payer == "they":
        return {"kind": "player", "scope": "triggered_player", "raw": payer}
    return {"raw": payer}


def build_pay_resource_cost_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    costs = resource_payment_costs(match.group("cost"))
    if not costs:
        return []
    effect_text = match.group("effect").strip()
    payload: dict[str, Any] = {"costs": costs, "conditions": [{"applies_to": action_from_pay_effect(effect_text), "effect": effect_text}]}
    if payer := payer_from_pay_match(match):
        payload["payer"] = payer
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "cost_or_requirement", "fact_type": "activated_ability_cost", "predicate": "pay", "modality": "line_optional"},
            rule_evidence(rule, match),
            payload,
        )
    ]


def build_keyword_grant_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    evidence = rule_evidence(rule, match)
    keywords = [
        keyword
        for keyword in keyword_ids_from_text(match.group("keywords"))
        if keyword not in NON_GRANTED_BRACKET_ACTION_KEYWORDS
    ]
    if not keywords:
        return []
    target_raw = re.sub(r"^While I'm [^,]+,\s*", "", match.group("target").strip(), flags=re.I)
    target = {"raw": target_raw}
    target_raw_key = target["raw"].casefold()
    if target_raw_key in {"it", "that unit"}:
        evidence_start = line.casefold().find(evidence.casefold())
        prefix = line[:evidence_start] if evidence_start >= 0 else line
        if re.search(r"\bchoose (?:one |a |an |another |friendly |enemy |target )*unit\b", prefix, re.I):
            target = {"raw": "chosen unit", "kind": "unit", "scope": "chosen"}
        elif re.search(r"\bunit token\b", prefix, re.I):
            target = {"raw": "created unit token", "kind": "unit", "scope": "created", "token_state": "token"}
    payload: dict[str, Any] = {
        "target": target,
        "keywords": keywords,
        "outputs": [{"id": "keyword_granted", "action": "gain_keyword", "object": "keyword"}],
    }
    if "this turn" in evidence.casefold():
        payload["duration"] = "this_turn"
    if "this combat" in evidence.casefold():
        payload["duration"] = "this_combat"
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "state_or_modifier", "fact_type": "keyword_grant", "predicate": "gain_keyword", "modality": "line_optional"},
            evidence,
            payload,
        )
    ]


def kind_from_play_target(raw: str) -> str:
    lowered = raw.casefold()
    if re.search(r"\b(?:equipment|gear)\b", lowered):
        return "gear"
    if re.search(r"\bspell\b", lowered):
        return "spell"
    if re.search(r"\bunit\b", lowered):
        return "unit"
    return "card"


def zone_from_text(raw: str) -> str:
    lowered = raw.casefold()
    if "trash" in lowered:
        return "trash"
    if "banished" in lowered:
        return "banished"
    if "hand" in lowered:
        return "hand"
    if "deck" in lowered:
        return "main_deck"
    return "unknown"


def cost_constraints_from_text(raw: str) -> list[dict[str, Any]]:
    constraints: list[dict[str, Any]] = []
    for match in re.finditer(r"no more than :rb_energy_(?P<amount>\d+):", raw, re.I):
        constraints.append({"resource": "energy", "maximum": int(match.group("amount"))})
    for match in re.finditer(r"no more than :rb_rune_(?P<domain>[a-z]+):", raw, re.I):
        domain = match.group("domain").casefold()
        constraints.append({"resource": "rune", "domain": "any" if domain == "rainbow" else domain, "maximum": 1})
    return constraints


def build_play_from_zone_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    evidence = rule_evidence(rule, match)
    target_text = match.group("target").strip()
    kind = kind_from_play_target(target_text)
    zone = zone_from_text(match.group("zone"))
    event_id = f"{kind}_played" if kind in {"gear", "spell", "unit"} else "card_played"
    payload: dict[str, Any] = {
        "event": {"id": event_id, "produced": True},
        "target": {"kind": kind, "raw": target_text, "zone": zone},
        "outputs": [{"id": event_id, "action": "play", "object": kind}],
    }
    constraints = cost_constraints_from_text(evidence)
    if constraints:
        payload["cost_constraints"] = constraints
    if "ignoring" in evidence.casefold():
        payload["modifiers"] = [{"cost": "ignored"}]
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "event_produced", "fact_type": "produced_event", "predicate": "play", "modality": "line_optional"},
            evidence,
            payload,
        )
    ]


def build_look_reveal_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    amount = word_number(match.group("amount")) if match.group("amount") else 1
    predicate = "look" if match.group("verb").casefold().startswith("look") else "reveal"
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "payoff_output", "fact_type": "card_flow", "predicate": predicate, "modality": "line_optional"},
            rule_evidence(rule, match),
            {
                "object": {"kind": "card", "zone": "main_deck", "location": "top"},
                "target": {"controller": (match.group("deck") or "your").casefold()},
                "amounts": [{"value": amount, "unit": "card"}],
            },
        )
    ]


def build_recycle_card_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    if re.search(r"\bWhen you recycle\b", line[: match.start() + len(match.group(0))], re.I):
        return []
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "event_produced", "fact_type": "card_flow", "predicate": "recycle", "modality": "line_optional"},
            rule_evidence(rule, match),
            {
                "event": {"id": "card_recycled", "produced": True},
                "target": {"kind": "card", "zone": "main_deck"},
                "outputs": [{"id": "card_recycled", "action": "recycle", "object": "card"}],
            },
        )
    ]


def build_recycle_rune_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    if re.search(r"\bWhen you recycle\b", line[: match.start() + len(match.group(0))], re.I):
        return []
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "event_produced", "fact_type": "resource_change", "predicate": "recycle", "modality": "line_optional"},
            rule_evidence(rule, match),
            {
                "event": {"id": "rune_recycled", "produced": True},
                "target": {"kind": "rune"},
                "outputs": [{"id": "rune_recycled", "action": "recycle", "object": "rune"}],
            },
        )
    ]


def build_kill_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    event_id = rule["event_id"]
    fact_type = rule.get("fact_type") or ("produced_event" if event_id == "self_dies" else "removal")
    evidence = rule_evidence(rule, match)
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "event_produced", "fact_type": fact_type, "predicate": "kill"},
            evidence,
            {
                "event": {"id": event_id, "produced": True},
                "target": rule.get("target", {}),
                "modality": "must" if "must" in evidence.casefold() else ("optional" if line_has_optional_governor(line) else "required"),
            },
        )
    ]


def build_repeat_effect_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    evidence = rule_evidence(rule, match)
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "payoff_output", "fact_type": "payoff", "predicate": "repeat_effect", "modality": "line_optional"},
            evidence,
            {"outputs": [{"action": "repeat_effect", "object": "this_gear_play_effect" if "gear" in evidence.casefold() else "referenced_effect"}]},
        )
    ]


def build_gear_cost_modifier_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    direction = match.group("direction").casefold()
    action = "reduce_cost" if direction == "less" else "increase_cost"
    output_id = "gear_cost_reduced" if direction == "less" else "gear_cost_increased"
    evidence = rule_evidence(rule, match)
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "state_or_modifier", "fact_type": "static_modifier", "predicate": action, "modality": "line_optional"},
            evidence,
            {
                "target": {
                    "kind": "card",
                    "card_types": ["gear"],
                    "controller": "friendly",
                    "exclude": ["token"],
                    "ordinal": "first_each_turn" if "first" in evidence.casefold() else None,
                },
                "amounts": [{"value": int(match.group("amount")), "unit": "energy", "symbol": f":rb_energy_{match.group('amount')}:"}],
                "outputs": [{"id": output_id, "action": action, "object": "gear"}],
                "duration": "each_turn",
            },
        )
    ]


def build_score_rule_facts(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rule: dict[str, Any],
    match: re.Match[str],
) -> list[dict[str, Any]]:
    amount = int(match.group("amount") or match.group("needed"))
    return [
        contract_fact(
            card,
            source_field,
            line_index,
            line,
            builder,
            rule,
            {"semantic_role": "payoff_output", "fact_type": "score_change", "predicate": "score", "modality": "line_optional"},
            rule_evidence(rule, match),
            {"amounts": [{"value": amount, "unit": "point"}]},
        )
    ]


CONTRACT_BUILDERS = {
    "activation_cost": build_activation_cost_rule_facts,
    "additional_cost": build_additional_cost_rule_facts,
    "add_resource": build_add_resource_rule_facts,
    "condition_state": build_condition_rule_facts,
    "control_change": build_control_change_rule_facts,
    "counter_spell": build_counter_rule_facts,
    "draw_cards": build_draw_rule_facts,
    "gear_cost_modifier": build_gear_cost_modifier_rule_facts,
    "keyword_grant": build_keyword_grant_rule_facts,
    "kill_event": build_kill_rule_facts,
    "look_reveal_top_deck": build_look_reveal_rule_facts,
    "pay_resource_cost": build_pay_resource_cost_rule_facts,
    "play_from_zone": build_play_from_zone_rule_facts,
    "recycle_card": build_recycle_card_rule_facts,
    "recycle_rune": build_recycle_rune_rule_facts,
    "repeat_effect": build_repeat_effect_rule_facts,
    "score_points": build_score_rule_facts,
    "template": build_template_rule_facts,
    "token_creation": build_token_rule_facts,
    "trigger_events": build_trigger_rule_facts,
}


def contract_facts_for_line(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    rules: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for rule in rules:
        source_fields = rule.get("source_fields")
        if source_fields and source_field not in source_fields:
            continue
        build = CONTRACT_BUILDERS.get(rule.get("builder"))
        if build is None:
            raise ValueError(f"Unknown semantic extraction builder: {rule.get('builder')} in {rule.get('rule_id')}")
        for match in rule["_pattern"].finditer(line):
            rows.extend(build(card, source_field, line_index, line, builder, rule, match))
    return rows


def official_facts(card: dict[str, Any], builder: FactBuilder) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    group_id = f"clause:{card['play_id']}:official"

    for domain in card.get("domain_ids", []):
        rows.append(
            builder.fact(
                card,
                source_field="official_field",
                line_index=None,
                line_text=f"domain:{domain}",
                evidence=str(domain),
                clause_group_id=group_id,
                semantic_role="identity_or_descriptor",
                fact_type="identity_reference",
                predicate="has_domain",
                payload={"object": {"kind": "domain", "id": domain}},
                confidence=1.0,
                rule_id="official_domain",
                source_kind="structural_field",
                contract="cards_normalized",
            )
        )

    for card_type in card.get("card_type_ids", []):
        rows.append(
            builder.fact(
                card,
                source_field="official_field",
                line_index=None,
                line_text=f"card_type:{card_type}",
                evidence=str(card_type),
                clause_group_id=group_id,
                semantic_role="identity_or_descriptor",
                fact_type="identity_reference",
                predicate="has_card_type",
                payload={"object": {"kind": "card_type", "id": card_type}},
                confidence=1.0,
                rule_id="official_card_type",
                source_kind="structural_field",
                contract="cards_normalized",
            )
        )

    for tag in card.get("tags", []) or []:
        tag_name = tag.get("name") if isinstance(tag, dict) else tag
        if not tag_name:
            continue
        rows.append(
            builder.fact(
                card,
                source_field="official_field",
                line_index=None,
                line_text=f"tag:{tag_name}",
                evidence=str(tag_name),
                clause_group_id=group_id,
                semantic_role="identity_or_descriptor",
                fact_type="identity_reference",
                predicate="has_tag",
                payload={"object": {"kind": "tag", "id": slug(str(tag_name)), "label": str(tag_name)}},
                confidence=1.0,
                rule_id="official_tag",
                source_kind="structural_field",
                contract="cards_normalized",
            )
        )

    if "rune" in set(card.get("card_type_ids", []) or []):
        for domain in card.get("domain_ids", []) or []:
            if domain == "colorless":
                continue
            rows.append(
                builder.fact(
                    card,
                    source_field="official_field",
                    line_index=None,
                    line_text=f"basic_rune:{domain}",
                    evidence=f"basic_rune:{domain}",
                    clause_group_id=group_id,
                    semantic_role="payoff_output",
                    fact_type="resource_change",
                    predicate="add_resource",
                    payload={
                        "outputs": [{"id": "resource_added", "action": "add_resource", "object": "rune"}],
                        "amounts": [{"value": 1, "unit": "rune", "domain": normalize_rune_domain(domain)}],
                        "resource": {"resource": "rune", "domain": normalize_rune_domain(domain), "amount": 1},
                        "source": "basic_rune",
                    },
                    confidence=1.0,
                    rule_id="official_basic_rune_resource",
                    source_kind="structural_field",
                    contract="cards_normalized",
                )
            )

    for stat_name in ("energy", "might", "power", "might_bonus"):
        value = card.get(stat_name)
        if value is None:
            continue
        rows.append(
            builder.fact(
                card,
                source_field="official_field",
                line_index=None,
                line_text=f"{stat_name}:{value}",
                evidence=f"{stat_name}:{value}",
                clause_group_id=group_id,
                semantic_role="identity_or_descriptor",
                fact_type="stat_change",
                predicate="has_stat",
                payload={"stat": stat_name, "amounts": [{"value": value, "unit": stat_name}]},
                confidence=1.0,
                rule_id="official_stat",
                source_kind="structural_field",
                contract="cards_normalized",
            )
        )
    return rows


def trigger_facts(card: dict[str, Any], source_field: str, line_index: int, line: str, builder: FactBuilder) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    group_id = line_clause_group_id(card["play_id"], source_field, line_index)

    for rule_id, pattern, event_ids, defaults in TRIGGER_PATTERNS:
        for match in pattern.finditer(line):
            evidence = match.group(0)
            for event_id in event_ids:
                marker = (event_id, evidence.casefold())
                if marker in seen:
                    continue
                seen.add(marker)
                event = {"id": event_id, **defaults}
                rows.append(
                    builder.fact(
                        card,
                        source_field=source_field,
                        line_index=line_index,
                        line_text=line,
                        evidence=evidence,
                        clause_group_id=group_id,
                        semantic_role="trigger_observed",
                        fact_type="event_trigger",
                        predicate="observe_event",
                        payload={"event": event, "modality": "required"},
                        confidence=0.9,
                        rule_id=f"trigger_{rule_id}",
                    )
                )
    return rows


def condition_facts(card: dict[str, Any], source_field: str, line_index: int, line: str, builder: FactBuilder) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for rule_id, pattern, condition_id in STATIC_CONDITION_PATTERNS:
        for match in pattern.finditer(line):
            rows.append(
                builder.fact(
                    card,
                    source_field=source_field,
                    line_index=line_index,
                    line_text=line,
                    evidence=match.group(0),
                    clause_group_id=line_clause_group_id(card["play_id"], source_field, line_index),
                    semantic_role="restriction_or_permission",
                    fact_type="restriction",
                    predicate="require",
                    payload={"conditions": [{"state": condition_id}], "duration": "while"},
                    confidence=0.86,
                    rule_id=f"condition_{rule_id}",
                )
            )
    if match := re.search(r"\bIf you paid my additional cost, you don't kill a unit this way\b", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=line_clause_group_id(card["play_id"], source_field, line_index),
                semantic_role="restriction_or_permission",
                fact_type="restriction",
                predicate="prevent",
                payload={
                    "conditions": [{"if": "additional_cost_paid"}],
                    "modifiers": [{"action": "kill", "target": "your_unit", "polarity": "prevention"}],
                },
                confidence=0.9,
                rule_id="restriction_additional_cost_prevents_self_kill",
            )
        )
    return rows


def symbol_costs(text: str) -> list[dict[str, Any]]:
    costs: list[dict[str, Any]] = []
    for match in ENERGY_SYMBOL_RE.finditer(text):
        costs.append({"resource": "energy", "amount": int(match.group("amount")), "symbol": match.group(0)})
    for match in RUNE_SYMBOL_RE.finditer(text):
        costs.append({"resource": "rune", "domain": normalize_rune_domain(match.group("domain")), "amount": 1, "symbol": match.group(0)})
    if re.search(r":rb_exhaust:", text, re.I):
        costs.append({"action": "exhaust", "subject": "self", "symbol": ":rb_exhaust:"})
    return costs


def parse_non_symbol_costs(text: str) -> list[dict[str, Any]]:
    costs = symbol_costs(text)
    for match in re.finditer(r"\bSpend (?P<amount>\d+) XP\b", text, re.I):
        costs.append({"resource": "xp", "amount": int(match.group("amount"))})
    for match in re.finditer(r"\bPay (?P<amount>any amount of|\d+)?\s*Energy\b", text, re.I):
        amount_text = (match.group("amount") or "1").casefold().strip()
        costs.append({"resource": "energy", "amount": "variable" if amount_text == "any amount of" else int(amount_text)})
    for match in re.finditer(r"\bPay (?P<amount>any amount of|\d+)?\s*(?P<symbol>:rb_rune_(?P<domain>[a-z]+):)", text, re.I):
        if not match.group("amount"):
            continue
        symbol = match.group("symbol")
        costs = [
            cost
            for cost in costs
            if not (cost.get("resource") == "rune" and str(cost.get("symbol") or "").casefold() == symbol.casefold())
        ]
        amount_text = match.group("amount").casefold().strip()
        costs.append(
            {
                "resource": "rune",
                "domain": normalize_rune_domain(match.group("domain")),
                "amount": "variable" if amount_text == "any amount of" else int(amount_text),
                "symbol": symbol,
            }
        )
    if re.search(r"\bKill this\b", text, re.I):
        costs.append({"action": "kill", "subject": "self", "event": "self_dies"})
    if match := re.search(r"\bDiscard (?P<amount>\d+)\b", text, re.I):
        costs.append({"action": "discard", "amount": int(match.group("amount")), "object": "card"})
    if match := re.search(r"\bRecycle (?P<amount>\d+|a|an|one|two|three|four|five|six)?\s*(?P<object>[^,:]*)", text, re.I):
        amount = word_number(match.group("amount")) if match.group("amount") else None
        cost = {"action": "recycle", "object": match.group("object").strip() or "card"}
        if amount is not None:
            cost["amount"] = amount
        costs.append(cost)
    return costs


def activation_split(line: str) -> tuple[str, str] | None:
    if re.search(r"\bhave all\s+:rb_exhaust:\s+abilities\b", line, re.I):
        return None
    candidates = list(re.finditer(r":\s+", line))
    for separator in candidates:
        cost_text = line[: separator.start() + 1].strip()
        effect_text = line[separator.end() :].strip()
        if not cost_text or not effect_text:
            continue
        if re.match(r"\s*(?:less|more|or less|or more)\b", effect_text, re.I):
            continue
        if re.match(r"\s*(?:When|If|While)\b", cost_text, re.I):
            continue
        if re.search(r"\bcost(?:s|ing)?\b", cost_text, re.I) and not re.search(
            r"\b(?:pay|spend|kill|discard|recycle|exhaust)\b|:rb_exhaust:",
            cost_text,
            re.I,
        ):
            continue
        if not (RB_SYMBOL_RE.search(cost_text) or re.search(r"\b(?:Kill|Discard|Recycle|Pay|Spend|Exhaust)\b", cost_text, re.I)):
            continue
        return cost_text, effect_text
    return None


def activation_cost_evidence(cost_text: str) -> str:
    text = cost_text.strip()
    if text.endswith("::"):
        return text[:-1].strip()
    if re.search(r":rb_[a-z0-9_]+:$", text, re.I):
        return text
    return text.rstrip(":").strip()


def cost_facts(card: dict[str, Any], source_field: str, line_index: int, line: str, builder: FactBuilder) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    for match in re.finditer(r"\bYou may (?P<verb>pay|spend|kill|discard|recycle) (?P<body>.+?) as an additional cost to play me\b", line, re.I):
        verb = match.group("verb").casefold()
        body = match.group("body")
        costs: list[dict[str, Any]] = []
        if verb == "spend" and (amount := re.search(r"(?P<amount>\d+) XP", body, re.I)):
            costs.append({"resource": "xp", "amount": int(amount.group("amount"))})
        elif verb == "pay":
            costs.extend(symbol_costs(body))
        elif verb == "kill":
            costs.append({"action": "kill", "object": body.strip(), "event": "unit_dies"})
        else:
            costs.append({"action": verb, "object": body.strip()})
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=line_clause_group_id(card["play_id"], source_field, line_index),
                semantic_role="cost_or_requirement",
                fact_type="additional_cost",
                predicate=verb,
                payload={"costs": costs, "modality": "optional", "conditions": [{"applies_to": "play_self"}]},
                confidence=0.9,
                rule_id=f"additional_cost_{verb}",
            )
        )

    for match in re.finditer(r"\byou may exhaust me\b(?=\s+to\b)", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=line_clause_group_id(card["play_id"], source_field, line_index),
                semantic_role="cost_or_requirement",
                fact_type="activated_ability_cost",
                predicate="exhaust",
                payload={"costs": [{"action": "exhaust", "subject": "self"}], "modality": "optional"},
                confidence=0.9,
                rule_id="optional_exhaust_self",
            )
        )

    if split := activation_split(line):
        cost_text, _effect_text = split
        costs = parse_non_symbol_costs(cost_text)
        if costs:
            evidence = activation_cost_evidence(cost_text)
            is_repeat_cost = "[repeat]" in cost_text.casefold()
            payload = {"costs": costs}
            if is_repeat_cost:
                payload.update({"modality": "optional", "conditions": [{"applies_to": "repeat_effect"}], "repeat": True})
            rows.append(
                builder.fact(
                    card,
                    source_field=source_field,
                    line_index=line_index,
                    line_text=line,
                    evidence=evidence,
                    clause_group_id=line_clause_group_id(card["play_id"], source_field, line_index),
                    semantic_role="cost_or_requirement",
                    fact_type="additional_cost" if is_repeat_cost else "activated_ability_cost",
                    predicate="pay",
                    payload=payload_with_line_modality(line, payload, evidence=evidence),
                    confidence=0.88,
                    rule_id="activation_cost",
                )
            )
    return rows


def intrinsic_unbracketed_keyword_match(line: str) -> re.Match[str] | None:
    return re.match(rf"(?P<keyword>{'|'.join(sorted(UNBRACKETED_INTRINSIC_KEYWORDS))})\s*\(", line.strip(), re.I)


def is_intrinsic_bracket_keyword_context(line: str, start: int) -> bool:
    prefix = line[:start].strip()
    if not prefix:
        return True
    if not re.fullmatch(r"(?:\[[^\]]+\]\s*)+", prefix):
        return False
    prior_tokens = [token.strip() for token in BRACKET_TOKEN_RE.findall(prefix)]
    return all(is_angle_marker(token) or slug(token) == "level" for token in prior_tokens)


def is_granted_keyword_context(line: str, start: int) -> bool:
    prefix = normalize_text(line[:start])
    sentence_start = max(prefix.rfind("."), prefix.rfind(";"))
    local_prefix = prefix[sentence_start + 1 :] if sentence_start >= 0 else prefix
    return bool(re.search(r"\b(?:give|gives|gain|gains|have|has)(?:\s+[^.;:]*)?$", local_prefix))


def keyword_fact_payload(keyword_id: str, label: str) -> dict[str, Any]:
    return {"object": {"kind": "keyword", "id": keyword_id, "label": label}}


def keyword_facts(card: dict[str, Any], source_field: str, line_index: int, line: str, builder: FactBuilder) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if match := intrinsic_unbracketed_keyword_match(line):
        keyword = match.group("keyword")
        keyword_id = slug(keyword)
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=keyword,
                clause_group_id=f"clause:{card['play_id']}:{source_field}:{line_index}:keyword",
                semantic_role="identity_or_descriptor",
                fact_type="keyword_marker",
                predicate="has_keyword",
                payload=keyword_fact_payload(keyword_id, keyword),
                confidence=0.94,
                rule_id="keyword_marker_unbracketed",
            )
        )
    for match in BRACKET_TOKEN_RE.finditer(line):
        keyword = match.group(1).strip()
        if not keyword or is_angle_marker(keyword):
            continue
        keyword_ids = keyword_ids_from_text(match.group(0))
        if not keyword_ids:
            continue
        keyword_id = keyword_ids[0]
        if is_granted_keyword_context(line, match.start()):
            continue
        intrinsic = is_intrinsic_bracket_keyword_context(line, match.start())
        semantic_role = "identity_or_descriptor" if intrinsic else "targeting_or_scope"
        fact_type = "keyword_marker" if intrinsic else "keyword_reference"
        predicate = "has_keyword" if intrinsic else "reference_keyword"
        rule_id = "keyword_marker" if intrinsic else "keyword_reference"
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=f"clause:{card['play_id']}:{source_field}:{line_index}:keyword",
                semantic_role=semantic_role,
                fact_type=fact_type,
                predicate=predicate,
                payload=keyword_fact_payload(keyword_id, keyword),
                confidence=0.96 if intrinsic else 0.86,
                rule_id=rule_id,
            )
        )
    return rows


def token_payload(match: re.Match[str], line: str) -> dict[str, Any]:
    count = word_number(match.group("count")) or 1
    might = int(match.group("might")) if match.group("might") else None
    tag = match.group("tag")
    token_type = match.group("type").casefold()
    state_words = []
    if match.group("pre_state"):
        state_words.append(match.group("pre_state").casefold())
    if match.group("post_state"):
        state_words.append(match.group("post_state").casefold())
    keywords = [slug(token) for token in BRACKET_TOKEN_RE.findall(match.group(0)) if token not in {">", "<"}]
    location = None
    location_context = match.group(0) + line[match.end() : match.end() + 80]
    if re.search(r"\b(?:to|into|in|at) your base\b", location_context, re.I):
        location = "your_base"
    elif re.search(r"\bhere\b", location_context, re.I):
        location = "here"
    elif re.search(r"\bto its base\b", location_context, re.I):
        location = "its_base"
    obj: dict[str, Any] = {
        "kind": "token",
        "card_types": [token_type],
        "tags": [tag],
    }
    if count != 1:
        obj["amount"] = count
    if might is not None:
        obj["stats"] = {"might": might}
    if state_words:
        obj["state"] = sorted(set(state_words))
    if keywords:
        obj["keywords"] = sorted(set(keywords))
    output_id = f"{slug(tag)}_{slug(token_type)}_token_created"
    payload = {
        "event": {"id": "token_created", "produced": True},
        "outputs": [{"id": output_id, "action": "play_token", "object": f"{tag} {token_type} token"}],
        "object": obj,
    }
    if location:
        payload["target"] = {"location": location}
    return payload


TOKEN_PATTERN = re.compile(
    r"\bplay (?P<count>a|an|one|two|three|four|five|six|\d+)\s+"
    r"(?:(?P<pre_state>ready|exhausted)\s+)?"
    r"(?:(?P<might>\d+)\s+:rb_might:\s+)?"
    r"(?P<tag>[A-Z][A-Za-z'-]+)\s+"
    r"(?P<type>unit|gear)\s+tokens?"
    r"(?:\s+with\s+\[[^\]]+\])?"
    r"(?:\s+(?P<post_state>ready|exhausted))?"
    r"(?:\s+(?:to|into|in|at)\s+(?:your base|the base|a battlefield|different locations|here))?",
    re.I,
)
DRAW_PATTERN = re.compile(r"\b[Dd]raws? (?P<amount>\d+)(?:\s+for each (?P<per>[^.,]+?)(?=\.|,|$))?")


def effect_facts(card: dict[str, Any], source_field: str, line_index: int, line: str, builder: FactBuilder) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    base_group = line_clause_group_id(card["play_id"], source_field, line_index)

    for match in TOKEN_PATTERN.finditer(line):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="payoff_output",
                fact_type="token_creation",
                predicate="play_token",
                payload=payload_with_line_modality(line, token_payload(match, line), evidence=match.group(0)),
                confidence=0.88,
                rule_id="play_token",
            )
        )

    for match in DRAW_PATTERN.finditer(line):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="payoff_output",
                fact_type="card_flow",
                predicate="draw",
                payload=payload_with_line_modality(line, draw_payload(match), evidence=match.group(0)),
                confidence=0.94,
                rule_id="draw_cards",
            )
        )

    if match := re.search(r"\bput a card from your hand on the top or bottom of your Main Deck\b", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="payoff_output",
                fact_type="card_flow",
                predicate="move",
                payload=payload_with_line_modality(line, {
                    "outputs": [{"id": "deck_card_put_top_or_bottom", "action": "move", "object": "card"}],
                    "object": {"kind": "card", "zone": "hand"},
                    "target": {"zone": "main_deck", "location": "top_or_bottom"},
                }, evidence=match.group(0)),
                confidence=0.9,
                rule_id="put_card_top_bottom",
            )
        )

    for match in re.finditer(r"\bchannel (?P<amount>\d+) rune(?:s)?(?: exhausted)?\b", line, re.I):
        amount = int(match.group("amount"))
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="payoff_output",
                fact_type="resource_change",
                predicate="channel",
                payload=payload_with_line_modality(line, {"outputs": [{"id": "rune_channeled", "action": "channel", "object": "rune"}], "amounts": [{"value": amount, "unit": "rune"}], "modifiers": [{"state": "exhausted"}] if "exhausted" in match.group(0).casefold() else []}),
                confidence=0.9,
                rule_id="channel_rune",
            )
        )

    for match in re.finditer(r"\bgain (?P<amount>\d+) XP\b", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="payoff_output",
                fact_type="resource_change",
                predicate="gain_xp",
                payload=payload_with_line_modality(line, {"outputs": [{"id": "xp_gained", "action": "gain_xp", "object": "xp"}], "amounts": [{"value": int(match.group("amount")), "unit": "xp"}]}),
                confidence=0.9,
                rule_id="gain_xp",
            )
        )

    for match in re.finditer(r"\bCounter (?P<object>an enemy spell or ability|a spell|that spell)(?P<tail>[^.]*)", line, re.I):
        raw_object = match.group("object").casefold()
        evidence = re.split(r"\s+and\s+give\b", match.group(0), maxsplit=1, flags=re.I)[0].strip()
        tail = re.split(r"\s+and\s+give\b", match.group("tail"), maxsplit=1, flags=re.I)[0]
        target_kind = "spell_or_ability" if "ability" in raw_object else "spell"
        target: dict[str, Any] = {"kind": target_kind}
        if "enemy" in raw_object:
            target["controller"] = "opponent"
        if "costs no more" in tail.casefold():
            target["cost_limit"] = tail.strip()
        if "unless" in tail.casefold():
            target["condition"] = tail.strip()
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=evidence,
                clause_group_id=base_group,
                semantic_role="event_produced",
                fact_type="produced_event",
                predicate="counter",
                payload=payload_with_line_modality(line, {
                    "event": {"id": "spell_countered", "produced": True},
                    "target": target,
                    "outputs": [{"id": "spell_countered", "action": "counter", "object": target_kind}],
                    "polarity": "prevention",
                }),
                confidence=0.9,
                rule_id="counter_spell",
            )
        )

    for match in re.finditer(r"\bReturn (?P<object>[^.]+?) to (?P<owner>its|their|your) owner'?s hand\b", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="payoff_output",
                fact_type="movement",
                predicate="return_to_hand",
                payload=payload_with_line_modality(line, {
                    "event": {"id": "card_moved", "produced": True},
                    "object": {"raw": match.group("object").strip()},
                    "target": {"zone": "hand", "owner": match.group("owner").casefold()},
                    "outputs": [{"id": "unit_recalled", "action": "return_to_hand", "object": "card"}],
                }),
                confidence=0.86,
                rule_id="return_to_owner_hand",
            )
        )

    for match in re.finditer(r"\b(?:look at|reveal) the top (?P<amount>\d+|one|two|three|four|five)?\s*cards? of (?P<deck>your|their|an opponent's|each opponent's)?\s*Main Deck\b", line, re.I):
        amount = word_number(match.group("amount")) if match.group("amount") else 1
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="payoff_output",
                fact_type="card_flow",
                predicate="look" if match.group(0).casefold().startswith("look") else "reveal",
                payload=payload_with_line_modality(line, {
                    "object": {"kind": "card", "zone": "main_deck", "location": "top"},
                    "target": {"controller": (match.group("deck") or "your").casefold()},
                    "amounts": [{"value": amount, "unit": "card"}],
                }, evidence=match.group(0)),
                confidence=0.84,
                rule_id="look_reveal_top_deck",
            )
        )

    recycle_patterns = [
        re.compile(r"\bYou may recycle it\b", re.I),
        re.compile(r"\bYou may recycle one or both of them\b", re.I),
        re.compile(r"\bRecycle (?:any of them|the rest|the remaining cards|the other|it|that card|them)\b", re.I),
        re.compile(r"\b(?:their owners recycle them|then recycle it)\b", re.I),
    ]
    for pattern in recycle_patterns:
        for match in pattern.finditer(line):
            if re.search(r"\bWhen you recycle\b", line[: match.start() + len(match.group(0))], re.I):
                continue
            if match.group(0).casefold() == "recycle it" and line[max(0, match.start() - 4) : match.start()].casefold() == "may ":
                continue
            rows.append(
                builder.fact(
                    card,
                    source_field=source_field,
                    line_index=line_index,
                    line_text=line,
                    evidence=match.group(0),
                    clause_group_id=base_group,
                    semantic_role="event_produced",
                    fact_type="card_flow",
                    predicate="recycle",
                    payload=payload_with_line_modality(line, {
                        "event": {"id": "card_recycled", "produced": True},
                        "target": {"kind": "card", "zone": "main_deck"},
                        "outputs": [{"id": "card_recycled", "action": "recycle", "object": "card"}],
                    }, evidence=match.group(0)),
                    confidence=0.88,
                    rule_id="recycle_card",
                )
            )

    for match in re.finditer(r"\brecycle (?:a|one|\d+)?\s*runes?\b", line, re.I):
        if re.search(r"\bWhen you recycle\b", line[: match.start() + len(match.group(0))], re.I):
            continue
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                    semantic_role="event_produced",
                    fact_type="resource_change",
                    predicate="recycle",
                    payload=payload_with_line_modality(line, {
                        "event": {"id": "rune_recycled", "produced": True},
                        "target": {"kind": "rune"},
                        "outputs": [{"id": "rune_recycled", "action": "recycle", "object": "rune"}],
                    }, evidence=match.group(0)),
                    confidence=0.84,
                    rule_id="recycle_rune",
                )
            )

    kill_patterns = [
        (re.compile(r"\bkill an enemy unit\b", re.I), {"kind": "unit", "controller": "opponent", "scope": "enemy"}, "enemy_unit_dies"),
        (re.compile(r"\beach player must kill one of their units\b", re.I), {"kind": "unit", "controller": "each_player", "amount": 1}, "unit_dies"),
        (re.compile(r"\bkill one of their units\b", re.I), {"kind": "unit", "controller": "opponent", "amount": 1}, "unit_dies"),
        (re.compile(r"\bkill up to one gear\b", re.I), {"kind": "gear", "maximum": 1}, "gear_dies"),
        (re.compile(r"\bkill a gear\b", re.I), {"kind": "gear"}, "gear_dies"),
        (re.compile(r"\bKill this\b", re.I), {"kind": "card", "scope": "self"}, "self_dies"),
    ]
    for pattern, target, event_id in kill_patterns:
        for match in pattern.finditer(line):
            fact_type = "produced_event" if event_id == "self_dies" else "removal"
            rows.append(
                builder.fact(
                    card,
                    source_field=source_field,
                    line_index=line_index,
                    line_text=line,
                    evidence=match.group(0),
                    clause_group_id=base_group,
                    semantic_role="event_produced",
                    fact_type=fact_type,
                    predicate="kill",
                    payload=payload_with_line_modality(
                        line,
                        {"event": {"id": event_id, "produced": True}, "target": target},
                        default="must" if "must" in match.group(0).casefold() else "required",
                        evidence=match.group(0),
                    ),
                    confidence=0.88,
                    rule_id=f"kill_{event_id}",
                )
            )

    for match in re.finditer(r"\b[Dd]eal (?P<amount>\d+) to (?P<target>[^.]+)", line):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0).strip(),
                clause_group_id=base_group,
                semantic_role="event_produced",
                fact_type="damage",
                predicate="damage",
                payload=payload_with_line_modality(
                    line,
                    {"event": {"id": "damage_dealt", "produced": True}, "amounts": [{"value": int(match.group("amount")), "unit": "damage"}], "target": {"raw": match.group("target").strip()}},
                    evidence=match.group(0).strip(),
                ),
                confidence=0.86,
                rule_id="deal_damage",
            )
        )

    for match in re.finditer(r"\b(?:spells and abilities|your spells and abilities) deal (?P<amount>\d+) Bonus Damage\b", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="state_or_modifier",
                fact_type="static_modifier",
                predicate="modify_stat",
                payload=payload_with_line_modality(line, {
                    "target": {"kind": "damage", "source": "spell_or_ability"},
                    "amounts": [{"value": int(match.group("amount")), "unit": "bonus_damage"}],
                    "outputs": [{"id": "bonus_damage_added", "action": "modify_stat", "object": "damage"}],
                }, default="static"),
                confidence=0.88,
                rule_id="bonus_damage_modifier",
            )
        )

    if match := re.search(r"\b(?:This|I) enters exhausted\b", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="state_or_modifier",
                fact_type="entry_state",
                predicate="enter_exhausted",
                payload=payload_with_line_modality(line, {"target": {"kind": "card", "scope": "self"}, "event": {"id": "self_enters", "subject": "self"}, "modifiers": [{"state": "exhausted"}]}),
                confidence=0.93,
                rule_id="self_enters_exhausted",
            )
        )

    if match := re.search(r"\bI enter ready\b", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="state_or_modifier",
                fact_type="entry_state",
                predicate="enter_ready",
                payload=payload_with_line_modality(line, {"target": {"kind": "card", "scope": "self"}, "event": {"id": "self_enters", "subject": "self"}, "modifiers": [{"state": "ready"}]}),
                confidence=0.93,
                rule_id="self_enters_ready",
            )
        )

    if match := re.search(r"\bYour tokens enter ready\b", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="state_or_modifier",
                fact_type="entry_state",
                predicate="enter_ready",
                payload=payload_with_line_modality(line, {
                    "target": {"kind": "token", "controller": "you"},
                    "event": {"id": "token_enters", "subject": "your_token"},
                    "outputs": [{"id": "token_enters_ready", "action": "enter_ready", "object": "your_token"}],
                    "modifiers": [{"state": "ready"}],
                }),
                confidence=0.94,
                rule_id="tokens_enter_ready",
            )
        )

    for match in re.finditer(r"\bready me\b", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="state_or_modifier",
                fact_type="state_modifier",
                predicate="ready",
                payload=payload_with_line_modality(line, {"target": {"kind": "card", "scope": "self"}, "outputs": [{"id": "self_ready", "action": "ready", "object": "self"}]}),
                confidence=0.92,
                rule_id="ready_self",
            )
        )

    for match in re.finditer(r"(?<!enter\s)\bReady (?P<target>(?!me\b)[^.]+?)(?:\.|,|$)", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0).rstrip(".,"),
                clause_group_id=base_group,
                semantic_role="state_or_modifier",
                fact_type="state_modifier",
                predicate="ready",
                payload=payload_with_line_modality(line, {
                    "target": {"raw": match.group("target").strip()},
                    "outputs": [{"id": "unit_ready", "action": "ready", "object": "unit"}],
                }),
                confidence=0.82,
                rule_id="ready_unit",
            )
        )

    for match in re.finditer(r"\bRepeat this [^.]+ effect\b", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="payoff_output",
                fact_type="payoff",
                predicate="repeat_effect",
                payload=payload_with_line_modality(line, {"outputs": [{"action": "repeat_effect", "object": "this_gear_play_effect" if "gear" in match.group(0).casefold() else "referenced_effect"}]}),
                confidence=0.88,
                rule_id="repeat_effect",
            )
        )

    for match in re.finditer(r"\b(?:the first )?friendly non-token gear played each turn costs :rb_energy_(?P<amount>\d+): (?P<direction>less|more)\b", line, re.I):
        direction = match.group("direction").casefold()
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="state_or_modifier",
                fact_type="static_modifier",
                predicate="reduce_cost" if direction == "less" else "increase_cost",
                payload=payload_with_line_modality(line, {
                    "target": {"kind": "card", "card_types": ["gear"], "controller": "friendly", "exclude": ["token"], "ordinal": "first_each_turn" if "first" in match.group(0).casefold() else None},
                    "amounts": [{"value": int(match.group("amount")), "unit": "energy", "symbol": f":rb_energy_{match.group('amount')}:"}],
                    "outputs": [{"id": "gear_cost_reduced" if direction == "less" else "gear_cost_increased", "action": "reduce_cost" if direction == "less" else "increase_cost", "object": "gear"}],
                    "duration": "each_turn",
                }),
                confidence=0.9,
                rule_id="gear_cost_modifier",
            )
        )

    for match in re.finditer(r"\bgive (?P<target>[^.]+?) (?P<delta>[+-]\d+) :rb_might:(?: this turn)?(?=\W|$)", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="state_or_modifier",
                fact_type="stat_change",
                predicate="modify_stat",
                payload=payload_with_line_modality(line, {
                    "target": {"raw": match.group("target").strip()},
                    "amounts": [{"value": int(match.group("delta")), "unit": "might"}],
                    "duration": "this_turn" if "this turn" in match.group(0).casefold() else None,
                    "outputs": [{"id": "might_modified", "action": "modify_stat", "object": "might"}],
                }),
                confidence=0.86,
                rule_id="give_might",
            )
        )

    for match in re.finditer(r"\b(?P<target>(?:your|other friendly|friendly|enemy)?\s*[^.]*?units?[^.]*) have (?P<delta>[+-]\d+) :rb_might:(?=\W|$)", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="state_or_modifier",
                fact_type="static_modifier",
                predicate="modify_stat",
                payload=payload_with_line_modality(line, {
                    "target": {"raw": match.group("target").strip()},
                    "amounts": [{"value": int(match.group("delta")), "unit": "might"}],
                    "outputs": [{"id": "might_modified", "action": "modify_stat", "object": "might"}],
                }, default="static"),
                confidence=0.82,
                rule_id="static_might_modifier",
            )
        )

    for match in re.finditer(r"\b(?:\[Buff\]\s*)?[Bb]uff (?P<target>[^.]+?)(?:\.|,| this turn|$)", line):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0).rstrip(".,"),
                clause_group_id=base_group,
                semantic_role="event_produced",
                fact_type="state_modifier",
                predicate="buff",
                payload=payload_with_line_modality(line, {
                    "event": {"id": "unit_buffed", "produced": True},
                    "target": {"raw": match.group("target").strip()},
                    "outputs": [{"id": "unit_buffed", "action": "buff", "object": "unit"}],
                }, evidence=match.group(0).rstrip(".,")),
                confidence=0.84,
                rule_id="buff_unit",
            )
        )

    for match in re.finditer(r"\b\[?Stun\]?\s+(?P<target>[^.]+?)(?:\.|,|$)", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0).rstrip(".,"),
                clause_group_id=base_group,
                semantic_role="event_produced",
                fact_type="state_modifier",
                predicate="stun",
                payload=payload_with_line_modality(line, {
                    "event": {"id": "unit_stunned", "produced": True},
                    "target": {"raw": match.group("target").strip()},
                    "outputs": [{"id": "unit_stunned", "action": "stun", "object": "unit"}],
                    "duration": "this_turn",
                }),
                confidence=0.86,
                rule_id="stun_unit",
            )
        )

    for match in re.finditer(r"(?<!can )(?<!When you )\bMove (?P<target>[^.]+?)(?: to (?P<destination>[^.]+?))?(?:\.|,| then|$)", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0).rstrip(".,"),
                clause_group_id=base_group,
                semantic_role="event_produced",
                fact_type="movement",
                predicate="move",
                payload=payload_with_line_modality(line, {
                    "event": {"id": "unit_moved", "produced": True},
                    "target": {"raw": match.group("target").strip()},
                    "location": (match.group("destination") or "").strip() or None,
                    "outputs": [{"id": "unit_moved", "action": "move", "object": "unit"}],
                }),
                confidence=0.82,
                rule_id="move_unit",
            )
        )

    for match in re.finditer(r"\brecall (?P<target>[^.]+?)(?:\.|,| instead| at end of turn|$)", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0).rstrip(".,"),
                clause_group_id=base_group,
                semantic_role="event_produced",
                fact_type="movement",
                predicate="return_to_hand",
                payload=payload_with_line_modality(line, {
                    "event": {"id": "unit_moved", "produced": True},
                    "target": {"raw": match.group("target").strip(), "zone": "base"},
                    "outputs": [{"id": "unit_recalled", "action": "return_to_hand", "object": "unit"}],
                }),
                confidence=0.82,
                rule_id="recall_unit",
            )
        )

    for match in re.finditer(r"\b(?:reduce|reducing|reduced by) (?P<body>[^.]*?:rb_energy_(?P<amount>\d+):[^.]*)", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="state_or_modifier",
                fact_type="static_modifier",
                predicate="reduce_cost",
                payload=payload_with_line_modality(line, {
                    "target": {"kind": "card", "raw": match.group("body").strip()},
                    "amounts": [{"value": int(match.group("amount")), "unit": "energy", "symbol": f":rb_energy_{match.group('amount')}:"}],
                    "outputs": [{"id": "play_cost_reduced", "action": "reduce_cost", "object": "card"}],
                }),
                confidence=0.78,
                rule_id="generic_cost_reduction",
            )
        )

    cost_reduction_pattern = (
        r"\b(?P<target>This ability|This|I|The next [^.]+?|The first [^.]+?|"
        r"(?:friendly|enemy|your|opposing|other friendly|units?|spells?|gear|cards?)[^.]{0,80}?)"
        r"\s+costs?\s+(?P<body>:rb_energy_(?P<amount>\d+):[^.]*?)\s+less\b"
    )
    for match in re.finditer(cost_reduction_pattern, line, re.I):
        payload = {
            "target": {"raw": match.group("target").strip()},
            "amounts": [{"value": int(match.group("amount")), "unit": "energy", "symbol": f":rb_energy_{match.group('amount')}:"}],
            "outputs": [{"id": "play_cost_reduced", "action": "reduce_cost", "object": "card"}],
        }
        if "this turn" in match.group(0).casefold():
            payload["duration"] = "this_turn"
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="state_or_modifier",
                fact_type="static_modifier",
                predicate="reduce_cost",
                payload=payload_with_line_modality(line, payload, evidence=match.group(0)),
                confidence=0.8,
                rule_id="costs_less_energy",
            )
        )

    for match in re.finditer(
        r"\bcosts?\s+(?!no more than\b)(?P<body>(?:(?!\bcosts?\b|\bor more\b).)*?:rb_energy_(?P<amount>\d+):(?:(?!\bcosts?\b|\bor more\b).)*?)\s+more(?: to play this turn)?\b",
        line,
        re.I,
    ):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="state_or_modifier",
                fact_type="static_modifier",
                predicate="increase_cost",
                payload=payload_with_line_modality(
                    line,
                    {
                        "target": {"kind": "card", "raw": match.group("body").strip()},
                        "amounts": [{"value": int(match.group("amount")), "unit": "energy", "symbol": f":rb_energy_{match.group('amount')}:"}],
                        "outputs": [{"id": "play_cost_increased", "action": "increase_cost", "object": "card"}],
                    },
                    evidence=match.group(0),
                ),
                confidence=0.82,
                rule_id="generic_cost_increase",
            )
        )

    for match in re.finditer(r"\bcosts? (?P<body>[^.]*?:rb_energy_(?P<amount>\d+):[^.]*?) or more\b", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="restriction_or_permission",
                fact_type="restriction",
                predicate="cost_threshold",
                payload={
                    "target": {"kind": "card", "raw": match.group("body").strip()},
                    "cost_constraints": [{"resource": "energy", "minimum": int(match.group("amount"))}],
                },
                confidence=0.82,
                rule_id="energy_cost_threshold",
            )
        )

    for match in re.finditer(r"\bcost(?:s|ing)? no more than (?P<body>[^.]+?)(?:\.|,| and| from|$)", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0).rstrip(".,"),
                clause_group_id=base_group,
                semantic_role="restriction_or_permission",
                fact_type="restriction",
                predicate="cost_cap_constraint",
                payload={
                    "target": {"kind": "card"},
                    "cost_text": match.group("body").strip(),
                    "cost_constraints": [{"raw": match.group("body").strip(), "maximum": True}],
                },
                confidence=0.82,
                rule_id="cost_cap_constraint",
            )
        )

    if match := re.search(r"\bPrevent all spell and ability damage this turn\b", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="restriction_or_permission",
                fact_type="restriction",
                predicate="prevent",
                payload={"target": {"kind": "damage", "source": "spell_or_ability"}, "duration": "this_turn", "polarity": "prevention", "prevented_event": "damage_dealt"},
                confidence=0.9,
                rule_id="prevent_spell_ability_damage",
            )
        )

    for match in re.finditer(r"\b(?:gain|gains|increase) (?P<amount>\d+) points?\b|\bpoints needed to win the game by (?P<needed>\d+)\b", line, re.I):
        amount = int(match.group("amount") or match.group("needed"))
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=base_group,
                semantic_role="payoff_output",
                fact_type="score_change",
                predicate="score",
                payload=payload_with_line_modality(line, {"amounts": [{"value": amount, "unit": "point"}]}),
                confidence=0.8,
                rule_id="score_points",
            )
        )
    return rows


def reminder_facts(card: dict[str, Any], source_field: str, line_index: int, line: str, builder: FactBuilder) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if match := re.search(r"\bKill this at the start of its controller's Beginning Phase, before scoring\b", line, re.I):
        rows.append(
            builder.fact(
                card,
                source_field=source_field,
                line_index=line_index,
                line_text=line,
                evidence=match.group(0),
                clause_group_id=line_clause_group_id(card["play_id"], source_field, line_index),
                semantic_role="event_produced",
                fact_type="produced_event",
                predicate="kill",
                payload={"event": {"id": "self_dies", "produced": True}, "conditions": [{"timing": "start_of_controller_beginning_phase", "before": "scoring"}]},
                confidence=0.9,
                rule_id="temporary_self_dies",
            )
        )
    return rows


POSITIVE_PREDICATES_BLOCKED_BY_NEGATION = {
    "damage",
    "kill",
    "move",
    "play",
    "ready",
    "score",
    "stun",
    "counter",
    "attach",
    "detach",
}


def evidence_offset(line: str, evidence: str) -> int:
    return normalize_text(line).find(normalize_text(evidence))


def has_negation_before_evidence(line: str, evidence: str) -> bool:
    start = evidence_offset(line, evidence)
    if start < 0:
        return False
    prefix = normalize_text(line)[max(0, start - 50) : start]
    return bool(re.search(r"(?:can(?:not|'t)|don't|doesn't|isn't|prevent(?:s|ed)?|instead)\s+$", prefix))


def has_replacement_context(line: str, evidence: str) -> bool:
    start = evidence_offset(line, evidence)
    if start < 0:
        return False
    source = normalize_text(line)
    clause = source[max(0, start - 90) : start + len(normalize_text(evidence)) + 90]
    return " would " in clause and " instead" in clause


def has_reminder_definition_context(line: str, evidence: str) -> bool:
    start = evidence_offset(line, evidence)
    if start < 0:
        return False
    source = normalize_text(line)
    prefix = source[:start]
    open_index = prefix.rfind("(")
    close_index = prefix.rfind(")")
    if open_index < 0 or open_index < close_index:
        return False
    reminder_prefix = source[open_index:]
    return (
        reminder_prefix.startswith("(to buff a unit")
        or reminder_prefix.startswith("(give it a +1")
        or reminder_prefix.startswith("(if i don't have a buff")
    )


def has_granted_ability_context(line: str, evidence: str) -> bool:
    start = evidence_offset(line, evidence)
    if start < 0:
        return False
    prefix = normalize_text(line)[:start]
    sentence_start = max(prefix.rfind("."), prefix.rfind(";"))
    local_prefix = prefix[sentence_start + 1 :] if sentence_start >= 0 else prefix
    return bool(re.search(r"\b(?:have|has)\s+\"", local_prefix))


def suppress_negated_positive_facts(rows: list[dict[str, Any]], line: str) -> list[dict[str, Any]]:
    filtered = []
    for row in rows:
        if row.get("semantic_role") in {"restriction_or_permission", "identity_or_descriptor", "trigger_observed"}:
            filtered.append(row)
            continue
        if has_reminder_definition_context(line, row.get("evidence", "")):
            continue
        predicate = row.get("predicate")
        if predicate in {"attach", "detach"} and has_granted_ability_context(line, row.get("evidence", "")):
            continue
        if predicate in POSITIVE_PREDICATES_BLOCKED_BY_NEGATION and has_negation_before_evidence(line, row.get("evidence", "")):
            continue
        filtered.append(row)
    return filtered


def facts_for_line(
    card: dict[str, Any],
    source_field: str,
    line_index: int,
    line: str,
    builder: FactBuilder,
    contract_rules: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    rows.extend(contract_facts_for_line(card, source_field, line_index, line, builder, contract_rules))
    rows.extend(keyword_facts(card, source_field, line_index, line, builder))
    rows.extend(trigger_facts(card, source_field, line_index, line, builder))
    rows.extend(condition_facts(card, source_field, line_index, line, builder))
    rows.extend(cost_facts(card, source_field, line_index, line, builder))
    rows.extend(effect_facts(card, source_field, line_index, line, builder))
    rows.extend(reminder_facts(card, source_field, line_index, line, builder))
    return dedupe_facts(suppress_negated_positive_facts(rows, line))


def choice_mode_from_header(line: str) -> str | None:
    if re.search(r"\bChoose one\b", line, re.I):
        return "choose_one"
    if re.search(r"\bChoose two\b", line, re.I):
        return "choose_two"
    return None


def annotate_choice_option(
    rows: list[dict[str, Any]],
    *,
    choice_group_id: str,
    option_index: int,
    choice_mode: str,
) -> None:
    for row in rows:
        if row.get("semantic_role") == "identity_or_descriptor":
            continue
        payload = dict(row.get("payload", {}) or {})
        payload.setdefault("choice_group_id", choice_group_id)
        payload.setdefault("option_group_id", f"{choice_group_id}:option:{option_index}")
        payload.setdefault("option_index", option_index)
        payload.setdefault("choice_mode", choice_mode)
        payload.setdefault("exclusive", choice_mode == "choose_one")
        row["payload"] = payload


def annotate_inline_or_choice(
    rows: list[dict[str, Any]],
    *,
    play_id: str,
    source_field: str,
    line_index: int,
    line: str,
) -> None:
    if not re.search(r"\byou may draw 1 or buff me\b", line, re.I):
        return
    choice_group_id = f"choice:{play_id}:{source_field}:{line_index}:inline:0"
    option_evidence = {
        "draw 1": 0,
        "buff me": 1,
    }
    for row in rows:
        evidence = normalize_text(str(row.get("evidence") or ""))
        if evidence not in option_evidence:
            continue
        option_index = option_evidence[evidence]
        payload = dict(row.get("payload", {}) or {})
        payload["modality"] = "optional"
        payload.setdefault("choice_group_id", choice_group_id)
        payload.setdefault("option_group_id", f"{choice_group_id}:option:{option_index}")
        payload.setdefault("option_index", option_index)
        payload.setdefault("choice_mode", "choose_one")
        payload.setdefault("exclusive", True)
        row["payload"] = payload


def fact_marker(row: dict[str, Any]) -> str:
    return json.dumps(
        {
            "play_id": row["play_id"],
            "source": row["source_ref"].get("source_field"),
            "line": row["source_ref"].get("line_index"),
            "role": row["semantic_role"],
            "type": row["fact_type"],
            "predicate": row["predicate"],
            "evidence": row["evidence"].casefold(),
            "payload": row["payload"],
        },
        ensure_ascii=False,
        sort_keys=True,
    )


def dedupe_facts(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    deduped = []
    for row in rows:
        marker = fact_marker(row)
        if marker in seen:
            continue
        seen.add(marker)
        deduped.append(row)
    return deduped


def extract_facts(cards: list[dict[str, Any]], inventory: dict[str, Any], contract_rules: list[dict[str, Any]]) -> list[dict[str, Any]]:
    builder = FactBuilder(load_inventory_line_units(inventory))
    rows: list[dict[str, Any]] = []
    for card in cards:
        rows.extend(official_facts(card, builder))
        for source_field in TEXT_SOURCE_FIELDS:
            active_choice_group_id: str | None = None
            active_choice_mode: str | None = None
            active_option_index = 0
            for line_index, line in enumerate(card.get(source_field, []) or []):
                line_choice_mode = choice_mode_from_header(line)
                if line_choice_mode:
                    active_choice_group_id = f"choice:{card['play_id']}:{source_field}:{line_index}"
                    active_choice_mode = line_choice_mode
                    active_option_index = 0
                line_rows = facts_for_line(card, source_field, line_index, line, builder, contract_rules)
                annotate_inline_or_choice(
                    line_rows,
                    play_id=card["play_id"],
                    source_field=source_field,
                    line_index=line_index,
                    line=line,
                )
                if active_choice_group_id and active_choice_mode and not line_choice_mode and line.strip():
                    annotate_choice_option(
                        line_rows,
                        choice_group_id=active_choice_group_id,
                        option_index=active_option_index,
                        choice_mode=active_choice_mode,
                    )
                    if any(row.get("semantic_role") != "identity_or_descriptor" for row in line_rows):
                        active_option_index += 1
                rows.extend(line_rows)
    rows.sort(key=lambda row: (row["play_id"], row["source_ref"]["source_field"], row["source_ref"]["line_index"] is None, row["source_ref"]["line_index"] or -1, row["fact_id"]))
    return rows


def build_report(cards: list[dict[str, Any]], facts: list[dict[str, Any]], inputs: dict[str, str]) -> dict[str, Any]:
    by_role = Counter(row["semantic_role"] for row in facts)
    by_type = Counter(row["fact_type"] for row in facts)
    by_predicate = Counter(row["predicate"] for row in facts)
    extractor_sources = Counter(
        (row.get("extractor") or {}).get("source_kind", "unknown") if isinstance(row.get("extractor"), dict) else "legacy_string"
        for row in facts
    )
    contract_rules = Counter(
        (row.get("extractor") or {}).get("rule_id")
        for row in facts
        if isinstance(row.get("extractor"), dict) and (row.get("extractor") or {}).get("source_kind") == "contract_rule"
    )
    facts_by_card = Counter(row["play_id"] for row in facts)
    text_fact_keys = {
        (row["play_id"], row["source_ref"]["source_field"], row["source_ref"]["line_index"])
        for row in facts
        if row["source_ref"]["source_field"] in TEXT_SOURCE_FIELDS
    }
    text_lines = [
        (card["play_id"], source_field, index, line)
        for card in cards
        for source_field in TEXT_SOURCE_FIELDS
        for index, line in enumerate(card.get(source_field, []) or [])
    ]
    uncovered_lines = [
        {"play_id": play_id, "source_field": source_field, "line_index": index, "line": line}
        for play_id, source_field, index, line in text_lines
        if (play_id, source_field, index) not in text_fact_keys
    ]
    return {
        "version": SCHEMA_VERSION,
        "extractor": EXTRACTOR_VERSION,
        "inputs": inputs,
        "summary": {
            "card_count": len(cards),
            "fact_count": len(facts),
            "cards_with_facts": len(facts_by_card),
            "text_line_count": len(text_lines),
            "text_lines_with_facts": len(text_fact_keys),
            "text_lines_without_facts": len(uncovered_lines),
            "text_line_fact_coverage": round(len(text_fact_keys) / len(text_lines), 4) if text_lines else 1.0,
            "legacy_rule_count": extractor_sources.get("legacy_rule", 0),
            "contract_rule_count": extractor_sources.get("contract_rule", 0),
        },
        "facts_by_source_kind": dict(extractor_sources.most_common()),
        "top_contract_rules": dict(contract_rules.most_common(40)),
        "contract_rule_coverage": {
            "contract_rule_count": extractor_sources.get("contract_rule", 0),
            "legacy_rule_count": extractor_sources.get("legacy_rule", 0),
            "contract_share": round(extractor_sources.get("contract_rule", 0) / len(facts), 4) if facts else 0.0,
        },
        "by_semantic_role": dict(by_role.most_common()),
        "by_fact_type": dict(by_type.most_common()),
        "by_predicate": dict(by_predicate.most_common()),
        "top_uncovered_text_lines": uncovered_lines[:80],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract semantic facts from normalized Riftbound cards.")
    parser.add_argument("--cards", type=Path, default=DEFAULT_CARDS)
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument("--taxonomy", type=Path, default=DEFAULT_TAXONOMY)
    parser.add_argument("--alignment", type=Path, default=DEFAULT_ALIGNMENT)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--ontology", type=Path, default=DEFAULT_ONTOLOGY)
    parser.add_argument("--extraction-rules", type=Path, default=DEFAULT_EXTRACTION_RULES)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cards = read_json(args.cards)
    inventory = read_json(args.inventory)
    # These reads make the dependency contract explicit and fail early if a required input is missing.
    read_json(args.taxonomy)
    if args.alignment.exists():
        read_json(args.alignment)
    read_json(args.schema)
    contracts = load_contract_bundle(CONTRACTS_DIR)
    if args.ontology != DEFAULT_ONTOLOGY:
        contracts["ontology"] = read_json(args.ontology)
    if args.extraction_rules != DEFAULT_EXTRACTION_RULES:
        contracts["extraction_rules"] = read_json(args.extraction_rules)
    contract_rules = compile_extraction_rules(contracts["extraction_rules"])

    facts = extract_facts(cards, inventory, contract_rules)
    write_jsonl(args.output, facts)
    report = build_report(
        cards,
        facts,
        {
            "cards": repo_path(args.cards),
            "inventory": repo_path(args.inventory),
            "taxonomy": repo_path(args.taxonomy),
            "alignment": repo_path(args.alignment),
            "schema": repo_path(args.schema),
            "ontology": repo_path(args.ontology),
            "extraction_rules": repo_path(args.extraction_rules),
        },
    )
    write_json(args.report, report)
    print(f"Wrote {len(facts)} semantic facts to {args.output}")
    print(f"Wrote report to {args.report}")


if __name__ == "__main__":
    main()
