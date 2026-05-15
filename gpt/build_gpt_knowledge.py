from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "gpt"
FOR_GPT_DIR = Path("for_gpt")
INSTRUCTIONS_DIR = FOR_GPT_DIR / "instructions"
KNOWLEDGE_DIR = FOR_GPT_DIR / "knowledge"
REPO_ONLY_DIR = Path("repo_only")

CARDS_PATH = PROJECT_ROOT / "data" / "processed" / "cards" / "normalized" / "cards_normalized.json"
RULES_PATH = PROJECT_ROOT / "data" / "processed" / "rules" / "core-rules.json"
FACTS_PATH = PROJECT_ROOT / "data" / "processed" / "cards" / "semantic" / "cards_semantic_facts.jsonl"
RELATIONS_PATH = PROJECT_ROOT / "data" / "processed" / "cards" / "relations" / "cards_card_relations.jsonl"
SEMANTIC_AUDIT_PATH = PROJECT_ROOT / "data" / "processed" / "cards" / "semantic" / "cards_semantic_audit_report.json"
WEB_DATASET_REPORT_PATH = PROJECT_ROOT / "data" / "processed" / "web" / "card_explorer_dataset_report.json"
WEB_QUALITY_REPORT_PATH = PROJECT_ROOT / "data" / "processed" / "web" / "card_explorer_quality_report.json"
WEB_INDEX_PATH = PROJECT_ROOT / "data" / "processed" / "web" / "card_explorer_index.json"
QUALITY_POLICY_PATH = (
    PROJECT_ROOT
    / "scripts"
    / "04_cards_feature_extraction"
    / "contracts"
    / "semantic_quality_policy.json"
)

WARN_BYTES = 750 * 1024
FAIL_BYTES = int(1.5 * 1024 * 1024)
FACTS_PER_CARD = 8
RELATIONS_PER_CARD = 8
MAX_GPT_KNOWLEDGE_FILES = 10

PACKAGE_FILES = [
    "instructions",
    "manifest",
    "rules",
    "cards_a_f",
    "cards_g_m",
    "cards_n_s",
    "cards_t_z",
    "mechanics",
    "semantic",
    "relations",
    "limitations",
    "playbooks",
    "evaluations",
]

FILE_TARGETS = {
    "instructions": INSTRUCTIONS_DIR / "00_gpt_instructions.md",
    "manifest": KNOWLEDGE_DIR / "00_manifest.md",
    "rules": KNOWLEDGE_DIR / "01_official_rules_reference.md",
    "cards_a_f": KNOWLEDGE_DIR / "02_official_cards_reference_a_f.md",
    "cards_g_m": KNOWLEDGE_DIR / "03_official_cards_reference_g_m.md",
    "cards_n_s": KNOWLEDGE_DIR / "04_official_cards_reference_n_s.md",
    "cards_t_z": KNOWLEDGE_DIR / "05_official_cards_reference_t_z.md",
    "mechanics": KNOWLEDGE_DIR / "06_mechanics_and_terms.md",
    "semantic": KNOWLEDGE_DIR / "07_derived_semantic_index.md",
    "relations": KNOWLEDGE_DIR / "08_inferred_relations_index.md",
    "limitations": KNOWLEDGE_DIR / "09_known_limitations.md",
    "playbooks": REPO_ONLY_DIR / "00_answer_playbooks.md",
    "evaluations": REPO_ONLY_DIR / "01_evaluation_questions.md",
}

DEFAULT_UPLOAD_FILES = [
    "for_gpt/knowledge/00_manifest.md",
    "for_gpt/knowledge/01_official_rules_reference.md",
    "for_gpt/knowledge/02_official_cards_reference_a_f.md",
    "for_gpt/knowledge/03_official_cards_reference_g_m.md",
    "for_gpt/knowledge/04_official_cards_reference_n_s.md",
    "for_gpt/knowledge/05_official_cards_reference_t_z.md",
    "for_gpt/knowledge/06_mechanics_and_terms.md",
    "for_gpt/knowledge/07_derived_semantic_index.md",
    "for_gpt/knowledge/08_inferred_relations_index.md",
    "for_gpt/knowledge/09_known_limitations.md",
]

CARD_SHARDS = {
    "cards_a_f": ("A-F", "Official Cards Reference A-F"),
    "cards_g_m": ("G-M", "Official Cards Reference G-M"),
    "cards_n_s": ("N-S", "Official Cards Reference N-S"),
    "cards_t_z": ("T-Z", "Official Cards Reference T-Z"),
}

FUNCTIONAL_ROLE_ORDER = {
    "trigger_observed": 0,
    "cost_or_requirement": 1,
    "restriction_or_permission": 2,
    "event_produced": 3,
    "payoff_output": 4,
    "state_or_modifier": 5,
    "targeting_or_scope": 6,
    "identity_or_descriptor": 20,
    None: 30,
    "": 30,
}

RELATION_LABELS = {
    "enables": "Enabled Cards",
    "enabled_by": "Enablers",
    "similar_effect": "Similar Effects",
    "deck_synergy": "Deck Synergy",
}


def repo_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def md_line(value: Any) -> str:
    text = "" if value is None else str(value)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def inline(value: Any, fallback: str = "None") -> str:
    if value is None:
        return fallback
    if isinstance(value, list):
        values = [inline(item, "") for item in value if inline(item, "")]
        return ", ".join(values) if values else fallback
    if isinstance(value, dict):
        return inline(value.get("name") or value.get("id") or value, fallback)
    text = md_line(value)
    return text if text else fallback


def list_names(items: list[dict[str, Any]] | list[str] | None) -> str:
    if not items:
        return "None"
    values = []
    for item in items:
        if isinstance(item, dict):
            values.append(str(item.get("name") or item.get("id") or item))
        else:
            values.append(str(item))
    return ", ".join(values) if values else "None"


def bullet_lines(items: list[str], empty: str = "- None") -> list[str]:
    if not items:
        return [empty]
    return [f"- {md_line(item)}" for item in items]


def truncate(text: Any, limit: int = 180) -> str:
    value = md_line(text)
    if len(value) <= limit:
        return value
    return value[: limit - 3].rstrip() + "..."


def first_letter_bucket(name: str) -> str:
    first = name[:1].upper()
    if "A" <= first <= "F":
        return "A-F"
    if "G" <= first <= "M":
        return "G-M"
    if "N" <= first <= "S":
        return "N-S"
    return "T-Z"


def card_sort_key(card: dict[str, Any]) -> tuple[str, str]:
    return (str(card.get("name") or "").lower(), str(card.get("play_id") or ""))


def render_card(card: dict[str, Any]) -> list[str]:
    lines = [
        f"## [official-card] {card['name']}",
        "",
        "Identity:",
        f"- play_id: `{card.get('play_id')}`",
        f"- canonical_printing_id: `{card.get('canonical_printing_id')}`",
        f"- domains: {list_names(card.get('domains'))}",
        f"- card_types: {list_names(card.get('card_types'))}",
        f"- supertypes: {list_names(card.get('supertypes'))}",
        f"- tags: {list_names(card.get('tags'))}",
        "",
        "Printed references:",
        f"- public_codes: {inline(card.get('public_codes'))}",
        f"- sets: {list_names(card.get('sets'))}",
        f"- rarities: {list_names(card.get('rarities'))}",
        "",
        "Game stats:",
        f"- energy: {inline(card.get('energy'))}",
        f"- might: {inline(card.get('might'))}",
        f"- power: {inline(card.get('power'))}",
        f"- might_bonus: {inline(card.get('might_bonus'))}",
        "",
        "Official rules text:",
    ]
    lines.extend(bullet_lines(card.get("rules_lines") or []))
    lines.extend(["", "Official effect text:"])
    lines.extend(bullet_lines(card.get("effect_lines") or []))
    lines.extend(["", "Rule text variants:"])
    variants = card.get("rule_variants") or []
    if not variants:
        lines.append("- None")
    else:
        for variant in variants:
            refs = inline(variant.get("public_codes"))
            variant_lines = variant.get("rules_lines") or []
            effect_lines = variant.get("effect_lines") or []
            lines.append(f"- refs: {refs}")
            for item in variant_lines:
                lines.append(f"  - rules: {md_line(item)}")
            for item in effect_lines:
                lines.append(f"  - effect: {md_line(item)}")
    lines.append("")
    return lines


def render_rules(rules_payload: dict[str, Any]) -> str:
    rules = rules_payload.get("rules", [])
    by_section: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for rule in rules:
        by_section[str(rule.get("section_id") or rule.get("id") or "")].append(rule)

    lines = [
        "# Official Core Rules Reference",
        "",
        "## How To Use This File",
        "",
        "[official-rule] This file is the primary source for general rulings. If a question involves a specific card, compare the general rule here with the official card text and apply the Golden Rule when they conflict.",
        "",
        "## Section Index",
        "",
    ]
    for section_id in sorted(by_section, key=lambda item: [int(part) if part.isdigit() else part for part in item.split(".")]):
        first = by_section[section_id][0]
        title = first.get("section_title") or first.get("text") or section_id
        lines.append(f"- {section_id}: {md_line(title)}")
    lines.extend(["", "## Rules", ""])

    for rule in rules:
        rule_id = str(rule.get("id") or "")
        title = rule.get("section_title") or rule.get("text") or ""
        heading = truncate(title, 90)
        lines.extend(
            [
                f"### [official-rule] {rule_id} - {heading}",
                "",
                f"- parent_rule: {inline(rule.get('parent_id'))}",
                f"- section_id: {inline(rule.get('section_id'))}",
                f"- page: {inline(rule.get('page_start'))}"
                + (f"-{rule.get('page_end')}" if rule.get("page_end") != rule.get("page_start") else ""),
                f"- source: {inline(rule.get('source'))}",
                "",
                "Official rule text:",
                "",
                f"> {md_line(rule.get('text'))}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def render_cards_reference(filename: str, title: str, cards: list[dict[str, Any]]) -> str:
    lines = [
        f"# {title}",
        "",
        "[official-card] This file contains official normalized card identity, stats, rules text, effect text, and rule text variants only. It intentionally excludes derived semantic facts and inferred relations.",
        "",
    ]
    if filename == "cards_t_z":
        lines.extend(["## Other Names", "", "Names starting with symbols or numbers are included in this T-Z shard.", ""])
    for card in cards:
        lines.extend(render_card(card))
    return "\n".join(lines).rstrip() + "\n"


def fact_keyword_label(fact: dict[str, Any]) -> str | None:
    payload = fact.get("payload") or {}
    obj = payload.get("object") if isinstance(payload, dict) else None
    if isinstance(obj, dict):
        return str(obj.get("label") or obj.get("id") or "")
    return None


def render_mechanics_and_terms(
    cards: list[dict[str, Any]],
    facts: list[dict[str, Any]],
    rules: list[dict[str, Any]],
) -> str:
    keyword_cards: dict[str, set[str]] = defaultdict(set)
    keyword_labels: dict[str, str] = {}
    for fact in facts:
        if fact.get("predicate") != "has_keyword":
            continue
        label = fact_keyword_label(fact)
        if not label:
            continue
        key = label.lower().replace(" ", "_")
        keyword_labels[key] = label
        keyword_cards[key].add(str(fact.get("card_name") or ""))

    rule_text_by_id = {str(rule.get("id")): str(rule.get("text") or "") for rule in rules}
    lines = [
        "# Mechanics And Terms",
        "",
        "[editorial] This file is a terminology aid. Verify rules-sensitive answers against `for_gpt/knowledge/01_official_rules_reference.md` and the official card reference shards.",
        "",
        "## Keywords",
        "",
    ]
    for key in sorted(keyword_cards):
        label = keyword_labels.get(key, key)
        matching_rules = [
            rule_id
            for rule_id, text in rule_text_by_id.items()
            if re.search(rf"\b{re.escape(label)}\b", text, flags=re.IGNORECASE)
        ][:8]
        examples = sorted(name for name in keyword_cards[key] if name)[:10]
        lines.extend(
            [
                f"### [official-card] {label}",
                "",
                f"- observed_card_count: {len(keyword_cards[key])}",
                f"- related_rules: {inline(matching_rules)}",
                f"- example_cards: {inline(examples)}",
                "",
            ]
        )

    resources = ["energy", "rune", "runes", "power", "might", "XP"]
    zones = ["base", "battlefield", "board", "hand", "main deck", "rune deck", "trash", "banishment"]
    actions = ["play", "move", "attack", "defend", "conquer", "hold", "score", "draw", "discard", "recycle", "banish", "kill", "stun", "ready", "exhaust"]

    def render_terms(title: str, terms: list[str]) -> None:
        lines.extend([f"## {title}", ""])
        for term in terms:
            rule_matches = [
                rule_id
                for rule_id, text in rule_text_by_id.items()
                if re.search(rf"\b{re.escape(term)}\b", text, flags=re.IGNORECASE)
            ][:8]
            card_matches = [
                str(card.get("name"))
                for card in cards
                if term.lower() in " ".join(card.get("rules_lines") or []).lower()
            ][:8]
            tag = "[official-rule]" if rule_matches else "[official-card]"
            lines.extend(
                [
                    f"### {tag} {term}",
                    "",
                    f"- related_rules: {inline(rule_matches)}",
                    f"- example_cards: {inline(card_matches)}",
                    "",
                ]
            )

    render_terms("Resources", resources)
    render_terms("Zones", zones)
    render_terms("Actions", actions)
    lines.extend(
        [
            "## Internal Naming Notes",
            "",
            "[editorial] Internal IDs may use snake_case, while official card and rule text may use printed terminology. Prefer official wording in answers and mention internal IDs only when explaining how this package was built.",
            "",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def render_answer_playbooks() -> str:
    return """# Answer Playbooks

## [editorial] Rules Question Playbook

- Start from `for_gpt/knowledge/01_official_rules_reference.md`.
- If the question names one or more cards, verify every named card in the official card reference shards before concluding.
- If a card contradicts a general rule, apply the Golden Rule and explain that the card text controls that case.
- Do not cite derived facts or inferred relations as ruling authority.

## [editorial] Card Question Playbook

- Start from the relevant official card reference shard for every named card.
- Report identity, stats, and official rules/effect text from `[official-card]` sections.
- Mention rule text variants when they exist.
- Use rules only to explain terminology or timing.
- Do not answer with hypothetical wording such as "if this card costs..." when the named card exists in the official reference. Look up the card and answer from its text.

## [editorial] Synergy Question Playbook

- Start with official card text for every named card.
- For interactions involving equipment, costs, reducers, targets, replacement effects, or triggers, retrieve both the acting card and the affected card before giving the line of play.
- Use `for_gpt/knowledge/07_derived_semantic_index.md` for discovery and `for_gpt/knowledge/08_inferred_relations_index.md` for suggestions.
- Label suggestions as inferred, pipeline-suggested, or likely synergy.
- Tell the user when no official evidence establishes a rules interaction.

## [editorial] Gameplay And List Question Playbook

- Separate legal/rules claims from strategy suggestions.
- Use derived and inferred files only as discovery layers.
- Avoid metagame claims unless they are present in an official or explicitly provided source.

## [editorial] Uncertainty Examples

- There is not enough official evidence in this package to confirm that interaction.
- The relation index suggests these cards may work together, but that relation is inferred and should be verified against official card text.
- I can identify the relevant rule and card text, but I cannot resolve an unstated tournament or judge interpretation from this package alone.

## [editorial] Citation Examples

- For a ruling: cite `[official-rule] {rule_id}` and the relevant `[official-card] {card_name}` section.
- For card text: cite the official card shard and public code.
- For synergy: cite official cards first, then label any `[derived-fact]` or `[inferred-relation]` support as auxiliary.
"""


def fact_rank(fact: dict[str, Any]) -> tuple[int, int, float, int, str]:
    role = fact.get("semantic_role")
    source_ref = fact.get("source_ref") or {}
    source_kind = (fact.get("extractor") or {}).get("source_kind")
    structural_penalty = 5 if source_kind == "structural_field" else 0
    line_index = source_ref.get("line_index")
    if line_index is None:
        line_index = 999
    return (
        FUNCTIONAL_ROLE_ORDER.get(role, 15) + structural_penalty,
        int(line_index),
        -float(fact.get("confidence") or 0),
        len(str(fact.get("evidence") or "")),
        str(fact.get("fact_id") or ""),
    )


def is_functional_fact(fact: dict[str, Any]) -> bool:
    return FUNCTIONAL_ROLE_ORDER.get(fact.get("semantic_role"), 15) < 20


def render_fact_line(fact: dict[str, Any]) -> str:
    source_ref = fact.get("source_ref") or {}
    parts = [
        f"predicate `{inline(fact.get('predicate'))}`",
        f"role `{inline(fact.get('semantic_role'))}`",
        f"type `{inline(fact.get('fact_type'))}`",
        f"confidence {inline(fact.get('confidence'))}",
    ]
    evidence = truncate(fact.get("evidence") or source_ref.get("line_text"), 220)
    return f"- {'; '.join(parts)}; evidence: {evidence}"


def render_derived_semantic_index(cards: list[dict[str, Any]], facts: list[dict[str, Any]]) -> str:
    facts_by_card: dict[str, list[dict[str, Any]]] = defaultdict(list)
    facts_by_role: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for fact in facts:
        facts_by_card[str(fact.get("play_id"))].append(fact)
        facts_by_role[str(fact.get("semantic_role") or "unknown")].append(fact)

    lines = [
        "# Derived Semantic Index",
        "",
        "## Use Policy",
        "",
        "[derived-fact] This file is derived from official text. Use it for discovery and recall. Verify rules-sensitive answers against official card text and official rules.",
        "",
        "## By Card",
        "",
    ]
    for card in sorted(cards, key=card_sort_key):
        card_facts = sorted(facts_by_card.get(str(card.get("play_id")), []), key=fact_rank)
        functional = [fact for fact in card_facts if is_functional_fact(fact)]
        if functional:
            selected = functional[:FACTS_PER_CARD]
            if len(selected) < FACTS_PER_CARD:
                selected.extend([fact for fact in card_facts if fact not in selected][: FACTS_PER_CARD - len(selected)])
        else:
            selected = card_facts[:FACTS_PER_CARD]

        lines.extend(
            [
                f"### [derived-fact] {card['name']}",
                "",
                f"- official_card: {card['name']} (`{card.get('play_id')}`)",
                "- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.",
                "",
                "Derived facts:",
            ]
        )
        lines.extend(render_fact_line(fact) for fact in selected)
        if not selected:
            lines.append("- None")
        lines.append("")

    lines.extend(["## By Semantic Role", ""])
    for role in sorted(facts_by_role):
        role_facts = facts_by_role[role]
        card_counts = Counter(str(fact.get("card_name") or fact.get("play_id")) for fact in role_facts)
        examples = [f"{name} ({count})" for name, count in card_counts.most_common(30)]
        lines.extend(
            [
                f"### [derived-fact] {role}",
                "",
                f"- fact_count: {len(role_facts)}",
                f"- example_cards: {inline(examples)}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def relation_reason(relation: dict[str, Any]) -> str:
    match = relation.get("match") or {}
    return str(match.get("reason") or match.get("rule_id") or "")


def load_broad_reasons(relations: list[dict[str, Any]], quality_policy: dict[str, Any], web_index: dict[str, Any], dataset_report: dict[str, Any]) -> set[str]:
    broad_reasons: set[str] = set()
    broad_reasons.update((dataset_report.get("top_broad_reasons") or {}).keys())
    manifest_broad = (((web_index.get("manifest") or {}).get("broad_policy") or {}).get("broad_reasons") or [])
    broad_reasons.update(str(item) for item in manifest_broad)
    threshold = int(quality_policy.get("broad_relation_count_threshold") or 500)
    reason_counts = Counter(relation_reason(relation) for relation in relations)
    broad_reasons.update(reason for reason, count in reason_counts.items() if reason and count >= threshold)
    broad_reasons.update(
        relation_reason(relation)
        for relation in relations
        if (relation.get("match") or {}).get("broad") or (relation.get("match") or {}).get("broad_reason")
    )
    return {reason for reason in broad_reasons if reason}


def is_broad_relation(relation: dict[str, Any], broad_reasons: set[str]) -> bool:
    match = relation.get("match") or {}
    return bool(match.get("broad")) or bool(match.get("broad_reason")) or relation_reason(relation) in broad_reasons


def relation_sort_key(relation: dict[str, Any]) -> tuple[float, str, str]:
    return (-float(relation.get("strength") or 0), str(relation.get("relation_type") or ""), str(relation.get("target_card_name") or ""))


def render_relation_line(relation: dict[str, Any], current_play_id: str | None = None) -> str:
    source_name = str(relation.get("source_card_name") or relation.get("source_play_id") or "")
    target_name = str(relation.get("target_card_name") or relation.get("target_play_id") or "")
    if current_play_id and relation.get("target_play_id") == current_play_id:
        direction = "in"
        other = source_name
    elif current_play_id and relation.get("source_play_id") == current_play_id:
        direction = "out"
        other = target_name
    else:
        direction = "pair"
        other = f"{source_name} -> {target_name}"
    reason = relation_reason(relation)
    return (
        f"- {direction}: {other}; type `{inline(relation.get('relation_type'))}`; "
        f"strength {inline(relation.get('strength'))}; reason `{truncate(reason, 90)}`"
    )


def render_inferred_relations_index(
    cards: list[dict[str, Any]],
    relations: list[dict[str, Any]],
    broad_reasons: set[str],
    include_broad_relations: bool,
    web_index: dict[str, Any],
) -> str:
    card_ids = {str(card.get("play_id")) for card in cards}
    high_by_card: dict[str, list[dict[str, Any]]] = defaultdict(list)
    deck_by_card: dict[str, list[dict[str, Any]]] = defaultdict(list)
    broad_relations: list[dict[str, Any]] = []
    relation_type_counts = Counter(str(relation.get("relation_type")) for relation in relations)
    broad_reason_counts = Counter()

    for relation in relations:
        if str(relation.get("source_play_id")) not in card_ids or str(relation.get("target_play_id")) not in card_ids:
            continue
        broad = is_broad_relation(relation, broad_reasons)
        if broad:
            broad_relations.append(relation)
            broad_reason_counts[relation_reason(relation)] += 1
            if not include_broad_relations:
                continue
        if relation.get("relation_type") == "deck_synergy":
            deck_by_card[str(relation.get("source_play_id"))].append(relation)
            deck_by_card[str(relation.get("target_play_id"))].append(relation)
        elif not broad:
            high_by_card[str(relation.get("source_play_id"))].append(relation)
            high_by_card[str(relation.get("target_play_id"))].append(relation)

    web_relation_types = ((web_index.get("manifest") or {}).get("relation_types") or {})
    lines = [
        "# Inferred Relations Index",
        "",
        "## Use Policy",
        "",
        "[inferred-relation] Relations are pipeline inferences. Use them for discovery, synergy, comparison, and list-building suggestions. Verify rules-sensitive answers against official cards and official rules.",
        "",
        "## Relation Types",
        "",
    ]
    for relation_type in sorted(relation_type_counts):
        metadata = web_relation_types.get(relation_type) or {}
        label = metadata.get("label") or RELATION_LABELS.get(relation_type, relation_type)
        lane = metadata.get("lane") or ("experimental" if relation_type == "deck_synergy" else "high_signal")
        default_visible = metadata.get("default_visible")
        experimental = bool(metadata.get("experimental")) or relation_type == "deck_synergy"
        lines.extend(
            [
                f"### [inferred-relation] {relation_type}",
                "",
                f"- label: {label}",
                f"- count: {relation_type_counts[relation_type]}",
                f"- lane: {lane}",
                f"- default_visible: {default_visible}",
                f"- experimental: {experimental}",
                "",
            ]
        )

    lines.extend(["## High-Signal Relations By Card", ""])
    for card in sorted(cards, key=card_sort_key):
        selected = sorted(high_by_card.get(str(card.get("play_id")), []), key=relation_sort_key)[:RELATIONS_PER_CARD]
        if not selected:
            continue
        lines.extend(
            [
                f"### [inferred-relation] {card['name']}",
                "",
                "- authority_note: pipeline-suggested relations only; never official ruling authority.",
                "",
                "Pipeline-suggested related cards:",
            ]
        )
        lines.extend(render_relation_line(relation, str(card.get("play_id"))) for relation in selected)
        lines.append("")

    lines.extend(["## Broad Or Low-Confidence Relations", ""])
    lines.append("[quality-warning] Broad relations are omitted from per-card blocks in the default GPT package. They are summarized here for audit context.")
    lines.append("")
    lines.append(f"- broad_relation_count: {len(broad_relations)}")
    lines.append(f"- broad_reasons: {inline([f'{reason} ({count})' for reason, count in broad_reason_counts.most_common(20)])}")
    lines.append("")
    if include_broad_relations:
        lines.extend(["### [inferred-relation] Broad Relation Examples", ""])
        for relation in sorted(broad_relations, key=relation_sort_key)[:100]:
            lines.append(render_relation_line(relation))
        lines.append("")

    lines.extend(["## Experimental Deck Synergy", ""])
    lines.append("[inferred-relation] `deck_synergy` is experimental and default hidden when the dataset manifest marks it that way.")
    lines.append("")
    for card in sorted(cards, key=card_sort_key):
        selected = sorted(deck_by_card.get(str(card.get("play_id")), []), key=relation_sort_key)[:RELATIONS_PER_CARD]
        if not selected:
            continue
        lines.extend([f"### [inferred-relation] {card['name']}", ""])
        lines.extend(render_relation_line(relation, str(card.get("play_id"))) for relation in selected)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_known_limitations(semantic_audit: dict[str, Any], dataset_report: dict[str, Any], web_quality: dict[str, Any]) -> str:
    semantic_summary = semantic_audit.get("summary") or {}
    dataset_summary = dataset_report.get("summary") or {}
    quality_summary = web_quality.get("summary") or {}
    issue_counts = semantic_audit.get("issue_counts") or {}
    top_broad = dataset_report.get("top_broad_reasons") or {}
    lines = [
        "# Known Limitations",
        "",
        "## [quality-warning] Official Sources Are Primary",
        "",
        "Use official rules and official card references as final authority. Derived semantic facts and inferred relations are auxiliary.",
        "",
        "## [quality-warning] Derived Semantic Limits",
        "",
        f"- fact_count: {inline(semantic_summary.get('fact_count'))}",
        f"- text_line_fact_coverage: {inline(semantic_summary.get('text_line_fact_coverage'))}",
        f"- warning_count: {inline(semantic_summary.get('warning_count'))}",
        f"- legacy_rule_count: {inline(semantic_summary.get('legacy_rule_count'))}",
        f"- issue_counts: {inline([f'{key}: {value}' for key, value in issue_counts.items()])}",
        "",
        "## [quality-warning] Inferred Relation Limits",
        "",
        f"- relation_count: {inline(dataset_summary.get('relation_count'))}",
        f"- high_signal_relation_count: {inline(dataset_summary.get('high_signal_relation_count'))}",
        f"- broad_relation_count: {inline(dataset_summary.get('broad_relation_count'))}",
        f"- top_broad_reasons: {inline([f'{key}: {value}' for key, value in top_broad.items()])}",
        "",
        "## [quality-warning] Current Quality Snapshot",
        "",
        f"- cards_without_relations: {inline(quality_summary.get('cards_without_relations'))}",
        f"- cards_with_only_broad_relations: {inline(quality_summary.get('cards_with_only_broad_relations'))}",
        f"- cards_with_rule_variants: {inline(quality_summary.get('cards_with_rule_variants'))}",
        f"- broad_relation_share: {inline(quality_summary.get('broad_relation_share'))}",
        "",
        "## [quality-warning] Cards And Patterns Requiring Caution",
        "",
        "- Cards with rule text variants require checking the official card shard before answering.",
        "- Facts are not programmatically linked to specific official rule IDs.",
        "- Relation strength is a pipeline signal, not proof of a legal interaction.",
        "",
        "## [quality-warning] Uncertainty Response Policy",
        "",
        "- Say there is not enough official evidence when rules or card text do not establish the requested conclusion.",
        "- For inferred synergy, say the relation is pipeline-suggested and verify against official text.",
        "- Do not turn audit warnings or relation reports into primary answer content.",
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


def render_evaluation_questions() -> str:
    return """# Evaluation Questions

[editorial] Use these questions after uploading the package to a custom GPT. They are not part of the default Knowledge upload profile unless there is spare file capacity.

## [editorial] 1. Golden Rule Ruling

Question: If official card text contradicts a general rule, which source controls the specific case?

Expected answer: The specific official card text controls that case under the Golden Rule, while general rules remain the default authority otherwise.

Sources that should be used: `for_gpt/knowledge/01_official_rules_reference.md`, especially `[official-rule] 002`; relevant `[official-card]` section if a card is named.

Sources that should not be used as authority: `for_gpt/knowledge/07_derived_semantic_index.md`, `for_gpt/knowledge/08_inferred_relations_index.md`.

Failure condition: The answer says rules always beat card text or treats a derived fact as official authority.

## [editorial] 2. Specific Card Text

Question: What does Abandon do?

Expected answer: Report Abandon's official card text, including Reaction, countering a spell, returning it to hand instead of trash, and Predict if present in the official shard.

Sources that should be used: `for_gpt/knowledge/02_official_cards_reference_a_f.md`.

Sources that should not be used as authority: relation suggestions, semantic summaries.

Failure condition: The answer omits official text, invents a ruling, or cites inferred relations as the source.

## [editorial] 3. Rules Term

Question: What does "Reaction" mean in this package?

Expected answer: Explain from official card/rule text where available, and state that rules-sensitive timing should be checked against official rules and the relevant card text.

Sources that should be used: `for_gpt/knowledge/01_official_rules_reference.md`, `for_gpt/knowledge/06_mechanics_and_terms.md`, official card shards with Reaction examples.

Sources that should not be used as authority: inferred relations.

Failure condition: The answer gives strategy-only advice or treats the mechanics glossary as stronger than official rules.

## [editorial] 4. Synergy Discovery

Question: What cards might work with Alpha Strike?

Expected answer: Use official Alpha Strike text first, then label any related cards from the relation index as pipeline-suggested or inferred synergy.

Sources that should be used: official card shard for Alpha Strike, `for_gpt/knowledge/08_inferred_relations_index.md`, and `for_gpt/knowledge/07_derived_semantic_index.md` only for discovery.

Sources that should not be used as authority: broad relations as rulings, audit reports as primary answer content.

Failure condition: The answer says the synergy is an official rule or hides that the relation is inferred.

## [editorial] 5. Card Comparison

Question: Compare Abandon and Not So Fast.

Expected answer: Compare official card text, stats, and conditions from their official card sections. Similarity or relation data may be mentioned only as auxiliary.

Sources that should be used: `for_gpt/knowledge/02_official_cards_reference_a_f.md`, `for_gpt/knowledge/04_official_cards_reference_n_s.md`, `for_gpt/knowledge/08_inferred_relations_index.md` only if clearly labeled.

Sources that should not be used as authority: `deck_synergy` as a ruling source.

Failure condition: The answer compares only inferred relation fields and skips official card text.

## [editorial] 6. List-Building

Question: Suggest cards for an XP-focused list.

Expected answer: Separate rules/card-text facts from strategy suggestions. Mention that recommendations from semantic facts or inferred relations are auxiliary.

Sources that should be used: official card shards, `for_gpt/knowledge/07_derived_semantic_index.md`, `for_gpt/knowledge/08_inferred_relations_index.md`.

Sources that should not be used as authority: unsupported metagame claims.

Failure condition: The answer claims tournament performance or metagame strength not present in the package.

## [editorial] 7. Inference Versus Official Rule

Question: If the relation index links a counterspell to many spells, does that prove those spells are always countered?

Expected answer: No. The relation is inferred discovery data. The actual interaction depends on official spell text, official counterspell text, and rules.

Sources that should be used: `for_gpt/knowledge/08_inferred_relations_index.md` for the relation label, then official card shards and `for_gpt/knowledge/01_official_rules_reference.md`.

Sources that should not be used as authority: broad relation counts.

Failure condition: The answer treats `spell_card_can_be_countered` or any broad relation as an official rule.

## [editorial] 8. Insufficient Evidence

Question: Does this package prove a specific inferred synergy is legal in every game state?

Expected answer: No. It can identify official text and inferred relation evidence, but it must say there is not enough official evidence for unstated game states.

Sources that should be used: `for_gpt/knowledge/09_known_limitations.md`, official rules, official card shards.

Sources that should not be used as authority: relation strength alone.

Failure condition: The answer overstates confidence or fails to communicate uncertainty.

## [editorial] 9. Named Multi-Card Cost Check

Question: I have Doran's Blade in play and Lucian, Merciless in hand, with runes to pay Lucian. What play can I make, and does Weaponmaster make Doran's Blade's equip cost zero?

Expected answer: Retrieve both official card sections before answering. State Lucian, Merciless has Weaponmaster and Doran's Blade has its official Equip cost. Explain the discount using the retrieved texts, not a hypothetical "if Doran's Blade costs...".

Sources that should be used: official card shard for Doran's Blade, official card shard for Lucian, Merciless, and official rules only as needed for cost/payment timing.

Sources that should not be used as authority: memory of card text, semantic facts alone, inferred relations.

Failure condition: The answer says "if Doran's Blade's equip cost is..." without checking the official Doran's Blade text, or concludes from Lucian alone.
"""


def render_gpt_instructions() -> str:
    return """# GPT Instructions

## Role

[editorial] You are a Riftbound rules and card-reference assistant. Answer from the generated official rules and official card references first. Use derived and inferred files only as auxiliary discovery layers.

## Source Authority

[editorial] Retrieval order:

1. Official rules and official normalized card text.
2. Editorial instructions and playbooks for response style.
3. Derived semantic facts for discovery and recall.
4. Inferred relations for synergy and recommendation discovery.
5. Audit reports and limitations for uncertainty context.

## Conflict Resolution

[editorial] The Golden Rule applies: when official card text contradicts a general rule, the official card text controls that specific case. Derived facts, inferred relations, and editorial examples never override official rules or official card text.

## Authority Tags

[editorial] Treat `[official-rule]` and `[official-card]` as primary evidence. Treat `[derived-fact]`, `[inferred-relation]`, `[editorial]`, and `[quality-warning]` as auxiliary.

## Named Card Verification

[editorial] Before answering an interaction, line of play, cost, keyword, equip, target, reducer, trigger, or replacement question, identify every card named by the user and consult each card's `[official-card]` section. Do not rely on memory, examples, semantic facts, or inferred relations for a named card's cost, keywords, stats, or exact text.

[editorial] If every named card exists in the official references, avoid hypothetical language about its printed values. Answer from the retrieved card text. Use "if" only for genuinely unknown game state, optional choices, or cards not found in the package.

## Rules Questions

[editorial] Consult `for_gpt/knowledge/01_official_rules_reference.md` first. If the question names any card, also consult every named card's official card shard before concluding. Cite rule IDs and card names when possible.

## Card Questions

[editorial] Consult the official card shard for every named card. Report card identity, stats, public codes, official rules text, official effect text, and variants if relevant.

## Gameplay And List Questions

[editorial] Separate rules claims from strategy suggestions. Use semantic and relation indexes only after checking official text for named cards.

## Derived Data Policy

[editorial] Derived facts are extracted from official text but are not official rules. Inferred relations are pipeline suggestions and must be described as such.

## Uncertainty Policy

[editorial] Say "there is not enough official evidence in this package" when the official rules and official cards do not support a conclusion.

## Citation Style

[editorial] Cite authority tags in prose, for example: `[official-rule] 002`, `[official-card] Abandon`, `[derived-fact] Abandon`, or `[inferred-relation] Abandon`.

## Examples

[editorial] Ruling: "Rule 002 says card text supersedes rules text. For this specific card, the official card text says ..."

[editorial] Synergy: "The relation index suggests these cards may work together, but that relation is inferred. The official card texts to verify are ..."
"""


def render_manifest(
    cards: list[dict[str, Any]],
    rules_payload: dict[str, Any],
    facts: list[dict[str, Any]],
    relations: list[dict[str, Any]],
    broad_reasons: set[str],
    shard_ranges: dict[str, str],
    file_sizes: dict[str, int],
    size_warnings: list[str],
    max_knowledge_files: int,
) -> str:
    upload_count = len(DEFAULT_UPLOAD_FILES)
    compact_plan = "Not required" if upload_count <= max_knowledge_files else "Required"
    lines = [
        "# Riftbound GPT Knowledge Manifest",
        "",
        "## Generation Snapshot",
        "",
        f"- generated_at: {date.today().isoformat()}",
        f"- generator: `{repo_path(Path(__file__))}`",
        "",
        "## Primary Sources",
        "",
        f"- cards: `{repo_path(CARDS_PATH)}`",
        f"- rules: `{repo_path(RULES_PATH)}`",
        "",
        "## Auxiliary Sources",
        "",
        f"- facts: `{repo_path(FACTS_PATH)}`",
        f"- relations: `{repo_path(RELATIONS_PATH)}`",
        f"- semantic_audit: `{repo_path(SEMANTIC_AUDIT_PATH)}`",
        f"- web_dataset_report: `{repo_path(WEB_DATASET_REPORT_PATH)}`",
        f"- web_quality_report: `{repo_path(WEB_QUALITY_REPORT_PATH)}`",
        f"- web_index: `{repo_path(WEB_INDEX_PATH)}`",
        f"- quality_policy: `{repo_path(QUALITY_POLICY_PATH)}`",
        "",
        "## Included Files",
        "",
    ]
    for filename in PACKAGE_FILES:
        size = file_sizes.get(filename)
        suffix = f" ({size} bytes)" if size is not None else ""
        lines.append(f"- `{FILE_TARGETS[filename].as_posix()}`{suffix}")
    lines.extend(
        [
            "",
            "## Counts",
            "",
            f"- card_count: {len(cards)}",
            f"- rule_count: {len(rules_payload.get('rules', []))}",
            f"- derived_fact_count: {len(facts)}",
            f"- inferred_relation_count: {len(relations)}",
            f"- broad_reason_count: {len(broad_reasons)}",
            "",
            "## Authority Order",
            "",
            "- Retrieval starts with official rules and official card references.",
            "- For conflicts, official card text controls a specific card case under the Golden Rule.",
            "- Derived facts and inferred relations never override official sources.",
            "",
            "## Authority Tags",
            "",
            "- `[official-rule]`: processed official rules.",
            "- `[official-card]`: normalized official card text, stats, and identity.",
            "- `[derived-fact]`: semantic fact extracted from official text.",
            "- `[inferred-relation]`: pipeline-inferred relation between cards.",
            "- `[editorial]`: response policy, playbook, or manually written behavior guidance.",
            "- `[quality-warning]`: audit warning, limitation, or known uncertainty.",
            "",
            "## Shard Ranges And Size Warnings",
            "",
        ]
    )
    for filename, range_label in shard_ranges.items():
        lines.append(f"- `{filename}`: {range_label}")
    if size_warnings:
        lines.extend(["", "Size warnings:"])
        lines.extend(f"- {warning}" for warning in size_warnings)
    else:
        lines.extend(["", "- No generated package file exceeded the warning threshold."])
    lines.extend(
        [
            "",
            "## GPT Upload Plan",
            "",
            f"- max_gpt_knowledge_files: {max_knowledge_files}",
            f"- default_upload_file_count: {upload_count}",
            f"- compact_plan: {compact_plan}",
            "- copy_to_instructions: `for_gpt/instructions/00_gpt_instructions.md`",
            "- default_knowledge_files:",
        ]
    )
    lines.extend(f"  - `{filename}`" for filename in DEFAULT_UPLOAD_FILES)
    lines.extend(
        [
            "",
            "## Global Cautions",
            "",
            "- Facts and relations are derived or inferred and must not be treated as official rules.",
            "- `repo_only/00_answer_playbooks.md` is editorial support and is not part of the default Knowledge upload profile.",
            "- `repo_only/01_evaluation_questions.md` is a post-upload evaluation checklist and is not part of the default Knowledge upload profile.",
            "- Check current GPT file limits before upload; use the compact profile if the limit is lower than this package requires.",
            "",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def target_path(output_dir: Path, filename: str) -> Path:
    return output_dir / FILE_TARGETS[filename]


def write_file(output_dir: Path, filename: str, content: str) -> None:
    path = target_path(output_dir, filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def collect_file_sizes(output_dir: Path, filenames: list[str]) -> dict[str, int]:
    return {filename: target_path(output_dir, filename).stat().st_size for filename in filenames if target_path(output_dir, filename).exists()}


def validate_package(
    output_dir: Path,
    cards: list[dict[str, Any]],
    rules_payload: dict[str, Any],
    facts: list[dict[str, Any]],
    relations: list[dict[str, Any]],
    broad_reasons: set[str],
    file_sizes: dict[str, int],
    max_knowledge_files: int,
    allow_large_files: bool,
) -> list[str]:
    errors: list[str] = []
    card_ids = {str(card.get("play_id")) for card in cards}
    card_names = {str(card.get("name")) for card in cards}

    seen_cards: Counter[str] = Counter()
    for filename in CARD_SHARDS:
        text = target_path(output_dir, filename).read_text(encoding="utf-8")
        if "[derived-fact]" in text or "[inferred-relation]" in text:
            errors.append(f"{filename} contains derived or inferred authority tags")
        for match in re.finditer(r"^## \[official-card\] (.+)$", text, flags=re.MULTILINE):
            seen_cards[match.group(1).strip()] += 1
    missing_cards = sorted(card_names - set(seen_cards))
    duplicate_cards = sorted(name for name, count in seen_cards.items() if count != 1)
    if missing_cards:
        errors.append(f"missing official cards in shards: {missing_cards[:10]}")
    if duplicate_cards:
        errors.append(f"duplicate official cards in shards: {duplicate_cards[:10]}")

    rules_text = target_path(output_dir, "rules").read_text(encoding="utf-8")
    official_rule_headings = re.findall(r"^### \[official-rule\] ", rules_text, flags=re.MULTILINE)
    if len(official_rule_headings) != len(rules_payload.get("rules", [])):
        errors.append(
            f"official rule tag count mismatch: {len(official_rule_headings)} rendered vs {len(rules_payload.get('rules', []))} rules"
        )

    invalid_fact_refs = [fact.get("fact_id") for fact in facts if str(fact.get("play_id")) not in card_ids]
    if invalid_fact_refs:
        errors.append(f"derived facts reference unknown cards: {invalid_fact_refs[:10]}")

    invalid_relation_refs = [
        relation.get("relation_id")
        for relation in relations
        if str(relation.get("source_play_id")) not in card_ids or str(relation.get("target_play_id")) not in card_ids
    ]
    if invalid_relation_refs:
        errors.append(f"relations reference unknown cards: {invalid_relation_refs[:10]}")

    derived_text = target_path(output_dir, "semantic").read_text(encoding="utf-8")
    if "Verify rules-sensitive answers against official card text and official rules" not in derived_text:
        errors.append("derived semantic index missing authority warning")

    relations_text = target_path(output_dir, "relations").read_text(encoding="utf-8")
    if "Verify rules-sensitive answers against official cards and official rules" not in relations_text:
        errors.append("relations index missing authority warning")
    if any(reason in relations_text for reason in broad_reasons):
        broad_section = relations_text.split("## Broad Or Low-Confidence Relations", 1)[-1]
        high_section = relations_text.split("## High-Signal Relations By Card", 1)[-1].split("## Broad Or Low-Confidence Relations", 1)[0]
        if any(reason in high_section for reason in broad_reasons):
            errors.append("broad reason appears in high-signal per-card relation blocks")
        if not broad_section:
            errors.append("broad relations summary is missing")

    if len(DEFAULT_UPLOAD_FILES) > max_knowledge_files:
        errors.append(f"default upload plan has {len(DEFAULT_UPLOAD_FILES)} files, above max {max_knowledge_files}")

    for filename, size in file_sizes.items():
        if size > FAIL_BYTES and not allow_large_files:
            errors.append(f"{filename} is {size} bytes, above fail threshold {FAIL_BYTES}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Riftbound GPT Knowledge Markdown package.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--allow-large-files", action="store_true")
    parser.add_argument("--include-broad-relations", action="store_true")
    parser.add_argument("--max-gpt-knowledge-files", type=int, default=MAX_GPT_KNOWLEDGE_FILES)
    args = parser.parse_args()

    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    cards = load_json(CARDS_PATH, [])
    rules_payload = load_json(RULES_PATH, {})
    facts = load_jsonl(FACTS_PATH)
    relations = load_jsonl(RELATIONS_PATH)
    semantic_audit = load_json(SEMANTIC_AUDIT_PATH, {})
    dataset_report = load_json(WEB_DATASET_REPORT_PATH, {})
    web_quality = load_json(WEB_QUALITY_REPORT_PATH, {})
    web_index = load_json(WEB_INDEX_PATH, {})
    quality_policy = load_json(QUALITY_POLICY_PATH, {})

    cards_sorted = sorted(cards, key=card_sort_key)
    rules = rules_payload.get("rules", [])
    broad_reasons = load_broad_reasons(relations, quality_policy, web_index, dataset_report)

    shard_cards: dict[str, list[dict[str, Any]]] = {filename: [] for filename in CARD_SHARDS}
    bucket_to_filename = {label: filename for filename, (label, _) in CARD_SHARDS.items()}
    for card in cards_sorted:
        shard_cards[bucket_to_filename[first_letter_bucket(str(card.get("name") or ""))]].append(card)

    write_file(output_dir, "instructions", render_gpt_instructions())
    write_file(output_dir, "rules", render_rules(rules_payload))
    for filename, (_range_label, title) in CARD_SHARDS.items():
        write_file(output_dir, filename, render_cards_reference(filename, title, shard_cards[filename]))
    write_file(output_dir, "mechanics", render_mechanics_and_terms(cards_sorted, facts, rules))
    write_file(output_dir, "playbooks", render_answer_playbooks())
    write_file(output_dir, "semantic", render_derived_semantic_index(cards_sorted, facts))
    write_file(
        output_dir,
        "relations",
        render_inferred_relations_index(cards_sorted, relations, broad_reasons, args.include_broad_relations, web_index),
    )
    write_file(output_dir, "limitations", render_known_limitations(semantic_audit, dataset_report, web_quality))
    write_file(output_dir, "evaluations", render_evaluation_questions())

    shard_ranges = {filename: range_label for filename, (range_label, _title) in CARD_SHARDS.items()}
    file_sizes = collect_file_sizes(output_dir, [filename for filename in PACKAGE_FILES if filename != "manifest"])
    for _ in range(8):
        size_warnings = [f"`{filename}` is {size} bytes" for filename, size in file_sizes.items() if size > WARN_BYTES]
        write_file(
            output_dir,
            "manifest",
            render_manifest(
                cards_sorted,
                rules_payload,
                facts,
                relations,
                broad_reasons,
                shard_ranges,
                file_sizes,
                size_warnings,
                args.max_gpt_knowledge_files,
            ),
        )
        next_file_sizes = collect_file_sizes(output_dir, PACKAGE_FILES)
        if next_file_sizes == file_sizes:
            break
        file_sizes = next_file_sizes
    size_warnings = [f"`{filename}` is {size} bytes" for filename, size in file_sizes.items() if size > WARN_BYTES]

    errors = validate_package(
        output_dir,
        cards_sorted,
        rules_payload,
        facts,
        relations,
        broad_reasons,
        file_sizes,
        args.max_gpt_knowledge_files,
        args.allow_large_files,
    )
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Generated GPT knowledge package:")
    for filename in PACKAGE_FILES:
        print(f"- {filename}: {file_sizes.get(filename, 0)} bytes")
    if size_warnings:
        print("Size warnings:")
        for warning in size_warnings:
            print(f"- {warning}")
    print(f"Default upload files: {len(DEFAULT_UPLOAD_FILES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
