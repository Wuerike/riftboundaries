import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
CONTRACTS_DIR = SCRIPT_DIR / "contracts"

DEFAULT_FACTS = PROJECT_ROOT / "data" / "processed" / "cards" / "semantic" / "cards_semantic_facts.jsonl"
DEFAULT_RELATIONS = PROJECT_ROOT / "data" / "processed" / "cards" / "relations" / "cards_card_relations.jsonl"
DEFAULT_DATASET = PROJECT_ROOT / "data" / "processed" / "web" / "card_explorer_dataset.json"
DEFAULT_GOLDEN = CONTRACTS_DIR / "semantic_golden_examples.json"
DEFAULT_REGRESSIONS = CONTRACTS_DIR / "semantic_regression_invariants.json"
DEFAULT_REPORT = PROJECT_ROOT / "data" / "processed" / "cards" / "semantic" / "cards_semantic_golden_report.json"
DAMAGE_MODIFIER_OUTPUT_IDS = {"bonus_damage_added", "damage_modified"}
BLOCKED_POSITIVE_ALIASES = {
    "damage_dealt": {"damage", "damage_dealt"},
    "deal_combat_damage": {"damage", "damage_dealt", "deal_combat_damage"},
    "kill": {"kill"},
    "move": {"move", "card_moved", "unit_moved", "self_moves"},
    "play": {"play", "play_token", "card_played", "unit_played", "spell_played", "gear_played", "self_played"},
    "ready": {"ready", "unit_ready", "self_ready"},
    "unit_dies": {"kill", "unit_dies", "friendly_unit_dies", "enemy_unit_dies", "self_dies"},
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def normalized(value: str) -> str:
    return " ".join(value.strip().casefold().split())


def value_contains(actual: Any, expected: Any) -> bool:
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            return False
        for key, expected_value in expected.items():
            if key not in actual:
                return False
            if not value_contains(actual[key], expected_value):
                return False
        return True

    if isinstance(expected, list):
        if not isinstance(actual, list):
            return False
        unmatched = list(actual)
        for expected_item in expected:
            match_index = None
            for index, actual_item in enumerate(unmatched):
                if value_contains(actual_item, expected_item):
                    match_index = index
                    break
            if match_index is None:
                return False
            unmatched.pop(match_index)
        return True

    if isinstance(expected, str) and isinstance(actual, str):
        return normalized(actual) == normalized(expected)

    return actual == expected


def fact_matches(actual: dict[str, Any], expected: dict[str, Any]) -> bool:
    for key in ("semantic_role", "fact_type", "predicate"):
        if actual.get(key) != expected.get(key):
            return False

    if normalized(actual.get("evidence", "")) != normalized(expected.get("evidence", "")):
        return False

    expected_payload = expected.get("payload", {})
    actual_payload = actual.get("payload", {})
    return value_contains(actual_payload, expected_payload)


def fact_matches_partial(actual: dict[str, Any], expected: dict[str, Any]) -> bool:
    for key in ("semantic_role", "fact_type", "predicate"):
        if expected.get(key) is not None and actual.get(key) != expected.get(key):
            return False

    expected_evidence = expected.get("evidence")
    if isinstance(expected_evidence, str) and normalized(actual.get("evidence", "")) != normalized(expected_evidence):
        return False

    if "payload" in expected and not value_contains(actual.get("payload", {}), expected.get("payload", {})):
        return False

    if expected.get("source_field") is not None and actual.get("source_ref", {}).get("source_field") != expected["source_field"]:
        return False
    if expected.get("line_index") is not None and actual.get("source_ref", {}).get("line_index") != expected["line_index"]:
        return False
    return True


def source_line_matches(actual: dict[str, Any], expected_sources: list[dict[str, Any]]) -> bool:
    source_ref = actual.get("source_ref", {})
    for source in expected_sources:
        if source_ref.get("source_field") != source.get("source_field"):
            continue
        if source_ref.get("line_index") != source.get("line_index"):
            continue
        return True
    return False


def expected_sources_for_fact(expected: dict[str, Any], fallback_sources: list[dict[str, Any]]) -> list[dict[str, Any]]:
    source_field = expected.get("source_field")
    line_index = expected.get("line_index")
    if source_field is not None and line_index is not None:
        return [{"source_field": source_field, "line_index": line_index}]
    return fallback_sources


def validate(golden: dict[str, Any], facts: list[dict[str, Any]]) -> dict[str, Any]:
    facts_by_card: dict[str, list[dict[str, Any]]] = {}
    for fact in facts:
        facts_by_card.setdefault(fact.get("play_id", ""), []).append(fact)

    failures = []
    matched_count = 0
    expected_count = 0

    for example in golden.get("examples", []):
        play_id = example["play_id"]
        card_facts = facts_by_card.get(play_id, [])
        sources = example.get("source_lines", [])
        used_fact_ids: set[str] = set()

        for expected in example.get("minimum_expected_facts", []):
            expected_count += 1
            expected_sources = expected_sources_for_fact(expected, sources)
            candidates = [
                fact
                for fact in card_facts
                if fact.get("fact_id") not in used_fact_ids and source_line_matches(fact, expected_sources)
            ]
            match = next((fact for fact in candidates if fact_matches(fact, expected)), None)
            if match:
                used_fact_ids.add(match["fact_id"])
                matched_count += 1
                continue

            failures.append(
                {
                    "play_id": play_id,
                    "name": example.get("name"),
                    "expected_fact_id": expected.get("fact_id"),
                    "semantic_role": expected.get("semantic_role"),
                    "fact_type": expected.get("fact_type"),
                    "predicate": expected.get("predicate"),
                    "evidence": expected.get("evidence"),
                    "candidate_count": len(candidates),
                }
            )

    return {
        "version": golden.get("version"),
        "summary": {
            "example_count": len(golden.get("examples", [])),
            "expected_fact_count": expected_count,
            "matched_fact_count": matched_count,
            "missing_fact_count": len(failures),
            "pass": not failures,
        },
        "failures": failures,
    }


def validate_regression_facts(regressions: dict[str, Any], facts: list[dict[str, Any]]) -> dict[str, Any]:
    facts_by_card: dict[str, list[dict[str, Any]]] = {}
    for fact in facts:
        facts_by_card.setdefault(fact.get("play_id", ""), []).append(fact)

    failures = []
    expected_count = 0
    forbidden_count = 0
    for fixture in regressions.get("fact_expectations", []) or []:
        card_facts = facts_by_card.get(fixture.get("play_id", ""), [])
        for expected in fixture.get("expected_facts", []) or []:
            expected_count += 1
            if not any(fact_matches_partial(fact, expected) for fact in card_facts):
                failures.append(
                    {
                        "kind": "missing_expected_regression_fact",
                        "play_id": fixture.get("play_id"),
                        "name": fixture.get("name"),
                        "expected": expected,
                    }
                )
        for forbidden in fixture.get("forbidden_facts", []) or []:
            forbidden_count += 1
            matches = [fact for fact in card_facts if fact_matches_partial(fact, forbidden)]
            if matches:
                failures.append(
                    {
                        "kind": "forbidden_fact_present",
                        "play_id": fixture.get("play_id"),
                        "name": fixture.get("name"),
                        "forbidden": forbidden,
                        "matches": [fact.get("fact_id") for fact in matches[:10]],
                    }
                )

    return {
        "summary": {
            "fixture_count": len(regressions.get("fact_expectations", []) or []),
            "expected_regression_fact_count": expected_count,
            "forbidden_regression_fact_count": forbidden_count,
            "pass": not failures,
        },
        "failures": failures,
    }


def relation_reason(relation: dict[str, Any]) -> str:
    return str(relation.get("match", {}).get("reason") or "")


def relation_fact_ids(relation: dict[str, Any]) -> set[str]:
    fact_ids = {relation.get("source_fact_id"), relation.get("target_fact_id")}
    fact_ids.update(relation.get("match", {}).get("supporting_fact_ids", []) or [])
    return {str(fact_id) for fact_id in fact_ids if fact_id}


def fact_condition_states(fact: dict[str, Any] | None) -> set[str]:
    if not fact:
        return set()
    states = set()
    for condition in fact.get("payload", {}).get("conditions", []) or []:
        if isinstance(condition, dict) and condition.get("state"):
            states.add(str(condition["state"]))
    return states


def fact_resource_costs(fact: dict[str, Any] | None) -> list[dict[str, Any]]:
    if not fact:
        return []
    return [cost for cost in fact.get("payload", {}).get("costs", []) or [] if isinstance(cost, dict) and cost.get("resource")]


def replacement_context(fact: dict[str, Any] | None) -> dict[str, Any]:
    if not fact:
        return {"prevented": "", "replacement": "", "target_families": []}
    payload = fact.get("payload", {}) or {}
    target = payload.get("target") if isinstance(payload.get("target"), dict) else {}
    target_kind = compact_value_key(target.get("kind") or target.get("scope") or target.get("raw"))
    return {
        "prevented": compact_value_key(payload.get("prevented_event") or payload.get("prevented_action") or payload.get("replaced_event")),
        "replacement": compact_value_key(payload.get("replacement")),
        "target_families": [target_kind] if target_kind else [],
    }


def compact_value_key(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"[^a-z0-9_+-]+", "_", str(value).casefold()).strip("_")


def source_line_key(fact: dict[str, Any]) -> tuple[str, str, int | None, Any, str]:
    source_ref = fact.get("source_ref", {}) or {}
    return (
        str(fact.get("play_id") or ""),
        str(source_ref.get("source_field") or ""),
        source_ref.get("line_index"),
        source_ref.get("unit_index"),
        str(source_ref.get("normalized_unit") or ""),
    )


def prevented_positive_aliases(fact: dict[str, Any]) -> set[str]:
    payload = fact.get("payload", {}) or {}
    values = [
        payload.get("prevented_action"),
        payload.get("prevented_event"),
        payload.get("replaced_event"),
    ]
    for modifier in payload.get("modifiers", []) or []:
        if isinstance(modifier, dict) and modifier.get("polarity") == "prevention":
            values.append(modifier.get("action"))
    aliases: set[str] = set()
    for value in values:
        key = compact_value_key(value)
        if not key:
            continue
        aliases.add(key)
        aliases.update(BLOCKED_POSITIVE_ALIASES.get(key, set()))
    return aliases


def positive_semantic_values(fact: dict[str, Any]) -> set[str]:
    if fact.get("semantic_role") not in {"event_produced", "payoff_output", "state_or_modifier"}:
        return set()
    if fact.get("predicate") in {"prevent", "require"}:
        return set()
    payload = fact.get("payload", {}) or {}
    values = {compact_value_key(fact.get("predicate"))}
    event = payload.get("event")
    if isinstance(event, dict):
        values.add(compact_value_key(event.get("id")))
    elif isinstance(event, str):
        values.add(compact_value_key(event))
    for output in payload.get("outputs", []) or []:
        if not isinstance(output, dict):
            continue
        values.add(compact_value_key(output.get("id")))
        values.add(compact_value_key(output.get("action")))
    return {value for value in values if value}


def exclusive_choice_context(fact: dict[str, Any] | None) -> tuple[str, Any] | None:
    if not fact:
        return None
    payload = fact.get("payload", {}) or {}
    if not payload.get("exclusive") or not payload.get("choice_group_id"):
        return None
    return (str(payload.get("choice_group_id")), payload.get("option_index"))


def is_gear_or_equipment_fact(fact: dict[str, Any] | None) -> bool:
    if not fact:
        return False
    snapshot = fact.get("card_snapshot", {}) or {}
    card_types = {str(item).casefold() for item in snapshot.get("card_type_ids", []) or []}
    tags = {str(item).casefold() for item in snapshot.get("tags", []) or []}
    return "gear" in card_types or "equipment" in tags


def attached_context_payload_ok(payload: dict[str, Any]) -> bool:
    return (
        payload.get("activation_context") == "attached"
        and payload.get("inactive_until_attached") is True
        and payload.get("applies_to") == "top_most_card"
    )


def output_ids_from_fact(fact: dict[str, Any] | None) -> list[str]:
    if not fact:
        return []
    return sorted(
        {
            output["id"]
            for output in fact.get("payload", {}).get("outputs", []) or []
            if isinstance(output, dict) and isinstance(output.get("id"), str)
        }
    )


def attachment_context_key(fact: dict[str, Any]) -> str:
    payload = fact.get("payload", {}) or {}
    facets = []
    if payload.get("activation_context"):
        facets.append(f"activation={payload['activation_context']}")
    if payload.get("inactive_until_attached"):
        facets.append("inactive_until_attached")
    if payload.get("applies_to"):
        facets.append(f"applies_to={payload['applies_to']}")
    return ";".join(facets) or "active"


def is_damage_modifier_fact(fact: dict[str, Any] | None) -> bool:
    if not fact:
        return False
    if fact.get("semantic_role") != "state_or_modifier" or fact.get("predicate") != "modify_stat":
        return False
    return bool(DAMAGE_MODIFIER_OUTPUT_IDS & set(output_ids_from_fact(fact)))


def damage_modifier_context(fact: dict[str, Any]) -> dict[str, str]:
    payload = fact.get("payload", {}) or {}
    amounts = payload.get("amounts") or []
    amount = amounts[0] if amounts and isinstance(amounts[0], dict) else {}
    target = payload.get("target")
    target_kind = ""
    target_source = ""
    if isinstance(target, dict):
        if isinstance(target.get("kinds"), list):
            target_kind = "+".join(sorted(compact_value_key(item) for item in target["kinds"]))
        else:
            target_kind = compact_value_key(target.get("kind") or target.get("scope") or target.get("zone") or target.get("location"))
        target_source = compact_value_key(target.get("source"))
    value_key = compact_value_key(amount.get("value"))
    if not value_key and payload.get("multiplier") is not None:
        value_key = f"x{compact_value_key(payload.get('multiplier'))}"
    return {
        "outputs": ",".join(output_ids_from_fact(fact)),
        "unit": compact_value_key(amount.get("unit") or payload.get("stat") or "damage"),
        "value": value_key or "variable",
        "target_kind": target_kind,
        "target_source": target_source,
        "duration": compact_value_key(payload.get("duration")) or "ongoing",
        "modality": compact_value_key(payload.get("modality")) or "required",
        "context": attachment_context_key(fact),
    }


def inferred_target_family_from_raw(target: dict[str, Any]) -> str:
    raw = str(target.get("raw") or "").casefold()
    if not raw:
        return ""
    raw = re.sub(r"^\s*(?:or|and|then)\s+", "", raw)
    families = (
        (r"\brunes?\b", "rune"),
        (r"\blegends?\b", "legend"),
        (r"\bmechs?\b", "mech"),
        (r"\bequipments?\b", "equipment"),
        (r"\bgears?\b", "gear"),
        (r"\bunits?\b", "unit"),
        (r"\btokens?\b", "token"),
    )
    for pattern, family in families:
        if re.search(pattern, raw):
            return family
    return ""


def state_target_family_from_payload(target: Any) -> str:
    if not isinstance(target, dict):
        return ""
    if isinstance(target.get("kinds"), list):
        base = "+".join(sorted(compact_value_key(item) for item in target["kinds"]))
    else:
        base = compact_value_key(target.get("kind") or target.get("scope") or "")
    raw_family = inferred_target_family_from_raw(target)
    if raw_family and (not base or base in {"card", "self"}):
        base = raw_family
    if not base:
        base = compact_value_key(target.get("zone") or target.get("location"))
    return base


def state_target_families_from_payload(target: Any) -> list[str]:
    primary = state_target_family_from_payload(target)
    families = {primary} if primary else set()
    if isinstance(target, dict):
        if isinstance(target.get("kinds"), list):
            families.update(compact_value_key(item) for item in target["kinds"] if compact_value_key(item))
        raw_family = inferred_target_family_from_raw(target)
        if raw_family:
            families.add(raw_family)
    return sorted(family for family in families if family)


def is_keyword_grant_fact(fact: dict[str, Any] | None) -> bool:
    if not fact:
        return False
    return (
        fact.get("semantic_role") == "state_or_modifier"
        and fact.get("fact_type") == "keyword_grant"
        and fact.get("predicate") == "gain_keyword"
        and "keyword_granted" in output_ids_from_fact(fact)
    )


def keyword_grant_context(fact: dict[str, Any]) -> dict[str, Any]:
    payload = fact.get("payload", {}) or {}
    keywords = payload.get("keywords") or []
    keyword_values: list[str] = []
    if isinstance(keywords, list):
        keyword_values = sorted({compact_value_key(keyword) for keyword in keywords if compact_value_key(keyword)})
    return {
        "keywords": keyword_values,
        "target_families": state_target_families_from_payload(payload.get("target")),
        "duration": compact_value_key(payload.get("duration")) or "ongoing",
        "modality": compact_value_key(payload.get("modality")) or "required",
        "context": attachment_context_key(fact),
    }


def duration_bucket(duration: Any) -> str:
    duration_key = compact_value_key(duration)
    if duration_key in {"this_turn", "this_combat", "until_end_of_turn"}:
        return "temporary"
    return duration_key or "ongoing"


def keyword_grant_reason_keywords(reason: str) -> set[str]:
    if reason.startswith("secondary:keyword_grant:") or reason.startswith("secondary:keyword_grant_by_keyword:"):
        parts = reason.split(":")
        if len(parts) > 2:
            return {compact_value_key(parts[2])}
    if reason.startswith("secondary:temporary_grant:"):
        return {"temporary"}
    if reason.startswith("secondary:keyword:"):
        parts = reason.split(":")
        if len(parts) > 2:
            return {compact_value_key(keyword) for keyword in parts[2].split(",") if compact_value_key(keyword)}
    matched: set[str] = set()
    for match in re.finditer(r"(?:^|[:;])keywords=([^:;]+)", reason):
        matched.update(compact_value_key(keyword) for keyword in match.group(1).split(",") if compact_value_key(keyword))
    return matched


def keyword_grant_reason_target_family(reason: str) -> str:
    if not reason.startswith("secondary:keyword_grant:"):
        if reason.startswith("secondary:keyword_grant_by_keyword:"):
            parts = reason.split(":")
            if len(parts) >= 4:
                return compact_value_key(parts[3])
        if reason.startswith("secondary:temporary_grant:"):
            parts = reason.split(":")
            if len(parts) >= 3:
                return compact_value_key(parts[2])
        return ""
    parts = reason.split(":")
    if len(parts) >= 7:
        return compact_value_key(parts[3])
    return ""


def relation_matches_expectation(relation: dict[str, Any], expected: dict[str, Any]) -> bool:
    relation_type = expected.get("relation_type")
    if relation_type and relation.get("relation_type") != relation_type:
        return False

    source = expected.get("source_play_id")
    target = expected.get("target_play_id")
    if source and target:
        exact_pair = relation.get("source_play_id") == source and relation.get("target_play_id") == target
        reverse_pair = relation.get("source_play_id") == target and relation.get("target_play_id") == source
        if expected.get("directed", False):
            if not exact_pair:
                return False
        elif not (exact_pair or reverse_pair):
            return False
    elif source and relation.get("source_play_id") != source:
        return False
    elif target and relation.get("target_play_id") != target:
        return False

    reason = relation_reason(relation)
    expected_reason = expected.get("reason")
    if isinstance(expected_reason, str) and normalized(reason) != normalized(expected_reason):
        return False
    reason_prefix = expected.get("reason_prefix")
    if isinstance(reason_prefix, str) and not reason.startswith(reason_prefix):
        return False
    if "broad" in expected and bool(relation.get("match", {}).get("broad")) != expected["broad"]:
        return False
    supporting_fact_ids = expected.get("supporting_fact_ids_include")
    if isinstance(supporting_fact_ids, list):
        actual_supporting_fact_ids = set(relation.get("match", {}).get("supporting_fact_ids", []) or [])
        if not set(supporting_fact_ids).issubset(actual_supporting_fact_ids):
            return False
    return True


def validate_relation_expectations(regressions: dict[str, Any], relations: list[dict[str, Any]]) -> dict[str, Any]:
    failures = []
    expected_count = 0
    for fixture in regressions.get("relation_expectations", []) or []:
        expected_count += 1
        if not any(relation_matches_expectation(relation, fixture) for relation in relations):
            failures.append({"kind": "missing_expected_relation", "expected": fixture})
    return {
        "summary": {
            "expected_relation_count": expected_count,
            "pass": not failures,
        },
        "failures": failures,
    }


def validate_relation_invariants(
    regressions: dict[str, Any], relations: list[dict[str, Any]], facts: list[dict[str, Any]] | None = None
) -> dict[str, Any]:
    enabled = set(regressions.get("relation_invariants", []) or [])
    failures = []
    facts_by_id = {str(fact.get("fact_id")): fact for fact in facts or [] if fact.get("fact_id")}

    if "textual_fact_evidence_matches_source_line" in enabled:
        for fact in facts or []:
            source_ref = fact.get("source_ref", {}) or {}
            if source_ref.get("source_field") not in {"rules_lines", "effect_lines"}:
                continue
            evidence = str(fact.get("evidence") or "")
            if not evidence:
                failures.append({"kind": "textual_fact_missing_evidence", "fact_id": fact.get("fact_id")})
                continue
            source_text = " ".join(
                str(source_ref.get(key) or "")
                for key in ("line_text", "unit_text", "normalized_unit", "parameterized_unit")
            )
            if normalized(evidence) not in normalized(source_text):
                failures.append(
                    {
                        "kind": "textual_fact_evidence_not_in_source",
                        "fact_id": fact.get("fact_id"),
                        "evidence": evidence,
                    }
                )

    if "broad_relations_have_broad_reason" in enabled:
        for relation in relations:
            match = relation.get("match", {})
            if match.get("broad") and not match.get("broad_reason"):
                failures.append({"kind": "broad_relation_missing_reason", "relation_id": relation.get("relation_id")})

    if "spell_card_can_be_countered_is_broad" in enabled:
        for relation in relations:
            if relation_reason(relation) == "spell_card_can_be_countered" and not relation.get("match", {}).get("broad"):
                failures.append({"kind": "counterability_not_broad", "relation_id": relation.get("relation_id")})

    if "generic_similarity_keys_are_skipped" in enabled:
        skipped_generic_reasons = {
            "output:payoff_output:card_flow:draw:card_drawn:1:card::::required",
            "output:payoff_output:card_flow:draw:card_drawn:1:card::::optional",
            "predicate:payoff_output:payoff:repeat_effect::::optional",
            "output:state_or_modifier:state_modifier:ready:self_ready:card:::required",
            "output:state_or_modifier:state_modifier:ready:self_ready:card:::optional",
            "output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::required",
            "output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional",
        }
        for relation in relations:
            reason = relation_reason(relation)
            if relation.get("relation_type") == "similar_effect" and reason in skipped_generic_reasons:
                failures.append(
                    {
                        "kind": "generic_similarity_key_not_skipped",
                        "relation_id": relation.get("relation_id"),
                        "reason": reason,
                    }
                )

    if "no_duplicate_visual_relations" in enabled:
        seen = set()
        for relation in relations:
            key = (
                relation.get("source_play_id"),
                relation.get("target_play_id"),
                relation.get("relation_type"),
                normalized(relation_reason(relation)),
            )
            if key in seen:
                failures.append({"kind": "duplicate_visual_relation", "relation_id": relation.get("relation_id"), "key": key})
            seen.add(key)

    if "derived_synergy_does_not_duplicate_enables" in enabled:
        enables_keys = {
            (
                relation.get("source_play_id"),
                relation.get("target_play_id"),
                relation_reason(relation).removeprefix("synergy_from_"),
            )
            for relation in relations
            if relation.get("relation_type") == "enables"
        }
        for relation in relations:
            if relation.get("relation_type") != "deck_synergy" or not relation_reason(relation).startswith("synergy_from_"):
                continue
            key = (
                relation.get("source_play_id"),
                relation.get("target_play_id"),
                relation_reason(relation).removeprefix("synergy_from_"),
            )
            if key in enables_keys:
                failures.append({"kind": "derived_synergy_duplicates_enables", "relation_id": relation.get("relation_id")})

    if "opponent_paid_costs_do_not_create_relation_context" in enabled:
        opponent_paid_cost_fact_ids = {
            str(fact.get("fact_id"))
            for fact in facts or []
            if fact.get("semantic_role") == "cost_or_requirement"
            and "opponents must pay" in normalized(str(fact.get("evidence") or ""))
        }
        for relation in relations:
            matched_fact_ids = sorted(relation_fact_ids(relation) & opponent_paid_cost_fact_ids)
            if matched_fact_ids:
                failures.append(
                    {
                        "kind": "opponent_paid_cost_used_in_relation",
                        "relation_id": relation.get("relation_id"),
                        "fact_ids": matched_fact_ids,
                    }
                )

    if "cost_polarity_and_resource_synergy_are_consistent" in enabled:
        for fact in facts or []:
            evidence = normalized(str(fact.get("evidence") or ""))
            if (
                fact.get("predicate") == "reduce_cost"
                and "cost" in evidence
                and " more" in evidence
                and "no more than" not in evidence
                and "or more" not in evidence
            ):
                failures.append({"kind": "cost_more_emitted_reduce_cost", "fact_id": fact.get("fact_id")})
            if re.search(r"\bcost(?:s|ing)? no more than\b", evidence) and (
                fact.get("semantic_role") == "cost_or_requirement"
                or fact.get("predicate") in {"pay", "spend", "reduce_cost", "increase_cost"}
            ):
                failures.append(
                    {
                        "kind": "cost_cap_not_restriction",
                        "fact_id": fact.get("fact_id"),
                        "semantic_role": fact.get("semantic_role"),
                        "fact_type": fact.get("fact_type"),
                        "predicate": fact.get("predicate"),
                    }
                )

        excluded_cost_predicates = {"cost_cap_constraint", "cost_threshold", "reduce_cost", "increase_cost", "ignore_cost"}
        for relation in relations:
            match = relation.get("match", {}) or {}
            if match.get("rule_id") != "resource_synergy" and not relation_reason(relation).startswith("cost:"):
                continue
            source = facts_by_id.get(str(relation.get("source_fact_id")))
            target = facts_by_id.get(str(relation.get("target_fact_id")))
            if not source or not target:
                failures.append({"kind": "resource_synergy_missing_fact", "relation_id": relation.get("relation_id")})
                continue
            if source.get("fact_type") != "resource_change":
                failures.append(
                    {
                        "kind": "resource_synergy_source_not_resource_change",
                        "relation_id": relation.get("relation_id"),
                        "source_fact_id": source.get("fact_id"),
                    }
                )
            if (
                target.get("semantic_role") != "cost_or_requirement"
                or target.get("fact_type") not in {"activated_ability_cost", "additional_cost"}
                or target.get("predicate") in excluded_cost_predicates
                or not fact_resource_costs(target)
            ):
                failures.append(
                    {
                        "kind": "resource_synergy_target_not_real_cost",
                        "relation_id": relation.get("relation_id"),
                        "target_fact_id": target.get("fact_id"),
                        "semantic_role": target.get("semantic_role"),
                        "fact_type": target.get("fact_type"),
                        "predicate": target.get("predicate"),
                    }
                )
            supply = match.get("supply_amount")
            demand = match.get("demand_amount")
            coverage = match.get("coverage")
            cost_modality = match.get("cost_modality")
            strength = relation.get("strength")
            if isinstance(supply, int) and isinstance(demand, int) and demand > 0:
                expected_coverage = "full" if supply >= demand else "partial"
                if coverage != expected_coverage:
                    failures.append(
                        {
                            "kind": "resource_synergy_coverage_mismatch",
                            "relation_id": relation.get("relation_id"),
                            "supply_amount": supply,
                            "demand_amount": demand,
                            "coverage": coverage,
                            "expected_coverage": expected_coverage,
                        }
                    )
            if (coverage == "variable" or cost_modality == "optional") and isinstance(strength, (int, float)) and strength >= 0.68:
                failures.append(
                    {
                        "kind": "resource_synergy_unadjusted_variable_or_optional_strength",
                        "relation_id": relation.get("relation_id"),
                        "coverage": coverage,
                        "cost_modality": cost_modality,
                        "strength": strength,
                    }
                )

    if "prevented_actions_do_not_emit_blocked_positive_facts" in enabled:
        facts_by_source_line: dict[tuple[str, str, int | None, Any, str], list[dict[str, Any]]] = defaultdict(list)
        for fact in facts or []:
            facts_by_source_line[source_line_key(fact)].append(fact)

        for fact in facts or []:
            if fact.get("semantic_role") != "restriction_or_permission" or fact.get("predicate") != "prevent":
                continue
            payload = fact.get("payload", {}) or {}
            if payload.get("polarity") == "replacement" or payload.get("replacement"):
                continue
            blocked_values = prevented_positive_aliases(fact)
            if not blocked_values:
                continue
            for sibling in facts_by_source_line.get(source_line_key(fact), []):
                if sibling.get("fact_id") == fact.get("fact_id"):
                    continue
                overlap = blocked_values & positive_semantic_values(sibling)
                if overlap:
                    failures.append(
                        {
                            "kind": "prevented_action_emitted_positive_fact",
                            "prevent_fact_id": fact.get("fact_id"),
                            "positive_fact_id": sibling.get("fact_id"),
                            "blocked_values": sorted(blocked_values),
                            "matched_values": sorted(overlap),
                        }
                    )

    if "exclusive_choice_relations_do_not_mix_options" in enabled:
        for relation in relations:
            grouped_options: dict[tuple[str, str], set[Any]] = defaultdict(set)
            grouped_fact_ids: dict[tuple[str, str], list[str]] = defaultdict(list)
            for fact_id in relation_fact_ids(relation):
                fact = facts_by_id.get(fact_id)
                context = exclusive_choice_context(fact)
                if not fact or not context:
                    continue
                choice_group_id, option_index = context
                key = (str(fact.get("play_id") or ""), choice_group_id)
                grouped_options[key].add(option_index)
                grouped_fact_ids[key].append(fact_id)
            for key, options in grouped_options.items():
                if len(options) > 1:
                    failures.append(
                        {
                            "kind": "exclusive_choice_relation_mixes_options",
                            "relation_id": relation.get("relation_id"),
                            "play_id": key[0],
                            "choice_group_id": key[1],
                            "option_indexes": sorted(options),
                            "fact_ids": sorted(grouped_fact_ids[key]),
                        }
                    )

    if "gear_effect_lines_are_attached_only" in enabled:
        for fact in facts or []:
            source_ref = fact.get("source_ref", {}) or {}
            if (
                source_ref.get("source_field") != "effect_lines"
                or fact.get("semantic_role") == "identity_or_descriptor"
                or not is_gear_or_equipment_fact(fact)
            ):
                continue
            payload = fact.get("payload", {}) or {}
            if not attached_context_payload_ok(payload):
                failures.append(
                    {
                        "kind": "gear_effect_line_missing_attached_context",
                        "fact_id": fact.get("fact_id"),
                        "payload": {
                            "activation_context": payload.get("activation_context"),
                            "inactive_until_attached": payload.get("inactive_until_attached"),
                            "applies_to": payload.get("applies_to"),
                        },
                    }
                )

    if "attached_context_relations_do_not_mix_static_and_attached" in enabled:
        for relation in relations:
            if relation.get("relation_type") != "similar_effect":
                continue
            source = facts_by_id.get(str(relation.get("source_fact_id")))
            target = facts_by_id.get(str(relation.get("target_fact_id")))
            if not source or not target:
                continue
            source_context = attachment_context_key(source)
            target_context = attachment_context_key(target)
            if any("activation=attached" in context for context in (source_context, target_context)) and source_context != target_context:
                failures.append(
                    {
                        "kind": "attached_context_mixed_with_static",
                        "relation_id": relation.get("relation_id"),
                        "reason": relation_reason(relation),
                        "source_fact_id": source.get("fact_id"),
                        "source_context": source_context,
                        "target_fact_id": target.get("fact_id"),
                        "target_context": target_context,
                    }
                )

    if "combat_might_relations_preserve_attack_defense_context" in enabled:
        combat_states = {"while_attacker", "while_defender"}
        for relation in relations:
            source = facts_by_id.get(str(relation.get("source_fact_id")))
            target = facts_by_id.get(str(relation.get("target_fact_id")))
            source_states = fact_condition_states(source) & combat_states
            target_states = fact_condition_states(target) & combat_states
            if not source_states or not target_states:
                continue
            if source_states.isdisjoint(target_states):
                failures.append(
                    {
                        "kind": "combat_might_context_mismatch",
                        "relation_id": relation.get("relation_id"),
                        "source_fact_id": relation.get("source_fact_id"),
                        "source_states": sorted(source_states),
                        "target_fact_id": relation.get("target_fact_id"),
                        "target_states": sorted(target_states),
                    }
                )

    if "damage_modifier_relations_preserve_source_target_duration" in enabled:
        for relation in relations:
            if relation.get("relation_type") != "similar_effect":
                continue
            source = facts_by_id.get(str(relation.get("source_fact_id")))
            target = facts_by_id.get(str(relation.get("target_fact_id")))
            if not (is_damage_modifier_fact(source) and is_damage_modifier_fact(target)):
                continue
            source_context = damage_modifier_context(source)
            target_context = damage_modifier_context(target)
            mismatches = {
                key: {"source": source_context[key], "target": target_context[key]}
                for key in ("outputs", "unit", "value", "target_kind", "target_source", "duration", "modality", "context")
                if source_context[key] != target_context[key]
            }
            if mismatches:
                failures.append(
                    {
                        "kind": "damage_modifier_context_mismatch",
                        "relation_id": relation.get("relation_id"),
                        "reason": relation_reason(relation),
                        "source_fact_id": relation.get("source_fact_id"),
                        "target_fact_id": relation.get("target_fact_id"),
                        "mismatches": mismatches,
                    }
                )

    if "replacement_relations_preserve_prevented_event_and_mode" in enabled:
        for relation in relations:
            if relation.get("relation_type") != "similar_effect":
                continue
            source = facts_by_id.get(str(relation.get("source_fact_id")))
            target = facts_by_id.get(str(relation.get("target_fact_id")))
            if not (
                source
                and target
                and source.get("fact_type") == "replacement_effect"
                and target.get("fact_type") == "replacement_effect"
            ):
                continue
            source_context = replacement_context(source)
            target_context = replacement_context(target)
            mismatches = {
                key: {"source": source_context[key], "target": target_context[key]}
                for key in ("prevented", "replacement")
                if source_context[key] != target_context[key]
            }
            reason = relation_reason(relation)
            if reason.startswith("secondary:replacement:"):
                parts = reason.split(":")
                relation_prevented = parts[2] if len(parts) > 2 else ""
                relation_replacement = parts[3] if len(parts) > 3 else ""
                if relation_prevented not in {source_context["prevented"], target_context["prevented"]}:
                    mismatches["relation_prevented"] = {
                        "relation": relation_prevented,
                        "source": source_context["prevented"],
                        "target": target_context["prevented"],
                    }
                if relation_replacement not in {source_context["replacement"], target_context["replacement"]}:
                    mismatches["relation_replacement"] = {
                        "relation": relation_replacement,
                        "source": source_context["replacement"],
                        "target": target_context["replacement"],
                    }
            if mismatches:
                failures.append(
                    {
                        "kind": "replacement_context_mismatch",
                        "relation_id": relation.get("relation_id"),
                        "reason": reason,
                        "source_fact_id": relation.get("source_fact_id"),
                        "target_fact_id": relation.get("target_fact_id"),
                        "mismatches": mismatches,
                    }
                )

    if "keyword_grant_relations_preserve_keyword_target_duration" in enabled:
        for relation in relations:
            if relation.get("relation_type") != "similar_effect":
                continue
            source = facts_by_id.get(str(relation.get("source_fact_id")))
            target = facts_by_id.get(str(relation.get("target_fact_id")))
            if not (is_keyword_grant_fact(source) and is_keyword_grant_fact(target)):
                continue
            source_context = keyword_grant_context(source)
            target_context = keyword_grant_context(target)
            source_keywords = set(source_context["keywords"])
            target_keywords = set(target_context["keywords"])
            reason = relation_reason(relation)
            uses_duration_bucket = reason.startswith("secondary:keyword_grant_by_keyword:") or reason.startswith(
                "secondary:temporary_grant:"
            )
            relation_keywords = keyword_grant_reason_keywords(reason)
            source_target_families = set(source_context["target_families"])
            target_target_families = set(target_context["target_families"])
            relation_target_family = keyword_grant_reason_target_family(reason)
            mismatches: dict[str, Any] = {
                key: {"source": source_context[key], "target": target_context[key]}
                for key in ("modality", "context")
                if source_context[key] != target_context[key]
            }
            if uses_duration_bucket:
                if duration_bucket(source_context["duration"]) != duration_bucket(target_context["duration"]):
                    mismatches["duration_bucket"] = {
                        "source": duration_bucket(source_context["duration"]),
                        "target": duration_bucket(target_context["duration"]),
                    }
            elif source_context["duration"] != target_context["duration"]:
                mismatches["duration"] = {"source": source_context["duration"], "target": target_context["duration"]}
            if relation_target_family:
                if relation_target_family not in source_target_families or relation_target_family not in target_target_families:
                    mismatches["target_family"] = {
                        "relation": relation_target_family,
                        "source": sorted(source_target_families),
                        "target": sorted(target_target_families),
                    }
            elif source_target_families.isdisjoint(target_target_families):
                mismatches["target_family"] = {
                    "source": sorted(source_target_families),
                    "target": sorted(target_target_families),
                }
            if relation_keywords:
                missing = {
                    keyword: {
                        "source": keyword in source_keywords,
                        "target": keyword in target_keywords,
                    }
                    for keyword in sorted(relation_keywords)
                    if keyword not in source_keywords or keyword not in target_keywords
                }
                if missing:
                    mismatches["keywords"] = missing
            elif source_keywords.isdisjoint(target_keywords):
                mismatches["keywords"] = {"source": sorted(source_keywords), "target": sorted(target_keywords)}
            if mismatches:
                failures.append(
                    {
                        "kind": "keyword_grant_context_mismatch",
                        "relation_id": relation.get("relation_id"),
                        "reason": relation_reason(relation),
                        "source_fact_id": relation.get("source_fact_id"),
                        "target_fact_id": relation.get("target_fact_id"),
                        "mismatches": mismatches,
                    }
                )

    return {
        "summary": {
            "relation_count": len(relations),
            "invariant_count": len(enabled),
            "pass": not failures,
        },
        "failures": failures,
    }


def validate_dataset_invariants(regressions: dict[str, Any], dataset: dict[str, Any]) -> dict[str, Any]:
    enabled = set(regressions.get("dataset_invariants", []) or [])
    failures = []
    cards = dataset.get("cards", []) or []
    manifest = dataset.get("manifest", {})
    relation_manifest = manifest.get("relation_types", {})
    relation_types = {
        relation.get("relation_type")
        for card in cards
        for bucket in ("outgoing", "incoming")
        for relation in card.get("relations", {}).get(bucket, []) or []
        if relation.get("relation_type")
    }

    if "manifest_covers_published_relation_types" in enabled:
        missing = sorted(relation_types - set(relation_manifest))
        if missing:
            failures.append({"kind": "manifest_missing_relation_types", "missing": missing})

    if "published_relations_include_manifest_required_fields" in enabled:
        for card in cards:
            for bucket in ("outgoing", "incoming"):
                for relation in card.get("relations", {}).get(bucket, []) or []:
                    relation_type = relation.get("relation_type")
                    required = set((relation_manifest.get(relation_type) or {}).get("required_fields", []) or [])
                    missing = sorted(field for field in required if field not in relation)
                    if missing:
                        failures.append(
                            {
                                "kind": "published_relation_missing_required_fields",
                                "play_id": card.get("play_id"),
                                "relation_id": relation.get("relation_id"),
                                "relation_type": relation_type,
                                "missing": missing,
                            }
                        )

    if "cards_publish_high_signal_and_broad_counts" in enabled:
        required = {"high_signal_relation_count", "broad_relation_count", "broad_only", "outgoing_high_signal_counts", "outgoing_broad_counts"}
        for card in cards:
            missing = sorted(required - set(card.get("relations", {})))
            if missing:
                failures.append({"kind": "card_missing_relation_quality_counts", "play_id": card.get("play_id"), "missing": missing})

    if "broad_only_cards_are_explicit" in enabled:
        for card in cards:
            relations = card.get("relations", {})
            if relations.get("broad_relation_count", 0) and not relations.get("high_signal_relation_count", 0) and not relations.get("broad_only"):
                failures.append({"kind": "broad_only_not_marked", "play_id": card.get("play_id")})

    if "published_broad_relations_are_annotated" in enabled:
        broad_reasons = set(manifest.get("broad_policy", {}).get("broad_reasons", []) or [])
        for card in cards:
            for bucket in ("outgoing", "incoming"):
                for relation in card.get("relations", {}).get(bucket, []) or []:
                    match = relation.get("match", {}) or {}
                    reason = str(match.get("reason") or "")
                    if reason not in broad_reasons and not match.get("broad") and not match.get("broad_reason"):
                        continue
                    if match.get("broad") is not True:
                        failures.append(
                            {
                                "kind": "published_broad_relation_missing_flag",
                                "play_id": card.get("play_id"),
                                "relation_id": relation.get("relation_id"),
                                "reason": reason,
                            }
                        )
                    if not match.get("broad_reason"):
                        failures.append(
                            {
                                "kind": "published_broad_relation_missing_reason",
                                "play_id": card.get("play_id"),
                                "relation_id": relation.get("relation_id"),
                                "reason": reason,
                            }
                        )

    if "deck_synergy_visibility_is_explicit" in enabled:
        config = relation_manifest.get("deck_synergy")
        if not isinstance(config, dict) or "default_visible" not in config:
            failures.append({"kind": "deck_synergy_visibility_missing"})

    return {
        "summary": {
            "card_count": len(cards),
            "published_relation_type_count": len(relation_types),
            "invariant_count": len(enabled),
            "pass": not failures,
        },
        "failures": failures,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate semantic facts against curated golden examples.")
    parser.add_argument("--facts", type=Path, default=DEFAULT_FACTS)
    parser.add_argument("--relations", type=Path, default=DEFAULT_RELATIONS)
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET)
    parser.add_argument("--golden", type=Path, default=DEFAULT_GOLDEN)
    parser.add_argument("--regressions", type=Path, default=DEFAULT_REGRESSIONS)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    golden = read_json(args.golden)
    facts = read_jsonl(args.facts)
    relations = read_jsonl(args.relations) if args.relations.exists() else []
    dataset = read_json(args.dataset) if args.dataset.exists() else {}
    regressions = read_json(args.regressions) if args.regressions.exists() else {}
    report = validate(golden, facts)
    regression_report = validate_regression_facts(regressions, facts) if regressions else {"summary": {"pass": True}, "failures": []}
    relation_expectation_report = (
        validate_relation_expectations(regressions, relations) if regressions and relations else {"summary": {"pass": True}, "failures": []}
    )
    relation_report = (
        validate_relation_invariants(regressions, relations, facts)
        if regressions and relations
        else {"summary": {"pass": True}, "failures": []}
    )
    dataset_report = validate_dataset_invariants(regressions, dataset) if regressions and dataset else {"summary": {"pass": True}, "failures": []}
    report["regressions"] = regression_report
    report["relation_expectations"] = relation_expectation_report
    report["relation_invariants"] = relation_report
    report["dataset_invariants"] = dataset_report
    report["summary"]["regression_pass"] = regression_report["summary"]["pass"]
    report["summary"]["relation_expectations_pass"] = relation_expectation_report["summary"]["pass"]
    report["summary"]["relation_invariants_pass"] = relation_report["summary"]["pass"]
    report["summary"]["dataset_invariants_pass"] = dataset_report["summary"]["pass"]
    report["summary"]["pass"] = (
        report["summary"]["pass"]
        and regression_report["summary"]["pass"]
        and relation_expectation_report["summary"]["pass"]
        and relation_report["summary"]["pass"]
        and dataset_report["summary"]["pass"]
    )
    write_json(args.report, report)
    print(
        "Golden validation: "
        f"{report['summary']['matched_fact_count']}/{report['summary']['expected_fact_count']} matched"
    )
    if not report["summary"]["pass"]:
        print(f"Wrote failures to {args.report}")
        raise SystemExit(1)
    print(f"Wrote report to {args.report}")


if __name__ == "__main__":
    main()
