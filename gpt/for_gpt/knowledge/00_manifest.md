# Riftbound GPT Knowledge Manifest

## Generation Snapshot

- generated_at: 2026-05-15
- generator: `gpt/build_gpt_knowledge.py`

## Primary Sources

- cards: `data/processed/cards/normalized/cards_normalized.json`
- rules: `data/processed/rules/core-rules.json`

## Auxiliary Sources

- facts: `data/processed/cards/semantic/cards_semantic_facts.jsonl`
- relations: `data/processed/cards/relations/cards_card_relations.jsonl`
- semantic_audit: `data/processed/cards/semantic/cards_semantic_audit_report.json`
- web_dataset_report: `data/processed/web/card_explorer_dataset_report.json`
- web_quality_report: `data/processed/web/card_explorer_quality_report.json`
- web_index: `data/processed/web/card_explorer_index.json`
- quality_policy: `scripts/04_cards_feature_extraction/contracts/semantic_quality_policy.json`

## Included Files

- `for_gpt/instructions/00_gpt_instructions.md` (3152 bytes)
- `for_gpt/knowledge/00_manifest.md` (3887 bytes)
- `for_gpt/knowledge/01_official_rules_reference.md` (634755 bytes)
- `for_gpt/knowledge/02_official_cards_reference_a_f.md` (148871 bytes)
- `for_gpt/knowledge/03_official_cards_reference_g_m.md` (107025 bytes)
- `for_gpt/knowledge/04_official_cards_reference_n_s.md` (126168 bytes)
- `for_gpt/knowledge/05_official_cards_reference_t_z.md` (78429 bytes)
- `for_gpt/knowledge/06_mechanics_and_terms.md` (16057 bytes)
- `for_gpt/knowledge/07_derived_semantic_index.md` (845090 bytes)
- `for_gpt/knowledge/08_inferred_relations_index.md` (968779 bytes)
- `for_gpt/knowledge/09_known_limitations.md` (1503 bytes)
- `repo_only/00_answer_playbooks.md` (2473 bytes)
- `repo_only/01_evaluation_questions.md` (6164 bytes)

## Counts

- card_count: 767
- rule_count: 2088
- derived_fact_count: 6311
- inferred_relation_count: 14590
- broad_reason_count: 2

## Authority Order

- Retrieval starts with official rules and official card references.
- For conflicts, official card text controls a specific card case under the Golden Rule.
- Derived facts and inferred relations never override official sources.

## Authority Tags

- `[official-rule]`: processed official rules.
- `[official-card]`: normalized official card text, stats, and identity.
- `[derived-fact]`: semantic fact extracted from official text.
- `[inferred-relation]`: pipeline-inferred relation between cards.
- `[editorial]`: response policy, playbook, or manually written behavior guidance.
- `[quality-warning]`: audit warning, limitation, or known uncertainty.

## Shard Ranges And Size Warnings

- `cards_a_f`: A-F
- `cards_g_m`: G-M
- `cards_n_s`: N-S
- `cards_t_z`: T-Z

Size warnings:
- `semantic` is 845090 bytes
- `relations` is 968779 bytes

## GPT Upload Plan

- max_gpt_knowledge_files: 10
- default_upload_file_count: 10
- compact_plan: Not required
- copy_to_instructions: `for_gpt/instructions/00_gpt_instructions.md`
- default_knowledge_files:
  - `for_gpt/knowledge/00_manifest.md`
  - `for_gpt/knowledge/01_official_rules_reference.md`
  - `for_gpt/knowledge/02_official_cards_reference_a_f.md`
  - `for_gpt/knowledge/03_official_cards_reference_g_m.md`
  - `for_gpt/knowledge/04_official_cards_reference_n_s.md`
  - `for_gpt/knowledge/05_official_cards_reference_t_z.md`
  - `for_gpt/knowledge/06_mechanics_and_terms.md`
  - `for_gpt/knowledge/07_derived_semantic_index.md`
  - `for_gpt/knowledge/08_inferred_relations_index.md`
  - `for_gpt/knowledge/09_known_limitations.md`

## Global Cautions

- Facts and relations are derived or inferred and must not be treated as official rules.
- `repo_only/00_answer_playbooks.md` is editorial support and is not part of the default Knowledge upload profile.
- `repo_only/01_evaluation_questions.md` is a post-upload evaluation checklist and is not part of the default Knowledge upload profile.
- Check current GPT file limits before upload; use the compact profile if the limit is lower than this package requires.
