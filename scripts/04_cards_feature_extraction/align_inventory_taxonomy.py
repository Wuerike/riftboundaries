import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
CONTRACTS_DIR = SCRIPT_DIR / "contracts"
DEFAULT_INVENTORY = PROJECT_ROOT / "data" / "processed" / "cards" / "inventory" / "cards_text_inventory.json"
DEFAULT_TAXONOMY = CONTRACTS_DIR / "feature_relation_taxonomy.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "processed" / "cards" / "inventory" / "cards_taxonomy_alignment.json"
DEFAULT_MARKDOWN = PROJECT_ROOT / "data" / "processed" / "cards" / "inventory" / "cards_taxonomy_alignment.md"

TOP_EXAMPLES_PER_GROUP = 12
TOP_SEEDS_PER_TARGET = 30
PRIORITY_RANK = {"high": 3, "medium": 2, "low": 1}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_markdown(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(markdown_report(payload), encoding="utf-8")


def unique_list(values: list[str]) -> list[str]:
    return sorted(set(values))


def mapping_for_family(taxonomy: dict[str, Any], family: str) -> dict[str, Any]:
    mappings = taxonomy.get("family_mappings", {})
    return mappings.get(
        family,
        {
            "roles": [],
            "axes": [],
            "semantic_targets": [],
            "web_uses": [],
            "priority": "unmapped",
        },
    )


def priority_for_families(taxonomy: dict[str, Any], families: list[str]) -> str:
    best = "unmapped"
    best_rank = 0
    for family in families:
        priority = mapping_for_family(taxonomy, family).get("priority", "unmapped")
        rank = PRIORITY_RANK.get(priority, 0)
        if rank > best_rank:
            best = priority
            best_rank = rank
    return best


def dimensions_for_families(taxonomy: dict[str, Any], families: list[str]) -> dict[str, list[str]]:
    roles = []
    axes = []
    semantic_targets = []
    web_uses = []

    for family in families:
        mapping = mapping_for_family(taxonomy, family)
        roles.extend(mapping.get("roles", []))
        axes.extend(mapping.get("axes", []))
        semantic_targets.extend(mapping.get("semantic_targets", []))
        web_uses.extend(mapping.get("web_uses", []))

    return {
        "roles": unique_list(roles),
        "axes": unique_list(axes),
        "semantic_targets": unique_list(semantic_targets),
        "web_uses": unique_list(web_uses),
        "priority": priority_for_families(taxonomy, families),
    }


def family_line_stats(inventory: dict[str, Any]) -> dict[str, dict[str, int]]:
    return {
        item["family"]: {
            "line_occurrence_count": item["occurrence_count"],
            "unique_normalized_line_count": item["unique_normalized_line_count"],
            "distinct_card_count": item["distinct_card_count"],
        }
        for item in inventory.get("candidate_families", [])
    }


def family_unit_stats(inventory: dict[str, Any]) -> dict[str, dict[str, int]]:
    stats: dict[str, dict[str, int]] = defaultdict(
        lambda: {"unit_occurrence_count": 0, "unique_normalized_unit_count": 0, "distinct_card_count": 0}
    )
    family_cards: dict[str, set[str]] = defaultdict(set)

    for unit in inventory.get("text_units", []):
        for family in unit.get("candidate_families", []):
            stats[family]["unit_occurrence_count"] += unit["occurrence_count"]
            stats[family]["unique_normalized_unit_count"] += 1
            for example in unit.get("examples", []):
                for card in example.get("example_cards", []):
                    family_cards[family].add(card.get("play_id", ""))

    for family, cards in family_cards.items():
        stats[family]["distinct_card_count"] = len({card for card in cards if card})
    return dict(stats)


def build_family_alignment(inventory: dict[str, Any], taxonomy: dict[str, Any]) -> list[dict[str, Any]]:
    line_stats = family_line_stats(inventory)
    unit_stats = family_unit_stats(inventory)
    families = sorted(set(line_stats) | set(unit_stats) | set(taxonomy.get("family_mappings", {})))
    rows = []

    for family in families:
        mapping = mapping_for_family(taxonomy, family)
        row = {
            "family": family,
            "mapped": family in taxonomy.get("family_mappings", {}),
            "priority": mapping.get("priority", "unmapped"),
            "roles": mapping.get("roles", []),
            "axes": mapping.get("axes", []),
            "semantic_targets": mapping.get("semantic_targets", []),
            "web_uses": mapping.get("web_uses", []),
            **line_stats.get(
                family,
                {"line_occurrence_count": 0, "unique_normalized_line_count": 0, "distinct_card_count": 0},
            ),
            **unit_stats.get(
                family,
                {"unit_occurrence_count": 0, "unique_normalized_unit_count": 0},
            ),
        }
        rows.append(row)

    rows.sort(
        key=lambda item: (
            -PRIORITY_RANK.get(item["priority"], 0),
            -item["unit_occurrence_count"],
            -item["line_occurrence_count"],
            item["family"],
        )
    )
    return rows


def unit_alignment_record(unit: dict[str, Any], taxonomy: dict[str, Any]) -> dict[str, Any]:
    families = unit.get("candidate_families", [])
    dimensions = dimensions_for_families(taxonomy, families)
    return {
        "unit_text": unit["unit_text"],
        "normalized_unit": unit["normalized_unit"],
        "parameterized_unit": unit["parameterized_unit"],
        "primary_unit_kind": unit["primary_unit_kind"],
        "occurrence_count": unit["occurrence_count"],
        "unique_normalized_line_count": unit["unique_normalized_line_count"],
        "distinct_card_count": unit["distinct_card_count"],
        "candidate_families": families,
        **dimensions,
        "examples": unit.get("examples", [])[:3],
    }


def parameterized_unit_alignment_record(unit: dict[str, Any], taxonomy: dict[str, Any]) -> dict[str, Any]:
    families = list(unit.get("candidate_family_counts", {}).keys())
    dimensions = dimensions_for_families(taxonomy, families)
    return {
        "parameterized_unit": unit["parameterized_unit"],
        "primary_unit_kind": unit["primary_unit_kind"],
        "occurrence_count": unit["occurrence_count"],
        "unique_normalized_line_count": unit["unique_normalized_line_count"],
        "distinct_card_count": unit["distinct_card_count"],
        "candidate_families": families,
        "candidate_family_counts": unit.get("candidate_family_counts", {}),
        **dimensions,
        "examples": unit.get("examples", [])[:3],
    }


def add_group_example(group: dict[str, Any], record: dict[str, Any]) -> None:
    if len(group["examples"]) >= TOP_EXAMPLES_PER_GROUP:
        return
    group["examples"].append(
        {
            "text": record.get("parameterized_unit") or record.get("unit_text"),
            "kind": record.get("primary_unit_kind"),
            "occurrence_count": record.get("occurrence_count"),
            "families": record.get("candidate_families", []),
        }
    )


def summarize_groups(records: list[dict[str, Any]], group_key: str) -> list[dict[str, Any]]:
    groups: dict[str, dict[str, Any]] = {}
    for record in records:
        for key in record.get(group_key, []):
            if key not in groups:
                groups[key] = {
                    group_key[:-1] if group_key.endswith("s") else group_key: key,
                    "unit_occurrence_count": 0,
                    "unique_unit_count": 0,
                    "families": Counter(),
                    "examples": [],
                }
            group = groups[key]
            group["unit_occurrence_count"] += record["occurrence_count"]
            group["unique_unit_count"] += 1
            for family in record.get("candidate_families", []):
                group["families"][family] += record["occurrence_count"]
            add_group_example(group, record)

    rows = []
    for group in groups.values():
        group["top_families"] = dict(group.pop("families").most_common(12))
        rows.append(group)
    rows.sort(key=lambda item: (-item["unit_occurrence_count"], item.get(group_key[:-1], "")))
    return rows


def semantic_seed_groups(records: list[dict[str, Any]], target_key: str) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        for target in record.get(target_key, []):
            groups[target].append(record)

    rows = []
    for target, items in groups.items():
        sorted_items = sorted(
            items,
            key=lambda item: (
                -PRIORITY_RANK.get(item["priority"], 0),
                -item["occurrence_count"],
                -item["unique_normalized_line_count"],
                item["parameterized_unit"],
            ),
        )
        rows.append(
            {
                "target": target,
                "unit_occurrence_count": sum(item["occurrence_count"] for item in items),
                "unique_parameterized_unit_count": len(items),
                "top_seeds": [
                    {
                        "parameterized_unit": item["parameterized_unit"],
                        "occurrence_count": item["occurrence_count"],
                        "unique_normalized_line_count": item["unique_normalized_line_count"],
                        "priority": item["priority"],
                        "families": item["candidate_families"],
                        "roles": item["roles"],
                    }
                    for item in sorted_items[:TOP_SEEDS_PER_TARGET]
                ],
            }
        )
    rows.sort(key=lambda item: (-item["unit_occurrence_count"], item["target"]))
    return rows


def build_web_readiness(role_summary: list[dict[str, Any]], web_use_summary: list[dict[str, Any]]) -> dict[str, Any]:
    role_counts = {
        item["role"]: item["unit_occurrence_count"]
        for item in role_summary
        if "role" in item
    }
    web_counts = {
        item["web_use"]: item["unit_occurrence_count"]
        for item in web_use_summary
        if "web_use" in item
    }
    return {
        "enablement_core": {
            "event_produced_unit_occurrences": role_counts.get("event_produced", 0),
            "trigger_observed_unit_occurrences": role_counts.get("trigger_observed", 0),
            "payoff_output_unit_occurrences": role_counts.get("payoff_output", 0),
        },
        "web_use_coverage": web_counts,
        "notes": [
            "Enablement analysis needs event_produced and trigger_observed to become typed events, not just shared words.",
            "Similarity can use payoff_output, state_or_modifier, target, location, cost, and duration facets.",
            "Deck synergy should prioritize producer/payoff pairs and cost/resource compatibility.",
        ],
    }


def build_alignment(inventory: dict[str, Any], taxonomy: dict[str, Any]) -> dict[str, Any]:
    family_alignment = build_family_alignment(inventory, taxonomy)
    unit_records = [unit_alignment_record(unit, taxonomy) for unit in inventory.get("text_units", [])]
    parameterized_records = [
        parameterized_unit_alignment_record(unit, taxonomy)
        for unit in inventory.get("parameterized_units", [])
    ]

    unmapped_families = [
        row["family"]
        for row in family_alignment
        if row["line_occurrence_count"] or row["unit_occurrence_count"]
        if not row["mapped"]
    ]
    role_summary = summarize_groups(unit_records, "roles")
    axis_summary = summarize_groups(unit_records, "axes")
    semantic_target_summary = summarize_groups(unit_records, "semantic_targets")
    web_use_summary = summarize_groups(unit_records, "web_uses")

    mapped_units = [record for record in unit_records if record["roles"]]
    multi_role_units = [record for record in unit_records if len(record["roles"]) >= 3]
    high_priority_units = [
        record
        for record in unit_records
        if record["priority"] == "high"
    ]

    return {
        "inputs": {
            "inventory": str(DEFAULT_INVENTORY).replace("\\", "/"),
            "taxonomy": str(DEFAULT_TAXONOMY).replace("\\", "/"),
            "inventory_summary": inventory.get("summary", {}),
            "taxonomy_version": taxonomy.get("version"),
        },
        "summary": {
            "family_count": len(family_alignment),
            "mapped_family_count": sum(1 for row in family_alignment if row["mapped"]),
            "unmapped_family_count": len(unmapped_families),
            "unmapped_families": unmapped_families,
            "unique_normalized_unit_count": len(unit_records),
            "mapped_unit_count": len(mapped_units),
            "unmapped_unit_count": len(unit_records) - len(mapped_units),
            "multi_role_unit_count": len(multi_role_units),
            "high_priority_unit_count": len(high_priority_units),
            "parameterized_unit_count": len(parameterized_records),
        },
        "family_alignment": family_alignment,
        "role_summary": role_summary,
        "axis_summary": axis_summary,
        "semantic_target_summary": semantic_target_summary,
        "web_use_summary": web_use_summary,
        "web_readiness": build_web_readiness(role_summary, web_use_summary),
        "semantic_target_seed_groups": semantic_seed_groups(parameterized_records, "semantic_targets"),
        "top_high_priority_units": sorted(
            high_priority_units,
            key=lambda item: (-item["occurrence_count"], item["parameterized_unit"]),
        )[:80],
        "top_multi_role_units": sorted(
            multi_role_units,
            key=lambda item: (-len(item["roles"]), -item["occurrence_count"], item["parameterized_unit"]),
        )[:80],
    }


def md_escape(value: Any) -> str:
    return str(value).replace("\n", " ").replace("|", "\\|")


def markdown_table(headers: list[str], rows: list[list[Any]]) -> list[str]:
    output = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        output.append("| " + " | ".join(md_escape(value) for value in row) + " |")
    return output


def markdown_report(alignment: dict[str, Any]) -> str:
    summary = alignment["summary"]
    readiness = alignment["web_readiness"]["enablement_core"]
    lines = [
        "# Cards Taxonomy Alignment",
        "",
        "Bridge report from text inventory families/units to the target semantic contract.",
        "This report does not read extracted facts or web relations.",
        "",
        "## Summary",
        "",
        f"- Families: {summary['family_count']}",
        f"- Mapped families: {summary['mapped_family_count']}",
        f"- Unmapped families: {summary['unmapped_family_count']}",
        f"- Unique normalized units: {summary['unique_normalized_unit_count']}",
        f"- Mapped units: {summary['mapped_unit_count']}",
        f"- Multi-role units: {summary['multi_role_unit_count']}",
        f"- High-priority units: {summary['high_priority_unit_count']}",
        f"- Event-produced unit occurrences: {readiness['event_produced_unit_occurrences']}",
        f"- Trigger-observed unit occurrences: {readiness['trigger_observed_unit_occurrences']}",
        f"- Payoff-output unit occurrences: {readiness['payoff_output_unit_occurrences']}",
        "",
    ]

    lines.extend(["## Family Alignment", ""])
    family_rows = [
        [
            row["family"],
            row["priority"],
            row["unit_occurrence_count"],
            row["unique_normalized_unit_count"],
            ", ".join(row["roles"]),
            ", ".join(row["axes"]),
            ", ".join(row["semantic_targets"]),
        ]
        for row in alignment["family_alignment"]
        if row["line_occurrence_count"] or row["unit_occurrence_count"]
    ]
    lines.extend(
        markdown_table(
            [
                "Family",
                "Priority",
                "Unit occ.",
                "Unique units",
                "Roles",
                "Axes",
                "Semantic targets",
            ],
            family_rows,
        )
    )

    lines.extend(["", "## Role Summary", ""])
    role_rows = [
        [
            item["role"],
            item["unit_occurrence_count"],
            item["unique_unit_count"],
            ", ".join(item["top_families"].keys()),
        ]
        for item in alignment["role_summary"]
    ]
    lines.extend(markdown_table(["Role", "Unit occ.", "Unique units", "Top families"], role_rows))

    lines.extend(["", "## Semantic Target Coverage", ""])
    semantic_rows = [
        [
            item["semantic_target"],
            item["unit_occurrence_count"],
            item["unique_unit_count"],
            ", ".join(item["top_families"].keys()),
        ]
        for item in alignment["semantic_target_summary"]
    ]
    lines.extend(markdown_table(["Semantic target", "Unit occ.", "Unique units", "Top families"], semantic_rows))

    lines.extend(["", "## Web Use Coverage", ""])
    web_rows = [
        [
            item["web_use"],
            item["unit_occurrence_count"],
            item["unique_unit_count"],
            ", ".join(item["top_families"].keys()),
        ]
        for item in alignment["web_use_summary"]
    ]
    lines.extend(markdown_table(["Web use", "Unit occ.", "Unique units", "Top families"], web_rows))

    lines.extend(["", "## Semantic Target Seed Groups", ""])
    for group in alignment["semantic_target_seed_groups"][:18]:
        lines.extend(["", f"### {group['target']}", ""])
        seed_rows = [
            [
                seed["occurrence_count"],
                seed["priority"],
                ", ".join(seed["families"]),
                seed["parameterized_unit"],
            ]
            for seed in group["top_seeds"][:12]
        ]
        lines.extend(markdown_table(["Occ.", "Priority", "Families", "Parameterized unit"], seed_rows))

    lines.extend(["", "## High Priority Unit Examples", ""])
    high_rows = [
        [
            item["occurrence_count"],
            item["primary_unit_kind"],
            ", ".join(item["roles"]),
            ", ".join(item["candidate_families"]),
            item["parameterized_unit"],
        ]
        for item in alignment["top_high_priority_units"][:40]
    ]
    lines.extend(markdown_table(["Occ.", "Kind", "Roles", "Families", "Parameterized unit"], high_rows))

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Align card text inventory families with the target semantic taxonomy."
    )
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument("--taxonomy", type=Path, default=DEFAULT_TAXONOMY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args()

    inventory = read_json(args.inventory)
    taxonomy = read_json(args.taxonomy)
    alignment = build_alignment(inventory, taxonomy)
    alignment["inputs"]["inventory"] = str(args.inventory).replace("\\", "/")
    alignment["inputs"]["taxonomy"] = str(args.taxonomy).replace("\\", "/")

    write_json(args.output, alignment)
    write_markdown(args.markdown, alignment)

    print(f"[OK] families: {alignment['summary']['family_count']}")
    print(f"[OK] mapped families: {alignment['summary']['mapped_family_count']}")
    print(f"[OK] mapped units: {alignment['summary']['mapped_unit_count']}")
    print(f"[OK] output: {args.output}")
    print(f"[OK] markdown: {args.markdown}")


if __name__ == "__main__":
    main()
