# Known Limitations

## [quality-warning] Official Sources Are Primary

Use official rules and official card references as final authority. Derived semantic facts and inferred relations are auxiliary.

## [quality-warning] Derived Semantic Limits

- fact_count: 6311
- text_line_fact_coverage: 0.984
- warning_count: 179
- legacy_rule_count: 622
- issue_counts: multiple_relational_clause_groups_on_line: 90, optional_line_without_optional_modality: 88, payoff_without_output: 1

## [quality-warning] Inferred Relation Limits

- relation_count: 14590
- high_signal_relation_count: 9701
- broad_relation_count: 4889
- top_broad_reasons: spell_card_can_be_countered: 3438, cost:rune:any: 1451

## [quality-warning] Current Quality Snapshot

- cards_without_relations: 42
- cards_with_only_broad_relations: 0
- cards_with_rule_variants: 44
- broad_relation_share: 0.3351

## [quality-warning] Cards And Patterns Requiring Caution

- Cards with rule text variants require checking the official card shard before answering.
- Facts are not programmatically linked to specific official rule IDs.
- Relation strength is a pipeline signal, not proof of a legal interaction.

## [quality-warning] Uncertainty Response Policy

- Say there is not enough official evidence when rules or card text do not establish the requested conclusion.
- For inferred synergy, say the relation is pipeline-suggested and verify against official text.
- Do not turn audit warnings or relation reports into primary answer content.
