# Answer Playbooks

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
