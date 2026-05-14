import argparse
import hashlib
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
FEATURE_EXTRACTION_DIR = PROJECT_ROOT / "scripts" / "04_cards_feature_extraction"
sys.path.append(str(FEATURE_EXTRACTION_DIR))

from semantic_contracts import DEFAULT_QUALITY_POLICY, load_contract_bundle

DEFAULT_CARDS = PROJECT_ROOT / "data" / "processed" / "cards" / "normalized" / "cards_normalized.json"
DEFAULT_FACTS = PROJECT_ROOT / "data" / "processed" / "cards" / "semantic" / "cards_semantic_facts.jsonl"
DEFAULT_RELATIONS = PROJECT_ROOT / "data" / "processed" / "cards" / "relations" / "cards_card_relations.jsonl"
DEFAULT_WEB_DIR = PROJECT_ROOT / "data" / "processed" / "web"
DEFAULT_OUTPUT = DEFAULT_WEB_DIR / "card_explorer_index.json"
DEFAULT_RELATION_SHARDS = DEFAULT_WEB_DIR / "relations"
DEFAULT_FACT_SHARDS = DEFAULT_WEB_DIR / "facts"
DEFAULT_REPORT = PROJECT_ROOT / "data" / "processed" / "web" / "card_explorer_dataset_report.json"
DEFAULT_MARKDOWN = PROJECT_ROOT / "data" / "processed" / "web" / "card_explorer_dataset_report.md"

VERSION = "2026-05-12"
SNAPSHOT_DATE = date.today().isoformat()
DEFAULT_SHARD_COUNT = 32
DEFAULT_MAX_ARTIFACT_BYTES = 50 * 1024 * 1024
RELATION_TYPES = ("enables", "enabled_by", "similar_effect", "deck_synergy")


def repo_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


RELATION_TYPE_MANIFEST = {
    "enabled_by": {
        "label": "Enablers",
        "default_visible": True,
        "lane": "high_signal",
        "required_fields": ["relation_id", "relation_type", "source_fact_id", "target_fact_id", "match", "strength", "evidence"],
    },
    "enables": {
        "label": "Enabled Cards",
        "default_visible": True,
        "lane": "high_signal",
        "required_fields": ["relation_id", "relation_type", "source_fact_id", "target_fact_id", "match", "strength", "evidence"],
    },
    "similar_effect": {
        "label": "Similar Effects",
        "default_visible": True,
        "lane": "high_signal",
        "required_fields": ["relation_id", "relation_type", "source_fact_id", "target_fact_id", "match", "strength", "evidence"],
    },
    "deck_synergy": {
        "label": "Deck Synergy",
        "default_visible": False,
        "experimental": True,
        "lane": "experimental",
        "required_fields": ["relation_id", "relation_type", "source_fact_id", "target_fact_id", "match", "strength", "evidence"],
    },
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


def json_bytes(payload: Any) -> int:
    return len(json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))


def write_json(path: Path, payload: dict[str, Any], *, pretty: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if pretty:
        body = json.dumps(payload, ensure_ascii=False, indent=2)
    else:
        body = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    path.write_text(body + "\n", encoding="utf-8")


def reset_directory(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def shard_index(value: Any, shard_count: int) -> int:
    digest = hashlib.sha1(str(value).encode("utf-8")).hexdigest()
    return int(digest[:8], 16) % shard_count


def shard_name(index: int) -> str:
    return f"{index:02d}.json"


def shard_ref(kind: str, index: int) -> str:
    return f"{kind}/{shard_name(index)}"


def empty_relation_shards(shard_count: int) -> dict[int, dict[str, Any]]:
    return {
        index: {
            "version": VERSION,
            "shard": {"type": "relations", "index": index, "count": shard_count},
            "cards": {},
        }
        for index in range(shard_count)
    }


def empty_fact_shards(shard_count: int) -> dict[int, dict[str, Any]]:
    return {
        index: {
            "version": VERSION,
            "shard": {"type": "facts", "index": index, "count": shard_count},
            "facts": {},
        }
        for index in range(shard_count)
    }


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


def compact_fact(fact: dict[str, Any]) -> dict[str, Any]:
    source_ref = fact.get("source_ref", {})
    return {
        "fact_id": fact.get("fact_id"),
        "play_id": fact.get("play_id"),
        "semantic_role": fact.get("semantic_role"),
        "fact_type": fact.get("fact_type"),
        "predicate": fact.get("predicate"),
        "payload": fact.get("payload", {}),
        "evidence": fact.get("evidence"),
        "source": {
            "field": source_ref.get("source_field"),
            "line_index": source_ref.get("line_index"),
            "line_text": source_ref.get("line_text"),
            "unit_text": source_ref.get("unit_text"),
            "normalized_unit": source_ref.get("normalized_unit"),
            "parameterized_unit": source_ref.get("parameterized_unit"),
            "families": source_ref.get("inventory_families", []),
        },
        "web_uses": fact.get("web_uses", []),
        "extractor": fact.get("extractor"),
        "confidence": fact.get("confidence"),
    }


def compact_relation(
    relation: dict[str, Any],
    variant_play_ids: set[str] | None = None,
    broad_reasons: set[str] | None = None,
    facts_by_id: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    variant_play_ids = variant_play_ids or set()
    broad_reasons = broad_reasons or set()
    match = dict(relation.get("match", {}) or {})
    reason = str(match.get("reason") or "")
    if reason in broad_reasons:
        match.setdefault("broad", True)
        match.setdefault("broad_reason", reason)
    row = {
        "relation_id": relation.get("relation_id"),
        "relation_type": relation.get("relation_type"),
        "source_play_id": relation.get("source_play_id"),
        "target_play_id": relation.get("target_play_id"),
        "source_card_name": relation.get("source_card_name"),
        "target_card_name": relation.get("target_card_name"),
        "source_fact_id": relation.get("source_fact_id"),
        "target_fact_id": relation.get("target_fact_id"),
        "match": match,
        "strength": relation.get("strength"),
        "evidence": relation.get("evidence", {}),
    }
    if facts_by_id is not None:
        source_fact = facts_by_id.get(str(relation.get("source_fact_id")))
        target_fact = facts_by_id.get(str(relation.get("target_fact_id")))
        row["facts"] = {
            "source": compact_fact(source_fact) if source_fact else None,
            "target": compact_fact(target_fact) if target_fact else None,
        }
    source_has_variants = relation.get("source_play_id") in variant_play_ids
    target_has_variants = relation.get("target_play_id") in variant_play_ids
    if source_has_variants or target_has_variants:
        row["variant_warning"] = {
            "relation_uses_variant_sensitive_card": True,
            "source_has_rule_variants": source_has_variants,
            "target_has_rule_variants": target_has_variants,
        }
    return row


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


def keyword_ids_from_fact(fact: dict[str, Any]) -> list[str]:
    payload = fact.get("payload", {})
    obj = payload.get("object")
    if fact.get("fact_type") == "keyword_marker" and isinstance(obj, dict) and obj.get("id"):
        return [obj["id"]]
    keywords = []
    for value in nested_values(payload, "keywords"):
        if isinstance(value, list):
            keywords.extend(str(item) for item in value)
        elif isinstance(value, str):
            keywords.append(value)
    return sorted(set(keywords))


def image_url(card: dict[str, Any]) -> str | None:
    image = card.get("image")
    if isinstance(image, dict) and isinstance(image.get("url"), str):
        return image["url"]
    for key in ("image_url", "image", "card_image_url", "full_art_url", "thumbnail_url"):
        value = card.get(key)
        if isinstance(value, str) and value:
            return value
    for printing in card.get("printings", []) or []:
        if isinstance(printing, dict):
            image_value = printing.get("image")
            if isinstance(image_value, dict) and isinstance(image_value.get("url"), str):
                return image_value["url"]
            value = printing.get("image_url") or image_value
            if isinstance(value, str) and value:
                return value
    return None


def searchable_text(card: dict[str, Any], facts: list[dict[str, Any]]) -> str:
    parts = [
        card.get("name", ""),
        card.get("rules_text", ""),
        card.get("effect_text", ""),
        " ".join(card.get("domain_ids", []) or []),
        " ".join(card.get("card_type_ids", []) or []),
        " ".join(str(tag.get("name") if isinstance(tag, dict) else tag) for tag in card.get("tags", []) or []),
    ]
    parts.extend(str(fact.get("evidence", "")) for fact in facts)
    return " ".join(part for part in parts if part).casefold()


def relation_counts(relations: list[dict[str, Any]]) -> dict[str, int]:
    counts = Counter(relation.get("relation_type") for relation in relations)
    return {relation_type: counts.get(relation_type, 0) for relation_type in RELATION_TYPES}


def relation_reason(relation: dict[str, Any]) -> str:
    return str(relation.get("match", {}).get("reason") or "")


def is_broad_relation(relation: dict[str, Any], broad_reasons: set[str]) -> bool:
    match = relation.get("match", {})
    return bool(match.get("broad")) or bool(match.get("broad_reason")) or relation_reason(relation) in broad_reasons


def relation_quality_counts(relations: list[dict[str, Any]], broad_reasons: set[str]) -> dict[str, Any]:
    broad = [relation for relation in relations if is_broad_relation(relation, broad_reasons)]
    high_signal = [relation for relation in relations if not is_broad_relation(relation, broad_reasons)]
    return {
        "relation_count": len(relations),
        "high_signal_relation_count": len(high_signal),
        "broad_relation_count": len(broad),
        "broad_only": bool(relations and not high_signal),
        "high_signal_counts": relation_counts(high_signal),
        "broad_counts": relation_counts(broad),
    }


def blind_spot_bucket(text: str, quality_policy: dict[str, Any]) -> str:
    text = text.casefold()
    if not text.strip():
        return quality_policy.get("empty_text_blind_spot_bucket", "vanilla/no_text")
    for bucket in quality_policy.get("blind_spot_buckets", []) or []:
        if any(token in text for token in bucket.get("tokens", [])):
            return bucket.get("id", quality_policy.get("default_blind_spot_bucket", "other"))
    return quality_policy.get("default_blind_spot_bucket", "other")


def filter_option(values: Counter) -> list[dict[str, Any]]:
    return [{"id": key, "count": count} for key, count in sorted(values.items()) if key not in {None, ""}]


def build_dataset(
    cards: list[dict[str, Any]],
    facts: list[dict[str, Any]],
    relations: list[dict[str, Any]],
    quality_policy: dict[str, Any],
    shard_count: int = DEFAULT_SHARD_COUNT,
) -> tuple[dict[str, Any], dict[int, dict[str, Any]], dict[int, dict[str, Any]], dict[str, Any]]:
    facts_by_card: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for fact in facts:
        facts_by_card[fact["play_id"]].append(fact)
    facts_by_id = {str(fact.get("fact_id")): fact for fact in facts if fact.get("fact_id")}
    relation_shards = empty_relation_shards(shard_count)
    fact_shards = empty_fact_shards(shard_count)
    for fact_id, fact in facts_by_id.items():
        fact_shards[shard_index(fact_id, shard_count)]["facts"][fact_id] = compact_fact(fact)

    outgoing_relations_by_card: dict[str, list[dict[str, Any]]] = defaultdict(list)
    incoming_relations_by_card: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for relation in relations:
        outgoing_relations_by_card[relation["source_play_id"]].append(relation)
        incoming_relations_by_card[relation["target_play_id"]].append(relation)
    variant_play_ids = {card["play_id"] for card in cards if card.get("rule_variants")}

    relation_reason_counts = Counter(relation_reason(relation) for relation in relations)
    broad_threshold = int(quality_policy.get("broad_relation_count_threshold", 500))
    broad_reasons = {
        reason
        for reason, count in relation_reason_counts.items()
        if reason and count >= broad_threshold
    }
    broad_reasons.update(
        relation_reason(relation)
        for relation in relations
        if relation.get("match", {}).get("broad") or relation.get("match", {}).get("broad_reason")
    )

    filters = {
        "domains": Counter(),
        "card_types": Counter(),
        "tags": Counter(),
        "keywords": Counter(),
        "triggers": Counter(),
        "produced_events": Counter(),
        "outputs": Counter(),
        "predicates": Counter(),
        "energy": Counter(),
        "might": Counter(),
        "power": Counter(),
    }

    web_cards = []
    for card in cards:
        play_id = card["play_id"]
        card_facts = facts_by_card.get(play_id, [])
        outgoing = outgoing_relations_by_card.get(play_id, [])
        incoming = incoming_relations_by_card.get(play_id, [])

        keyword_ids = sorted({keyword for fact in card_facts for keyword in keyword_ids_from_fact(fact)})
        trigger_ids = sorted(
            {
                event_id
                for fact in card_facts
                if fact.get("semantic_role") == "trigger_observed"
                for event_id in event_ids_from_fact(fact)
            }
        )
        produced_event_ids = sorted(
            {
                event_id
                for fact in card_facts
                if fact.get("semantic_role") == "event_produced" or fact.get("fact_type") == "token_creation"
                for event_id in event_ids_from_fact(fact)
            }
        )
        output_ids = sorted({output_id for fact in card_facts for output_id in output_ids_from_fact(fact)})
        predicates = sorted({fact.get("predicate") for fact in card_facts if fact.get("predicate")})
        tags = [tag.get("name") if isinstance(tag, dict) else tag for tag in card.get("tags", []) or []]

        for domain in card.get("domain_ids", []) or []:
            filters["domains"][domain] += 1
        for card_type in card.get("card_type_ids", []) or []:
            filters["card_types"][card_type] += 1
        for tag in tags:
            filters["tags"][tag] += 1
        for keyword in keyword_ids:
            filters["keywords"][keyword] += 1
        for trigger in trigger_ids:
            filters["triggers"][trigger] += 1
        for event_id in produced_event_ids:
            filters["produced_events"][event_id] += 1
        for output_id in output_ids:
            filters["outputs"][output_id] += 1
        for predicate in predicates:
            filters["predicates"][predicate] += 1
        for stat in ("energy", "might", "power"):
            if card.get(stat) is not None:
                filters[stat][str(card.get(stat))] += 1

        compact_outgoing = [
            compact_relation(row, variant_play_ids, broad_reasons)
            for row in sorted(outgoing, key=lambda item: (-item.get("strength", 0), item.get("target_card_name") or ""))
        ]
        outgoing_quality = relation_quality_counts(outgoing, broad_reasons)
        incoming_quality = relation_quality_counts(incoming, broad_reasons)
        rule_variants = card.get("rule_variants", []) or []
        relation_shard = shard_index(play_id, shard_count)
        relation_shards[relation_shard]["cards"][play_id] = {"outgoing": compact_outgoing}

        web_cards.append(
            {
                "play_id": play_id,
                "name": card.get("name"),
                "public_codes": card.get("public_codes", []),
                "collector_numbers": card.get("collector_numbers", []),
                "sets": card.get("sets", []),
                "rarity_ids": card.get("rarity_ids", []),
                "domains": card.get("domains", []),
                "domain_ids": card.get("domain_ids", []),
                "card_types": card.get("card_types", []),
                "card_type_ids": card.get("card_type_ids", []),
                "tags": tags,
                "energy": card.get("energy"),
                "might": card.get("might"),
                "power": card.get("power"),
                "might_bonus": card.get("might_bonus"),
                "rules_lines": card.get("rules_lines", []),
                "effect_lines": card.get("effect_lines", []),
                "image_url": image_url(card),
                "search_text": searchable_text(card, card_facts),
                "semantic": {
                    "keywords": keyword_ids,
                    "triggers": trigger_ids,
                    "produced_events": produced_event_ids,
                    "outputs": output_ids,
                    "predicates": predicates,
                    "variant_warning": {
                        "has_rule_variants": bool(rule_variants),
                        "rule_variant_count": len(rule_variants),
                        "message": "Rules text differs across printings; facts currently use the normalized primary text."
                        if rule_variants
                        else None,
                    },
                    "fact_counts": dict(Counter(fact.get("semantic_role") for fact in card_facts)),
                },
                "relations": {
                    "shard": shard_ref("relations", relation_shard),
                    "outgoing_counts": relation_counts(outgoing),
                    "incoming_counts": relation_counts(incoming),
                    "outgoing_high_signal_counts": outgoing_quality["high_signal_counts"],
                    "incoming_high_signal_counts": incoming_quality["high_signal_counts"],
                    "outgoing_broad_counts": outgoing_quality["broad_counts"],
                    "incoming_broad_counts": incoming_quality["broad_counts"],
                    "relation_count": outgoing_quality["relation_count"] + incoming_quality["relation_count"],
                    "high_signal_relation_count": outgoing_quality["high_signal_relation_count"] + incoming_quality["high_signal_relation_count"],
                    "broad_relation_count": outgoing_quality["broad_relation_count"] + incoming_quality["broad_relation_count"],
                    "broad_only": bool(
                        (outgoing_quality["relation_count"] + incoming_quality["relation_count"])
                        and not (outgoing_quality["high_signal_relation_count"] + incoming_quality["high_signal_relation_count"])
                    ),
                },
            }
        )

    payload = {
        "version": VERSION,
        "snapshot": {
            "date": SNAPSHOT_DATE,
            "quality_policy_version": quality_policy.get("version"),
            "thresholds": {
                "broad_relation_count_threshold": broad_threshold,
                "similarity": quality_policy.get("similarity", {}),
                "legacy_rule_count_max": quality_policy.get("legacy_rule_count_max"),
            },
        },
        "sources": {
            "cards": repo_path(DEFAULT_CARDS),
            "facts": repo_path(DEFAULT_FACTS),
            "relations": repo_path(DEFAULT_RELATIONS),
            "quality_policy": repo_path(DEFAULT_QUALITY_POLICY),
        },
        "summary": {
            "card_count": len(web_cards),
            "fact_count": len(facts),
            "relation_count": len(relations),
            "high_signal_relation_count": sum(1 for relation in relations if not is_broad_relation(relation, broad_reasons)),
            "broad_relation_count": sum(1 for relation in relations if is_broad_relation(relation, broad_reasons)),
            "cards_with_rule_variants": len(variant_play_ids),
        },
        "manifest": {
            "relation_types": RELATION_TYPE_MANIFEST,
            "broad_policy": {
                "default_visible": False,
                "secondary_lane": True,
                "broad_reasons": sorted(broad_reasons),
            },
        },
        "filters": {key: filter_option(counter) for key, counter in filters.items()},
        "cards": sorted(web_cards, key=lambda item: item["name"] or ""),
    }

    relation_type_counts = Counter(relation.get("relation_type") for relation in relations)
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
    relations_by_card: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for relation in relations:
        relations_by_card[relation["source_play_id"]].append(relation)
        relations_by_card[relation["target_play_id"]].append(relation)
    cards_without_relations = sorted(
        card["play_id"]
        for card in cards
        if not outgoing_relations_by_card.get(card["play_id"]) and not incoming_relations_by_card.get(card["play_id"])
    )
    card_lines = {
        (card["play_id"], source_field, index): line
        for card in cards
        for source_field in ("rules_lines", "effect_lines")
        for index, line in enumerate(card.get(source_field, []) or [])
    }
    fact_line_keys = {
        (fact["play_id"], fact.get("source_ref", {}).get("source_field"), fact.get("source_ref", {}).get("line_index"))
        for fact in facts
        if fact.get("source_ref", {}).get("source_field") in {"rules_lines", "effect_lines"}
    }
    uncovered_relational_line_cards = sorted(
        {
            play_id
            for (play_id, source_field, index), line in card_lines.items()
            if (play_id, source_field, index) not in fact_line_keys
            if line_has_any_token(line, quality_policy.get("relational_keywords", []))
        }
    )
    bucket_counts = Counter()
    for card in cards:
        if card["play_id"] not in cards_without_relations:
            continue
        text = " ".join((card.get("rules_lines", []) or []) + (card.get("effect_lines", []) or []))
        bucket_counts[blind_spot_bucket(text, quality_policy)] += 1
    relation_shard_sizes = {shard_name(index): json_bytes(shard) for index, shard in relation_shards.items()}
    fact_shard_sizes = {shard_name(index): json_bytes(shard) for index, shard in fact_shards.items()}
    report = {
        "version": VERSION,
        "snapshot": payload["snapshot"],
        "inputs": payload["sources"],
        "summary": payload["summary"],
        "web_artifacts": {
            "shard_count": shard_count,
            "max_artifact_bytes": DEFAULT_MAX_ARTIFACT_BYTES,
            "index_bytes": json_bytes(payload),
            "largest_relation_shard_bytes": max(relation_shard_sizes.values(), default=0),
            "largest_relation_shard": max(relation_shard_sizes, key=relation_shard_sizes.get)
            if relation_shard_sizes
            else None,
            "largest_fact_shard_bytes": max(fact_shard_sizes.values(), default=0),
            "largest_fact_shard": max(fact_shard_sizes, key=fact_shard_sizes.get) if fact_shard_sizes else None,
            "relation_shard_bytes": relation_shard_sizes,
            "fact_shard_bytes": fact_shard_sizes,
        },
        "filter_option_counts": {key: len(value) for key, value in payload["filters"].items()},
        "by_relation_type": dict(relation_type_counts.most_common()),
        "cards_missing_facts": sorted(card["play_id"] for card in cards if not facts_by_card.get(card["play_id"])),
        "facts_by_source_kind": dict(facts_by_source_kind.most_common()),
        "top_contract_rules": dict(contract_rules.most_common(40)),
        "contract_rule_coverage": {
            "contract_rule_count": facts_by_source_kind.get("contract_rule", 0),
            "legacy_rule_count": facts_by_source_kind.get("legacy_rule", 0),
            "legacy_rule_count_max": quality_policy.get("legacy_rule_count_max"),
            "legacy_rule_count_within_limit": (
                facts_by_source_kind.get("legacy_rule", 0) <= int(quality_policy.get("legacy_rule_count_max", 999999))
            ),
            "contract_share": round(facts_by_source_kind.get("contract_rule", 0) / len(facts), 4) if facts else 0.0,
        },
        "cards_without_relations": cards_without_relations,
        "cards_with_only_broad_relations": sorted(
            play_id
            for play_id, card_relations in relations_by_card.items()
            if card_relations and broad_reasons
            if all(is_broad_relation(relation, broad_reasons) for relation in card_relations)
        ),
        "cards_with_uncovered_relational_lines": uncovered_relational_line_cards,
        "top_broad_reasons": {
            reason: count
            for reason, count in relation_reason_counts.most_common(20)
            if reason in broad_reasons
        },
        "relation_coverage_by_bucket": dict(bucket_counts.most_common()),
    }
    return payload, relation_shards, fact_shards, report


def markdown_report(report: dict[str, Any]) -> str:
    lines = [
        "# Card Explorer Dataset Report",
        "",
        "Report for the sharded card explorer dataset rooted at `data/processed/web/card_explorer_index.json`.",
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
    lines.extend(["", "## Filter Option Counts", ""])
    for key, value in report["filter_option_counts"].items():
        lines.append(f"- {key}: {value}")
    if report.get("web_artifacts"):
        artifacts = report["web_artifacts"]
        lines.extend(["", "## Web Artifacts", ""])
        lines.append(f"- shard_count: {artifacts.get('shard_count')}")
        lines.append(f"- max_artifact_bytes: {artifacts.get('max_artifact_bytes')}")
        lines.append(f"- index_bytes: {artifacts.get('index_bytes')}")
        lines.append(
            f"- largest_relation_shard: {artifacts.get('largest_relation_shard')} "
            f"({artifacts.get('largest_relation_shard_bytes')} bytes)"
        )
        lines.append(
            f"- largest_fact_shard: {artifacts.get('largest_fact_shard')} "
            f"({artifacts.get('largest_fact_shard_bytes')} bytes)"
        )
    lines.extend(["", "## Relation Types", ""])
    for key, value in report["by_relation_type"].items():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Coverage", ""])
    lines.append(f"- cards_missing_facts: {len(report['cards_missing_facts'])}")
    lines.append(f"- cards_without_relations: {len(report['cards_without_relations'])}")
    lines.append(f"- cards_with_only_broad_relations: {len(report['cards_with_only_broad_relations'])}")
    lines.append(f"- cards_with_uncovered_relational_lines: {len(report['cards_with_uncovered_relational_lines'])}")
    lines.extend(["", "## Extraction Provenance", ""])
    for key, value in report.get("facts_by_source_kind", {}).items():
        lines.append(f"- {key}: {value}")
    if report.get("top_contract_rules"):
        lines.extend(["", "### Top Contract Rules", ""])
        for key, value in report["top_contract_rules"].items():
            lines.append(f"- {key}: {value}")
    if report["relation_coverage_by_bucket"]:
        lines.extend(["", "## Cards Without Relations By Bucket", ""])
        for key, value in report["relation_coverage_by_bucket"].items():
            lines.append(f"- {key}: {value}")
    if report["top_broad_reasons"]:
        lines.extend(["", "## Broad Relation Reasons", ""])
        for key, value in report["top_broad_reasons"].items():
            lines.append(f"- {key}: {value}")
    return "\n".join(lines) + "\n"


def artifact_sizes(
    index_payload: dict[str, Any],
    relation_shards: dict[int, dict[str, Any]],
    fact_shards: dict[int, dict[str, Any]],
) -> dict[str, int]:
    sizes = {"card_explorer_index.json": json_bytes(index_payload)}
    sizes.update({f"relations/{shard_name(index)}": json_bytes(payload) for index, payload in relation_shards.items()})
    sizes.update({f"facts/{shard_name(index)}": json_bytes(payload) for index, payload in fact_shards.items()})
    return sizes


def validate_artifact_sizes(sizes: dict[str, int], max_bytes: int) -> None:
    oversized = {path: size for path, size in sizes.items() if size > max_bytes}
    if oversized:
        details = ", ".join(f"{path}={size}" for path, size in sorted(oversized.items()))
        raise ValueError(f"Web artifact size limit exceeded ({max_bytes} bytes): {details}")


def write_sharded_dataset(
    index_path: Path,
    relation_dir: Path,
    fact_dir: Path,
    index_payload: dict[str, Any],
    relation_shards: dict[int, dict[str, Any]],
    fact_shards: dict[int, dict[str, Any]],
) -> None:
    index_path.parent.mkdir(parents=True, exist_ok=True)
    reset_directory(relation_dir)
    reset_directory(fact_dir)
    write_json(index_path, index_payload, pretty=False)
    for index, payload in sorted(relation_shards.items()):
        write_json(relation_dir / shard_name(index), payload, pretty=False)
    for index, payload in sorted(fact_shards.items()):
        write_json(fact_dir / shard_name(index), payload, pretty=False)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the aggregate dataset consumed by the card explorer frontend.")
    parser.add_argument("--cards", type=Path, default=DEFAULT_CARDS)
    parser.add_argument("--facts", type=Path, default=DEFAULT_FACTS)
    parser.add_argument("--relations", type=Path, default=DEFAULT_RELATIONS)
    parser.add_argument("--quality-policy", type=Path, default=DEFAULT_QUALITY_POLICY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Output path for the sharded dataset index.")
    parser.add_argument("--relations-dir", type=Path, default=DEFAULT_RELATION_SHARDS)
    parser.add_argument("--facts-dir", type=Path, default=DEFAULT_FACT_SHARDS)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MARKDOWN)
    parser.add_argument("--shard-count", type=int, default=DEFAULT_SHARD_COUNT)
    parser.add_argument("--max-artifact-mib", type=int, default=50)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.shard_count <= 0:
        raise ValueError("--shard-count must be positive")
    max_artifact_bytes = args.max_artifact_mib * 1024 * 1024
    cards = read_json(args.cards)
    facts = read_jsonl(args.facts)
    relations = read_jsonl(args.relations)
    contracts = load_contract_bundle(FEATURE_EXTRACTION_DIR / "contracts")
    quality_policy = contracts["quality_policy"] if args.quality_policy == DEFAULT_QUALITY_POLICY else read_json(args.quality_policy)
    index_payload, relation_shards, fact_shards, report = build_dataset(cards, facts, relations, quality_policy, args.shard_count)
    report["web_artifacts"]["max_artifact_bytes"] = max_artifact_bytes
    sizes = artifact_sizes(index_payload, relation_shards, fact_shards)
    validate_artifact_sizes(sizes, max_artifact_bytes)
    write_sharded_dataset(args.output, args.relations_dir, args.facts_dir, index_payload, relation_shards, fact_shards)
    write_json(args.report, report)
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.write_text(markdown_report(report), encoding="utf-8")
    print(f"Wrote web dataset index with {len(index_payload['cards'])} cards to {args.output}")
    print(f"Wrote {len(relation_shards)} relation shards to {args.relations_dir}")
    print(f"Wrote {len(fact_shards)} fact shards to {args.facts_dir}")
    print(f"Wrote report to {args.report}")


if __name__ == "__main__":
    main()
