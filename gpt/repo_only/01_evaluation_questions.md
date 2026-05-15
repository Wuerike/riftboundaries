# Evaluation Questions

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
