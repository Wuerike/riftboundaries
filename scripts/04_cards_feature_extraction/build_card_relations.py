import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
from typing import Any

from semantic_contracts import DEFAULT_QUALITY_POLICY, DEFAULT_RELATION_RULES, load_contract_bundle


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
CONTRACTS_DIR = SCRIPT_DIR / "contracts"

DEFAULT_FACTS = PROJECT_ROOT / "data" / "processed" / "cards" / "semantic" / "cards_semantic_facts.jsonl"
DEFAULT_SCHEMA = CONTRACTS_DIR / "semantic_facts_schema.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "processed" / "cards" / "relations" / "cards_card_relations.jsonl"
DEFAULT_REPORT = PROJECT_ROOT / "data" / "processed" / "cards" / "relations" / "cards_card_relations_report.json"
DEFAULT_MARKDOWN = PROJECT_ROOT / "data" / "processed" / "cards" / "relations" / "cards_card_relations_report.md"

SCHEMA_VERSION = "2026-05-12"
DAMAGE_MODIFIER_OUTPUT_IDS = {"bonus_damage_added", "damage_modified"}


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


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def slug(value: str) -> str:
    cleaned = "".join(ch if ch.isalnum() else "_" for ch in value.casefold()).strip("_")
    return "_".join(part for part in cleaned.split("_") if part) or "unknown"


def normalize_rune_domain(domain: Any) -> str:
    value = str(domain or "").casefold()
    return "any" if value in {"rainbow", "any"} else value


def is_opponent_paid_cost(fact: dict[str, Any]) -> bool:
    if fact.get("semantic_role") != "cost_or_requirement":
        return False
    return bool(re.search(r"\bopponents?\s+must\s+pay\b", str(fact.get("evidence") or ""), flags=re.IGNORECASE))


def relation_id(relation_type: str, source_fact_id: str, target_fact_id: str, reason: str) -> str:
    digest = hashlib.sha1(f"{relation_type}|{source_fact_id}|{target_fact_id}|{reason}".encode("utf-8")).hexdigest()[:16]
    return f"rel:{slug(relation_type)}:{slug(reason)}:{digest}"


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
    return sorted(set(event_ids))


def output_ids_from_fact(fact: dict[str, Any]) -> list[str]:
    return sorted(
        {
            output["id"]
            for output in fact.get("payload", {}).get("outputs", []) or []
            if isinstance(output, dict) and isinstance(output.get("id"), str)
        }
    )


def payload_path(payload: dict[str, Any], path: str) -> Any:
    value: Any = payload
    for part in path.split("."):
        if isinstance(value, list):
            try:
                value = value[int(part)]
            except (ValueError, IndexError):
                return None
            continue
        if not isinstance(value, dict):
            return None
        value = value.get(part)
    return value


def fact_matches_selector(fact: dict[str, Any], selector: dict[str, Any]) -> bool:
    if selector.get("semantic_role") and fact.get("semantic_role") != selector["semantic_role"]:
        return False
    if selector.get("fact_type") and fact.get("fact_type") != selector["fact_type"]:
        return False
    if selector.get("predicate") and fact.get("predicate") != selector["predicate"]:
        return False
    if selector.get("event_id") and selector["event_id"] not in event_ids_from_fact(fact):
        return False
    if selector.get("output_id") and selector["output_id"] not in output_ids_from_fact(fact):
        return False
    for path, expected in (selector.get("payload") or {}).items():
        if payload_path(fact.get("payload", {}), path) != expected:
            return False
    for path in selector.get("payload_absent") or []:
        if payload_path(fact.get("payload", {}), str(path)) is not None:
            return False
    return True


def cost_keys_from_fact(fact: dict[str, Any]) -> list[str]:
    if is_opponent_paid_cost(fact):
        return []
    keys = []
    for cost in fact.get("payload", {}).get("costs", []) or []:
        if not isinstance(cost, dict):
            continue
        resource = cost.get("resource")
        if resource:
            domain = normalize_rune_domain(cost.get("domain"))
            amount = cost.get("amount")
            if resource == "energy" and amount is not None:
                keys.append(f"cost:energy:{amount}")
            elif resource == "rune" and domain:
                keys.append(f"cost:rune:{domain}")
        action = cost.get("action")
        if action:
            keys.append(f"cost_action:{action}")
    return sorted(set(keys))


def output_keys_from_fact(fact: dict[str, Any]) -> list[str]:
    keys = []
    for output in fact.get("payload", {}).get("outputs", []) or []:
        if not isinstance(output, dict):
            continue
        action = output.get("action")
        object_id = output.get("object")
        output_id = output.get("id")
        if output_id:
            keys.append(f"output:{output_id}")
        if action:
            keys.append(f"output_action:{action}:{object_id or 'any'}")
    if fact.get("fact_type") == "resource_change":
        for amount in fact.get("payload", {}).get("amounts", []) or []:
            if not isinstance(amount, dict):
                continue
            unit = amount.get("unit")
            if unit == "energy":
                if amount.get("value") is not None and amount.get("value") != "variable":
                    keys.append(f"cost:energy:{amount.get('value')}")
            elif unit == "rune":
                domain = normalize_rune_domain(amount.get("domain"))
                if domain:
                    keys.append(f"cost:rune:{domain}")
                    if domain != "any":
                        keys.append("cost:rune:any")
        resource = fact.get("payload", {}).get("resource")
        if isinstance(resource, dict):
            unit = resource.get("resource")
            if unit == "energy":
                if resource.get("amount") is not None:
                    keys.append(f"cost:energy:{resource.get('amount')}")
            elif unit == "rune":
                domain = normalize_rune_domain(resource.get("domain"))
                if domain:
                    keys.append(f"cost:rune:{domain}")
                    if domain != "any":
                        keys.append("cost:rune:any")
    return sorted(set(keys))


def relation(
    relation_type: str,
    source: dict[str, Any],
    target: dict[str, Any],
    *,
    reason: str,
    strength: float,
    event_id: str | None = None,
    output_id: str | None = None,
    extra_match: dict[str, Any] | None = None,
) -> dict[str, Any]:
    match = {
        "event_id": event_id,
        "output_id": output_id,
        "source_role": source.get("semantic_role"),
        "target_role": target.get("semantic_role"),
        "reason": reason,
    }
    if extra_match:
        match.update(extra_match)
    if match.get("broad") and not match.get("broad_reason"):
        match["broad_reason"] = reason
    return {
        "schema_version": SCHEMA_VERSION,
        "relation_id": relation_id(relation_type, source["fact_id"], target["fact_id"], reason),
        "source_play_id": source["play_id"],
        "target_play_id": target["play_id"],
        "source_card_name": source.get("card_name"),
        "target_card_name": target.get("card_name"),
        "relation_type": relation_type,
        "source_fact_id": source["fact_id"],
        "target_fact_id": target["fact_id"],
        "match": match,
        "strength": round(strength, 3),
        "evidence": {
            "source": source.get("evidence"),
            "target": target.get("evidence"),
        },
    }


def produced_event_facts(facts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        fact
        for fact in facts
        if fact.get("semantic_role") == "event_produced" or fact.get("fact_type") == "token_creation"
    ]


def observed_trigger_facts(facts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [fact for fact in facts if fact.get("semantic_role") == "trigger_observed"]


def relation_event_matches(
    source_event: str,
    target_event: str,
    producer: dict[str, Any],
    event_rules: list[dict[str, Any]],
) -> tuple[dict[str, Any] | None, float, str]:
    for rule in event_rules:
        if rule.get("source_event") != source_event or rule.get("target_event") != target_event:
            continue
        source_selector = rule.get("source_selector")
        if source_selector and not fact_matches_selector(producer, source_selector):
            continue
        source_card_types = set(rule.get("source_card_types") or [])
        if source_card_types:
            producer_card_types = set(producer.get("card_snapshot", {}).get("card_type_ids", []) or [])
            if not source_card_types.intersection(producer_card_types):
                continue
        return rule, float(rule.get("strength", 0.0)), str(rule.get("reason") or rule.get("rule_id"))
    return None, 0.0, ""


def build_identity_event_relations(facts: list[dict[str, Any]], relation_rules: dict[str, Any]) -> list[dict[str, Any]]:
    relations = []
    for rule in relation_rules.get("identity_event_relations", []) or []:
        source_facts = [fact for fact in facts if fact_matches_selector(fact, rule.get("source_selector", {}))]
        target_facts = [fact for fact in facts if fact_matches_selector(fact, rule.get("target_selector", {}))]
        for source in source_facts:
            for target in target_facts:
                if source["play_id"] == target["play_id"]:
                    continue
                reason = str(rule.get("reason") or rule["rule_id"])
                strength = float(rule.get("strength", 0.0))
                if "enables" in rule.get("relation_types", []):
                    relations.append(
                        relation(
                            "enables",
                            source,
                            target,
                            reason=reason,
                            strength=strength,
                            event_id=rule.get("event_id"),
                            extra_match={
                                "rule_id": rule["rule_id"],
                                "target_event_id": rule.get("target_selector", {}).get("event_id"),
                                "broad": bool(rule.get("broad")),
                            },
                        )
                    )
                if "enabled_by" in rule.get("relation_types", []):
                    relations.append(
                        relation(
                            "enabled_by",
                            target,
                            source,
                            reason=reason,
                            strength=strength,
                            event_id=rule.get("event_id"),
                            extra_match={
                                "rule_id": rule["rule_id"],
                                "source_event_id": rule.get("target_selector", {}).get("event_id"),
                                "broad": bool(rule.get("broad")),
                            },
                        )
                    )
    return relations


def build_direct_synergy_relations(facts: list[dict[str, Any]], relation_rules: dict[str, Any]) -> list[dict[str, Any]]:
    relations = []
    for rule in relation_rules.get("direct_synergy", []) or []:
        sources = [fact for fact in facts if fact_matches_selector(fact, rule.get("source_selector", {}))]
        targets = [fact for fact in facts if fact_matches_selector(fact, rule.get("target_selector", {}))]
        for source in sources:
            for target in targets:
                if source["play_id"] == target["play_id"]:
                    continue
                relations.append(
                    relation(
                        rule.get("relation_type", "deck_synergy"),
                        source,
                        target,
                        reason=str(rule.get("reason") or rule["rule_id"]),
                        strength=float(rule.get("strength", 0.0)),
                        event_id=rule.get("event_id"),
                        extra_match={"rule_id": rule["rule_id"], "target_event_id": rule.get("target_event_id")},
                    )
                )
    return relations


def build_enables_relations(facts: list[dict[str, Any]], relation_rules: dict[str, Any]) -> list[dict[str, Any]]:
    relations = []
    observers_by_event: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for observer in observed_trigger_facts(facts):
        for event_id in event_ids_from_fact(observer):
            observers_by_event[event_id].append(observer)

    for producer in produced_event_facts(facts):
        for source_event in event_ids_from_fact(producer):
            possible_targets = []
            for target_event, observers in observers_by_event.items():
                matched_rule, strength, reason = relation_event_matches(
                    source_event,
                    target_event,
                    producer,
                    relation_rules.get("event_enables", []) or [],
                )
                if matched_rule:
                    possible_targets.extend((observer, target_event, strength, reason, matched_rule) for observer in observers)
            for observer, target_event, strength, reason, matched_rule in possible_targets:
                if producer["play_id"] == observer["play_id"]:
                    continue
                relations.append(
                    relation(
                        "enables",
                        producer,
                        observer,
                        reason=reason,
                        strength=strength,
                        event_id=target_event,
                        extra_match={"source_event_id": source_event, "rule_id": matched_rule["rule_id"]},
                    )
                )
                relations.append(
                    relation(
                        "enabled_by",
                        observer,
                        producer,
                        reason=reason,
                        strength=strength,
                        event_id=target_event,
                        extra_match={
                            "source_event_id": target_event,
                            "target_event_id": source_event,
                            "rule_id": matched_rule["rule_id"],
                        },
                    )
                )
    return relations


def build_token_synergy_relations(facts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    token_creators = [
        fact
        for fact in facts
        if fact.get("fact_type") == "token_creation" and "token_created" in event_ids_from_fact(fact)
    ]
    token_entry_modifiers = [
        fact
        for fact in facts
        if fact.get("semantic_role") == "state_or_modifier" and "token_enters" in event_ids_from_fact(fact)
    ]
    relations = []
    for creator in token_creators:
        for modifier in token_entry_modifiers:
            if creator["play_id"] == modifier["play_id"]:
                continue
            relations.append(
                relation(
                    "deck_synergy",
                    creator,
                    modifier,
                    reason="token_created_to_token_entry_modifier",
                    strength=0.82,
                    event_id="token_created",
                    extra_match={"target_event_id": "token_enters"},
                )
            )
    return relations


def build_enables_synergy_relations(
    enables_relations: list[dict[str, Any]],
    facts_by_id: dict[str, dict[str, Any]],
    relation_rules: dict[str, Any],
) -> list[dict[str, Any]]:
    config = relation_rules.get("derived_synergy", {})
    if not config.get("enabled", True):
        return []
    relations = []
    for enables_relation in enables_relations:
        if enables_relation["relation_type"] != config.get("source_relation_type", "enables"):
            continue
        if enables_relation.get("match", {}).get("broad"):
            continue
        source = facts_by_id[enables_relation["source_fact_id"]]
        target = facts_by_id[enables_relation["target_fact_id"]]
        relations.append(
            relation(
                config.get("relation_type", "deck_synergy"),
                source,
                target,
                reason=f"{config.get('reason_prefix', 'synergy_from_')}{enables_relation['match']['reason']}",
                strength=max(0.0, enables_relation["strength"] + float(config.get("strength_delta", -0.12))),
                event_id=enables_relation["match"].get("event_id"),
                extra_match={
                    "source_relation_id": enables_relation["relation_id"],
                    "rule_id": "derived_synergy",
                },
            )
        )
    return relations


def numeric_amount(value: Any, default: int = 1) -> int | str:
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str) and value.isdigit():
        return int(value)
    if value == "variable":
        return "variable"
    return default


def resource_output_entries(fact: dict[str, Any]) -> list[dict[str, Any]]:
    if fact.get("fact_type") != "resource_change":
        return []
    payload = fact.get("payload", {}) or {}
    entries = []
    for amount in payload.get("amounts", []) or []:
        if not isinstance(amount, dict):
            continue
        unit = amount.get("unit")
        value = numeric_amount(amount.get("value"))
        if unit == "energy":
            entries.append({"key": f"cost:energy:{value}", "family_key": "cost:energy:any", "amount": value, "resource": "energy"})
            entries.append({"key": "cost:energy:partial", "amount": value, "resource": "energy"})
        elif unit == "xp":
            entries.append({"key": f"cost:xp:{value}", "amount": value, "resource": "xp"})
            entries.append({"key": "cost:xp:partial", "amount": value, "resource": "xp"})
        elif unit == "rune":
            domain = normalize_rune_domain(amount.get("domain") or payload.get("resource", {}).get("domain"))
            if domain:
                entries.append({"key": f"cost:rune:{domain}", "family_key": "cost:rune:any", "amount": value, "resource": "rune", "domain": domain})
    resource = payload.get("resource")
    if isinstance(resource, dict) and not entries:
        unit = resource.get("resource")
        value = numeric_amount(resource.get("amount"))
        if unit == "energy":
            entries.append({"key": f"cost:energy:{value}", "family_key": "cost:energy:any", "amount": value, "resource": "energy"})
            entries.append({"key": "cost:energy:partial", "amount": value, "resource": "energy"})
        elif unit == "xp":
            entries.append({"key": f"cost:xp:{value}", "amount": value, "resource": "xp"})
            entries.append({"key": "cost:xp:partial", "amount": value, "resource": "xp"})
        elif unit == "rune":
            domain = normalize_rune_domain(resource.get("domain"))
            if domain:
                entries.append({"key": f"cost:rune:{domain}", "family_key": "cost:rune:any", "amount": value, "resource": "rune", "domain": domain})
    return entries


def resource_cost_entries(fact: dict[str, Any]) -> list[dict[str, Any]]:
    if fact.get("semantic_role") != "cost_or_requirement":
        return []
    if is_opponent_paid_cost(fact):
        return []
    if fact.get("predicate") in {"cost_cap_constraint", "cost_threshold", "reduce_cost", "increase_cost", "ignore_cost"}:
        return []
    if fact.get("fact_type") not in {"activated_ability_cost", "additional_cost"}:
        return []
    costs = [cost for cost in fact.get("payload", {}).get("costs", []) or [] if isinstance(cost, dict)]
    entries = []
    rune_counts: Counter[str] = Counter()
    energy_counts: Counter[int | str] = Counter()
    xp_counts: Counter[int | str] = Counter()
    base_entry = {
        "modality": fact.get("payload", {}).get("modality"),
        "fact_type": fact.get("fact_type"),
    }
    for cost in costs:
        resource = cost.get("resource")
        amount = numeric_amount(cost.get("amount"))
        if resource == "energy":
            energy_counts[amount] += amount if isinstance(amount, int) else 1
        elif resource == "xp":
            xp_counts[amount] += amount if isinstance(amount, int) else 1
        elif resource == "rune":
            domain = normalize_rune_domain(cost.get("domain"))
            if domain:
                rune_counts[domain] += amount if isinstance(amount, int) else 1
    for amount, count in energy_counts.items():
        entries.append({"key": f"cost:energy:{amount}", "demand": count, "resource": "energy", **base_entry})
        if isinstance(amount, int) and amount >= 3:
            entries.append({"key": "cost:energy:partial", "demand": count, "resource": "energy", **base_entry})
    for amount, count in xp_counts.items():
        entries.append({"key": f"cost:xp:{amount}", "demand": count, "resource": "xp", **base_entry})
        if isinstance(amount, int) and amount >= 4:
            entries.append({"key": "cost:xp:partial", "demand": count, "resource": "xp", **base_entry})
    for domain, count in rune_counts.items():
        entries.append({"key": f"cost:rune:{domain}", "demand": count, "resource": "rune", "domain": domain, **base_entry})
        if domain == "any":
            for rune_domain in ("body", "calm", "chaos", "fury", "mind", "order"):
                entries.append({"key": f"cost:rune:{rune_domain}", "demand": count, "resource": "rune", "domain": "any", **base_entry})
        else:
            entries.append({"key": "cost:rune:any", "demand": count, "resource": "rune", "domain": domain, **base_entry})
    return entries


def coverage_strength(base_strength: float, supply: Any, demand: Any) -> tuple[float, str]:
    if supply == "variable" or demand == "variable":
        return round(base_strength * 0.9, 3), "variable"
    if not isinstance(supply, int) or not isinstance(demand, int) or demand <= 0:
        return base_strength, "unknown"
    if supply >= demand:
        return base_strength, "full"
    return max(0.25, round(base_strength * max(0.45, supply / demand), 3)), "partial"


def adjust_resource_synergy_strength(strength: float, cost_entry: dict[str, Any]) -> tuple[float, list[str]]:
    adjustments = []
    if cost_entry.get("modality") == "optional":
        strength = round(strength * 0.9, 3)
        adjustments.append("optional_cost")
    return strength, adjustments


def build_resource_synergy_relations(facts: list[dict[str, Any]], relation_rules: dict[str, Any]) -> list[dict[str, Any]]:
    config = relation_rules.get("resource_synergy", {})
    if not config.get("enabled", True):
        return []
    producers_by_key: dict[str, list[dict[str, Any]]] = defaultdict(list)
    costs_by_key: dict[str, list[dict[str, Any]]] = defaultdict(list)
    producer_entries_by_fact_id: dict[str, dict[str, Any]] = {}
    cost_entries_by_fact_id: dict[str, dict[str, Any]] = {}

    for fact in facts:
        for entry in resource_output_entries(fact):
            producers_by_key[entry["key"]].append(fact)
            producer_entries_by_fact_id[f"{fact['fact_id']}|{entry['key']}"] = entry
        for entry in resource_cost_entries(fact):
            costs_by_key[entry["key"]].append(fact)
            cost_entries_by_fact_id[f"{fact['fact_id']}|{entry['key']}"] = entry

    relations = []
    producer_key_prefix = config.get("producer_key_prefix", "cost:")
    for key, producers in producers_by_key.items():
        if not key.startswith(producer_key_prefix):
            continue
        for producer in producers:
            for cost in costs_by_key.get(key, []):
                if producer["play_id"] == cost["play_id"]:
                    continue
                producer_entry = producer_entries_by_fact_id.get(f"{producer['fact_id']}|{key}", {})
                cost_entry = cost_entries_by_fact_id.get(f"{cost['fact_id']}|{key}", {})
                strength, coverage = coverage_strength(
                    float(config.get("strength", 0.68)),
                    producer_entry.get("amount", 1),
                    cost_entry.get("demand", 1),
                )
                strength, strength_adjustments = adjust_resource_synergy_strength(strength, cost_entry)
                relations.append(
                    relation(
                        config.get("relation_type", "deck_synergy"),
                        producer,
                        cost,
                        reason=key,
                        strength=strength,
                        extra_match={
                            "resource_key": key,
                            "coverage": coverage,
                            "supply_amount": producer_entry.get("amount"),
                            "demand_amount": cost_entry.get("demand"),
                            "cost_modality": cost_entry.get("modality"),
                            "strength_adjustments": strength_adjustments,
                            "rule_id": "resource_synergy",
                        },
                    )
                )
    return relations


def build_tag_target_synergy_relations(facts: list[dict[str, Any]], relation_rules: dict[str, Any]) -> list[dict[str, Any]]:
    config = relation_rules.get("tag_target_synergy", {})
    if not config.get("enabled", False):
        return []
    tag_facts_by_id: dict[str, list[dict[str, Any]]] = defaultdict(list)
    labels_by_tag_id: dict[str, str] = {}
    for fact in facts:
        tag_id = tag_id_from_identity_fact(fact)
        if not tag_id:
            continue
        tag_facts_by_id[tag_id].append(fact)
        labels_by_tag_id.setdefault(tag_id, tag_label_from_identity_fact(fact))

    max_targets = int(config.get("max_targets_per_tag", 30))
    relations = []
    for source in facts:
        for tag_id in referenced_tag_ids_from_fact(source, labels_by_tag_id):
            targets = tag_facts_by_id.get(tag_id, [])
            if not targets or len({target["play_id"] for target in targets}) > max_targets:
                continue
            for target in targets:
                if source["play_id"] == target["play_id"]:
                    continue
                relations.append(
                    relation(
                        config.get("relation_type", "deck_synergy"),
                        source,
                        target,
                        reason=f"{config.get('reason_prefix', 'target_tag:')}{tag_id}",
                        strength=float(config.get("strength", 0.66)),
                        extra_match={"rule_id": "tag_target_synergy", "target_tag": tag_id},
                    )
                )
    return relations


def target_key_from_payload(target: Any) -> str:
    if not isinstance(target, dict):
        return ""
    if isinstance(target.get("kinds"), list):
        base = "+".join(sorted(str(item) for item in target["kinds"]))
    else:
        base = str(target.get("kind") or target.get("scope") or "")
    if not base:
        base = str(target.get("raw") or "")
    if not base:
        base = str(target.get("zone") or target.get("location") or "")
    facets = []
    for key in ("controller", "location", "location_state", "token_state", "zone"):
        if target.get(key):
            facets.append(f"{key}={target[key]}")
    if facets and base:
        return f"{base}[{';'.join(facets)}]"
    return base


def normalized_controller(value: Any) -> str:
    if value == "you":
        return "friendly"
    return str(value or "")


def coarse_target_key_from_payload(target: Any, *, include_location: bool = True) -> str:
    if not isinstance(target, dict):
        return ""
    if isinstance(target.get("kinds"), list):
        base = "+".join(sorted(str(item) for item in target["kinds"]))
    else:
        base = str(target.get("kind") or target.get("scope") or "")
    if not base:
        base = str(target.get("zone") or target.get("location") or "")
    if not base:
        return ""
    facets = []
    controller = normalized_controller(target.get("controller"))
    if controller:
        facets.append(f"controller={controller}")
    if include_location:
        for key in ("location", "token_state", "zone"):
            if target.get(key):
                facets.append(f"{key}={target[key]}")
    elif target.get("zone"):
        facets.append(f"zone={target['zone']}")
    if facets:
        return f"{base}[{';'.join(facets)}]"
    return base


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


def state_target_key_from_payload(target: Any, *, include_location: bool = False) -> str:
    if not isinstance(target, dict):
        return ""
    if isinstance(target.get("kinds"), list):
        base = "+".join(sorted(str(item) for item in target["kinds"]))
    else:
        base = str(target.get("kind") or target.get("scope") or "")
    raw_family = inferred_target_family_from_raw(target)
    if raw_family and (not base or base in {"card", "self"}):
        base = raw_family
    if not base:
        base = str(target.get("zone") or target.get("location") or "")
    if not base:
        return ""
    facets = []
    controller = normalized_controller(target.get("controller"))
    if controller:
        facets.append(f"controller={controller}")
    if target.get("token_state") and base != "token":
        facets.append(f"token_state={target['token_state']}")
    if include_location:
        for key in ("location", "location_state", "zone"):
            if target.get(key):
                facets.append(f"{key}={target[key]}")
    elif target.get("zone"):
        facets.append(f"zone={target['zone']}")
    if facets:
        return f"{base}[{';'.join(facets)}]"
    return base


def state_target_families_from_payload(target: Any, *, include_location: bool = False) -> list[str]:
    target_key = state_target_key_from_payload(target, include_location=include_location)
    families = {target_key.split("[", 1)[0]} if target_key else set()
    if isinstance(target, dict):
        if isinstance(target.get("kinds"), list):
            families.update(str(item) for item in target["kinds"] if item)
        raw_family = inferred_target_family_from_raw(target)
        if raw_family:
            families.add(raw_family)
    return sorted(family for family in families if family)


def stat_target_key_from_payload(target: Any, *, include_location: bool = True) -> str:
    return coarse_target_key_from_payload(target, include_location=include_location) or state_target_key_from_payload(
        target, include_location=include_location
    )


def destination_key_from_payload(destination: Any) -> str:
    if not isinstance(destination, dict):
        return ""
    base = str(destination.get("zone") or destination.get("location") or destination.get("raw") or "")
    facets = []
    for key in ("state", "controller", "location", "owner"):
        if destination.get(key):
            facets.append(f"{key}={destination[key]}")
    if facets and base:
        return f"{base}[{';'.join(facets)}]"
    return base


def coarse_destination_key_from_payload(destination: Any) -> str:
    if not isinstance(destination, dict):
        return ""
    base = str(destination.get("zone") or destination.get("location") or "")
    if not base:
        return ""
    facets = []
    if destination.get("controller"):
        facets.append(f"controller={normalized_controller(destination['controller'])}")
    if facets:
        return f"{base}[{';'.join(facets)}]"
    return base


def source_key_from_payload(source: Any) -> str:
    if not isinstance(source, dict):
        return ""
    base = str(source.get("zone") or source.get("location") or source.get("raw") or "")
    if not base:
        return ""
    facets = []
    if source.get("controller"):
        facets.append(f"controller={normalized_controller(source['controller'])}")
    if facets:
        return f"{base}[{';'.join(facets)}]"
    return base


def object_key_from_payload(obj: Any) -> str:
    if not isinstance(obj, dict):
        return ""
    if isinstance(obj.get("kinds"), list):
        base = "+".join(sorted(str(item) for item in obj["kinds"]))
    else:
        base = str(obj.get("kind") or obj.get("raw") or obj.get("zone") or "")
    if not base:
        return ""
    facets = []
    for key in ("controller", "location", "zone"):
        if obj.get(key):
            facets.append(f"{key}={obj[key]}")
    if facets:
        return f"{base}[{';'.join(facets)}]"
    return base


def tag_id_from_identity_fact(fact: dict[str, Any]) -> str:
    if fact.get("predicate") != "has_tag":
        return ""
    obj = fact.get("payload", {}).get("object") or {}
    if not isinstance(obj, dict) or obj.get("kind") != "tag":
        return ""
    return str(obj.get("id") or "")


def tag_label_from_identity_fact(fact: dict[str, Any]) -> str:
    obj = fact.get("payload", {}).get("object") or {}
    if not isinstance(obj, dict):
        return ""
    return str(obj.get("label") or obj.get("id") or "")


def raw_texts_from_payload(value: Any) -> list[str]:
    texts: list[str] = []
    if isinstance(value, dict):
        raw = value.get("raw")
        if isinstance(raw, str) and raw.strip():
            texts.append(raw)
        for key in ("target", "object", "source", "destination"):
            nested = value.get(key)
            if isinstance(nested, dict):
                texts.extend(raw_texts_from_payload(nested))
    elif isinstance(value, list):
        for item in value:
            texts.extend(raw_texts_from_payload(item))
    return texts


def referenced_tag_ids_from_fact(fact: dict[str, Any], labels_by_tag_id: dict[str, str]) -> list[str]:
    if fact.get("semantic_role") in {"identity_or_descriptor", "trigger_observed"}:
        return []
    text = " ".join(raw_texts_from_payload(fact.get("payload", {}) or {}))
    if not text.strip():
        return []
    found = []
    for tag_id, label in labels_by_tag_id.items():
        label_text = str(label or tag_id).strip()
        if not label_text:
            continue
        pattern = r"(?<![A-Za-z0-9])" + re.escape(label_text) + r"(?![A-Za-z0-9])"
        if re.search(pattern, text, re.I):
            found.append(tag_id)
    return sorted(set(found))


def attachment_context_key(payload: dict[str, Any]) -> str:
    facets = []
    if payload.get("activation_context"):
        facets.append(f"activation={payload['activation_context']}")
    if payload.get("inactive_until_attached"):
        facets.append("inactive_until_attached")
    if payload.get("applies_to"):
        facets.append(f"applies_to={payload['applies_to']}")
    return ";".join(facets) or "active"


def amount_sign(value: Any) -> str:
    if isinstance(value, (int, float)):
        if value > 0:
            return "positive"
        if value < 0:
            return "negative"
        return "zero"
    if value is not None:
        return "variable"
    return ""


def amount_bucket(value: Any) -> str:
    if isinstance(value, (int, float)):
        if value >= 3:
            return "large"
        if value > 0:
            return "small"
        return "zero"
    if value is not None:
        return "variable"
    return ""


def compact_value_key(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"[^a-z0-9_+-]+", "_", str(value).casefold()).strip("_")


def damage_modifier_target_key_from_payload(target: Any, *, include_location: bool = False) -> str:
    base = coarse_target_key_from_payload(target, include_location=include_location) or state_target_key_from_payload(
        target, include_location=include_location
    )
    if not base or not isinstance(target, dict):
        return base
    facets = []
    source = compact_value_key(target.get("source"))
    if source:
        facets.append(f"source={source}")
    if not facets:
        return base
    if base.endswith("]") and "[" in base:
        return f"{base[:-1]};{';'.join(facets)}]"
    return f"{base}[{';'.join(facets)}]"


def damage_scaling_basis(value: Any) -> str:
    text = str(value or "").casefold()
    if "might" not in text:
        return ""
    if re.search(r"\b(?:our|their)\s+mights?\b", text):
        return "mutual_might"
    if re.search(r"\bmy\s+might\b", text):
        return "self_might"
    if re.search(r"\b(?:its|his|her)\s+might\b", text):
        return "source_might"
    return "might"


def condition_states_from_payload(payload: dict[str, Any]) -> list[str]:
    states = []
    for condition in payload.get("conditions", []) or []:
        if not isinstance(condition, dict):
            continue
        state = compact_value_key(condition.get("state"))
        if state:
            states.append(state)
    return sorted(set(states))


INTRINSIC_KEYWORD_REQUIREMENT_CONTEXTS = {
    "assault": "duration=while,state=while_attacker",
    "shield": "duration=while,state=while_defender",
}


def keyword_from_similarity_key(key: str) -> str:
    if key.startswith("secondary:keyword_grant:") or key.startswith("secondary:keyword_grant_by_keyword:"):
        parts = key.split(":")
        if len(parts) > 2:
            return compact_value_key(parts[2])
    if key.startswith("secondary:temporary_grant:"):
        return "temporary"
    match = re.search(r"(?:^|[:;])keywords=([^:;]+)", key)
    if match:
        keywords = [compact_value_key(keyword) for keyword in match.group(1).split(",") if compact_value_key(keyword)]
        if len(keywords) == 1:
            return keywords[0]
    return ""


def duration_bucket(duration: Any) -> str:
    duration_key = compact_value_key(duration)
    if duration_key in {"this_turn", "this_combat", "until_end_of_turn"}:
        return "temporary"
    return duration_key or "ongoing"


def intrinsic_keyword_requirement_context_for_key(key: str) -> str:
    keyword = keyword_from_similarity_key(key)
    return INTRINSIC_KEYWORD_REQUIREMENT_CONTEXTS.get(keyword, "")


def cost_reduction_target_families(payload: dict[str, Any]) -> list[str]:
    target = payload.get("target")
    families: set[str] = set()
    if isinstance(target, dict):
        for value in target.get("card_types", []) or []:
            families.add(str(value))
        for value in target.get("kinds", []) or []:
            families.add(str(value))
        if target.get("kind"):
            families.add(str(target["kind"]))
    if not families:
        target_key = coarse_target_key_from_payload(target, include_location=False)
        if target_key:
            families.add(target_key.split("[", 1)[0])
    normalized = {compact_value_key(value) for value in families}
    normalized.discard("")
    normalized.discard("card")
    return sorted(normalized)


def cost_context_facets_from_fact(fact: dict[str, Any]) -> list[str]:
    if fact.get("semantic_role") != "cost_or_requirement":
        return []
    if is_opponent_paid_cost(fact):
        return []
    facets = []
    for cost in fact.get("payload", {}).get("costs", []) or []:
        if not isinstance(cost, dict):
            continue
        resource = cost.get("resource")
        amount = cost.get("amount")
        if resource == "rune":
            domain = normalize_rune_domain(cost.get("domain"))
            if domain:
                suffix = f"x{compact_value_key(amount)}" if amount not in {None, 1} else ""
                facets.append(f"rune={domain}{suffix}")
        elif resource:
            amount_key = compact_value_key(amount) or "any"
            facets.append(f"{compact_value_key(resource)}={amount_key}")
        action = cost.get("action")
        if action:
            actor = cost.get("subject") or cost.get("object") or ""
            actor_key = compact_value_key(actor)
            facets.append(f"action={compact_value_key(action)}{':' + actor_key if actor_key else ''}")
    return sorted(set(facets))


def requirement_context_facets_from_fact(fact: dict[str, Any]) -> list[str]:
    if (
        fact.get("semantic_role") != "restriction_or_permission"
        or fact.get("predicate") != "require"
    ):
        return []
    payload = fact.get("payload", {}) or {}
    facets = []
    for condition in payload.get("conditions", []) or []:
        if not isinstance(condition, dict):
            continue
        state = condition.get("state")
        if state:
            facets.append(f"state={compact_value_key(state)}")
            continue
        for key, value in sorted(condition.items()):
            if isinstance(value, (str, int, float, bool)):
                value_key = compact_value_key(value)
                if value_key:
                    facets.append(f"{compact_value_key(key)}={value_key}")
    duration = compact_value_key(payload.get("duration"))
    if duration:
        facets.append(f"duration={duration}")
    attachment_context = attachment_context_key(payload)
    if attachment_context != "active":
        facets.append(attachment_context)
    return sorted(set(facets))


def secondary_similar_keys(fact: dict[str, Any], relation_rules: dict[str, Any]) -> list[str]:
    config = relation_rules.get("similarity", {})
    enabled_families = set(config.get("secondary_key_families", []) or [])
    payload = fact.get("payload", {}) or {}
    output_ids = output_ids_from_fact(fact)
    output_ids_set = set(output_ids)
    event_ids = event_ids_from_fact(fact)
    amounts = payload.get("amounts") or []
    amount = amounts[0] if amounts and isinstance(amounts[0], dict) else {}
    duration = payload.get("duration") or ""
    modality = payload.get("modality") or ""
    context = attachment_context_key(payload)
    keys: list[str] = []

    if (
        "stat_modifier"
        in enabled_families
        and fact.get("predicate") == "modify_stat"
        and output_ids
        and not (DAMAGE_MODIFIER_OUTPUT_IDS & output_ids_set)
        and fact.get("semantic_role") == "state_or_modifier"
    ):
        multiplier = payload.get("multiplier")
        if multiplier:
            stat = payload.get("stat") or ("might" if "might_modified" in output_ids else output_ids[0])
            keys.append(f"secondary:stat_multiplier:{stat}:{multiplier}:{context}")
            keys.append(f"secondary:stat_multiplier:{stat}:{multiplier}:{duration}:{modality}:{context}")
        target_key = stat_target_key_from_payload(payload.get("target"), include_location=True)
        if target_key and not target_key.startswith("card"):
            unit = amount.get("unit") or payload.get("stat") or output_ids[0]
            sign = amount_sign(amount.get("value"))
            keys.append(f"secondary:stat_family:{output_ids[0]}:{unit}:{sign}:{context}")
            keys.append(f"secondary:stat:{output_ids[0]}:{unit}:{sign}:{target_key}:{duration}:{modality}:{context}")
            no_location_target_key = stat_target_key_from_payload(payload.get("target"), include_location=False)
            if no_location_target_key and no_location_target_key != target_key:
                keys.append(f"secondary:stat_no_location:{output_ids[0]}:{unit}:{sign}:{no_location_target_key}:{duration}:{modality}:{context}")

    if (
        "self_stat_modifier"
        in enabled_families
        and fact.get("predicate") == "modify_stat"
        and output_ids
        and fact.get("semantic_role") == "state_or_modifier"
    ):
        target = payload.get("target")
        raw_target = str(target.get("raw") or "").casefold().strip() if isinstance(target, dict) else ""
        self_target = isinstance(target, dict) and target.get("scope") == "self" and raw_target in {"", "me"}
        value_key = compact_value_key(amount.get("value")) or amount_bucket(amount.get("value"))
        unit = amount.get("unit") or payload.get("stat") or output_ids[0]
        sign = amount_sign(amount.get("value"))
        if self_target and duration and duration != "while" and value_key and sign and context == "active":
            keys.append(f"secondary:stat_self:{output_ids[0]}:{unit}:{sign}:{value_key}:{duration}:{context}")
        if self_target and sign == "variable" and isinstance(payload.get("scaling"), dict) and context == "active":
            keys.append(f"secondary:stat_self_scaling:{output_ids[0]}:{unit}:{sign}:{context}")
        if self_target and isinstance(payload.get("scaling"), dict) and context == "active":
            keys.append(f"secondary:stat_self_scaling:{output_ids[0]}:{unit}:scaling:{context}")

    if (
        "combat_might_modifier"
        in enabled_families
        and fact.get("predicate") == "modify_stat"
        and "might_modified" in output_ids
        and fact.get("semantic_role") == "state_or_modifier"
        and duration == "while"
        and context == "active"
    ):
        target = payload.get("target")
        self_target = isinstance(target, dict) and target.get("scope") == "self"
        value_key = compact_value_key(amount.get("value"))
        unit = amount.get("unit") or "might"
        sign = amount_sign(amount.get("value"))
        if self_target and value_key and sign:
            for state in condition_states_from_payload(payload):
                if state in {"while_attacker", "while_defender"}:
                    keys.append(f"secondary:combat_might_modifier:might_modified:{unit}:{sign}:{value_key}:self:{state}:{context}")

    if (
        "attached_stat_modifier"
        in enabled_families
        and fact.get("predicate") == "modify_stat"
        and output_ids
        and fact.get("semantic_role") == "state_or_modifier"
        and context != "active"
    ):
        target = payload.get("target")
        raw_target = str(target.get("raw") or "").casefold().strip() if isinstance(target, dict) else ""
        attached_self_target = isinstance(target, dict) and target.get("scope") == "self" and raw_target in {"", "me"}
        unit = amount.get("unit") or payload.get("stat") or output_ids[0]
        sign = amount_sign(amount.get("value"))
        value_key = compact_value_key(amount.get("value")) or amount_bucket(amount.get("value"))
        if attached_self_target and sign:
            condition_states = condition_states_from_payload(payload)
            if condition_states:
                for state in condition_states:
                    keys.append(f"secondary:stat_attached:{output_ids[0]}:{unit}:{sign}:{state}:{context}")
                    if value_key:
                        keys.append(f"secondary:stat_attached_exact:{output_ids[0]}:{unit}:{sign}:{value_key}:{state}:{context}")
            else:
                keys.append(f"secondary:stat_attached:{output_ids[0]}:{unit}:{sign}:{context}")
                if value_key:
                    keys.append(f"secondary:stat_attached_exact:{output_ids[0]}:{unit}:{sign}:{value_key}:{context}")

    if (
        "damage_modifier"
        in enabled_families
        and fact.get("predicate") == "modify_stat"
        and DAMAGE_MODIFIER_OUTPUT_IDS & output_ids_set
    ):
        unit = amount.get("unit") or payload.get("stat") or "damage"
        modifier_value = amount.get("value")
        if modifier_value is None and payload.get("multiplier") is not None:
            modifier_value = payload.get("multiplier")
        sign = amount_sign(modifier_value)
        value_key = compact_value_key(amount.get("value"))
        if not value_key and payload.get("multiplier") is not None:
            value_key = f"x{compact_value_key(payload.get('multiplier'))}"
        value_key = value_key or amount_bucket(amount.get("value")) or "variable"
        duration_key = compact_value_key(duration) or "ongoing"
        modality_key = compact_value_key(modality) or "required"
        target_key = damage_modifier_target_key_from_payload(payload.get("target"), include_location=False)
        if target_key:
            keys.append(
                f"secondary:damage_modifier:{','.join(output_ids)}:{unit}:{sign}:{value_key}:{target_key}:{duration_key}:{modality_key}:{context}"
            )

    if (
        "damage_target"
        in enabled_families
        and fact.get("predicate") == "damage"
        and ("damage_dealt" in output_ids or "damage_dealt" in event_ids)
    ):
        target_key = coarse_target_key_from_payload(payload.get("target"), include_location=True)
        if target_key:
            sign = amount_sign(amount.get("value"))
            keys.append(f"secondary:damage:{sign}:{target_key}:{duration}:{modality}:{context}")

    if (
        "damage_amount"
        in enabled_families
        and fact.get("predicate") == "damage"
        and ("damage_dealt" in output_ids or "damage_dealt" in event_ids)
    ):
        value_key = compact_value_key(amount.get("value"))
        unit = amount.get("unit") or "damage"
        if value_key:
            keys.append(f"secondary:damage_amount:{value_key}:{unit}:{duration}:{modality}:{context}")

    if (
        "damage_scaling"
        in enabled_families
        and fact.get("predicate") == "damage"
        and ("damage_dealt" in output_ids or "damage_dealt" in event_ids)
    ):
        basis = damage_scaling_basis(amount.get("value"))
        if basis:
            target_key = coarse_target_key_from_payload(payload.get("target"), include_location=True)
            no_location_target_key = coarse_target_key_from_payload(payload.get("target"), include_location=False)
            raw_target = ""
            if isinstance(payload.get("target"), dict):
                raw_target = compact_value_key(payload["target"].get("raw"))
            target_key = target_key or raw_target
            if target_key:
                keys.append(f"secondary:damage_scaling:{basis}:{target_key}:{context}")
            if no_location_target_key and no_location_target_key != target_key:
                keys.append(f"secondary:damage_scaling:{basis}:{no_location_target_key}:{context}")

    if (
        "damage_threshold"
        in enabled_families
        and fact.get("predicate") == "damage"
        and ("damage_dealt" in output_ids or "damage_dealt" in event_ids)
    ):
        threshold = compact_value_key(payload.get("threshold"))
        target_key = coarse_target_key_from_payload(payload.get("target"), include_location=False)
        if threshold:
            keys.append(f"secondary:damage_threshold:{threshold}:{target_key}:{context}")

    if (
        "card_draw"
        in enabled_families
        and fact.get("predicate") == "draw"
        and "card_drawn" in output_ids
        and not payload.get("scaling")
    ):
        value = amount.get("value")
        if isinstance(value, int) and value >= 2:
            keys.append(f"secondary:draw_cards:multi:{duration}:{modality}:{context}")

    if (
        "cost_reduction"
        in enabled_families
        and fact.get("predicate") == "reduce_cost"
        and {"play_cost_reduced", "gear_cost_reduced"} & set(output_ids)
    ):
        unit = amount.get("unit") or "energy"
        bucket = amount_bucket(amount.get("value"))
        if unit and bucket in {"large", "variable"}:
            output_key = ",".join(output_ids)
            target_key = coarse_target_key_from_payload(payload.get("target"), include_location=False)
            target_family = target_key.split("[", 1)[0] if target_key else ""
            keys.append(f"secondary:cost_reduction:{output_key}:{unit}:{bucket}:{context}")
            if target_family:
                keys.append(f"secondary:cost_reduction:{output_key}:{unit}:{bucket}:{target_family}:{context}")
        value_key = compact_value_key(amount.get("value"))
        if unit == "energy" and value_key in {"1", "2"}:
            output_key = ",".join(output_ids)
            for target_family in cost_reduction_target_families(payload):
                keys.append(f"secondary:cost_reduction_exact:{output_key}:{unit}:{value_key}:{target_family}:{context}")

    if (
        "play_from_zone"
        in enabled_families
        and fact.get("predicate") == "play"
        and fact.get("semantic_role") == "event_produced"
        and (output_ids or event_ids)
    ):
        target = payload.get("target")
        if isinstance(target, dict) and target.get("zone"):
            output_key = ",".join(output_ids or event_ids)
            kind = target.get("kind")
            if not kind and output_key.endswith("_played"):
                kind = output_key.removesuffix("_played")
            kind_key = compact_value_key(kind or "card")
            zone_key = compact_value_key(target.get("zone"))
            if kind_key and zone_key:
                base_key = f"secondary:play_from_zone:{output_key}:{kind_key}:from={zone_key}:{context}"
                keys.append(base_key)
                cost_modifiers = sorted(
                    compact_value_key(modifier.get("cost"))
                    for modifier in payload.get("modifiers", []) or []
                    if isinstance(modifier, dict) and modifier.get("cost")
                )
                if cost_modifiers:
                    keys.append(f"{base_key}:cost={','.join(cost_modifiers)}")

    if (
        "removal_target"
        in enabled_families
        and fact.get("predicate") == "kill"
        and event_ids
    ):
        target_key = coarse_target_key_from_payload(payload.get("target"), include_location=False)
        event_key = ",".join(event_ids)
        if target_key:
            target_family = target_key.split("[", 1)[0]
            keys.append(f"secondary:removal:{event_key}:{target_family}:{modality}:{context}")
            keys.append(f"secondary:removal:{event_key}:{target_key}:{modality}:{context}")

    if (
        {"movement_target_destination", "movement_to_zone"} & enabled_families
        and fact.get("predicate") in {"move", "return_to_hand"}
        and (
            {"unit_moved", "card_moved"} & set(event_ids)
            or {"unit_moved", "unit_recalled", "card_returned_to_hand", "deck_card_put_top_or_bottom", "battlefield_replaced"} & set(output_ids)
        )
    ):
        target_key = coarse_target_key_from_payload(payload.get("target"), include_location=False) or object_key_from_payload(payload.get("object"))
        destination_payload = payload.get("destination") or payload.get("target")
        destination_key = coarse_destination_key_from_payload(destination_payload) or target_key_from_payload(destination_payload)
        if "movement_target_destination" in enabled_families and (target_key or destination_key):
            keys.append(f"secondary:move:{target_key}:{destination_key}:{modality}:{context}")
        if "movement_target_destination" in enabled_families and output_ids and destination_key:
            keys.append(f"secondary:move_output:{','.join(output_ids)}:{destination_key}:{context}")
            keys.append(f"secondary:move_output:{','.join(output_ids)}:{destination_key}:{modality}:{context}")
        if "movement_to_zone" in enabled_families and destination_key:
            target_family = (target_key.split("[", 1)[0] if target_key else "") or "card"
            keys.append(f"secondary:move_to_zone:{target_family}:{destination_key}:{modality}:{context}")

    if (
        "movement_permission"
        in enabled_families
        and fact.get("semantic_role") == "restriction_or_permission"
        and fact.get("predicate") == "move"
    ):
        target_key = coarse_target_key_from_payload(payload.get("target"), include_location=False)
        source_key = source_key_from_payload(payload.get("source"))
        destination_key = coarse_destination_key_from_payload(payload.get("destination"))
        if target_key or source_key or destination_key:
            keys.append(f"secondary:move_permission:{target_key}:{source_key}>{destination_key}:{modality}:{context}")

    if (
        "movement_permission"
        in enabled_families
        and fact.get("semantic_role") == "restriction_or_permission"
        and fact.get("predicate") == "prevent"
        and payload.get("prevented_action") == "move"
    ):
        target_key = coarse_target_key_from_payload(payload.get("target"), include_location=False)
        source_key = source_key_from_payload(payload.get("source"))
        destination_key = coarse_destination_key_from_payload(payload.get("destination"))
        if target_key or source_key or destination_key:
            keys.append(f"secondary:move_prevention:{target_key}:{source_key}>{destination_key}:{modality}:{context}")

    if (
        "play_restriction"
        in enabled_families
        and fact.get("semantic_role") == "restriction_or_permission"
        and (fact.get("predicate") == "play" or payload.get("prevented_action") == "play")
    ):
        target_key = coarse_target_key_from_payload(payload.get("target"), include_location=False)
        destination_key = coarse_destination_key_from_payload(payload.get("destination"))
        mode = payload.get("restriction") or payload.get("prevented_action") or fact.get("predicate")
        if target_key:
            target_family = target_key.split("[", 1)[0]
            if target_family and target_family != target_key:
                keys.append(f"secondary:play_restriction:{target_family}:{context}")
            keys.append(f"secondary:play_restriction:{target_key}:{context}")
            keys.append(f"secondary:play_restriction:{target_key}:{destination_key}:{mode}:{context}")

    if (
        "keyword_grant"
        in enabled_families
        and fact.get("predicate") == "gain_keyword"
        and "keyword_granted" in output_ids
    ):
        keywords = payload.get("keywords") or []
        keyword_values: list[str] = []
        if isinstance(keywords, list) and keywords:
            for keyword in keywords:
                keyword_value = compact_value_key(keyword)
                if keyword_value:
                    keyword_values.append(keyword_value)
            keyword_values = sorted(set(keyword_values))
        if isinstance(keywords, list) and keyword_values:
            target_families = state_target_families_from_payload(payload.get("target"), include_location=False)
            duration_key = compact_value_key(duration) or "ongoing"
            modality_key = compact_value_key(modality) or "required"
            for keyword in keyword_values:
                if target_families:
                    for target_family in target_families:
                        keys.append(f"secondary:keyword_grant:{keyword}:{target_family}:{duration_key}:{modality_key}:{context}")
                else:
                    keys.append(f"secondary:keyword_grant:{keyword}:{duration_key}:{modality_key}:{context}")

    if (
        {"keyword_grant_by_keyword", "temporary_grant"} & enabled_families
        and fact.get("predicate") == "gain_keyword"
        and "keyword_granted" in output_ids
    ):
        keywords = payload.get("keywords") or []
        keyword_values = sorted({compact_value_key(keyword) for keyword in keywords if compact_value_key(keyword)})
        target_families = state_target_families_from_payload(payload.get("target"), include_location=False)
        duration_key = duration_bucket(duration)
        modality_key = compact_value_key(modality) or "required"
        if "keyword_grant_by_keyword" in enabled_families:
            for keyword in keyword_values:
                for target_family in target_families or [""]:
                    keys.append(f"secondary:keyword_grant_by_keyword:{keyword}:{target_family}:{duration_key}:{modality_key}:{context}")
        if "temporary_grant" in enabled_families and "temporary" in keyword_values:
            for target_family in target_families or [""]:
                keys.append(f"secondary:temporary_grant:{target_family}:{duration_key}:{modality_key}:{context}")

    if (
        "require_state"
        in enabled_families
        and fact.get("predicate") == "require"
        and fact.get("semantic_role") == "restriction_or_permission"
    ):
        conditions = payload.get("conditions") or []
        for condition in conditions:
            if not isinstance(condition, dict) or not condition.get("state"):
                continue
            keys.append(f"secondary:require_state:{condition['state']}:{duration}:{context}")

    if (
        "state_action"
        in enabled_families
        and fact.get("semantic_role") == "state_or_modifier"
        and fact.get("predicate") in {"ready", "enter_ready", "enter_exhausted"}
        and (output_ids or fact.get("fact_type") == "entry_state")
    ):
        target_key = state_target_key_from_payload(payload.get("target"), include_location=False)
        target_key_with_location = state_target_key_from_payload(payload.get("target"), include_location=True)
        action = fact.get("predicate") or ""
        output_key = ",".join(output_ids) or action
        if target_key and target_key != "card":
            target_family = target_key.split("[", 1)[0]
            keys.append(f"secondary:state_action:{action}:{output_key}:{target_family}:{context}")
            keys.append(f"secondary:state_action:{action}:{output_key}:{target_key}:{duration}:{modality}:{context}")
            if target_key_with_location and target_key_with_location != target_key:
                keys.append(f"secondary:state_action:{action}:{output_key}:{target_key_with_location}:{duration}:{modality}:{context}")

    if (
        "control_change"
        in enabled_families
        and fact.get("fact_type") == "control_change"
        and fact.get("predicate") in {"gain_control", "lose_control"}
        and "control_changed" in event_ids
    ):
        target_key = coarse_target_key_from_payload(payload.get("target"), include_location=False)
        target_key_with_location = coarse_target_key_from_payload(payload.get("target"), include_location=True)
        action = str(fact.get("predicate") or "")
        polarity = payload.get("polarity") or action.removesuffix("_control")
        keys.append(f"secondary:control_change:{action}:{polarity}:{context}")
        if target_key:
            target_family = target_key.split("[", 1)[0]
            keys.append(f"secondary:control_change:{action}:{polarity}:{target_family}:{context}")
            keys.append(f"secondary:control_change:{action}:{polarity}:{target_key}:{duration}:{modality}:{context}")
        if target_key_with_location and target_key_with_location != target_key:
            keys.append(f"secondary:control_change:{action}:{polarity}:{target_key_with_location}:{duration}:{modality}:{context}")

    if (
        "prevention"
        in enabled_families
        and fact.get("predicate") == "prevent"
        and fact.get("semantic_role") == "restriction_or_permission"
        and payload.get("polarity") != "replacement"
        and not payload.get("replacement")
    ):
        prevented = payload.get("prevented_event") or payload.get("prevented_action") or ""
        if prevented:
            target_key = coarse_target_key_from_payload(payload.get("target"), include_location=False)
            limit = payload.get("limit") or ""
            keys.append(f"secondary:prevent:{prevented}:{context}")
            keys.append(f"secondary:prevent:{prevented}:{duration}:{limit}:{context}")
            if target_key:
                keys.append(f"secondary:prevent:{prevented}:{target_key}:{duration}:{limit}:{context}")

    if "replacement" in enabled_families and fact.get("fact_type") == "replacement_effect":
        replacement = compact_value_key(payload.get("replacement"))
        replaced = compact_value_key(payload.get("prevented_event") or payload.get("prevented_action") or payload.get("replaced_event"))
        if replacement and replaced:
            limit = compact_value_key(payload.get("limit"))
            keys.append(f"secondary:replacement:{replaced}:{replacement}:{context}")
            keys.append(f"secondary:replacement:{replaced}:{replacement}:{duration}:{limit}:{context}")
            for target_family in state_target_families_from_payload(payload.get("target"), include_location=False):
                keys.append(f"secondary:replacement:{replaced}:{replacement}:{target_family}:{context}")
                keys.append(f"secondary:replacement:{replaced}:{replacement}:{target_family}:{duration}:{limit}:{context}")

    if (
        "attachment_action"
        in enabled_families
        and fact.get("predicate") in {"attach", "detach"}
        and ({"equipment_attached", "equipment_detached"} & set(output_ids + event_ids))
    ):
        object_key = object_key_from_payload(payload.get("object")) or "gear"
        target_key = coarse_target_key_from_payload(payload.get("target"), include_location=False)
        keys.append(f"secondary:attachment:{fact.get('predicate')}:{object_key}:{context}")
        if target_key:
            keys.append(f"secondary:attachment:{fact.get('predicate')}:{object_key}:{target_key}:{context}")

    if (
        "copy_effect"
        in enabled_families
        and fact.get("predicate") == "copy"
        and ("card_copied" in output_ids or "token_copied" in output_ids)
    ):
        target_key = coarse_target_key_from_payload(payload.get("target"), include_location=False)
        keys.append(f"secondary:copy:{','.join(output_ids)}:{context}")
        keys.append(f"secondary:copy:{','.join(output_ids)}:{target_key}:{context}")

    if (
        "score_amount"
        in enabled_families
        and fact.get("predicate") == "score"
        and fact.get("fact_type") == "score_change"
    ):
        if amount.get("unit") == "point" and amount.get("value") is not None:
            keys.append(f"secondary:score_amount:{amount['value']}:{amount['unit']}:{context}")

    if (
        "swap_stat"
        in enabled_families
        and fact.get("predicate") == "modify_stat"
        and fact.get("fact_type") == "stat_change"
        and payload.get("operation") == "swap"
    ):
        stat_unit = amount.get("unit") or "stat"
        target_key = coarse_target_key_from_payload(payload.get("target"), include_location=False)
        target_key_with_location = coarse_target_key_from_payload(payload.get("target"), include_location=True)
        if target_key:
            target_family = target_key.split("[", 1)[0]
            keys.append(f"secondary:swap_stat:{stat_unit}:{target_family}:{duration}:{context}")
            keys.append(f"secondary:swap_stat:{stat_unit}:{target_key}:{duration}:{modality}:{context}")
        if target_key_with_location and target_key_with_location != target_key:
            keys.append(f"secondary:swap_stat:{stat_unit}:{target_key_with_location}:{duration}:{modality}:{context}")

    return sorted(set(keys))


def similar_key(fact: dict[str, Any], relation_rules: dict[str, Any]) -> str | None:
    config = relation_rules.get("similarity", {})
    if fact.get("semantic_role") not in set(config.get("roles", [])):
        return None
    if (
        fact.get("semantic_role") == "restriction_or_permission"
        and fact.get("predicate") not in set(config.get("restriction_predicate_allowlist", []))
    ):
        return None
    if fact.get("fact_type") in set(config.get("ignored_fact_types", [])):
        return None
    event_ids = event_ids_from_fact(fact)
    output_ids = output_ids_from_fact(fact)
    payload = fact.get("payload", {})
    amounts = payload.get("amounts") or []
    amount_key = ""
    if amounts and isinstance(amounts[0], dict):
        amount_key = f":{amounts[0].get('value')}:{amounts[0].get('unit')}"
    duration = payload.get("duration") or ""
    modality = payload.get("modality") or ""
    target_key = target_key_from_payload(payload.get("target") or {})
    destination_key = destination_key_from_payload(payload.get("destination") or {})
    source_key = source_key_from_payload(payload.get("source"))
    object_key = object_key_from_payload(payload.get("object"))
    location = payload.get("location") or ""
    extra_key = destination_key or location
    semantic_facets = []
    if source_key:
        semantic_facets.append(f"source={source_key}")
    if object_key:
        semantic_facets.append(f"object={object_key}")
    target = payload.get("target")
    if DAMAGE_MODIFIER_OUTPUT_IDS & set(output_ids) and isinstance(target, dict):
        target_source = compact_value_key(target.get("source"))
        if target_source:
            semantic_facets.append(f"target_source={target_source}")
    keywords = payload.get("keywords") or []
    if isinstance(keywords, list) and keywords:
        semantic_facets.append("keywords=" + ",".join(sorted(str(keyword) for keyword in keywords)))
    if payload.get("activation_context"):
        semantic_facets.append(f"activation_context={payload['activation_context']}")
    if payload.get("inactive_until_attached"):
        semantic_facets.append("inactive_until_attached=true")
    if payload.get("applies_to"):
        semantic_facets.append(f"applies_to={payload['applies_to']}")
    scaling = payload.get("scaling") or {}
    if isinstance(scaling, dict) and scaling.get("per"):
        semantic_facets.append(f"per={scaling['per']}")
    condition_states = condition_states_from_payload(payload)
    if condition_states and (
        fact.get("semantic_role") != "restriction_or_permission"
        or fact.get("predicate") != "require"
        or payload.get("activation_context")
    ):
        semantic_facets.append("conditions=" + ",".join(condition_states))
    prevented_action = payload.get("prevented_action")
    if prevented_action:
        semantic_facets.append(f"prevented={prevented_action}")
    prevented_event = payload.get("prevented_event")
    if prevented_event:
        semantic_facets.append(f"prevented_event={prevented_event}")
    if payload.get("limit"):
        semantic_facets.append(f"limit={payload['limit']}")
    if payload.get("replacement"):
        semantic_facets.append(f"replacement={payload['replacement']}")
    if payload.get("polarity"):
        semantic_facets.append(f"polarity={payload['polarity']}")
    cost_constraints = payload.get("cost_constraints") or []
    if isinstance(cost_constraints, list) and cost_constraints:
        constraint_keys = []
        for item in cost_constraints:
            if not isinstance(item, dict):
                continue
            if item.get("minimum") is not None:
                constraint_keys.append(f"{item.get('resource') or 'cost'}>={compact_value_key(item.get('minimum'))}")
            elif item.get("maximum") is not None:
                maximum = item.get("maximum")
                cost_text = payload.get("cost_text") or item.get("raw")
                maximum_key = compact_value_key(cost_text) if maximum is True and cost_text else compact_value_key(maximum)
                constraint_keys.append(f"{item.get('resource') or 'cost'}<={maximum_key}")
        if constraint_keys:
            semantic_facets.append("costs=" + ",".join(sorted(constraint_keys)))
    semantic_key = f":{';'.join(semantic_facets)}" if semantic_facets else ""
    if output_ids:
        return f"output:{fact.get('semantic_role')}:{fact.get('fact_type')}:{fact.get('predicate')}:{','.join(output_ids)}{amount_key}:{target_key}:{extra_key}:{duration}:{modality}{semantic_key}"
    if event_ids:
        return f"event:{fact.get('semantic_role')}:{fact.get('fact_type')}:{fact.get('predicate')}:{','.join(event_ids)}{amount_key}:{target_key}:{extra_key}:{duration}:{modality}{semantic_key}"
    return f"predicate:{fact.get('semantic_role')}:{fact.get('fact_type')}:{fact.get('predicate')}{amount_key}:{target_key}:{extra_key}:{duration}:{modality}{semantic_key}"


def trigger_context_by_clause(facts: list[dict[str, Any]]) -> dict[str, list[str]]:
    context: dict[str, set[str]] = defaultdict(set)
    for fact in facts:
        if fact.get("semantic_role") != "trigger_observed":
            continue
        clause_group_id = fact.get("clause_group_id")
        if not clause_group_id:
            continue
        context[str(clause_group_id)].update(event_ids_from_fact(fact))
    return {key: sorted(value) for key, value in context.items() if value}


def trigger_fact_ids_by_clause(facts: list[dict[str, Any]]) -> dict[str, list[str]]:
    context: dict[str, set[str]] = defaultdict(set)
    for fact in facts:
        if fact.get("semantic_role") != "trigger_observed":
            continue
        clause_group_id = fact.get("clause_group_id")
        if not clause_group_id:
            continue
        context[str(clause_group_id)].add(fact["fact_id"])
    return {key: sorted(value) for key, value in context.items() if value}


def cost_context_by_clause(facts: list[dict[str, Any]]) -> tuple[dict[str, str], dict[str, list[str]]]:
    facets_by_clause: dict[str, set[str]] = defaultdict(set)
    fact_ids_by_clause: dict[str, set[str]] = defaultdict(set)
    for fact in facts:
        clause_group_id = fact.get("clause_group_id")
        if not clause_group_id:
            continue
        facets = cost_context_facets_from_fact(fact)
        if not facets:
            continue
        clause_key = str(clause_group_id)
        facets_by_clause[clause_key].update(facets)
        fact_ids_by_clause[clause_key].add(fact["fact_id"])
    context_by_clause = {
        key: ",".join(sorted(facets))
        for key, facets in facets_by_clause.items()
        if facets
    }
    return context_by_clause, {key: sorted(value) for key, value in fact_ids_by_clause.items() if value}


def requirement_context_by_clause(facts: list[dict[str, Any]]) -> tuple[dict[str, str], dict[str, list[str]]]:
    facets_by_clause: dict[str, set[str]] = defaultdict(set)
    fact_ids_by_clause: dict[str, set[str]] = defaultdict(set)
    for fact in facts:
        clause_group_id = fact.get("clause_group_id")
        if not clause_group_id:
            continue
        facets = requirement_context_facets_from_fact(fact)
        if not facets:
            continue
        clause_key = str(clause_group_id)
        facets_by_clause[clause_key].update(facets)
        fact_ids_by_clause[clause_key].add(fact["fact_id"])
    context_by_clause = {
        key: ",".join(sorted(facets))
        for key, facets in facets_by_clause.items()
        if facets
    }
    return context_by_clause, {key: sorted(value) for key, value in fact_ids_by_clause.items() if value}


def build_similar_effect_relations(
    facts: list[dict[str, Any]],
    relation_rules: dict[str, Any],
    quality_policy: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    config = relation_rules.get("similarity", {})
    if not config.get("enabled", True):
        return [], {}
    similarity_policy = quality_policy.get("similarity", {})
    max_similar = int(similarity_policy.get("max_similar_facts_per_key", 35))
    broad_max_similar = int(similarity_policy.get("broad_similar_facts_per_key", 12))
    always_skip_keys = set(similarity_policy.get("always_skip_keys", []) or [])
    broad_markers = tuple(similarity_policy.get("broad_key_markers", []))
    triggers_by_clause = trigger_context_by_clause(facts)
    trigger_fact_ids_by_clause_id = trigger_fact_ids_by_clause(facts)
    costs_by_clause, cost_fact_ids_by_clause_id = cost_context_by_clause(facts)
    requirements_by_clause, requirement_fact_ids_by_clause_id = requirement_context_by_clause(facts)

    def max_for_key(key: str) -> int:
        return broad_max_similar if any(marker in key for marker in broad_markers) else max_similar

    def context_options_for_fact(fact: dict[str, Any], key: str) -> list[tuple[str, tuple[str, ...]]]:
        if fact.get("semantic_role") in {"trigger_observed", "cost_or_requirement"}:
            return []
        if (
            fact.get("semantic_role") == "restriction_or_permission"
            and fact.get("predicate") == "require"
        ):
            return []
        clause_key = str(fact.get("clause_group_id") or "")
        options: list[tuple[str, tuple[str, ...]]] = []
        trigger_ids = triggers_by_clause.get(clause_key)
        if trigger_ids:
            trigger_fact_ids = tuple(trigger_fact_ids_by_clause_id.get(clause_key, []))
            options.append((f"{key}:when={','.join(trigger_ids)}", trigger_fact_ids))
        requirement_context = requirements_by_clause.get(clause_key)
        if requirement_context and not condition_states_from_payload(fact.get("payload", {}) or {}):
            requirement_fact_ids = tuple(requirement_fact_ids_by_clause_id.get(clause_key, []))
            options.append((f"{key}:require={requirement_context}", requirement_fact_ids))
        elif fact.get("fact_type") == "keyword_grant":
            intrinsic_requirement_context = intrinsic_keyword_requirement_context_for_key(key)
            if intrinsic_requirement_context:
                options.append((f"{key}:require={intrinsic_requirement_context}", ()))
        cost_context = costs_by_clause.get(clause_key)
        if cost_context:
            cost_fact_ids = tuple(cost_fact_ids_by_clause_id.get(clause_key, []))
            options.append((f"{key}:cost={cost_context}", cost_fact_ids))
        return options

    facts_by_key: dict[str, list[tuple[dict[str, Any], tuple[str, ...]]]] = defaultdict(list)
    skipped_by_key = {}
    candidate_rows: list[tuple[dict[str, Any], str, list[tuple[str, tuple[str, ...]]]]] = []
    base_rows: list[tuple[dict[str, Any], str, list[tuple[str, tuple[str, ...]]]]] = []
    base_distinct_cards_by_key: dict[str, set[str]] = defaultdict(set)
    secondary_needed_fact_ids_by_key: dict[str, set[str]] = defaultdict(set)
    distinct_cards_by_context_key: dict[str, set[str]] = defaultdict(set)
    for fact in facts:
        base_key = similar_key(fact, relation_rules)
        if not base_key:
            continue
        base_distinct_cards_by_key[base_key].add(fact["play_id"])
        context_options = context_options_for_fact(fact, base_key)
        for context_key, _supporting_fact_ids in context_options:
            distinct_cards_by_context_key[context_key].add(fact["play_id"])
        base_rows.append((fact, base_key, context_options))

    for fact, base_key, context_options in base_rows:
        candidate_rows.append((fact, base_key, context_options))
        for secondary_key in secondary_similar_keys(fact, relation_rules):
            secondary_context_options = context_options_for_fact(fact, secondary_key)
            for secondary_context_key, _supporting_fact_ids in secondary_context_options:
                distinct_cards_by_context_key[secondary_context_key].add(fact["play_id"])
            base_distinct_count = len(base_distinct_cards_by_key.get(base_key, set()))
            if base_distinct_count < 2 or base_distinct_count > max_for_key(base_key):
                secondary_needed_fact_ids_by_key[secondary_key].add(fact["fact_id"])
                for secondary_context_key, _supporting_fact_ids in secondary_context_options:
                    secondary_needed_fact_ids_by_key[secondary_context_key].add(fact["fact_id"])
            candidate_rows.append((fact, secondary_key, secondary_context_options))

    for fact, key, context_options in candidate_rows:
        selected_context = next(
            (
                (context_key, supporting_fact_ids)
                for context_key, supporting_fact_ids in context_options
                if len(distinct_cards_by_context_key.get(context_key, set())) >= 2
            ),
            None,
        )
        if selected_context:
            context_key, supporting_fact_ids = selected_context
            facts_by_key[context_key].append((fact, supporting_fact_ids))
        else:
            facts_by_key[key].append((fact, ()))

    relations = []
    for key, key_fact_rows in sorted(facts_by_key.items()):
        unique_key_fact_rows = []
        seen_fact_ids = set()
        for fact, supporting_fact_ids in key_fact_rows:
            if fact["fact_id"] in seen_fact_ids:
                continue
            seen_fact_ids.add(fact["fact_id"])
            unique_key_fact_rows.append((fact, supporting_fact_ids))
        key_fact_rows = unique_key_fact_rows
        if key.startswith("secondary:") and key not in secondary_needed_fact_ids_by_key:
            continue
        distinct_cards = {fact["play_id"] for fact, _supporting_fact_ids in key_fact_rows}
        if len(distinct_cards) < 2:
            continue
        if key in always_skip_keys:
            skipped_by_key[key] = len(distinct_cards)
            continue
        key_limit = max_for_key(key)
        if len(distinct_cards) >= key_limit:
            skipped_by_key[key] = len(distinct_cards)
            continue
        emitted = 0
        for (left, left_supporting_fact_ids), (right, right_supporting_fact_ids) in combinations(key_fact_rows, 2):
            if left["play_id"] == right["play_id"]:
                continue
            if key.startswith("secondary:") and not (
                left["fact_id"] in secondary_needed_fact_ids_by_key[key]
                or right["fact_id"] in secondary_needed_fact_ids_by_key[key]
            ):
                continue
            extra_match = {"rule_id": "similarity"}
            supporting_fact_ids = sorted(set(left_supporting_fact_ids + right_supporting_fact_ids))
            if supporting_fact_ids:
                extra_match["supporting_fact_ids"] = supporting_fact_ids
            relations.append(
                relation(
                    "similar_effect",
                    left,
                    right,
                    reason=key,
                    strength=float(config.get("strength", 0.72)),
                    event_id=",".join(event_ids_from_fact(left)) or None,
                    output_id=",".join(output_ids_from_fact(left)) or None,
                    extra_match=extra_match,
                )
            )
            relations.append(
                relation(
                    "similar_effect",
                    right,
                    left,
                    reason=key,
                    strength=float(config.get("strength", 0.72)),
                    event_id=",".join(event_ids_from_fact(right)) or None,
                    output_id=",".join(output_ids_from_fact(right)) or None,
                    extra_match=extra_match,
                )
            )
            emitted += 2
    return relations, skipped_by_key


def normalized_reason(reason: str) -> str:
    return re.sub(r"\s+", " ", reason.strip().casefold())


def collapsed_supporting_fact_ids(primary: dict[str, Any], collapsed: dict[str, Any]) -> list[str]:
    primary_fact_ids = {primary.get("source_fact_id"), primary.get("target_fact_id")}
    supporting_fact_ids = set(primary.get("match", {}).get("supporting_fact_ids", []) or [])
    supporting_fact_ids.update(collapsed.get("match", {}).get("supporting_fact_ids", []) or [])
    for fact_id in (collapsed.get("source_fact_id"), collapsed.get("target_fact_id")):
        if fact_id and fact_id not in primary_fact_ids:
            supporting_fact_ids.add(str(fact_id))
    return sorted(supporting_fact_ids)


def dedupe_relations(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, int]]:
    deduped: dict[tuple[str, str, str, str], dict[str, Any]] = {}
    duplicate_candidates = 0
    collapsed_relations = 0
    for row in rows:
        key = (
            row["source_play_id"],
            row["target_play_id"],
            row["relation_type"],
            normalized_reason(str(row.get("match", {}).get("reason") or "")),
        )
        existing = deduped.get(key)
        if existing is None:
            deduped[key] = row
            continue
        duplicate_candidates += 1
        collapsed_relations += 1
        if row.get("strength", 0) > existing.get("strength", 0):
            supporting_fact_ids = collapsed_supporting_fact_ids(row, existing)
            if supporting_fact_ids:
                row["match"]["supporting_fact_ids"] = supporting_fact_ids
            row["match"]["collapsed_relation_count"] = existing.get("match", {}).get("collapsed_relation_count", 1) + 1
            row["match"]["collapsed_relation_ids"] = sorted(
                set(existing.get("match", {}).get("collapsed_relation_ids", []) + [existing["relation_id"], row["relation_id"]])
            )
            deduped[key] = row
        else:
            supporting_fact_ids = collapsed_supporting_fact_ids(existing, row)
            if supporting_fact_ids:
                existing["match"]["supporting_fact_ids"] = supporting_fact_ids
            existing["match"]["collapsed_relation_count"] = existing.get("match", {}).get("collapsed_relation_count", 1) + 1
            existing["match"]["collapsed_relation_ids"] = sorted(
                set(existing.get("match", {}).get("collapsed_relation_ids", []) + [existing["relation_id"], row["relation_id"]])
            )
    return sorted(
        deduped.values(),
        key=lambda row: (
            row["relation_type"],
            row["source_card_name"] or "",
            row["target_card_name"] or "",
            row["relation_id"],
        ),
    ), {"duplicate_relation_candidates": duplicate_candidates, "collapsed_relations": collapsed_relations}


def build_relations(
    facts: list[dict[str, Any]],
    relation_rules: dict[str, Any],
    quality_policy: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    facts_by_id = {fact["fact_id"]: fact for fact in facts}
    enables = build_enables_relations(facts, relation_rules)
    identity_event = build_identity_event_relations(facts, relation_rules)
    enables_synergy = build_enables_synergy_relations(enables, facts_by_id, relation_rules)
    direct_synergy = build_direct_synergy_relations(facts, relation_rules)
    resource_synergy = build_resource_synergy_relations(facts, relation_rules)
    tag_target_synergy = build_tag_target_synergy_relations(facts, relation_rules)
    similar_effect, skipped_similarity = build_similar_effect_relations(facts, relation_rules, quality_policy)
    relations, dedupe_report = dedupe_relations(
        enables + identity_event + enables_synergy + direct_synergy + resource_synergy + tag_target_synergy + similar_effect
    )

    by_type = Counter(row["relation_type"] for row in relations)
    by_reason = Counter(row["match"]["reason"] for row in relations)
    by_contract_rule = Counter(row["match"].get("rule_id") for row in relations if row.get("match", {}).get("rule_id"))
    outgoing_degree = Counter(row["source_card_name"] for row in relations)
    incoming_degree = Counter(row["target_card_name"] for row in relations)
    cards_with_outgoing = {row["source_play_id"] for row in relations}
    cards_with_incoming = {row["target_play_id"] for row in relations}
    report = {
        "version": SCHEMA_VERSION,
        "inputs": {
            "facts": str(DEFAULT_FACTS),
            "schema": str(DEFAULT_SCHEMA),
            "relation_rules": str(DEFAULT_RELATION_RULES),
            "quality_policy": str(DEFAULT_QUALITY_POLICY),
        },
        "summary": {
            "fact_count": len(facts),
            "relation_count": len(relations),
            "cards_with_outgoing_relations": len(cards_with_outgoing),
            "cards_with_incoming_relations": len(cards_with_incoming),
            **dedupe_report,
        },
        "by_relation_type": dict(by_type.most_common()),
        "top_match_reasons": dict(by_reason.most_common(40)),
        "top_contract_rules": dict(by_contract_rule.most_common(40)),
        "contract_rule_coverage": {
            "relation_count_with_contract_rule": sum(by_contract_rule.values()),
            "relation_count": len(relations),
            "contract_rule_share": round(sum(by_contract_rule.values()) / len(relations), 4) if relations else 0.0,
        },
        "broad_match_reasons": {
            reason: count
            for reason, count in by_reason.items()
            if count >= int(quality_policy.get("broad_relation_count_threshold", 500))
        },
        "top_outgoing_cards": dict(outgoing_degree.most_common(20)),
        "top_incoming_cards": dict(incoming_degree.most_common(20)),
        "skipped_similarity_keys": skipped_similarity,
    }
    return relations, report


def markdown_report(report: dict[str, Any]) -> str:
    lines = [
        "# Cards Card Relations Report",
        "",
        "Report for `data/processed/cards/relations/cards_card_relations.jsonl`.",
        "",
        "## Summary",
        "",
    ]
    for key, value in report["summary"].items():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## By Relation Type", ""])
    for key, value in report["by_relation_type"].items():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Top Match Reasons", ""])
    for key, value in report["top_match_reasons"].items():
        lines.append(f"- {key}: {value}")
    if report.get("top_contract_rules"):
        lines.extend(["", "## Top Contract Rules", ""])
        for key, value in report["top_contract_rules"].items():
            lines.append(f"- {key}: {value}")
    if report["skipped_similarity_keys"]:
        lines.extend(["", "## Skipped Similarity Keys", ""])
        for key, value in report["skipped_similarity_keys"].items():
            lines.append(f"- {key}: {value}")
    if report["broad_match_reasons"]:
        lines.extend(["", "## Broad Match Reasons", ""])
        for key, value in report["broad_match_reasons"].items():
            lines.append(f"- {key}: {value}")
    return "\n".join(lines) + "\n"


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(markdown_report(report), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build deterministic card-to-card relations from semantic facts.")
    parser.add_argument("--facts", type=Path, default=DEFAULT_FACTS)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--relation-rules", type=Path, default=DEFAULT_RELATION_RULES)
    parser.add_argument("--quality-policy", type=Path, default=DEFAULT_QUALITY_POLICY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MARKDOWN)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    facts = read_jsonl(args.facts)
    schema = read_json(args.schema)
    contracts = load_contract_bundle(CONTRACTS_DIR)
    relation_types = set(contracts["ontology"].get("relation_types", schema.get("card_relation_record", {}).get("relation_types", [])))
    missing_types = {"enables", "enabled_by", "similar_effect", "deck_synergy"} - relation_types
    if missing_types:
        raise ValueError(f"semantic_ontology.json is missing relation types: {sorted(missing_types)}")
    relation_rules = contracts["relation_rules"] if args.relation_rules == DEFAULT_RELATION_RULES else read_json(args.relation_rules)
    quality_policy = contracts["quality_policy"] if args.quality_policy == DEFAULT_QUALITY_POLICY else read_json(args.quality_policy)

    relations, report = build_relations(facts, relation_rules, quality_policy)
    write_jsonl(args.output, relations)
    write_json(args.report, report)
    write_markdown(args.markdown, report)
    print(f"Wrote {len(relations)} card relations to {args.output}")
    print(f"Wrote report to {args.report}")


if __name__ == "__main__":
    main()
