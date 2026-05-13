# Cards Semantic Audit Report

Audit for `data/processed/cards/semantic/cards_semantic_facts.jsonl`.

## Summary

- card_count: 767
- fact_count: 6311
- cards_with_facts: 767
- text_line_count: 1248
- text_lines_with_facts: 1228
- text_lines_without_facts: 20
- text_line_fact_coverage: 0.984
- error_count: 0
- warning_count: 179
- info_count: 0
- golden_pass: True
- legacy_rule_count: 622

## Issue Counts

- multiple_relational_clause_groups_on_line: 90
- optional_line_without_optional_modality: 88
- payoff_without_output: 1

## Extraction Provenance

- structural_field: 3796
- contract_rule: 1893
- legacy_rule: 622

### Top Contract Rules

- activation_cost: 232
- trigger_self_played: 127
- draw_cards: 105
- give_might: 76
- move_unit: 64
- play_token: 64
- deal_damage: 56
- attach_equipment: 48
- buff_unit: 43
- ready_unit: 40
- recycle_card: 36
- trigger_self_conquers: 35
- intrinsic_combat_might_modifier: 34
- look_reveal_top_deck: 33
- gain_xp: 31
- trigger_self_conquers_or_holds: 30
- add_resource: 27
- condition_while_attacker: 25
- costs_less_energy: 25
- trigger_self_dies: 24
- channel_rune: 23
- stun_unit: 23
- target_has_keywords: 22
- play_card_from_zone: 22
- self_move_permission: 21
- repeat_effect: 21
- return_to_owner_hand: 20
- trigger_self_moves: 20
- discard_cards: 20
- grant_keyword_to_target: 20
- trigger_self_attacks: 19
- banish_target: 18
- weaponmaster_equip: 18
- ready_self: 18
- condition_while_defender: 18
- deal_variable_damage: 18
- self_enters_ready: 17
- trigger_self_holds: 16
- trigger_self_attacks_or_defends: 16
- self_has_might_modifier: 15

## Top Issues

| Severity | Code | Card | Fact | Detail |
| --- | --- | --- | --- | --- |
| warning | multiple_relational_clause_groups_on_line | Ancient Henge | fact:play:ancient-henge:9117108a:rules_lines:0:cost_or_requirement:pay:0 | clause:play:ancient-henge:9117108a:rules_lines:0:ability, clause:play:ancient-henge:9117108a:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Armed Assailant | fact:play:armed-assailant:32d279bc:rules_lines:1:event_produced:attach:0 | clause:play:armed-assailant:32d279bc:rules_lines:1:ability, clause:play:armed-assailant:32d279bc:rules_lines:1:keyword |
| warning | multiple_relational_clause_groups_on_line | Ava Achiever | fact:play:ava-achiever:59c46b4f:rules_lines:0:event_produced:play:0 | clause:play:ava-achiever:59c46b4f:rules_lines:0:ability, clause:play:ava-achiever:59c46b4f:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Azir, Ascendant | fact:play:azir-ascendant:82d12920:rules_lines:0:cost_or_requirement:pay:0 | clause:play:azir-ascendant:82d12920:rules_lines:0:ability, clause:play:azir-ascendant:82d12920:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Bashful Bloom | fact:play:bashful-bloom:a2a8b0d1:rules_lines:0:cost_or_requirement:pay:0 | clause:play:bashful-bloom:a2a8b0d1:rules_lines:0:ability, clause:play:bashful-bloom:a2a8b0d1:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Black Flame Altar | fact:play:black-flame-altar:32878e11:rules_lines:0:state_or_modifier:gain_keyword:0 | clause:play:black-flame-altar:32878e11:rules_lines:0:ability, clause:play:black-flame-altar:32878e11:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Blast Cone | fact:play:blast-cone:55eeaf2f:rules_lines:1:event_produced:stun:0 | clause:play:blast-cone:55eeaf2f:rules_lines:1:ability, clause:play:blast-cone:55eeaf2f:rules_lines:1:keyword |
| warning | multiple_relational_clause_groups_on_line | Bone Skewer | fact:play:bone-skewer:34218ae3:rules_lines:1:event_produced:stun:0 | clause:play:bone-skewer:34218ae3:rules_lines:1:ability, clause:play:bone-skewer:34218ae3:rules_lines:1:keyword |
| warning | multiple_relational_clause_groups_on_line | Carrion Dredger | fact:play:carrion-dredger:a627978f:rules_lines:0:identity_or_descriptor:has_keyword:0 | clause:play:carrion-dredger:a627978f:rules_lines:0:ability, clause:play:carrion-dredger:a627978f:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Combat Chef | fact:play:combat-chef:404f2e45:rules_lines:0:event_produced:attach:0 | clause:play:combat-chef:404f2e45:rules_lines:0:ability, clause:play:combat-chef:404f2e45:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Crowd Favorite | fact:play:crowd-favorite:59f362fc:rules_lines:1:cost_or_requirement:pay:0 | clause:play:crowd-favorite:59f362fc:rules_lines:1:ability, clause:play:crowd-favorite:59f362fc:rules_lines:1:keyword |
| warning | multiple_relational_clause_groups_on_line | Daughter of the Void | fact:play:daughter-of-the-void:41f2894f:rules_lines:0:cost_or_requirement:pay:0 | clause:play:daughter-of-the-void:41f2894f:rules_lines:0:ability, clause:play:daughter-of-the-void:41f2894f:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Diana, Lunari | fact:play:diana-lunari:4a172786:rules_lines:0:event_produced:recycle:0 | clause:play:diana-lunari:4a172786:rules_lines:0:ability, clause:play:diana-lunari:4a172786:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Dramatic Visionary | fact:play:dramatic-visionary:2074f413:rules_lines:0:event_produced:recycle:0 | clause:play:dramatic-visionary:2074f413:rules_lines:0:ability, clause:play:dramatic-visionary:2074f413:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Ember Monk | fact:play:ember-monk:c2ff3a3a:rules_lines:0:state_or_modifier:modify_stat:0 | clause:play:ember-monk:c2ff3a3a:rules_lines:0:ability, clause:play:ember-monk:c2ff3a3a:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Emperor of the Sands | fact:play:emperor-of-the-sands:122152ab:rules_lines:0:state_or_modifier:gain_keyword:0 | clause:play:emperor-of-the-sands:122152ab:rules_lines:0:ability, clause:play:emperor-of-the-sands:122152ab:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Energy Conduit | fact:play:energy-conduit:e3a1b101:rules_lines:0:cost_or_requirement:pay:0 | clause:play:energy-conduit:e3a1b101:rules_lines:0:ability, clause:play:energy-conduit:e3a1b101:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Enthralling Protector | fact:play:enthralling-protector:ca6c0c98:rules_lines:1:cost_or_requirement:pay:0 | clause:play:enthralling-protector:ca6c0c98:rules_lines:1:ability, clause:play:enthralling-protector:ca6c0c98:rules_lines:1:keyword |
| warning | multiple_relational_clause_groups_on_line | Enthusiastic Promoter | fact:play:enthusiastic-promoter:954cad7e:rules_lines:1:event_produced:buff:0 | clause:play:enthusiastic-promoter:954cad7e:rules_lines:1:ability, clause:play:enthusiastic-promoter:954cad7e:rules_lines:1:keyword |
| warning | multiple_relational_clause_groups_on_line | Ezreal, Dashing | fact:play:ezreal-dashing:293244ee:rules_lines:2:cost_or_requirement:pay:0 | clause:play:ezreal-dashing:293244ee:rules_lines:2:ability, clause:play:ezreal-dashing:293244ee:rules_lines:2:keyword |
| warning | multiple_relational_clause_groups_on_line | Fiora, Victorious | fact:play:fiora-victorious:92559485:rules_lines:0:state_or_modifier:gain_keyword:0 | clause:play:fiora-victorious:92559485:rules_lines:0:ability, clause:play:fiora-victorious:92559485:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Fiora, Worthy | fact:play:fiora-worthy:e3105fbc:rules_lines:0:state_or_modifier:ready:0 | clause:play:fiora-worthy:e3105fbc:rules_lines:0:ability, clause:play:fiora-worthy:e3105fbc:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Fire Below the Mountain | fact:play:fire-below-the-mountain:2b9c0e7f:rules_lines:0:cost_or_requirement:pay:0 | clause:play:fire-below-the-mountain:2b9c0e7f:rules_lines:0:ability, clause:play:fire-below-the-mountain:2b9c0e7f:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Flurry of Feathers | fact:play:flurry-of-feathers:ab222324:rules_lines:3:payoff_output:play_token:0 | clause:play:flurry-of-feathers:ab222324:rules_lines:3:ability, clause:play:flurry-of-feathers:ab222324:rules_lines:3:keyword |
| warning | multiple_relational_clause_groups_on_line | Forgotten Library | fact:play:forgotten-library:f1e10333:rules_lines:0:event_produced:recycle:0 | clause:play:forgotten-library:f1e10333:rules_lines:0:ability, clause:play:forgotten-library:f1e10333:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Frisky Hunter | fact:play:frisky-hunter:a3ac8a1f:rules_lines:0:payoff_output:play_token:0 | clause:play:frisky-hunter:a3ac8a1f:rules_lines:0:ability, clause:play:frisky-hunter:a3ac8a1f:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Garen, Rugged | fact:play:garen-rugged:397ab8eb:rules_lines:0:identity_or_descriptor:has_keyword:0 | clause:play:garen-rugged:397ab8eb:rules_lines:0:ability, clause:play:garen-rugged:397ab8eb:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Grand Duelist | fact:play:grand-duelist:53b0f72b:rules_lines:0:cost_or_requirement:exhaust:0 | clause:play:grand-duelist:53b0f72b:rules_lines:0:ability, clause:play:grand-duelist:53b0f72b:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Guerilla Warfare | fact:play:guerilla-warfare:5df47749:rules_lines:0:payoff_output:return_to_hand:0 | clause:play:guerilla-warfare:5df47749:rules_lines:0:ability, clause:play:guerilla-warfare:5df47749:rules_lines:0:keyword |
| warning | multiple_relational_clause_groups_on_line | Gustwalker | fact:play:gustwalker:e1514be6:rules_lines:1:identity_or_descriptor:has_keyword:0 | clause:play:gustwalker:e1514be6:rules_lines:1:ability, clause:play:gustwalker:e1514be6:rules_lines:1:keyword |

## Relation Readiness

- produced event ids: 23
- observed event ids: 22
- output ids: 46
- relational text lines with facts: 1068
- relational text lines without facts: 1
- produced events without observers: 10
- observed events without producers: 2

### Web Uses

- similarity: 6311
- filters: 5834
- deck_synergy: 1830
- enables: 1207
- enabled_by: 358

### Role Payload Issues

- multiple_relational_clause_groups_on_line: 90
- optional_line_without_optional_modality: 88
- payoff_without_output: 1

### Produced Events Without Observers

- spell_countered: 9
- gear_dies: 9
- token_created: 64
- equipment_detached: 3
- damage_dealt: 75
- card_banished: 19
- unit_dies: 19
- card_discarded: 23
- card_moved: 1
- control_changed: 5

### Observed Events Without Producers

- combat_won: 5
- self_discarded: 1

## Top Uncovered Text Lines

| Card | Source | Line | Text |
| --- | --- | --- | --- |
| play:bandle-tree:1887131e | rules_lines | 0 | You may hide an additional card here. |
| play:baron-pit:245edbb0 | rules_lines | 0 | (You can't start the game with a token battlefield.) |
| play:blue-sentinel:1175ef0a | rules_lines | 1 | Your hold effects for holding here trigger an additional time. |
| play:caitlyn-patrolling:4a8d3da6 | rules_lines | 0 | I must be assigned combat damage last. |
| play:curtain-call:ca540b49 | rules_lines | 1 | Choose one you haven't already chosen — |
| play:disposal-order:68d05fb8 | rules_lines | 1 | Choose one — |
| play:experimental-hexplate:cb371eec | effect_lines | 0 | I am a Mech. |
| play:flurry-of-feathers:ab222324 | rules_lines | 1 | Choose one — |
| play:gearhead:a59c38ca | rules_lines | 1 | Each Equipment attached to me gives double its base Might bonus. |
| play:heimerdinger-inventor:2b2dc5bb | rules_lines | 0 | I have all :rb_exhaust: abilities of all friendly legends, units, and gear. |
| play:maduli-the-gatekeeper:29bfb45b | rules_lines | 0 | I can't be readied. |
| play:red-brambleback:5b4a4085 | rules_lines | 1 | Your conquer effects for conquering here trigger an additional time. |
| play:renata-glasc-mastermind:fa1087ce | rules_lines | 2 | Use my abilities only while I'm at a battlefield. |
| play:rocket-barrage:1ee001f2 | rules_lines | 1 | Choose one — |
| play:rumble-scrapper:c635249a | rules_lines | 0 | Your Mechs have +1 :rb_might: (including me). |
| play:scuttle-crab:8c3955ab | rules_lines | 0 | (Units with 0 :rb_might: can conquer and hold.) |
| play:sky-splitter:98da3e56 | rules_lines | 1 | This spell's Energy cost is reduced by the highest Might among units you control. |
| play:skyfall-of-areion:91394768 | effect_lines | 0 | My hold effects are also conquer effects, and vice versa. |
| play:soraka-wanderer:81c0ff4a | rules_lines | 0 | I must be assigned combat damage last. |
| play:wuju-bladesman-starter:17a1e7bb | rules_lines | 0 | While a friendly unit defends alone, it gets +2 :rb_might:. |

## Top Uncovered Relational Text Lines

| Card | Source | Line | Text |
| --- | --- | --- | --- |
| play:curtain-call:ca540b49 | rules_lines | 1 | Choose one you haven't already chosen — |
