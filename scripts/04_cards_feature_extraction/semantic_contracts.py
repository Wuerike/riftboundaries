import json
import re
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
CONTRACTS_DIR = SCRIPT_DIR / "contracts"

DEFAULT_ONTOLOGY = CONTRACTS_DIR / "semantic_ontology.json"
DEFAULT_EXTRACTION_RULES = CONTRACTS_DIR / "semantic_extraction_rules.json"
DEFAULT_RELATION_RULES = CONTRACTS_DIR / "semantic_relation_rules.json"
DEFAULT_QUALITY_POLICY = CONTRACTS_DIR / "semantic_quality_policy.json"
DEFAULT_CONTRACTS_SCHEMA = CONTRACTS_DIR / "semantic_contracts_schema.json"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_contract_bundle(contracts_dir: Path = CONTRACTS_DIR) -> dict[str, Any]:
    bundle = {
        "ontology": read_json(contracts_dir / DEFAULT_ONTOLOGY.name),
        "extraction_rules": read_json(contracts_dir / DEFAULT_EXTRACTION_RULES.name),
        "relation_rules": read_json(contracts_dir / DEFAULT_RELATION_RULES.name),
        "quality_policy": read_json(contracts_dir / DEFAULT_QUALITY_POLICY.name),
        "contracts_schema": read_json(contracts_dir / DEFAULT_CONTRACTS_SCHEMA.name),
    }
    validate_contract_bundle(bundle)
    return bundle


def ontology_values(ontology: dict[str, Any], key: str) -> set[str]:
    values = ontology.get(key, [])
    if isinstance(values, dict):
        return set(values)
    return {str(value) for value in values}


def _require_unique(items: list[dict[str, Any]], key: str, label: str) -> None:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for item in items:
        value = item.get(key)
        if not isinstance(value, str) or not value:
            raise ValueError(f"{label} item missing {key}: {item}")
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    if duplicates:
        raise ValueError(f"{label} has duplicate {key}: {sorted(duplicates)}")


def _compile_regexes(rules: list[dict[str, Any]], label: str) -> None:
    for rule in rules:
        pattern = rule.get("pattern")
        if not isinstance(pattern, str) or not pattern:
            raise ValueError(f"{label} rule {rule.get('rule_id')} is missing pattern")
        flags = re.I if "IGNORECASE" in rule.get("flags", []) else 0
        try:
            re.compile(pattern, flags)
        except re.error as exc:
            raise ValueError(f"{label} rule {rule.get('rule_id')} has invalid regex: {exc}") from exc


def iter_extraction_rules(extraction_rules: dict[str, Any]) -> list[dict[str, Any]]:
    rules = []
    for section in ("trigger_rules", "condition_rules", "cost_rules", "effect_rules", "reminder_rules"):
        section_rules = extraction_rules.get(section, [])
        if not isinstance(section_rules, list):
            raise ValueError(f"semantic_extraction_rules.{section} must be a list")
        rules.extend(section_rules)
    return rules


def iter_relation_rules(relation_rules: dict[str, Any]) -> list[dict[str, Any]]:
    rules = []
    for section in ("event_enables", "identity_event_relations", "direct_synergy"):
        section_rules = relation_rules.get(section, [])
        if not isinstance(section_rules, list):
            raise ValueError(f"semantic_relation_rules.{section} must be a list")
        rules.extend(section_rules)
    return rules


def _validate_fact_template(rule: dict[str, Any], ontology: dict[str, Any]) -> None:
    roles = ontology_values(ontology, "semantic_roles")
    fact_types = ontology_values(ontology, "fact_types")
    actions = ontology_values(ontology, "actions")
    events = ontology_values(ontology, "events")
    outputs = ontology_values(ontology, "outputs")
    for fact in rule.get("facts", []):
        role = fact.get("semantic_role")
        fact_type = fact.get("fact_type")
        predicate = fact.get("predicate")
        if role not in roles:
            raise ValueError(f"{rule['rule_id']} references unknown semantic role: {role}")
        if fact_type not in fact_types:
            raise ValueError(f"{rule['rule_id']} references unknown fact type: {fact_type}")
        if predicate not in actions:
            raise ValueError(f"{rule['rule_id']} references unknown action/predicate: {predicate}")
        payload = fact.get("payload", {})
        event = payload.get("event") if isinstance(payload, dict) else None
        if isinstance(event, dict) and isinstance(event.get("id"), str) and event["id"] not in events:
            raise ValueError(f"{rule['rule_id']} references unknown event id: {event['id']}")
        for output in payload.get("outputs", []) if isinstance(payload, dict) else []:
            if not isinstance(output, dict):
                continue
            output_id = output.get("id")
            action = output.get("action")
            if isinstance(output_id, str) and output_id and output_id not in outputs:
                raise ValueError(f"{rule['rule_id']} references unknown output id: {output_id}")
            if isinstance(action, str) and action and action not in actions:
                raise ValueError(f"{rule['rule_id']} references unknown output action: {action}")


def validate_contract_bundle(bundle: dict[str, Any]) -> None:
    ontology = bundle["ontology"]
    extraction_rules = bundle["extraction_rules"]
    relation_rules = bundle["relation_rules"]
    quality_policy = bundle["quality_policy"]

    for key in ("semantic_roles", "fact_types", "actions", "events", "outputs", "relation_types", "web_uses"):
        values = ontology.get(key)
        if not isinstance(values, list) or not values:
            raise ValueError(f"semantic_ontology.{key} must be a non-empty list")

    extraction = iter_extraction_rules(extraction_rules)
    relation = iter_relation_rules(relation_rules)
    _require_unique(extraction, "rule_id", "semantic_extraction_rules")
    _require_unique(relation, "rule_id", "semantic_relation_rules")
    _compile_regexes([rule for rule in extraction if "pattern" in rule], "semantic_extraction_rules")

    for rule in extraction:
        _validate_fact_template(rule, ontology)

    events = ontology_values(ontology, "events")
    relation_types = ontology_values(ontology, "relation_types")
    for rule in extraction:
        for event_id in rule.get("events", []) or []:
            if event_id not in events:
                raise ValueError(f"{rule['rule_id']} references unknown trigger event: {event_id}")
        if rule.get("event_id") and rule["event_id"] not in events:
            raise ValueError(f"{rule['rule_id']} references unknown event_id: {rule['event_id']}")

    for rule in relation_rules.get("event_enables", []):
        if rule.get("source_event") not in events:
            raise ValueError(f"{rule['rule_id']} references unknown source_event: {rule.get('source_event')}")
        if rule.get("target_event") not in events:
            raise ValueError(f"{rule['rule_id']} references unknown target_event: {rule.get('target_event')}")
        for relation_type in rule.get("relation_types", []):
            if relation_type not in relation_types:
                raise ValueError(f"{rule['rule_id']} references unknown relation type: {relation_type}")
    for rule in relation_rules.get("identity_event_relations", []):
        for relation_type in rule.get("relation_types", []):
            if relation_type not in relation_types:
                raise ValueError(f"{rule['rule_id']} references unknown relation type: {relation_type}")
        for selector_name in ("source_selector", "target_selector"):
            selector = rule.get(selector_name, {})
            if selector.get("event_id") and selector["event_id"] not in events:
                raise ValueError(f"{rule['rule_id']} references unknown {selector_name}.event_id: {selector['event_id']}")
        if rule.get("event_id") and rule["event_id"] not in events:
            raise ValueError(f"{rule['rule_id']} references unknown event_id: {rule['event_id']}")
    for rule in relation_rules.get("direct_synergy", []):
        relation_type = rule.get("relation_type")
        if relation_type and relation_type not in relation_types:
            raise ValueError(f"{rule['rule_id']} references unknown relation type: {relation_type}")
        for selector_name in ("source_selector", "target_selector"):
            selector = rule.get(selector_name, {})
            if selector.get("event_id") and selector["event_id"] not in events:
                raise ValueError(f"{rule['rule_id']} references unknown {selector_name}.event_id: {selector['event_id']}")
        for key in ("event_id", "target_event_id"):
            if rule.get(key) and rule[key] not in events:
                raise ValueError(f"{rule['rule_id']} references unknown {key}: {rule[key]}")

    if not isinstance(quality_policy.get("optional_governors"), list):
        raise ValueError("semantic_quality_policy.optional_governors must be a list")
    if not isinstance(quality_policy.get("blind_spot_buckets"), list):
        raise ValueError("semantic_quality_policy.blind_spot_buckets must be a list")
