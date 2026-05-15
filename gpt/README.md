# Riftbound GPT Knowledge Package

This directory contains a self-contained implementation of `tmp/spec.md` for building a custom GPT Knowledge package from treated official Riftbound sources.

## Generate

Run from the repository root:

```powershell
python gpt\build_gpt_knowledge.py
```

The generator writes GPT-facing files under `gpt/for_gpt` and repo-only support files under `gpt/repo_only`.

## GPT Setup

Copy or adapt this file into the GPT Instructions field:

- `for_gpt/instructions/00_gpt_instructions.md`

Upload these files as the default Knowledge profile:

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

`repo_only/00_answer_playbooks.md` is editorial support for maintainers. It is not part of the default Knowledge upload profile when using the conservative 10-file limit.

`repo_only/01_evaluation_questions.md` is a post-upload evaluation checklist. Use it to test the custom GPT after upload, but keep it out of the default Knowledge profile unless there is spare file capacity.

## Authority Policy

Use official rules and official card references before derived or inferred files. For conflicts, the Golden Rule applies: official card text controls a specific card case when it contradicts a general rule.

Derived semantic facts and inferred relations are discovery layers. They must not be treated as official rules.

## Configurable Limits

Defaults are implemented in `build_gpt_knowledge.py`:

- warning threshold: 750 KB per generated package Markdown file
- failure threshold: 1.5 MB per generated package Markdown file
- facts per card in the main semantic index: 8
- high-signal relations per card: 8
- default Knowledge upload limit: 10 files

Useful flags:

```powershell
python gpt\build_gpt_knowledge.py --allow-large-files
python gpt\build_gpt_knowledge.py --include-broad-relations
python gpt\build_gpt_knowledge.py --max-gpt-knowledge-files 20
```

Check the current GPT builder file limit before upload. If the limit is lower than the default upload profile requires, use a compact profile without merging inferred content into official card or rule files.

## Regenerate

Regenerate after any upstream change to:

- `data/processed/cards/normalized/cards_normalized.json`
- `data/processed/rules/core-rules.json`
- `data/processed/cards/semantic/cards_semantic_facts.jsonl`
- `data/processed/cards/relations/cards_card_relations.jsonl`
- semantic quality policy or web reports

## Evaluate

After uploading the Knowledge files and copying the Instructions, use `repo_only/01_evaluation_questions.md` to check that the GPT:

- uses official rules and official card text as primary evidence
- applies the Golden Rule correctly
- labels derived facts and inferred relations as auxiliary
- says there is not enough official evidence when appropriate
