# Card Relation Blind Spots - Temporary Snapshot

This tracked temporary snapshot is kept only as a quick historical note. The authoritative report is:

```text
data/processed/web/card_explorer_quality_report.md
data/processed/web/card_explorer_quality_report.json
```

## Current Summary

- Cards in web dataset: 767
- Semantic facts: 5382
- Card relations: 9047
- High-signal relations: 5609
- Broad relations: 3438
- Cards without any relation: 144
- Cards with only broad relations: 45
- Cards with uncovered relational lines: 0
- Golden examples: 60/60 passed
- Semantic audit text coverage: 0.9776
- Semantic audit errors/warnings: 0/0

## Current Diagnostics

- ok: 560
- missing_relation_rule: 90
- likely_vanilla_or_low_relational_text: 51
- broad_only: 45
- weak_fact: 12
- front_scoring_issue: 9

## Remaining Coverage By Bucket

- movement/location: 48
- stat/buff/damage_modifier: 30
- cost/resource: 19
- vanilla/no_text: 14
- other: 9
- damage: 7
- card_flow: 6
- permission/restriction: 3
- kill/heal/replacement: 3
- attachment/copy: 2
- deck_manipulation/recycle: 2
- score/victory: 1

## Top Broad Reasons

- spell_card_can_be_countered: 3438

## Interpretation

The earlier blind spots around counter, recycle, play-from-zone, keyword grants, attach/detach, token copy, multi-word tokens, damage, kill, score and replacement effects are now largely modeled as semantic facts. The remaining problem is less about missing text coverage and more about relation design.

Do not force isolation to zero by adding generic links. For the current residual cards, prefer precise relation families or front scoring changes:

- create relation families only when the shared semantic key is meaningful;
- keep `spell_card_can_be_countered` broad and demoted in default exploration;
- treat isolated cards with good facts as `missing_relation_rule`, not as extraction failures;
- treat isolated cards with weak facts as candidates for new extraction rules and golden examples.

## Sample Cards Without Relations

- play:blitzcrank-impassive:19f338cd
- play:the-academy:f9fe7741
- play:rumble-hotheaded:118ba12c
- play:yuumi-magical-cat:14e752b1
- play:ahri-inquisitive:d6396fae
- play:lucian-gunslinger:6cdb974d
- play:ornn-forge-god:01d7efe1
- play:rabadon-s-deathcrown:2161f7df
- play:fiora-peerless:f8a59eeb
- play:inviolus-vox:722201ee

## Sample Cards With Only Broad Relations

- play:acceptable-losses:23e05503
- play:against-the-odds:2a7b8a95
- play:angle-shot:f8a4b638
- play:block:5af86e4a
- play:bullet-time:3b6dabf3
- play:confront:dca66872
- play:convergent-mutation:981352cf
- play:counter-strike:cfba558c
- play:crescent-strike:01c8f47c
- play:dancing-grenade:1ebb941d
