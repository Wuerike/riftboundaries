import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from statistics import mean
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DEFAULT_DATASET = PROJECT_ROOT / "data" / "processed" / "web" / "card_explorer_index.json"
DEFAULT_QUALITY_POLICY = (
    PROJECT_ROOT
    / "scripts"
    / "04_cards_feature_extraction"
    / "contracts"
    / "semantic_quality_policy.json"
)
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "processed" / "web" / "card_explorer_quality_report.json"
DEFAULT_MARKDOWN = PROJECT_ROOT / "data" / "processed" / "web" / "card_explorer_quality_report.md"
SNAPSHOT_DATE = date.today().isoformat()

TEXT_SOURCE_FIELDS = ("rules_lines", "effect_lines")
RELATION_TYPES = ("enables", "enabled_by", "similar_effect", "deck_synergy")
RELATION_CANDIDATE_ROLES = {
    "cost_or_requirement",
    "event_produced",
    "payoff_output",
    "restriction_or_permission",
    "state_or_modifier",
    "trigger_observed",
    "targeting_or_scope",
}
RELATION_BUILDER_USES = {"deck_synergy", "enabled_by", "enables"}
DEFAULT_BROAD_REASONS = {
    "spell_card_can_be_countered",
    "output:event_produced:movement:move:unit_moved:from battlefield::required",
    "output:event_produced:card_flow:recycle:card_recycled:card::optional",
}
WEAK_EFFECT_TOKENS = (
    "add",
    "attach",
    "banish",
    "buff",
    "channel",
    "choose",
    "counter",
    "deal",
    "discard",
    "draw",
    "give",
    "kill",
    "move",
    "pay",
    "ready",
    "recall",
    "recycle",
    "return",
    "score",
    "spend",
    "stun",
)
DIAGNOSTIC_ORDER = {
    "missing_fact": 0,
    "weak_fact": 1,
    "missing_relation_rule": 2,
    "broad_only": 3,
    "front_scoring_issue": 4,
    "likely_vanilla_or_low_relational_text": 5,
    "ok": 6,
}
BUCKET_PRIORITY = {
    "stat/buff/damage_modifier": 0,
    "movement/location": 1,
    "cost/resource": 2,
    "card_flow": 3,
    "kill/heal/replacement": 4,
    "damage": 5,
    "deck_manipulation/recycle": 6,
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_dataset(path: Path) -> dict[str, Any]:
    dataset = read_json(path)
    cards = dataset.get("cards", []) or []
    if any((card.get("relations", {}) or {}).get("outgoing") for card in cards):
        return dataset

    shard_cache: dict[str, dict[str, Any]] = {}
    for card in cards:
        relations = card.setdefault("relations", {})
        shard_ref = relations.get("shard")
        if not shard_ref:
            relations["outgoing"] = []
            continue
        if shard_ref not in shard_cache:
            shard_cache[shard_ref] = read_json(path.parent / shard_ref)
        shard_cards = shard_cache[shard_ref].get("cards", {}) or {}
        relations["outgoing"] = (shard_cards.get(card.get("play_id"), {}) or {}).get("outgoing", [])

    facts_by_card: dict[str, list[dict[str, Any]]] = defaultdict(list)
    facts_dir = path.parent / "facts"
    if facts_dir.exists():
        for shard_path in sorted(facts_dir.glob("*.json")):
            shard = read_json(shard_path)
            for fact in (shard.get("facts", {}) or {}).values():
                if fact.get("play_id"):
                    facts_by_card[fact["play_id"]].append(fact)
    for card in cards:
        semantic = card.setdefault("semantic", {})
        if not semantic.get("facts"):
            semantic["facts"] = facts_by_card.get(card.get("play_id"), [])
    return dataset


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


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


def normalized_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").casefold()).strip()


def fact_play_id(fact: dict[str, Any]) -> str:
    return str(fact.get("play_id") or fact.get("_audit_play_id") or "")


def duplicate_relation_coverage_key(fact: dict[str, Any]) -> tuple[Any, ...] | None:
    predicate = fact.get("predicate")
    if predicate in {"pay", "spend"}:
        source_key = source_line_key(fact)
        payload = fact.get("payload", {}) or {}
        costs = payload.get("costs", []) or []
        if isinstance(costs, dict):
            costs = [costs]
        cost_key = tuple(
            sorted(
                (
                    str(cost.get("resource") or ""),
                    str(cost.get("action") or ""),
                    str(cost.get("amount") or ""),
                    str(cost.get("domain") or ""),
                    str(cost.get("subject") or ""),
                    str(cost.get("object") or ""),
                    str(cost.get("event") or ""),
                )
                for cost in costs
                if isinstance(cost, dict)
            )
        )
        if not source_key or not cost_key:
            return None
        return (
            fact_play_id(fact),
            source_key,
            fact.get("semantic_role"),
            predicate,
            cost_key,
        )
    if predicate != "reduce_cost":
        return None
    payload = fact.get("payload", {}) or {}
    amounts = tuple(
        (amount.get("value"), amount.get("unit"), amount.get("domain"))
        for amount in payload.get("amounts", []) or []
        if isinstance(amount, dict)
    )
    target = payload.get("target") if isinstance(payload.get("target"), dict) else {}
    target_key = (
        target.get("kind"),
        tuple(target.get("kinds", []) or []),
        tuple(target.get("card_types", []) or []),
        target.get("scope"),
        target.get("controller"),
        target.get("location"),
        target.get("ordinal"),
        target.get("token_state"),
    )
    return (
        fact_play_id(fact),
        fact.get("clause_group_id"),
        fact.get("semantic_role"),
        fact.get("fact_type"),
        fact.get("predicate"),
        tuple(event_ids_from_fact(fact)),
        tuple(output_ids_from_fact(fact)),
        amounts,
        target_key,
        payload.get("duration") or "",
        payload.get("modality") or "",
        normalized_text(fact.get("evidence")),
    )


def expand_used_fact_ids_by_duplicate_coverage(
    facts: list[dict[str, Any]],
    used_fact_ids: set[str],
) -> set[str]:
    used_duplicate_keys = {
        key
        for fact in facts
        if fact.get("fact_id") in used_fact_ids
        for key in [duplicate_relation_coverage_key(fact)]
        if key is not None
    }
    if not used_duplicate_keys:
        return used_fact_ids
    expanded = set(used_fact_ids)
    for fact in facts:
        key = duplicate_relation_coverage_key(fact)
        if key in used_duplicate_keys and fact.get("fact_id"):
            expanded.add(str(fact["fact_id"]))
    return expanded


def relation_reason(relation: dict[str, Any]) -> str:
    return str(relation.get("match", {}).get("reason") or "")


def is_broad_relation(relation: dict[str, Any], broad_reasons: set[str]) -> bool:
    match = relation.get("match", {})
    return bool(match.get("broad")) or relation_reason(relation) in broad_reasons


def relation_count_dict(relations: list[dict[str, Any]]) -> dict[str, int]:
    counts = Counter(row.get("relation_type") for row in relations)
    return {relation_type: counts.get(relation_type, 0) for relation_type in RELATION_TYPES}


def percentile(values: list[int], fraction: float) -> int:
    if not values:
        return 0
    ordered = sorted(values)
    index = round((len(ordered) - 1) * fraction)
    return int(ordered[index])


def describe_distribution(values: list[int]) -> dict[str, Any]:
    if not values:
        return {
            "min": 0,
            "p25": 0,
            "median": 0,
            "p75": 0,
            "p90": 0,
            "p95": 0,
            "p99": 0,
            "max": 0,
            "mean": 0.0,
            "zero_count": 0,
        }
    return {
        "min": min(values),
        "p25": percentile(values, 0.25),
        "median": percentile(values, 0.5),
        "p75": percentile(values, 0.75),
        "p90": percentile(values, 0.9),
        "p95": percentile(values, 0.95),
        "p99": percentile(values, 0.99),
        "max": max(values),
        "mean": round(mean(values), 3),
        "zero_count": sum(1 for value in values if value == 0),
    }


def text_lines(card: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for source_field in TEXT_SOURCE_FIELDS:
        for line_index, line in enumerate(card.get(source_field, []) or []):
            rows.append({"source_field": source_field, "line_index": line_index, "line": line})
    return rows


def source_line_key(fact: dict[str, Any]) -> tuple[str, int] | None:
    source = fact.get("source", {})
    source_field = source.get("field")
    line_index = source.get("line_index")
    if source_field not in TEXT_SOURCE_FIELDS or line_index is None:
        return None
    return (source_field, int(line_index))


def line_has_any_token(line: str, tokens: list[str] | tuple[str, ...]) -> bool:
    lowered = line.casefold()
    for token in tokens:
        normalized = str(token).casefold().strip()
        if not normalized:
            continue
        if any(char.isalnum() for char in normalized):
            if re.search(rf"(?<![a-z0-9_]){re.escape(normalized)}(?![a-z0-9_])", lowered):
                return True
        elif normalized in lowered:
            return True
    return False


def line_has_relational_keyword(line: str, quality_policy: dict[str, Any]) -> bool:
    return line_has_any_token(line, quality_policy.get("relational_keywords", []))


def blind_spot_bucket(text: str, quality_policy: dict[str, Any]) -> str:
    lowered = text.casefold()
    if not lowered.strip():
        return quality_policy.get("empty_text_blind_spot_bucket", "vanilla/no_text")
    for bucket in quality_policy.get("blind_spot_buckets", []) or []:
        if any(token in lowered for token in bucket.get("tokens", [])):
            return bucket.get("id", quality_policy.get("default_blind_spot_bucket", "other"))
    return quality_policy.get("default_blind_spot_bucket", "other")


def text_excerpt(card: dict[str, Any], limit: int = 260) -> str:
    text = " | ".join((card.get("rules_lines", []) or []) + (card.get("effect_lines", []) or []))
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def compact_fact_for_report(fact: dict[str, Any]) -> dict[str, Any]:
    extractor = fact.get("extractor") if isinstance(fact.get("extractor"), dict) else {}
    source = fact.get("source", {})
    return {
        "play_id": fact_play_id(fact),
        "card_name": fact.get("_audit_card_name"),
        "fact_id": fact.get("fact_id"),
        "line": f"{source.get('field')}:{source.get('line_index')}"
        if source.get("field") in TEXT_SOURCE_FIELDS
        else "official_field",
        "semantic_role": fact.get("semantic_role"),
        "fact_type": fact.get("fact_type"),
        "predicate": fact.get("predicate"),
        "event_ids": event_ids_from_fact(fact),
        "output_ids": output_ids_from_fact(fact),
        "evidence": fact.get("evidence"),
        "web_uses": fact.get("web_uses", []),
        "rule_id": extractor.get("rule_id"),
        "source_kind": extractor.get("source_kind"),
    }


def fact_is_relation_candidate(fact: dict[str, Any]) -> bool:
    if fact.get("semantic_role") in RELATION_CANDIDATE_ROLES:
        return True
    return bool(RELATION_BUILDER_USES.intersection(set(fact.get("web_uses", []) or [])))


def fact_matches_intentionally_skipped_similarity(fact: dict[str, Any], quality_policy: dict[str, Any]) -> bool:
    broad_markers = set(quality_policy.get("similarity", {}).get("broad_key_markers", []) or [])
    payload = fact.get("payload", {}) or {}
    amounts = payload.get("amounts") or []
    amount = amounts[0] if amounts and isinstance(amounts[0], dict) else {}
    if (
        "card_drawn:1:card" in broad_markers
        and fact.get("predicate") == "draw"
        and "card_drawn" in output_ids_from_fact(fact)
        and amount.get("value") == 1
        and amount.get("unit") == "card"
        and payload.get("modality") == "required"
        and not payload.get("scaling")
    ):
        return True
    return False


def fact_matches_context_only_cost(fact: dict[str, Any]) -> bool:
    if fact.get("semantic_role") != "cost_or_requirement":
        return False
    if fact.get("fact_type") != "activated_ability_cost":
        return False
    costs = fact.get("payload", {}).get("costs", []) or []
    if isinstance(costs, dict):
        costs = [costs]
    costs = [cost for cost in costs if isinstance(cost, dict)]
    if not costs:
        return False
    return all(
        cost.get("action") == "exhaust"
        and (cost.get("subject") == "self" or cost.get("object") == "self")
        and not cost.get("resource")
        for cost in costs
    )


def fact_matches_opponent_paid_cost(fact: dict[str, Any]) -> bool:
    if fact.get("semantic_role") != "cost_or_requirement":
        return False
    return bool(re.search(r"\bopponents?\s+must\s+pay\b", str(fact.get("evidence") or ""), flags=re.IGNORECASE))


def fact_has_overparsed_cost_symbols(fact: dict[str, Any]) -> bool:
    if fact.get("semantic_role") != "cost_or_requirement":
        return False
    costs = fact.get("payload", {}).get("costs", []) or []
    if isinstance(costs, dict):
        costs = [costs]
    generated_symbols: Counter[str] = Counter()
    for cost in costs:
        if not isinstance(cost, dict):
            continue
        for symbol in re.findall(r":rb_(?:energy_\d+|rune_[a-z]+):", str(cost.get("symbol") or "")):
            generated_symbols[symbol] += 1
    if not generated_symbols:
        return False
    evidence = str(fact.get("evidence") or "")
    evidence_symbols = Counter(re.findall(r":rb_(?:energy_\d+|rune_[a-z]+):", evidence))
    return any(count > evidence_symbols.get(symbol, 0) for symbol, count in generated_symbols.items())


def fact_context_group_key(fact: dict[str, Any]) -> str | None:
    play_id = fact_play_id(fact)
    clause_group_id = fact.get("clause_group_id")
    if clause_group_id:
        return f"{play_id}|clause:{clause_group_id}"
    line_key = source_line_key(fact)
    if line_key:
        return f"{play_id}|line:{line_key[0]}:{line_key[1]}"
    return None


def require_fact_has_effect_sibling(
    fact: dict[str, Any],
    facts_by_clause: dict[str, list[dict[str, Any]]] | None,
) -> bool:
    if not facts_by_clause:
        return True
    group_key = fact_context_group_key(fact)
    if not group_key:
        return True
    for sibling in facts_by_clause.get(group_key, []):
        if sibling.get("fact_id") == fact.get("fact_id"):
            continue
        if sibling.get("semantic_role") == "identity_or_descriptor":
            continue
        if sibling.get("semantic_role") == "restriction_or_permission" and sibling.get("predicate") == "require":
            continue
        return True
    return False


def unlinked_fact_bucket(
    fact: dict[str, Any],
    quality_policy: dict[str, Any],
    facts_by_clause: dict[str, list[dict[str, Any]]] | None = None,
) -> str:
    role = fact.get("semantic_role")
    predicate = fact.get("predicate")
    event_ids = event_ids_from_fact(fact)
    output_ids = output_ids_from_fact(fact)
    source_kind = (fact.get("extractor") or {}).get("source_kind") if isinstance(fact.get("extractor"), dict) else None
    if source_kind == "structural_field" or role == "identity_or_descriptor":
        return "intentional_ignored"
    if fact_matches_intentionally_skipped_similarity(fact, quality_policy):
        return "intentional_ignored"
    if fact_has_overparsed_cost_symbols(fact):
        return "needs_extraction_fix"
    if fact_matches_opponent_paid_cost(fact):
        return "intentional_ignored"
    if fact_matches_context_only_cost(fact):
        return "intentional_ignored"
    if not event_ids and not output_ids and role in {"event_produced", "payoff_output", "state_or_modifier"}:
        return "weak_fact"
    if role == "trigger_observed" and event_ids:
        ignored_events = set(quality_policy.get("relation_event_ignore", []) or [])
        if set(event_ids).issubset(ignored_events):
            return "intentional_ignored"
        return "needs_relation_rule"
    if role == "restriction_or_permission" and predicate == "require":
        if not require_fact_has_effect_sibling(fact, facts_by_clause):
            return "needs_extraction_fix"
        return "intentional_ignored"
    if predicate in {"prevent", "require", "play", "move", "return_to_hand", "attach", "detach", "copy", "score", "gain_keyword", "modify_stat", "gain_control", "lose_control"}:
        return "needs_relation_rule"
    if not fact.get("evidence"):
        return "needs_extraction_fix"
    return "needs_relation_rule"


def unlinked_fact_family(fact: dict[str, Any]) -> str:
    predicate = str(fact.get("predicate") or "unknown")
    fact_type = str(fact.get("fact_type") or "unknown")
    if predicate in {"move", "return_to_hand", "play"} or fact_type == "movement":
        return "movement/location"
    if predicate in {"modify_stat", "gain_keyword", "buff"}:
        return "stat/buff/damage_modifier"
    if predicate in {"add_resource", "pay", "spend", "reduce_cost", "increase_cost", "cost_cap_constraint", "cost_threshold"}:
        return "cost/resource"
    if predicate in {"prevent", "kill", "heal"}:
        return "kill/heal/replacement"
    if predicate in {"attach", "detach", "copy"}:
        return "attachment/copy"
    if predicate in {"gain_control", "lose_control"} or fact_type == "control_change":
        return "control_change"
    if predicate in {"draw", "discard", "recycle", "look", "reveal"}:
        return "card_flow"
    return predicate


def build_relation_indexes(cards: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]], dict[str, list[dict[str, Any]]]]:
    relations_by_id = {}
    for card in cards:
        for relation in card.get("relations", {}).get("outgoing", []) or []:
            relations_by_id[relation["relation_id"]] = relation
    relations = sorted(relations_by_id.values(), key=lambda row: row["relation_id"])
    outgoing_by_card: dict[str, list[dict[str, Any]]] = defaultdict(list)
    incoming_by_card: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for relation in relations:
        outgoing_by_card[relation["source_play_id"]].append(relation)
        incoming_by_card[relation["target_play_id"]].append(relation)
    return relations, outgoing_by_card, incoming_by_card


def broad_reason_report(
    relations: list[dict[str, Any]],
    quality_policy: dict[str, Any],
) -> tuple[set[str], list[dict[str, Any]]]:
    reason_counts = Counter(relation_reason(relation) for relation in relations)
    threshold = int(quality_policy.get("broad_relation_count_threshold", 500))
    reasons_by_source: dict[str, set[str]] = defaultdict(set)
    for reason, count in reason_counts.items():
        if reason and count >= threshold:
            reasons_by_source[reason].add("threshold")
    for relation in relations:
        if relation.get("match", {}).get("broad") and relation_reason(relation):
            reasons_by_source[relation_reason(relation)].add("match_flag")
    for reason in DEFAULT_BROAD_REASONS:
        if reason in reason_counts:
            reasons_by_source[reason].add("explicit_default")

    broad_reasons = set(reasons_by_source)
    rows = []
    for reason in sorted(broad_reasons, key=lambda item: (-reason_counts[item], item)):
        rows.append(
            {
                "reason": reason,
                "count": reason_counts[reason],
                "share": round(reason_counts[reason] / len(relations), 4) if relations else 0.0,
                "sources": sorted(reasons_by_source[reason]),
            }
        )
    return broad_reasons, rows


def analyze_card(
    card: dict[str, Any],
    outgoing: list[dict[str, Any]],
    incoming: list[dict[str, Any]],
    broad_reasons: set[str],
    used_fact_ids: set[str],
    quality_policy: dict[str, Any],
    high_degree_threshold: int,
) -> dict[str, Any]:
    facts = card.get("semantic", {}).get("facts", []) or []
    lines = text_lines(card)
    line_facts: dict[tuple[str, int], list[dict[str, Any]]] = defaultdict(list)
    for fact in facts:
        key = source_line_key(fact)
        if key:
            line_facts[key].append(fact)

    missing_relational_lines = []
    weak_relational_lines = []
    relational_line_count = 0
    for row in lines:
        key = (row["source_field"], row["line_index"])
        if not line_has_relational_keyword(row["line"], quality_policy):
            continue
        relational_line_count += 1
        facts_on_line = line_facts.get(key, [])
        if not facts_on_line:
            missing_relational_lines.append(row)
            continue
        roles = {fact.get("semantic_role") for fact in facts_on_line}
        has_effect_fact = bool(
            roles.intersection(
                {
                    "cost_or_requirement",
                    "event_produced",
                    "payoff_output",
                    "restriction_or_permission",
                    "state_or_modifier",
                    "targeting_or_scope",
                }
            )
        )
        if not has_effect_fact and line_has_any_token(row["line"], WEAK_EFFECT_TOKENS):
            weak_relational_lines.append(row)

    incident = outgoing + incoming
    broad_relations = [relation for relation in incident if is_broad_relation(relation, broad_reasons)]
    high_signal_relations = [relation for relation in incident if not is_broad_relation(relation, broad_reasons)]
    relation_count = len(incident)
    broad_count = len(broad_relations)
    high_signal_count = len(high_signal_relations)
    relation_candidate_facts = [fact for fact in facts if fact_is_relation_candidate(fact)]
    unlinked_relation_candidate_facts = [
        fact
        for fact in relation_candidate_facts
        if fact.get("fact_id") not in used_fact_ids
        and fact.get("semantic_role") != "identity_or_descriptor"
    ]
    full_text = " ".join((card.get("rules_lines", []) or []) + (card.get("effect_lines", []) or []))
    broad_share = round(broad_count / relation_count, 4) if relation_count else 0.0
    diagnostic = classify_diagnostic(
        relation_count=relation_count,
        broad_count=broad_count,
        high_signal_count=high_signal_count,
        broad_share=broad_share,
        relational_line_count=relational_line_count,
        missing_line_count=len(missing_relational_lines),
        weak_line_count=len(weak_relational_lines),
        relation_candidate_fact_count=len(relation_candidate_facts),
        unlinked_relation_candidate_fact_count=len(unlinked_relation_candidate_facts),
        has_text=bool(full_text.strip()),
        high_degree_threshold=high_degree_threshold,
    )
    reason_counts = Counter(relation_reason(relation) for relation in incident)
    top_reasons = [
        {"reason": reason, "count": count, "broad": reason in broad_reasons}
        for reason, count in reason_counts.most_common(5)
    ]

    return {
        "play_id": card["play_id"],
        "name": card.get("name"),
        "card_type_ids": card.get("card_type_ids", []),
        "domain_ids": card.get("domain_ids", []),
        "bucket": blind_spot_bucket(full_text, quality_policy),
        "diagnostic": diagnostic,
        "relation_count": relation_count,
        "outgoing_count": len(outgoing),
        "incoming_count": len(incoming),
        "relation_counts": {
            "outgoing": relation_count_dict(outgoing),
            "incoming": relation_count_dict(incoming),
            "incident": relation_count_dict(incident),
        },
        "broad_relation_count": broad_count,
        "high_signal_relation_count": high_signal_count,
        "broad_relation_share": broad_share,
        "top_relation_reasons": top_reasons,
        "text_excerpt": text_excerpt(card),
        "text_line_count": len(lines),
        "relational_line_count": relational_line_count,
        "missing_relational_lines": missing_relational_lines,
        "weak_relational_lines": weak_relational_lines,
        "fact_count": len(facts),
        "fact_counts": card.get("semantic", {}).get("fact_counts", {}),
        "relation_candidate_fact_count": len(relation_candidate_facts),
        "unlinked_relation_candidate_fact_count": len(unlinked_relation_candidate_facts),
        "semantic": {
            "keywords": card.get("semantic", {}).get("keywords", []),
            "triggers": card.get("semantic", {}).get("triggers", []),
            "produced_events": card.get("semantic", {}).get("produced_events", []),
            "outputs": card.get("semantic", {}).get("outputs", []),
            "predicates": card.get("semantic", {}).get("predicates", []),
        },
    }


def classify_diagnostic(
    *,
    relation_count: int,
    broad_count: int,
    high_signal_count: int,
    broad_share: float,
    relational_line_count: int,
    missing_line_count: int,
    weak_line_count: int,
    relation_candidate_fact_count: int,
    unlinked_relation_candidate_fact_count: int,
    has_text: bool,
    high_degree_threshold: int,
) -> str:
    if relation_count > 0 and high_signal_count == 0:
        return "broad_only"
    if relation_count >= high_degree_threshold and broad_count > 0 and broad_share >= 0.6:
        return "front_scoring_issue"
    if relation_count == 0:
        if not has_text or relational_line_count == 0:
            return "likely_vanilla_or_low_relational_text"
        if missing_line_count:
            return "missing_fact"
        if weak_line_count:
            return "weak_fact"
        if relation_candidate_fact_count or unlinked_relation_candidate_fact_count:
            return "missing_relation_rule"
        return "missing_fact"
    if missing_line_count:
        return "missing_fact"
    if weak_line_count:
        return "weak_fact"
    if high_signal_count == 0 and broad_count:
        return "broad_only"
    return "ok"


def card_summary(analysis: dict[str, Any]) -> dict[str, Any]:
    return {
        "play_id": analysis["play_id"],
        "name": analysis["name"],
        "card_type_ids": analysis["card_type_ids"],
        "domain_ids": analysis["domain_ids"],
        "bucket": analysis["bucket"],
        "diagnostic": analysis["diagnostic"],
        "relation_count": analysis["relation_count"],
        "broad_relation_count": analysis["broad_relation_count"],
        "high_signal_relation_count": analysis["high_signal_relation_count"],
        "broad_relation_share": analysis["broad_relation_share"],
        "relational_line_count": analysis["relational_line_count"],
        "missing_relational_line_count": len(analysis["missing_relational_lines"]),
        "weak_relational_line_count": len(analysis["weak_relational_lines"]),
        "relation_candidate_fact_count": analysis["relation_candidate_fact_count"],
        "unlinked_relation_candidate_fact_count": analysis["unlinked_relation_candidate_fact_count"],
        "fact_counts": analysis["fact_counts"],
        "semantic": analysis["semantic"],
        "text_excerpt": analysis["text_excerpt"],
        "top_relation_reasons": analysis["top_relation_reasons"],
    }


def sort_issue_cards(analyses: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        analyses,
        key=lambda item: (
            DIAGNOSTIC_ORDER.get(item["diagnostic"], 99),
            BUCKET_PRIORITY.get(item["bucket"], 99),
            -len(item["missing_relational_lines"]),
            -len(item["weak_relational_lines"]),
            -item["relation_candidate_fact_count"],
            item["name"] or "",
        ),
    )


def relation_sample(relations: list[dict[str, Any]], broad_reasons: set[str], limit: int = 8) -> list[dict[str, Any]]:
    ordered = sorted(
        relations,
        key=lambda relation: (
            is_broad_relation(relation, broad_reasons),
            -float(relation.get("strength", 0) or 0),
            relation.get("target_card_name") or relation.get("source_card_name") or "",
        ),
    )
    rows = []
    for relation in ordered[:limit]:
        rows.append(
            {
                "relation_id": relation.get("relation_id"),
                "relation_type": relation.get("relation_type"),
                "source": relation.get("source_card_name"),
                "target": relation.get("target_card_name"),
                "strength": relation.get("strength"),
                "reason": relation_reason(relation),
                "broad": is_broad_relation(relation, broad_reasons),
                "evidence": relation.get("evidence", {}),
            }
        )
    return rows


def build_backtrace(
    card: dict[str, Any],
    analysis: dict[str, Any],
    outgoing: list[dict[str, Any]],
    incoming: list[dict[str, Any]],
    broad_reasons: set[str],
    quality_policy: dict[str, Any],
) -> dict[str, Any]:
    facts = card.get("semantic", {}).get("facts", []) or []
    facts_by_line: dict[str, list[dict[str, Any]]] = defaultdict(list)
    official_facts = []
    for fact in facts:
        compact = compact_fact_for_report(fact)
        line = compact["line"]
        if line == "official_field":
            official_facts.append(compact)
        else:
            facts_by_line[line].append(compact)

    line_rows = []
    for row in text_lines(card):
        line_key = f"{row['source_field']}:{row['line_index']}"
        line_rows.append(
            {
                **row,
                "relational": line_has_relational_keyword(row["line"], quality_policy),
                "facts": facts_by_line.get(line_key, []),
            }
        )

    return {
        "play_id": card["play_id"],
        "name": card.get("name"),
        "diagnostic": analysis["diagnostic"],
        "bucket": analysis["bucket"],
        "card_type_ids": card.get("card_type_ids", []),
        "domain_ids": card.get("domain_ids", []),
        "rules_lines": card.get("rules_lines", []),
        "effect_lines": card.get("effect_lines", []),
        "semantic_summary": analysis["semantic"],
        "quality_summary": {
            "relation_count": analysis["relation_count"],
            "broad_relation_count": analysis["broad_relation_count"],
            "high_signal_relation_count": analysis["high_signal_relation_count"],
            "relational_line_count": analysis["relational_line_count"],
            "missing_relational_lines": analysis["missing_relational_lines"],
            "weak_relational_lines": analysis["weak_relational_lines"],
            "unlinked_relation_candidate_fact_count": analysis["unlinked_relation_candidate_fact_count"],
        },
        "facts_by_line": line_rows,
        "official_facts": official_facts,
        "relation_samples": {
            "outgoing": relation_sample(outgoing, broad_reasons),
            "incoming": relation_sample(incoming, broad_reasons),
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
            if isinstance(value, (dict, list)):
                value = json.dumps(value, ensure_ascii=False)
            values.append(str(value).replace("\n", " ").replace("|", "\\|"))
        lines.append("| " + " | ".join(values) + " |")
    return lines


def markdown_card_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    compact_rows = []
    for row in rows:
        missing_count = row.get("missing_relational_line_count", len(row.get("missing_relational_lines", [])))
        weak_count = row.get("weak_relational_line_count", len(row.get("weak_relational_lines", [])))
        compact_rows.append(
            {
                "card": row["name"],
                "diagnostic": row["diagnostic"],
                "bucket": row["bucket"],
                "degree": row["relation_count"],
                "high_signal": row["high_signal_relation_count"],
                "missing_lines": missing_count,
                "weak_lines": weak_count,
                "text": row["text_excerpt"],
            }
        )
    return compact_rows


def build_markdown(report: dict[str, Any], sample_size: int) -> str:
    lines = [
        "# Card Explorer Quality Report",
        "",
        "Audit for the sharded card explorer dataset rooted at `data/processed/web/card_explorer_index.json`.",
        "",
        "## Summary",
        "",
    ]
    for key, value in report["summary"].items():
        lines.append(f"- {key}: {value}")
    if report.get("snapshot"):
        lines.extend(["", "## Snapshot", ""])
        lines.append(f"- date: {report['snapshot'].get('date')}")
        for key, value in (report["snapshot"].get("thresholds") or {}).items():
            lines.append(f"- {key}: {value}")

    lines.extend(["", "## Relation Types", ""])
    for key, value in report["relation_type_counts"].items():
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## Degree Distribution", ""])
    distribution_rows = [
        {"scope": key, **value}
        for key, value in report["degree_distribution"].items()
        if isinstance(value, dict)
    ]
    lines.extend(
        markdown_table(
            distribution_rows,
            [
                ("Scope", "scope"),
                ("Min", "min"),
                ("P50", "median"),
                ("P90", "p90"),
                ("P95", "p95"),
                ("P99", "p99"),
                ("Max", "max"),
                ("Mean", "mean"),
                ("Zero", "zero_count"),
            ],
        )
    )

    lines.extend(["", "## Diagnostics", ""])
    for key, value in report["diagnostic_counts"].items():
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## Broad Relation Reasons", ""])
    if report["broad_relation_reasons"]:
        lines.extend(
            markdown_table(
                report["broad_relation_reasons"],
                [("Reason", "reason"), ("Count", "count"), ("Share", "share"), ("Sources", "sources")],
            )
        )
    else:
        lines.append("- none")

    lines.extend(["", "## Cards Without Relations By Bucket", ""])
    for key, value in report["cards_without_relations_by_bucket"].items():
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## Top Hubs", ""])
    lines.extend(
        markdown_table(
            report["top_hubs"][:sample_size],
            [
                ("Card", "name"),
                ("Degree", "relation_count"),
                ("Broad", "broad_relation_count"),
                ("High Signal", "high_signal_relation_count"),
                ("Broad Share", "broad_relation_share"),
                ("Diagnostic", "diagnostic"),
            ],
        )
    )

    samples = report["manual_review_samples"]
    lines.extend(["", "## Manual Review Samples", ""])
    sample_sections = [
        ("No Relations With Relational Text", "no_relations_with_relational_text"),
        ("Only Broad Relations", "only_broad_relations"),
        ("Uncovered Relational Lines", "uncovered_relational_lines"),
        ("Unlinked Relation Candidate Facts", "unlinked_relation_candidate_facts"),
    ]
    for title, key in sample_sections:
        lines.extend(["", f"### {title}", ""])
        rows = samples.get(key, [])[:sample_size]
        if rows:
            lines.extend(
                markdown_table(
                    markdown_card_rows(rows),
                    [
                        ("Card", "card"),
                        ("Diagnostic", "diagnostic"),
                        ("Bucket", "bucket"),
                        ("Degree", "degree"),
                        ("High Signal", "high_signal"),
                        ("Missing", "missing_lines"),
                        ("Weak", "weak_lines"),
                        ("Text", "text"),
                    ],
                )
            )
        else:
            lines.append("No cards found.")

    lines.extend(["", "## Facts Not Becoming Relations", ""])
    unlinked = report["facts_not_becoming_relations"]
    lines.append(f"- relation_candidate_fact_count: {unlinked['relation_candidate_fact_count']}")
    lines.append(f"- unlinked_relation_candidate_fact_count: {unlinked['unlinked_relation_candidate_fact_count']}")
    if "actionable_unlinked_relation_candidate_fact_count" in unlinked:
        lines.append(f"- actionable_unlinked_relation_candidate_fact_count: {unlinked['actionable_unlinked_relation_candidate_fact_count']}")
    if "needs_relation_rule_fact_count" in unlinked:
        lines.append(f"- needs_relation_rule_fact_count: {unlinked['needs_relation_rule_fact_count']}")
    if unlinked.get("classification_counts"):
        lines.extend(["", "### Classification Counts", ""])
        for key, value in unlinked["classification_counts"].items():
            lines.append(f"- {key}: {value}")
    if unlinked.get("classification_matrix_by_family"):
        lines.extend(["", "### Classification Matrix By Family", ""])
        for family, counts in list(unlinked["classification_matrix_by_family"].items())[:20]:
            summary = ", ".join(f"{key}={value}" for key, value in counts.items())
            lines.append(f"- {family}: {summary}")
    if unlinked.get("example_facts_by_family"):
        lines.extend(["", "### Example Facts By Family", ""])
        for family, classifications in list(unlinked["example_facts_by_family"].items())[:12]:
            lines.append(f"- {family}:")
            for classification, facts in classifications.items():
                examples = "; ".join(
                    f"{fact.get('card_name') or fact.get('play_id')} [{fact.get('predicate')}] {fact.get('evidence')}"
                    for fact in facts[:3]
                )
                lines.append(f"  - {classification}: {examples}")
    if unlinked.get("vanilla_or_intentionally_isolated_allowlist"):
        lines.extend(["", "### Vanilla / Intentionally Isolated Allowlist", ""])
        for play_id in unlinked["vanilla_or_intentionally_isolated_allowlist"][:40]:
            lines.append(f"- {play_id}")
    lines.extend(["", "### Top Unlinked Predicates", ""])
    for key, value in unlinked["top_unlinked_predicates"].items():
        lines.append(f"- {key}: {value}")
    if unlinked.get("top_actionable_unlinked_predicates"):
        lines.extend(["", "### Top Actionable Unlinked Predicates", ""])
        for key, value in unlinked["top_actionable_unlinked_predicates"].items():
            lines.append(f"- {key}: {value}")
    if unlinked.get("top_needs_relation_rule_predicates"):
        lines.extend(["", "### Top Needs Relation Rule Predicates", ""])
        for key, value in unlinked["top_needs_relation_rule_predicates"].items():
            lines.append(f"- {key}: {value}")

    lines.extend(["", "## Backtrace Samples", ""])
    for row in report["backtrace_samples"][:sample_size]:
        lines.extend(["", f"### {row['name']}", ""])
        lines.append(f"- diagnostic: {row['diagnostic']}")
        lines.append(f"- bucket: {row['bucket']}")
        lines.append(
            "- relation_count: "
            f"{row['quality_summary']['relation_count']} "
            f"(high_signal={row['quality_summary']['high_signal_relation_count']}, "
            f"broad={row['quality_summary']['broad_relation_count']})"
        )
        if row["rules_lines"]:
            lines.append("- rules: " + " | ".join(row["rules_lines"]))
        if row["effect_lines"]:
            lines.append("- effects: " + " | ".join(row["effect_lines"]))
        fact_rows = []
        for line in row["facts_by_line"]:
            for fact in line["facts"]:
                fact_rows.append(
                    {
                        "line": f"{line['source_field']}:{line['line_index']}",
                        "role": fact["semantic_role"],
                        "predicate": fact["predicate"],
                        "events": ",".join(fact["event_ids"]),
                        "outputs": ",".join(fact["output_ids"]),
                        "evidence": fact["evidence"],
                    }
                )
        if fact_rows:
            lines.extend(
                markdown_table(
                    fact_rows[:12],
                    [
                        ("Line", "line"),
                        ("Role", "role"),
                        ("Predicate", "predicate"),
                        ("Events", "events"),
                        ("Outputs", "outputs"),
                        ("Evidence", "evidence"),
                    ],
                )
            )
        else:
            lines.append("- facts: none on text lines")

    return "\n".join(lines) + "\n"


def build_report(
    dataset: dict[str, Any],
    quality_policy: dict[str, Any],
    sample_size: int,
    dataset_path: Path,
    quality_policy_path: Path,
) -> dict[str, Any]:
    cards = dataset.get("cards", []) or []
    card_by_id = {card["play_id"]: card for card in cards}
    all_facts = [
        {**fact, "_audit_play_id": card["play_id"], "_audit_card_name": card.get("name")}
        for card in cards
        for fact in card.get("semantic", {}).get("facts", []) or []
    ]
    facts_by_clause: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for fact in all_facts:
        group_key = fact_context_group_key(fact)
        if group_key:
            facts_by_clause[group_key].append(fact)
    relations, outgoing_by_card, incoming_by_card = build_relation_indexes(cards)
    broad_reasons, broad_reason_rows = broad_reason_report(relations, quality_policy)
    used_fact_ids = {
        fact_id
        for relation in relations
        for fact_id in (relation.get("source_fact_id"), relation.get("target_fact_id"))
        if fact_id
    }
    for relation in relations:
        match = relation.get("match") if isinstance(relation.get("match"), dict) else {}
        for fact_id in match.get("supporting_fact_ids", []) or []:
            if fact_id:
                used_fact_ids.add(str(fact_id))
    used_fact_ids = expand_used_fact_ids_by_duplicate_coverage(all_facts, used_fact_ids)
    degree_values = [
        len(outgoing_by_card.get(card["play_id"], [])) + len(incoming_by_card.get(card["play_id"], []))
        for card in cards
    ]
    high_degree_threshold = describe_distribution(degree_values)["p95"]

    analyses = [
        analyze_card(
            card,
            outgoing_by_card.get(card["play_id"], []),
            incoming_by_card.get(card["play_id"], []),
            broad_reasons,
            used_fact_ids,
            quality_policy,
            high_degree_threshold,
        )
        for card in cards
    ]

    cards_without_relations = [row for row in analyses if row["relation_count"] == 0]
    only_broad = [row for row in analyses if row["relation_count"] > 0 and row["high_signal_relation_count"] == 0]
    uncovered_relational = [row for row in analyses if row["missing_relational_lines"]]
    top_hubs = sorted(analyses, key=lambda row: (-row["relation_count"], row["name"] or ""))[:40]
    artificial_hubs = [
        row
        for row in top_hubs
        if row["broad_relation_count"] and (row["broad_relation_share"] >= 0.6 or row["diagnostic"] == "front_scoring_issue")
    ]
    no_relations_with_relational_text = [
        row
        for row in cards_without_relations
        if row["relational_line_count"] > 0 and row["text_excerpt"]
    ]
    unlinked_cards = [
        row
        for row in analyses
        if row["unlinked_relation_candidate_fact_count"] > 0
        and row["diagnostic"] in {"missing_relation_rule", "weak_fact", "missing_fact"}
    ]

    sample_groups = {
        "no_relations_with_relational_text": sort_issue_cards(no_relations_with_relational_text)[:sample_size],
        "only_broad_relations": sorted(only_broad, key=lambda row: (-row["relation_count"], row["name"] or ""))[:sample_size],
        "top_hubs": top_hubs[:sample_size],
        "uncovered_relational_lines": sort_issue_cards(uncovered_relational)[:sample_size],
        "unlinked_relation_candidate_facts": sorted(
            unlinked_cards,
            key=lambda row: (-row["unlinked_relation_candidate_fact_count"], DIAGNOSTIC_ORDER.get(row["diagnostic"], 99), row["name"] or ""),
        )[:sample_size],
    }
    backtrace_ids = []
    for rows in sample_groups.values():
        for row in rows:
            if row["play_id"] not in backtrace_ids:
                backtrace_ids.append(row["play_id"])

    relation_candidate_facts = [fact for fact in all_facts if fact_is_relation_candidate(fact)]
    unlinked_relation_candidate_facts = [
        fact
        for fact in relation_candidate_facts
        if fact.get("fact_id") not in used_fact_ids
        and fact.get("semantic_role") != "identity_or_descriptor"
    ]
    unlinked_fact_classifications = {
        fact["fact_id"]: unlinked_fact_bucket(fact, quality_policy, facts_by_clause)
        for fact in unlinked_relation_candidate_facts
        if fact.get("fact_id")
    }
    actionable_unlinked_relation_candidate_facts = [
        fact
        for fact in unlinked_relation_candidate_facts
        if unlinked_fact_classifications.get(fact.get("fact_id")) != "intentional_ignored"
    ]
    needs_relation_rule_facts = [
        fact
        for fact in unlinked_relation_candidate_facts
        if unlinked_fact_classifications.get(fact.get("fact_id")) == "needs_relation_rule"
    ]
    unlinked_predicates = Counter(str(fact.get("predicate")) for fact in unlinked_relation_candidate_facts)
    unlinked_roles = Counter(str(fact.get("semantic_role")) for fact in unlinked_relation_candidate_facts)
    unlinked_events = Counter(event_id for fact in unlinked_relation_candidate_facts for event_id in event_ids_from_fact(fact))
    unlinked_outputs = Counter(output_id for fact in unlinked_relation_candidate_facts for output_id in output_ids_from_fact(fact))
    actionable_unlinked_predicates = Counter(str(fact.get("predicate")) for fact in actionable_unlinked_relation_candidate_facts)
    actionable_unlinked_events = Counter(event_id for fact in actionable_unlinked_relation_candidate_facts for event_id in event_ids_from_fact(fact))
    relation_rule_unlinked_predicates = Counter(str(fact.get("predicate")) for fact in needs_relation_rule_facts)
    relation_rule_unlinked_events = Counter(event_id for fact in needs_relation_rule_facts for event_id in event_ids_from_fact(fact))
    unlinked_classification = Counter(unlinked_fact_classifications.values())
    unlinked_matrix: dict[str, Counter[str]] = defaultdict(Counter)
    example_facts_by_family: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    for fact in unlinked_relation_candidate_facts:
        classification = unlinked_fact_classifications.get(fact.get("fact_id"), unlinked_fact_bucket(fact, quality_policy, facts_by_clause))
        family = unlinked_fact_family(fact)
        unlinked_matrix[family][classification] += 1
        if len(example_facts_by_family[family][classification]) < 5:
            example_facts_by_family[family][classification].append(compact_fact_for_report(fact))
    vanilla_allowlist = [
        row["play_id"]
        for row in cards_without_relations
        if row["bucket"] == quality_policy.get("empty_text_blind_spot_bucket", "vanilla/no_text")
    ][:40]

    relation_type_counts = Counter(row.get("relation_type") for row in relations)
    diagnostic_counts = Counter(row["diagnostic"] for row in analyses)
    cards_without_relations_by_bucket = Counter(row["bucket"] for row in cards_without_relations)
    broad_relation_count = sum(1 for relation in relations if is_broad_relation(relation, broad_reasons))
    degree_distribution = {
        "total": describe_distribution(degree_values),
        "outgoing": describe_distribution([len(outgoing_by_card.get(card["play_id"], [])) for card in cards]),
        "incoming": describe_distribution([len(incoming_by_card.get(card["play_id"], [])) for card in cards]),
    }
    for relation_type in RELATION_TYPES:
        degree_distribution[relation_type] = describe_distribution(
            [
                sum(1 for relation in outgoing_by_card.get(card["play_id"], []) if relation.get("relation_type") == relation_type)
                + sum(1 for relation in incoming_by_card.get(card["play_id"], []) if relation.get("relation_type") == relation_type)
                for card in cards
            ]
        )

    backtraces = [
        build_backtrace(
            card_by_id[play_id],
            next(row for row in analyses if row["play_id"] == play_id),
            outgoing_by_card.get(play_id, []),
            incoming_by_card.get(play_id, []),
            broad_reasons,
            quality_policy,
        )
        for play_id in backtrace_ids
        if play_id in card_by_id
    ]

    return {
        "version": dataset.get("version"),
        "snapshot": {
            "date": SNAPSHOT_DATE,
            "dataset_snapshot": dataset.get("snapshot", {}),
            "thresholds": {
                "broad_relation_count_threshold": int(quality_policy.get("broad_relation_count_threshold", 500)),
                "high_degree_threshold_p95": high_degree_threshold,
                "legacy_rule_count_max": quality_policy.get("legacy_rule_count_max"),
            },
        },
        "inputs": {
            "dataset": str(dataset_path),
            "quality_policy": str(quality_policy_path),
        },
        "summary": {
            "card_count": len(cards),
            "fact_count": dataset.get("summary", {}).get("fact_count", len(all_facts)),
            "relation_count": len(relations),
            "cards_without_relations": len(cards_without_relations),
            "cards_with_only_broad_relations": len(only_broad),
            "cards_with_uncovered_relational_lines": len(uncovered_relational),
            "broad_relation_count": broad_relation_count,
            "high_signal_relation_count": len(relations) - broad_relation_count,
            "broad_relation_share": round(broad_relation_count / len(relations), 4) if relations else 0.0,
            "high_degree_threshold_p95": high_degree_threshold,
            "cards_with_rule_variants": dataset.get("summary", {}).get(
                "cards_with_rule_variants",
                sum(1 for card in cards if card.get("semantic", {}).get("variant_warning", {}).get("has_rule_variants")),
            ),
        },
        "relation_type_counts": {key: relation_type_counts.get(key, 0) for key in RELATION_TYPES},
        "degree_distribution": degree_distribution,
        "diagnostic_counts": dict(diagnostic_counts.most_common()),
        "broad_relation_reasons": broad_reason_rows,
        "cards_without_relations_by_bucket": dict(cards_without_relations_by_bucket.most_common()),
        "top_hubs": [card_summary(row) for row in top_hubs],
        "artificial_hubs": [card_summary(row) for row in artificial_hubs],
        "cards_without_relations": [card_summary(row) for row in sort_issue_cards(cards_without_relations)],
        "cards_with_only_broad_relations": [card_summary(row) for row in sorted(only_broad, key=lambda row: (-row["relation_count"], row["name"] or ""))],
        "cards_with_uncovered_relational_lines": [card_summary(row) for row in sort_issue_cards(uncovered_relational)],
        "manual_review_samples": {
            key: [card_summary(row) for row in rows]
            for key, rows in sample_groups.items()
        },
        "facts_not_becoming_relations": {
            "relation_candidate_fact_count": len(relation_candidate_facts),
            "unlinked_relation_candidate_fact_count": len(unlinked_relation_candidate_facts),
            "actionable_unlinked_relation_candidate_fact_count": len(actionable_unlinked_relation_candidate_facts),
            "needs_relation_rule_fact_count": len(needs_relation_rule_facts),
            "classification_counts": dict(unlinked_classification.most_common()),
            "classification_matrix_by_family": {
                family: dict(counts.most_common())
                for family, counts in sorted(unlinked_matrix.items(), key=lambda item: (-sum(item[1].values()), item[0]))
            },
            "example_facts_by_family": {
                family: dict(classifications)
                for family, classifications in sorted(
                    example_facts_by_family.items(),
                    key=lambda item: (-sum(len(rows) for rows in item[1].values()), item[0]),
                )
            },
            "vanilla_or_intentionally_isolated_allowlist": vanilla_allowlist,
            "top_unlinked_roles": dict(unlinked_roles.most_common(20)),
            "top_unlinked_predicates": dict(unlinked_predicates.most_common(30)),
            "top_unlinked_events": dict(unlinked_events.most_common(30)),
            "top_unlinked_outputs": dict(unlinked_outputs.most_common(30)),
            "top_actionable_unlinked_predicates": dict(actionable_unlinked_predicates.most_common(30)),
            "top_actionable_unlinked_events": dict(actionable_unlinked_events.most_common(30)),
            "top_needs_relation_rule_predicates": dict(relation_rule_unlinked_predicates.most_common(30)),
            "top_needs_relation_rule_events": dict(relation_rule_unlinked_events.most_common(30)),
            "example_facts": [compact_fact_for_report(fact) for fact in unlinked_relation_candidate_facts[:80]],
        },
        "backtrace_samples": backtraces,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit relation quality in the generated card explorer dataset.")
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET)
    parser.add_argument("--quality-policy", type=Path, default=DEFAULT_QUALITY_POLICY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MARKDOWN)
    parser.add_argument("--sample-size", type=int, default=10)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    dataset = load_dataset(args.dataset)
    quality_policy = read_json(args.quality_policy)
    report = build_report(dataset, quality_policy, args.sample_size, args.dataset, args.quality_policy)
    write_json(args.output, report)
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.write_text(build_markdown(report, args.sample_size), encoding="utf-8")
    summary = report["summary"]
    print(f"Wrote card explorer quality JSON to {args.output}")
    print(f"Wrote card explorer quality Markdown to {args.markdown}")
    print(
        "Quality audit: "
        f"{summary['card_count']} cards, "
        f"{summary['fact_count']} facts, "
        f"{summary['relation_count']} relations, "
        f"{summary['cards_without_relations']} without relations, "
        f"{summary['cards_with_only_broad_relations']} broad-only, "
        f"{summary['cards_with_uncovered_relational_lines']} with uncovered relational lines"
    )


if __name__ == "__main__":
    main()
