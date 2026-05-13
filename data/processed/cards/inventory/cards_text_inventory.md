# Cards Text Inventory

Pure inventory of card text lines from `data/processed/cards/normalized/cards_normalized.json`.
It does not read extracted facts, reports, or web relations. Candidate families are heuristic suggestions only.

## Summary

- Cards: 767
- Cards with text: 753
- Text lines: 1248
- Unique normalized lines: 873
- Unique parameterized lines: 811
- Text unit occurrences: 2337
- Unique normalized units: 1209
- Unique parameterized units: 1092
- Lines without candidate family: 0 unique / 0 occurrences
- Lines with 4+ candidate families: 272 unique / 317 occurrences
- Units without candidate family: 0 unique / 0 occurrences
- Units with 3+ candidate families: 317 unique / 379 occurrences
- Source fields: {"effect_lines": 27, "rules_lines": 1221}

## Surface Flags

| Flag | Occurrences | Unique lines |
| --- | --- | --- |
| contains_number | 654 | 533 |
| contains_bracket_keyword | 580 | 248 |
| contains_rb_symbol | 541 | 401 |
| starts_when | 298 | 295 |
| contains_additional | 96 | 66 |
| contains_cant_cannot | 39 | 38 |
| starts_if | 25 | 25 |
| contains_instead | 23 | 22 |
| starts_you_may | 22 | 18 |
| starts_while | 20 | 20 |
| starts_this | 6 | 4 |

## Candidate Family Suggestions

| Family | Occurrences | Unique lines | Cards |
| --- | --- | --- | --- |
| keyword_reminder | 455 | 124 | 353 |
| cost_modifier | 256 | 195 | 228 |
| combat_modifier | 244 | 183 | 216 |
| location_restriction | 236 | 219 | 220 |
| stat_modifier | 225 | 196 | 221 |
| deck_manipulation | 177 | 159 | 170 |
| ready_exhaust_effect | 177 | 148 | 170 |
| timing_window | 177 | 48 | 172 |
| duration_modifier | 162 | 160 | 158 |
| movement_modifier | 153 | 137 | 146 |
| damage_effect | 140 | 109 | 129 |
| removal_or_healing | 119 | 114 | 114 |
| target_selection | 102 | 78 | 97 |
| token_creation | 76 | 74 | 75 |
| trigger_modifier | 72 | 61 | 72 |
| attachment_modifier | 71 | 39 | 60 |
| xp_progression | 65 | 54 | 45 |
| keyword_modifier | 62 | 59 | 62 |
| play_permission | 55 | 38 | 51 |
| entry_state | 52 | 27 | 52 |
| buff_effect | 51 | 49 | 47 |
| resource_generation | 50 | 40 | 49 |
| hide_modifier | 41 | 10 | 40 |
| tag_reference | 30 | 30 | 26 |
| replacement_effect | 26 | 25 | 25 |
| resource_add_ability | 26 | 26 | 25 |
| stun_effect | 26 | 26 | 26 |
| trait_identity | 24 | 24 | 23 |
| score_modifier | 22 | 22 | 21 |
| banish_effect | 20 | 20 | 18 |
| conditional_resolution | 19 | 18 | 19 |
| contextual_clarification | 17 | 7 | 17 |
| choice_modal | 9 | 7 | 8 |
| counter_effect | 9 | 8 | 9 |
| usage_restriction | 8 | 8 | 8 |
| effect_equivalence | 7 | 7 | 7 |
| control_change | 6 | 6 | 5 |
| copy_effect | 6 | 6 | 6 |
| target_protection | 4 | 3 | 4 |
| turn_sequence | 4 | 4 | 4 |
| deckbuilding_restriction | 3 | 1 | 3 |
| play_restriction | 3 | 3 | 3 |
| modal_option | 2 | 2 | 2 |
| type_exclusion | 2 | 2 | 2 |
| ability_sharing | 1 | 1 | 1 |
| effect_suppression | 1 | 1 | 1 |

## Candidate Family Count Distribution

| Family count | Occurrences | Unique lines |
| --- | --- | --- |
| 1 | 155 | 132 |
| 2 | 459 | 245 |
| 3 | 317 | 224 |
| 4 | 195 | 154 |
| 5 | 70 | 67 |
| 6 | 33 | 32 |
| 7 | 14 | 14 |
| 8 | 3 | 3 |
| 9 | 1 | 1 |
| 10 | 1 | 1 |

## Unit Kind Counts

| Unit kind | Occurrences | Unique units |
| --- | --- | --- |
| effect | 752 | 544 |
| reminder | 670 | 161 |
| timing | 464 | 311 |
| keyword_marker | 234 | 29 |
| condition | 104 | 102 |
| activation_cost | 77 | 36 |
| restriction | 30 | 25 |
| choice_header | 6 | 4 |

## Unit Candidate Family Count Distribution

| Family count | Occurrences | Unique units |
| --- | --- | --- |
| 1 | 914 | 397 |
| 2 | 1044 | 495 |
| 3 | 282 | 225 |
| 4 | 75 | 70 |
| 5 | 17 | 17 |
| 6 | 5 | 5 |

## Top Openings

| Opening | Occurrences | Unique lines | Cards | Sources |
| --- | --- | --- | --- | --- |
| When you play me | 84 | 83 | 84 | {"rules_lines": 84} |
| [Action] | 73 | 1 | 73 | {"rules_lines": 73} |
| [Reaction] | 57 | 3 | 57 | {"rules_lines": 57} |
| [Equip] | 36 | 15 | 36 | {"rules_lines": 36} |
| [Hidden] | 32 | 1 | 32 | {"rules_lines": 32} |
| [Accelerate] | 24 | 6 | 24 | {"rules_lines": 24} |
| [Deflect] | 20 | 1 | 20 | {"effect_lines": 1, "rules_lines": 19} |
| [Repeat] | 20 | 10 | 20 | {"rules_lines": 20} |
| [Tank] | 19 | 1 | 19 | {"effect_lines": 1, "rules_lines": 18} |
| When I attack | 18 | 18 | 18 | {"rules_lines": 18} |
| [Ganking] | 15 | 1 | 15 | {"effect_lines": 1, "rules_lines": 14} |
| When I conquer | 15 | 14 | 15 | {"effect_lines": 5, "rules_lines": 10} |
| :rb_exhaust:: [Reaction] | 14 | 14 | 14 | {"rules_lines": 14} |
| [Deathknell] | 14 | 13 | 14 | {"effect_lines": 2, "rules_lines": 12} |
| When I hold | 14 | 13 | 14 | {"effect_lines": 2, "rules_lines": 12} |
| [Ambush] | 12 | 1 | 12 | {"rules_lines": 12} |
| When you conquer here | 12 | 12 | 12 | {"rules_lines": 12} |
| When you hold here | 12 | 12 | 12 | {"rules_lines": 12} |
| [Weaponmaster] | 10 | 2 | 10 | {"rules_lines": 10} |
| [Assault 2] | 9 | 2 | 9 | {"effect_lines": 1, "rules_lines": 8} |
| [Deathknell][>] | 9 | 9 | 9 | {"rules_lines": 9} |
| [Level 6][>] | 9 | 9 | 9 | {"rules_lines": 9} |
| [Shield] | 9 | 1 | 9 | {"rules_lines": 9} |
| When I move | 9 | 9 | 9 | {"effect_lines": 1, "rules_lines": 8} |
| When I move to a battlefield | 9 | 9 | 9 | {"rules_lines": 9} |
| [Assault] | 8 | 1 | 8 | {"rules_lines": 8} |
| When you play this | 8 | 8 | 8 | {"rules_lines": 8} |
| :rb_energy_1 | 7 | 7 | 7 | {"rules_lines": 7} |
| [Hunt] | 7 | 1 | 7 | {"effect_lines": 1, "rules_lines": 6} |
| [Legion] | 7 | 7 | 7 | {"rules_lines": 7} |
| [Vision] | 7 | 2 | 7 | {"rules_lines": 7} |
| Deal 2 to a unit | 7 | 2 | 2 | {"rules_lines": 7} |
| Draw 1 | 7 | 2 | 7 | {"rules_lines": 7} |
| When I attack or defend | 7 | 7 | 7 | {"effect_lines": 2, "rules_lines": 5} |
| [Level 3][>] | 6 | 6 | 6 | {"effect_lines": 1, "rules_lines": 5} |
| [Temporary] | 6 | 4 | 6 | {"rules_lines": 6} |
| Deal 2 to a unit at a battlefield | 6 | 4 | 6 | {"rules_lines": 6} |
| I enter ready | 6 | 1 | 6 | {"rules_lines": 6} |
| When you conquer | 6 | 6 | 6 | {"rules_lines": 6} |
| [Hunt 2] | 5 | 1 | 5 | {"rules_lines": 5} |

## Top Parameterized Lines

| Occurrences | Unique lines | Cards | Parameterized line | Candidate families |
| --- | --- | --- | --- | --- |
| 73 | 1 | 73 | [action] (play on your turn or in showdowns.) | timing_window, keyword_reminder |
| 53 | 1 | 53 | [reaction] (play any time, even before spells and abilities resolve.) | timing_window, keyword_reminder |
| 32 | 1 | 32 | [hidden] (hide now for {rb_symbol} to react with later for {rb_symbol}.) | hide_modifier, keyword_reminder |
| 27 | 7 | 27 | [equip] {rb_symbol} ({rb_symbol}: attach this to a unit you control.) | keyword_reminder, attachment_modifier |
| 24 | 6 | 24 | [accelerate] (you may pay {rb_symbol}{rb_symbol} as an additional cost to have me enter ready.) | ready_exhaust_effect, entry_state, cost_modifier, keyword_reminder |
| 20 | 1 | 20 | [deflect] (opponents must pay {rb_symbol} to choose me with a spell or ability.) | target_selection, cost_modifier, keyword_reminder |
| 19 | 1 | 19 | [tank] (i must be assigned combat damage first.) | combat_modifier, keyword_reminder, damage_effect |
| 15 | 1 | 15 | [ganking] (i can move from battlefield to battlefield.) | movement_modifier, keyword_reminder |
| 14 | 4 | 14 | [repeat] {rb_symbol} (you may pay the additional cost to repeat this spell's effect.) | trigger_modifier, cost_modifier, keyword_reminder |
| 12 | 1 | 12 | [ambush] (you may play me as a [reaction] to a battlefield where you have units.) | play_permission, location_restriction, keyword_reminder |
| 11 | 4 | 11 | draw {number}. | deck_manipulation |
| 10 | 4 | 4 | deal {number} to a unit. | damage_effect |
| 10 | 3 | 10 | [assault {number}] (+{number} {rb_symbol} while i'm an attacker.) | combat_modifier, stat_modifier, keyword_reminder |
| 9 | 1 | 9 | [shield] (+{number} {rb_symbol} while i'm a defender.) | combat_modifier, stat_modifier, keyword_reminder |
| 9 | 1 | 9 | [weaponmaster] (when you play me, you may [equip] one of your equipment to me for {rb_symbol} less, even if it's already attached.) | contextual_clarification, cost_modifier, keyword_reminder, attachment_modifier |
| 8 | 1 | 8 | [assault] (+{number} {rb_symbol} while i'm an attacker.) | combat_modifier, stat_modifier, keyword_reminder |
| 7 | 7 | 7 | {rb_symbol}: [reaction] - [add] {rb_symbol}. (abilities that add resources can't be reacted to.) | resource_add_ability |
| 7 | 3 | 7 | [shield {number}] (+{number} {rb_symbol} while i'm a defender.) | combat_modifier, stat_modifier, keyword_reminder |
| 7 | 1 | 7 | [hunt] (when i conquer or hold, gain {number} xp.) | combat_modifier, resource_generation, keyword_reminder, xp_progression |
| 6 | 4 | 6 | deal {number} to a unit at a battlefield. | location_restriction, damage_effect |
| 6 | 2 | 6 | [hunt {number}] (when i conquer or hold, gain {number} xp.) | combat_modifier, resource_generation, keyword_reminder, xp_progression |
| 6 | 1 | 6 | [vision] (when you play me, look at the top card of your main deck. you may recycle it.) | keyword_reminder, deck_manipulation |
| 6 | 1 | 6 | i enter ready. | ready_exhaust_effect, entry_state |
| 5 | 5 | 5 | give a unit +{number} {rb_symbol} this turn. | duration_modifier, stat_modifier |
| 5 | 4 | 5 | [equip] {rb_symbol}{rb_symbol} ({rb_symbol}{rb_symbol}: attach this to a unit you control.) | keyword_reminder, attachment_modifier |
| 5 | 4 | 5 | you may pay {rb_symbol} as an additional cost to play me. | cost_modifier |
| 4 | 1 | 4 | [backline] (i must be assigned combat damage last.) | combat_modifier, keyword_reminder, damage_effect |
| 4 | 1 | 4 | [quick-draw] (this has [reaction]. when you play it, attach it to a unit you control.) | play_permission, keyword_modifier, keyword_reminder, attachment_modifier, deck_manipulation |
| 3 | 3 | 3 | [repeat] {rb_symbol}{rb_symbol} (you may pay the additional cost to repeat this spell's effect.) | trigger_modifier, cost_modifier, keyword_reminder |
| 3 | 3 | 3 | give a unit -{number} {rb_symbol} this turn. | duration_modifier, stat_modifier |
| 3 | 3 | 3 | give a unit [assault {number}] this turn. (+{number} {rb_symbol} while it's an attacker.) | duration_modifier, keyword_modifier, combat_modifier, stat_modifier |
| 3 | 1 | 3 | [deflect {number}] (opponents must pay {rb_symbol}{rb_symbol} to choose me with a spell or ability.) | target_selection, cost_modifier, keyword_reminder |
| 3 | 1 | 3 | [reaction] (play any time, even before spells and abilities resolve, including to a battlefield you control.) | contextual_clarification, location_restriction, timing_window, keyword_reminder |
| 3 | 1 | 3 | [temporary] (kill this at the start of its controller's beginning phase, before scoring.) | timing_window, keyword_reminder, removal_or_healing |
| 3 | 1 | 3 | [unique] (your deck can have only {number} card with this name.) | deckbuilding_restriction, keyword_reminder |
| 3 | 1 | 3 | choose one - | choice_modal, target_selection |
| 3 | 1 | 3 | this enters exhausted. | ready_exhaust_effect, entry_state |
| 3 | 1 | 3 | you may play me to an open battlefield. | play_permission |
| 2 | 2 | 2 | [level {number}][>] i have +{number} {rb_symbol}. (while you have {number}+ xp, get the effect.) | trigger_modifier, stat_modifier, keyword_reminder, xp_progression |
| 2 | 2 | 2 | [reaction][>] {rb_symbol}: [add] {rb_symbol}. (abilities that add resources can't be reacted to.) | resource_add_ability, timing_window, keyword_reminder |
| 2 | 2 | 2 | draw {number} and channel {number} rune exhausted. | ready_exhaust_effect, resource_generation, deck_manipulation |
| 2 | 2 | 2 | give friendly units +{number} {rb_symbol} this turn. | duration_modifier, stat_modifier |
| 2 | 2 | 2 | give two friendly units each +{number} {rb_symbol} this turn. | duration_modifier, stat_modifier |
| 2 | 2 | 2 | when i hold, draw {number}. | combat_modifier, deck_manipulation |
| 2 | 2 | 2 | when you play a spell, give me +{number} {rb_symbol} this turn. | duration_modifier, stat_modifier |
| 2 | 2 | 2 | when you play me, discard {number}, then draw {number}. | deck_manipulation |
| 2 | 2 | 2 | when you play me, discard {number}. | deck_manipulation |
| 2 | 2 | 2 | when you play me, gain {number} xp. | resource_generation, xp_progression |
| 2 | 2 | 2 | you may pay {rb_symbol}{rb_symbol} as an additional cost to play me. | cost_modifier |
| 2 | 2 | 2 | {rb_symbol}: [reaction] - [add] {rb_symbol}. use only to play spells. (abilities that add resources can't be reacted to.) | resource_add_ability, usage_restriction |

## Top Atomic Units

| Occurrences | Lines | Cards | Kind | Unit | Parameterized unit | Candidate families |
| --- | --- | --- | --- | --- | --- | --- |
| 76 | 4 | 76 | timing | [Action] | [action] | timing_window, keyword_reminder |
| 73 | 1 | 73 | reminder | Play on your turn or in showdowns. | play on your turn or in showdowns. | timing_window |
| 70 | 16 | 70 | timing | [Reaction] | [reaction] | timing_window, keyword_reminder |
| 53 | 1 | 53 | reminder | Play any time, even before spells and abilities resolve. | play any time, even before spells and abilities resolve. | timing_window |
| 33 | 2 | 33 | reminder | Hide now for :rb_rune_rainbow: to react with later for :rb_energy_0:. | hide now for {rb_symbol} to react with later for {rb_symbol}. | hide_modifier |
| 32 | 26 | 32 | effect | Draw 1. | draw {number}. | deck_manipulation |
| 32 | 1 | 32 | keyword_marker | [Hidden] | [hidden] | hide_modifier, keyword_reminder |
| 30 | 29 | 30 | activation_cost | :rb_exhaust: | {rb_symbol} | symbol_option, cost_modifier |
| 24 | 6 | 24 | keyword_marker | [Accelerate] | [accelerate] | keyword_reminder |
| 20 | 20 | 20 | reminder | Abilities that add resources can't be reacted to. | abilities that add resources can't be reacted to. | resource_add_ability |
| 20 | 19 | 20 | reminder | When I die, get the effect. | when i die, get the effect. | trigger_modifier, removal_or_healing |
| 20 | 6 | 20 | reminder | I can move from battlefield to battlefield. | i can move from battlefield to battlefield. | movement_modifier |
| 20 | 1 | 20 | keyword_marker | [Deflect] | [deflect] | keyword_reminder |
| 20 | 1 | 20 | reminder | Opponents must pay :rb_rune_rainbow: to choose me with a spell or ability. | opponents must pay {rb_symbol} to choose me with a spell or ability. | target_selection, cost_modifier |
| 19 | 1 | 19 | keyword_marker | [Tank] | [tank] | combat_modifier, keyword_reminder |
| 19 | 1 | 19 | reminder | I must be assigned combat damage first. | i must be assigned combat damage first. | combat_modifier, damage_effect |
| 18 | 8 | 18 | reminder | You may pay the additional cost to repeat this spell's effect. | you may pay the additional cost to repeat this spell's effect. | trigger_modifier, cost_modifier |
| 15 | 1 | 15 | keyword_marker | [Ganking] | [ganking] | movement_modifier, keyword_reminder |
| 14 | 13 | 14 | keyword_marker | [Deathknell] | [deathknell] | keyword_reminder |
| 13 | 13 | 13 | reminder | It doesn't deal combat damage this turn. | it doesn't deal combat damage this turn. | duration_modifier, combat_modifier, damage_effect |
| 13 | 7 | 13 | reminder | You may recycle it. | you may recycle it. | deck_manipulation |
| 12 | 1 | 12 | keyword_marker | [Ambush] | [ambush] | keyword_reminder |
| 12 | 1 | 12 | reminder | You may play me as a [Reaction] to a battlefield where you have units. | you may play me as a [reaction] to a battlefield where you have units. | play_permission, location_restriction |
| 11 | 1 | 11 | effect | [Repeat] :rb_energy_2: | [repeat] {rb_symbol} | trigger_modifier, keyword_reminder |
| 10 | 10 | 10 | reminder | If it doesn't have a buff, it gets a +1 :rb_might: buff. | if it doesn't have a buff, it gets a +{number} {rb_symbol} buff. | buff_effect, stat_modifier |
| 10 | 2 | 10 | keyword_marker | [Weaponmaster] | [weaponmaster] | keyword_reminder |
| 9 | 8 | 9 | reminder | This isn't a move. | this isn't a move. | movement_modifier |
| 9 | 2 | 9 | reminder | +1 :rb_might: while I'm an attacker. | +{number} {rb_symbol} while i'm an attacker. | combat_modifier, stat_modifier |
| 9 | 1 | 9 | reminder | +1 :rb_might: while I'm a defender. | +{number} {rb_symbol} while i'm a defender. | combat_modifier, stat_modifier |
| 9 | 1 | 9 | keyword_marker | [Shield] | [shield] | combat_modifier, keyword_reminder |
| 9 | 1 | 9 | reminder | When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less, even if it's already attached. | when you play me, you may [equip] one of your equipment to me for {rb_symbol} less, even if it's already attached. | contextual_clarification, cost_modifier, attachment_modifier |
| 9 | 1 | 9 | reminder | You may pay :rb_energy_1::rb_rune_fury: as an additional cost to have me enter ready. | you may pay {rb_symbol}{rb_symbol} as an additional cost to have me enter ready. | ready_exhaust_effect, entry_state, cost_modifier |
| 8 | 8 | 8 | keyword_marker | [Legion] | [legion] | keyword_reminder |
| 8 | 8 | 8 | reminder | A unit is Mighty while it has 5+ :rb_might:. | a unit is mighty while it has {number}+ {rb_symbol}. | trait_identity |
| 8 | 8 | 8 | reminder | Get the effect if you've played another card this turn. | get the effect if you've played another card this turn. | duration_modifier, trigger_modifier |
| 8 | 8 | 8 | reminder | Kill it at the start of its controller's Beginning Phase, before scoring. | kill it at the start of its controller's beginning phase, before scoring. | timing_window, removal_or_healing |
| 8 | 6 | 8 | effect | Draw 2. | draw {number}. | deck_manipulation |
| 8 | 1 | 8 | reminder | +2 :rb_might: while I'm an attacker. | +{number} {rb_symbol} while i'm an attacker. | combat_modifier, stat_modifier |
| 8 | 1 | 8 | keyword_marker | [Assault 2] | [assault {number}] | combat_modifier, keyword_reminder |
| 8 | 1 | 8 | keyword_marker | [Assault] | [assault] | combat_modifier, keyword_reminder |
| 7 | 7 | 7 | activation_cost | :rb_energy_1:, :rb_exhaust: | {rb_symbol}, {rb_symbol} | cost_modifier |
| 7 | 7 | 7 | reminder | If I don't have a buff, I get a +1 :rb_might: buff. | if i don't have a buff, i get a +{number} {rb_symbol} buff. | buff_effect, stat_modifier |
| 7 | 7 | 7 | effect | Recycle the rest. | recycle the rest. | deck_manipulation |
| 7 | 6 | 7 | reminder | Send it to base. | send it to base. | movement_modifier |
| 7 | 2 | 7 | keyword_marker | [Vision] | [vision] | keyword_reminder |
| 7 | 2 | 2 | effect | Deal 2 to a unit. | deal {number} to a unit. | damage_effect |
| 7 | 1 | 7 | keyword_marker | [Hunt] | [hunt] | keyword_reminder |
| 7 | 1 | 7 | reminder | When I conquer or hold, gain 1 XP. | when i conquer or hold, gain {number} xp. | combat_modifier, resource_generation, xp_progression |
| 6 | 6 | 6 | effect | Channel 1 rune exhausted. | channel {number} rune exhausted. | ready_exhaust_effect, resource_generation |
| 6 | 6 | 6 | reminder | While you have 3+ XP, get the effect. | while you have {number}+ xp, get the effect. | trigger_modifier, xp_progression |
| 6 | 6 | 6 | reminder | While you have 6+ XP, get the effect. | while you have {number}+ xp, get the effect. | trigger_modifier, xp_progression |
| 6 | 6 | 6 | reminder | You must still pay its Power cost. | you must still pay its power cost. | cost_modifier, stat_modifier |
| 6 | 4 | 6 | keyword_marker | [Temporary] | [temporary] | keyword_reminder |
| 6 | 4 | 6 | effect | Deal 2 to a unit at a battlefield. | deal {number} to a unit at a battlefield. | location_restriction, damage_effect |
| 6 | 2 | 6 | reminder | I must be assigned combat damage last. | i must be assigned combat damage last. | combat_modifier, damage_effect |
| 6 | 1 | 6 | effect | I enter ready. | i enter ready. | ready_exhaust_effect, entry_state |
| 6 | 1 | 6 | reminder | When you play me, look at the top card of your Main Deck. | when you play me, look at the top card of your main deck. | deck_manipulation |
| 5 | 5 | 5 | effect | Choose a unit. | choose a unit. | target_selection |
| 5 | 5 | 5 | effect | draw it. | draw it. | deck_manipulation |
| 5 | 5 | 5 | effect | They deal damage equal to their Mights to each other. | they deal damage equal to their mights to each other. | damage_effect |

## Top Parameterized Atomic Units

| Occurrences | Lines | Cards | Kind | Parameterized unit | Candidate families |
| --- | --- | --- | --- | --- | --- |
| 76 | 4 | 76 | timing | [action] | timing_window, keyword_reminder |
| 73 | 1 | 73 | reminder | play on your turn or in showdowns. | timing_window |
| 70 | 16 | 70 | timing | [reaction] | timing_window, keyword_reminder |
| 53 | 1 | 53 | reminder | play any time, even before spells and abilities resolve. | timing_window |
| 42 | 34 | 42 | effect | draw {number}. | deck_manipulation |
| 36 | 35 | 34 | activation_cost | {rb_symbol} | symbol_option, cost_modifier |
| 33 | 2 | 33 | reminder | hide now for {rb_symbol} to react with later for {rb_symbol}. | hide_modifier |
| 32 | 1 | 32 | keyword_marker | [hidden] | hide_modifier, keyword_reminder |
| 27 | 7 | 27 | effect | [equip] {rb_symbol} | keyword_reminder, attachment_modifier |
| 27 | 7 | 27 | reminder | {rb_symbol}: attach this to a unit you control. | attachment_modifier |
| 24 | 6 | 24 | keyword_marker | [accelerate] | keyword_reminder |
| 24 | 6 | 24 | reminder | you may pay {rb_symbol}{rb_symbol} as an additional cost to have me enter ready. | ready_exhaust_effect, entry_state, cost_modifier |
| 20 | 20 | 20 | reminder | abilities that add resources can't be reacted to. | resource_add_ability |
| 20 | 19 | 20 | reminder | when i die, get the effect. | trigger_modifier, removal_or_healing |
| 20 | 6 | 20 | reminder | i can move from battlefield to battlefield. | movement_modifier |
| 20 | 1 | 20 | keyword_marker | [deflect] | keyword_reminder |
| 20 | 1 | 20 | reminder | opponents must pay {rb_symbol} to choose me with a spell or ability. | target_selection, cost_modifier |
| 19 | 5 | 19 | reminder | +{number} {rb_symbol} while i'm an attacker. | combat_modifier, stat_modifier |
| 19 | 1 | 19 | keyword_marker | [tank] | combat_modifier, keyword_reminder |
| 19 | 1 | 19 | reminder | i must be assigned combat damage first. | combat_modifier, damage_effect |
| 18 | 8 | 18 | reminder | you may pay the additional cost to repeat this spell's effect. | trigger_modifier, cost_modifier |
| 16 | 4 | 16 | reminder | +{number} {rb_symbol} while i'm a defender. | combat_modifier, stat_modifier |
| 15 | 15 | 15 | effect | [add] {rb_symbol}. | resource_add_ability, keyword_reminder |
| 15 | 1 | 15 | keyword_marker | [ganking] | movement_modifier, keyword_reminder |
| 14 | 13 | 14 | keyword_marker | [deathknell] | keyword_reminder |
| 14 | 4 | 14 | effect | [repeat] {rb_symbol} | trigger_modifier, keyword_reminder |
| 13 | 13 | 13 | reminder | it doesn't deal combat damage this turn. | duration_modifier, combat_modifier, damage_effect |
| 13 | 13 | 13 | reminder | while you have {number}+ xp, get the effect. | trigger_modifier, xp_progression |
| 13 | 11 | 13 | effect | deal {number} to a unit at a battlefield. | location_restriction, damage_effect |
| 13 | 7 | 13 | reminder | you may recycle it. | deck_manipulation |
| 13 | 3 | 13 | reminder | when i conquer or hold, gain {number} xp. | combat_modifier, resource_generation, xp_progression |
| 12 | 12 | 12 | activation_cost | {rb_symbol}, {rb_symbol} | cost_modifier |
| 12 | 6 | 6 | effect | deal {number} to a unit. | damage_effect |
| 12 | 1 | 12 | keyword_marker | [ambush] | keyword_reminder |
| 12 | 1 | 12 | reminder | you may play me as a [reaction] to a battlefield where you have units. | play_permission, location_restriction |
| 10 | 10 | 10 | reminder | if it doesn't have a buff, it gets a +{number} {rb_symbol} buff. | buff_effect, stat_modifier |
| 10 | 3 | 10 | keyword_marker | [assault {number}] | combat_modifier, keyword_reminder |
| 10 | 2 | 10 | keyword_marker | [weaponmaster] | keyword_reminder |
| 9 | 8 | 9 | effect | give a unit +{number} {rb_symbol} this turn. | duration_modifier, stat_modifier |
| 9 | 8 | 9 | reminder | this isn't a move. | movement_modifier |
| 9 | 1 | 9 | keyword_marker | [shield] | combat_modifier, keyword_reminder |
| 9 | 1 | 9 | reminder | when you play me, you may [equip] one of your equipment to me for {rb_symbol} less, even if it's already attached. | contextual_clarification, cost_modifier, attachment_modifier |
| 8 | 8 | 8 | keyword_marker | [legion] | keyword_reminder |
| 8 | 8 | 8 | reminder | a unit is mighty while it has {number}+ {rb_symbol}. | trait_identity |
| 8 | 8 | 8 | reminder | get the effect if you've played another card this turn. | duration_modifier, trigger_modifier |
| 8 | 8 | 8 | reminder | kill it at the start of its controller's beginning phase, before scoring. | timing_window, removal_or_healing |
| 8 | 1 | 8 | keyword_marker | [assault] | combat_modifier, keyword_reminder |
| 7 | 7 | 7 | reminder | if i don't have a buff, i get a +{number} {rb_symbol} buff. | buff_effect, stat_modifier |
| 7 | 7 | 7 | effect | recycle the rest. | deck_manipulation |
| 7 | 6 | 7 | reminder | send it to base. | movement_modifier |
| 7 | 3 | 7 | keyword_marker | [shield {number}] | combat_modifier, keyword_reminder |
| 7 | 2 | 7 | keyword_marker | [vision] | keyword_reminder |
| 7 | 1 | 7 | keyword_marker | [hunt] | keyword_reminder |
| 6 | 6 | 6 | effect | channel {number} rune exhausted. | ready_exhaust_effect, resource_generation |
| 6 | 6 | 6 | reminder | you must still pay its power cost. | cost_modifier, stat_modifier |
| 6 | 4 | 6 | keyword_marker | [temporary] | keyword_reminder |
| 6 | 2 | 6 | keyword_marker | [hunt {number}] | keyword_reminder |
| 6 | 2 | 6 | reminder | i must be assigned combat damage last. | combat_modifier, damage_effect |
| 6 | 1 | 6 | effect | i enter ready. | ready_exhaust_effect, entry_state |
| 6 | 1 | 6 | reminder | when you play me, look at the top card of your main deck. | deck_manipulation |

## Top Repeated Lines

| Occurrences | Cards | Sources | Opening | Parameterized line | Candidate families | Original line |
| --- | --- | --- | --- | --- | --- | --- |
| 73 | 73 | rules_lines | [Action] | [action] (play on your turn or in showdowns.) | timing_window, keyword_reminder | [Action] (Play on your turn or in showdowns.) |
| 53 | 53 | rules_lines | [Reaction] | [reaction] (play any time, even before spells and abilities resolve.) | timing_window, keyword_reminder | [Reaction] (Play any time, even before spells and abilities resolve.) |
| 32 | 32 | rules_lines | [Hidden] | [hidden] (hide now for {rb_symbol} to react with later for {rb_symbol}.) | hide_modifier, keyword_reminder | [Hidden] (Hide now for :rb_rune_rainbow: to react with later for :rb_energy_0:.) |
| 20 | 20 | effect_lines, rules_lines | [Deflect] | [deflect] (opponents must pay {rb_symbol} to choose me with a spell or ability.) | target_selection, cost_modifier, keyword_reminder | [Deflect] (Opponents must pay :rb_rune_rainbow: to choose me with a spell or ability.) |
| 19 | 19 | effect_lines, rules_lines | [Tank] | [tank] (i must be assigned combat damage first.) | combat_modifier, keyword_reminder, damage_effect | [Tank] (I must be assigned combat damage first.) |
| 15 | 15 | effect_lines, rules_lines | [Ganking] | [ganking] (i can move from battlefield to battlefield.) | movement_modifier, keyword_reminder | [Ganking] (I can move from battlefield to battlefield.) |
| 12 | 12 | rules_lines | [Ambush] | [ambush] (you may play me as a [reaction] to a battlefield where you have units.) | play_permission, location_restriction, keyword_reminder | [Ambush] (You may play me as a [Reaction] to a battlefield where you have units.) |
| 11 | 11 | rules_lines | [Repeat] | [repeat] {rb_symbol} (you may pay the additional cost to repeat this spell's effect.) | trigger_modifier, cost_modifier, keyword_reminder | [Repeat] :rb_energy_2: (You may pay the additional cost to repeat this spell's effect.) |
| 9 | 9 | rules_lines | [Accelerate] | [accelerate] (you may pay {rb_symbol}{rb_symbol} as an additional cost to have me enter ready.) | ready_exhaust_effect, entry_state, cost_modifier, keyword_reminder | [Accelerate] (You may pay :rb_energy_1::rb_rune_fury: as an additional cost to have me enter ready.) |
| 9 | 9 | rules_lines | [Shield] | [shield] (+{number} {rb_symbol} while i'm a defender.) | combat_modifier, stat_modifier, keyword_reminder | [Shield] (+1 :rb_might: while I'm a defender.) |
| 9 | 9 | rules_lines | [Weaponmaster] | [weaponmaster] (when you play me, you may [equip] one of your equipment to me for {rb_symbol} less, even if it's already attached.) | contextual_clarification, cost_modifier, keyword_reminder, attachment_modifier | [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less, even if it's already attached.) |
| 8 | 8 | effect_lines, rules_lines | [Assault 2] | [assault {number}] (+{number} {rb_symbol} while i'm an attacker.) | combat_modifier, stat_modifier, keyword_reminder | [Assault 2] (+2 :rb_might: while I'm an attacker.) |
| 8 | 8 | rules_lines | [Assault] | [assault] (+{number} {rb_symbol} while i'm an attacker.) | combat_modifier, stat_modifier, keyword_reminder | [Assault] (+1 :rb_might: while I'm an attacker.) |
| 7 | 7 | effect_lines, rules_lines | [Hunt] | [hunt] (when i conquer or hold, gain {number} xp.) | combat_modifier, resource_generation, keyword_reminder, xp_progression | [Hunt] (When I conquer or hold, gain 1 XP.) |
| 6 | 6 | rules_lines | [Vision] | [vision] (when you play me, look at the top card of your main deck. you may recycle it.) | keyword_reminder, deck_manipulation | [Vision] (When you play me, look at the top card of your Main Deck. You may recycle it.) |
| 6 | 1 | rules_lines | Deal 2 to a unit | deal {number} to a unit. | damage_effect | Deal 2 to a unit. |
| 6 | 6 | rules_lines | Draw 1 | draw {number}. | deck_manipulation | Draw 1. |
| 6 | 6 | rules_lines | I enter ready | i enter ready. | ready_exhaust_effect, entry_state | I enter ready. |
| 5 | 5 | rules_lines | [Accelerate] | [accelerate] (you may pay {rb_symbol}{rb_symbol} as an additional cost to have me enter ready.) | ready_exhaust_effect, entry_state, cost_modifier, keyword_reminder | [Accelerate] (You may pay :rb_energy_1::rb_rune_body: as an additional cost to have me enter ready.) |
| 5 | 5 | rules_lines | [Equip] | [equip] {rb_symbol} ({rb_symbol}: attach this to a unit you control.) | keyword_reminder, attachment_modifier | [Equip] :rb_rune_body: (:rb_rune_body:: Attach this to a unit you control.) |
| 5 | 5 | rules_lines | [Equip] | [equip] {rb_symbol} ({rb_symbol}: attach this to a unit you control.) | keyword_reminder, attachment_modifier | [Equip] :rb_rune_calm: (:rb_rune_calm:: Attach this to a unit you control.) |
| 5 | 5 | rules_lines | [Hunt 2] | [hunt {number}] (when i conquer or hold, gain {number} xp.) | combat_modifier, resource_generation, keyword_reminder, xp_progression | [Hunt 2] (When I conquer or hold, gain 2 XP.) |
| 5 | 5 | effect_lines, rules_lines | [Shield 2] | [shield {number}] (+{number} {rb_symbol} while i'm a defender.) | combat_modifier, stat_modifier, keyword_reminder | [Shield 2] (+2 :rb_might: while I'm a defender.) |
| 4 | 4 | rules_lines | [Accelerate] | [accelerate] (you may pay {rb_symbol}{rb_symbol} as an additional cost to have me enter ready.) | ready_exhaust_effect, entry_state, cost_modifier, keyword_reminder | [Accelerate] (You may pay :rb_energy_1::rb_rune_mind: as an additional cost to have me enter ready.) |
| 4 | 4 | rules_lines | [Backline] | [backline] (i must be assigned combat damage last.) | combat_modifier, keyword_reminder, damage_effect | [Backline] (I must be assigned combat damage last.) |
| 4 | 4 | rules_lines | [Equip] | [equip] {rb_symbol} ({rb_symbol}: attach this to a unit you control.) | keyword_reminder, attachment_modifier | [Equip] :rb_rune_chaos: (:rb_rune_chaos:: Attach this to a unit you control.) |
| 4 | 4 | rules_lines | [Equip] | [equip] {rb_symbol} ({rb_symbol}: attach this to a unit you control.) | keyword_reminder, attachment_modifier | [Equip] :rb_rune_rainbow: (:rb_rune_rainbow:: Attach this to a unit you control.) |
| 4 | 4 | rules_lines | [Quick-Draw] | [quick-draw] (this has [reaction]. when you play it, attach it to a unit you control.) | play_permission, keyword_modifier, keyword_reminder, attachment_modifier, deck_manipulation | [Quick-Draw] (This has [Reaction]. When you play it, attach it to a unit you control.) |
| 3 | 3 | rules_lines | [Accelerate] | [accelerate] (you may pay {rb_symbol}{rb_symbol} as an additional cost to have me enter ready.) | ready_exhaust_effect, entry_state, cost_modifier, keyword_reminder | [Accelerate] (You may pay :rb_energy_1::rb_rune_chaos: as an additional cost to have me enter ready.) |
| 3 | 3 | rules_lines | [Deflect 2] | [deflect {number}] (opponents must pay {rb_symbol}{rb_symbol} to choose me with a spell or ability.) | target_selection, cost_modifier, keyword_reminder | [Deflect 2] (Opponents must pay :rb_rune_rainbow::rb_rune_rainbow: to choose me with a spell or Ability.) |
| 3 | 3 | rules_lines | [Equip] | [equip] {rb_symbol} ({rb_symbol}: attach this to a unit you control.) | keyword_reminder, attachment_modifier | [Equip] :rb_rune_fury: (:rb_rune_fury:: Attach this to a unit you control.) |
| 3 | 3 | rules_lines | [Equip] | [equip] {rb_symbol} ({rb_symbol}: attach this to a unit you control.) | keyword_reminder, attachment_modifier | [Equip] :rb_rune_mind: (:rb_rune_mind:: Attach this to a unit you control.) |
| 3 | 3 | rules_lines | [Equip] | [equip] {rb_symbol} ({rb_symbol}: attach this to a unit you control.) | keyword_reminder, attachment_modifier | [Equip] :rb_rune_order: (:rb_rune_order:: Attach this to a unit you control.) |
| 3 | 3 | rules_lines | [Reaction] | [reaction] (play any time, even before spells and abilities resolve, including to a battlefield you control.) | contextual_clarification, location_restriction, timing_window, keyword_reminder | [Reaction] (Play any time, even before spells and abilities resolve, including to a battlefield you control.) |
| 3 | 3 | rules_lines | [Temporary] | [temporary] (kill this at the start of its controller's beginning phase, before scoring.) | timing_window, keyword_reminder, removal_or_healing | [Temporary] (Kill this at the start of its controller's Beginning Phase, before scoring.) |
| 3 | 3 | rules_lines | [Unique] | [unique] (your deck can have only {number} card with this name.) | deckbuilding_restriction, keyword_reminder | [Unique] (Your deck can have only 1 card with this name.) |
| 3 | 3 | rules_lines | Choose one | choose one - | choice_modal, target_selection | Choose one — |
| 3 | 3 | rules_lines | Deal 2 to a unit at a battlefield | deal {number} to a unit at a battlefield. | location_restriction, damage_effect | Deal 2 to a unit at a battlefield. |
| 3 | 3 | rules_lines | Draw 2 | draw {number}. | deck_manipulation | Draw 2. |
| 3 | 3 | rules_lines | This enters exhausted | this enters exhausted. | ready_exhaust_effect, entry_state | This enters exhausted. |
| 3 | 3 | rules_lines | You may play me to an open battlefield | you may play me to an open battlefield. | play_permission | You may play me to an open battlefield. |
| 2 | 2 | rules_lines | :rb_exhaust:: Give a unit +3 :rb_might: this turn | {rb_symbol}: give a unit +{number} {rb_symbol} this turn. | duration_modifier, stat_modifier | :rb_exhaust:: Give a unit +3 :rb_might: this turn. |
| 2 | 2 | rules_lines | [Accelerate] | [accelerate] (you may pay {rb_symbol}{rb_symbol} as an additional cost to have me enter ready.) | ready_exhaust_effect, entry_state, cost_modifier, keyword_reminder | [Accelerate] (You may pay :rb_energy_1::rb_rune_order: as an additional cost to have me enter ready.) |
| 2 | 2 | effect_lines, rules_lines | [Deathknell] | [deathknell] - draw {number}. (when i die, get the effect.) | trigger_modifier, keyword_reminder, deck_manipulation, removal_or_healing | [Deathknell] — Draw 1. (When I die, get the effect.) |
| 2 | 2 | rules_lines | [Equip] | [equip] {rb_symbol}{rb_symbol} ({rb_symbol}{rb_symbol}: attach this to a unit you control.) | keyword_reminder, attachment_modifier | [Equip] :rb_energy_1::rb_rune_fury: (:rb_energy_1::rb_rune_fury:: Attach this to a unit you control.) |
| 2 | 2 | rules_lines | [Predict] | [predict]. (look at the top card of your main deck. you may recycle it.) | keyword_reminder, deck_manipulation | [Predict]. (Look at the top card of your Main Deck. You may recycle it.) |
| 2 | 2 | rules_lines | As you play this | as you play this, you may spend a buff as an additional cost. if you do, ignore this spell's cost. | buff_effect, conditional_resolution, cost_modifier, timing_window | As you play this, you may spend a buff as an additional cost. If you do, ignore this spell's cost. |
| 2 | 2 | rules_lines | Choose a friendly unit | choose a friendly unit. the next time it would die this turn, heal it, exhaust it, and recall it instead. (send it to base. this isn't a move.) | ready_exhaust_effect, duration_modifier, target_selection, movement_modifier, replacement_effect, removal_or_healing | Choose a friendly unit. The next time it would die this turn, heal it, exhaust it, and recall it instead. (Send it to base. This isn't a move.) |
| 2 | 2 | rules_lines | Counter a spell | counter a spell. | counter_effect | Counter a spell. |
| 2 | 1 | rules_lines | Deal 3 to a unit | deal {number} to a unit. | damage_effect | Deal 3 to a unit. |

## Lines Without Candidate Family

- None.

## Atomic Units Without Candidate Family

- None.

## Atomic Units With 3+ Candidate Families

| Family count | Occurrences | Kind | Candidate families | Unit |
| --- | --- | --- | --- | --- |
| 3 | 13 | reminder | duration_modifier, combat_modifier, damage_effect | It doesn't deal combat damage this turn. |
| 3 | 9 | reminder | contextual_clarification, cost_modifier, attachment_modifier | When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less, even if it's already attached. |
| 3 | 9 | reminder | ready_exhaust_effect, entry_state, cost_modifier | You may pay :rb_energy_1::rb_rune_fury: as an additional cost to have me enter ready. |
| 3 | 7 | reminder | combat_modifier, resource_generation, xp_progression | When I conquer or hold, gain 1 XP. |
| 3 | 5 | reminder | combat_modifier, resource_generation, xp_progression | When I conquer or hold, gain 2 XP. |
| 3 | 5 | reminder | ready_exhaust_effect, entry_state, cost_modifier | You may pay :rb_energy_1::rb_rune_body: as an additional cost to have me enter ready. |
| 4 | 4 | reminder | stun_effect, duration_modifier, combat_modifier, damage_effect | A stunned unit doesn't deal combat damage this turn. |
| 3 | 4 | reminder | ready_exhaust_effect, entry_state, cost_modifier | You may pay :rb_energy_1::rb_rune_mind: as an additional cost to have me enter ready. |
| 3 | 3 | activation_cost | timing_window, keyword_reminder, cost_modifier | [Reaction][>] :rb_exhaust: |
| 3 | 3 | reminder | resource_add_ability, keyword_modifier, removal_or_healing | It has "[Reaction][>] Kill this, :rb_exhaust:: [Add] :rb_rune_rainbow:." |
| 3 | 3 | reminder | contextual_clarification, location_restriction, timing_window | Play any time, even before spells and abilities resolve, including to a battlefield you control. |
| 3 | 3 | reminder | ready_exhaust_effect, entry_state, cost_modifier | You may pay :rb_energy_1::rb_rune_chaos: as an additional cost to have me enter ready. |
| 4 | 2 | effect | tag_reference, trait_identity, location_restriction, token_creation | Play a 3 :rb_might: Mech unit token to your base. |
| 3 | 2 | condition | buff_effect, cost_modifier, timing_window | As you play this, you may spend a buff as an additional cost. |
| 4 | 2 | effect | ready_exhaust_effect, duration_modifier, replacement_effect, removal_or_healing | The next time it would die this turn, heal it, exhaust it |
| 3 | 2 | timing | ready_exhaust_effect, combat_modifier, token_creation | When I conquer, play a Gold gear token exhausted. |
| 3 | 2 | timing | ready_exhaust_effect, combat_modifier, token_creation | When I hold, play two Gold gear tokens exhausted. |
| 3 | 2 | reminder | ready_exhaust_effect, entry_state, cost_modifier | You may pay :rb_energy_1::rb_rune_order: as an additional cost to have me enter ready. |
| 3 | 1 | activation_cost | timing_window, keyword_reminder, cost_modifier | [Action][>] :rb_energy_1::rb_rune_rainbow:, :rb_exhaust: |
| 4 | 1 | activation_cost | ready_exhaust_effect, timing_window, keyword_reminder, cost_modifier | [Action][>] Exhaust a unit you control, :rb_exhaust: |
| 4 | 1 | activation_cost | timing_window, keyword_reminder, removal_or_healing, cost_modifier | [Action][>] Kill this, :rb_exhaust: |
| 3 | 1 | effect | ready_exhaust_effect, resource_generation, keyword_reminder | [Deathknell][>] Channel 1 rune exhausted. |
| 3 | 1 | effect | keyword_reminder, deck_manipulation, removal_or_healing | [Deathknell][>] If I didn't die alone, draw 1. |
| 4 | 1 | effect | tag_reference, location_restriction, token_creation, keyword_reminder | [Deathknell][>] Play a 1 :rb_might: Bird unit token with [Deflect] to your base. |
| 3 | 1 | effect | location_restriction, cost_modifier, keyword_reminder | [Deathknell][>] Play a unit from your hand to your base, ignoring its Energy cost. |
| 4 | 1 | effect | replacement_effect, cost_modifier, keyword_reminder, xp_progression | [Level 11][>] I cost :rb_energy_6::rb_rune_calm::rb_rune_calm::rb_rune_calm: less instead. |
| 3 | 1 | effect | stat_modifier, keyword_reminder, xp_progression | [Level 11][>] I have +4 :rb_might:. |
| 4 | 1 | effect | replacement_effect, cost_modifier, keyword_reminder, xp_progression | [Level 11][>] This costs :rb_energy_4: less instead. |
| 4 | 1 | effect | ready_exhaust_effect, entry_state, keyword_reminder, xp_progression | [Level 11][>] Your units enter ready. |
| 3 | 1 | restriction | target_protection, keyword_reminder, xp_progression | [Level 16][>] I can't be chosen by enemy spells and abilities. |
| 3 | 1 | effect | cost_modifier, keyword_reminder, xp_progression | [Level 3][>] I cost :rb_energy_2::rb_rune_calm: less. |
| 4 | 1 | effect | ready_exhaust_effect, entry_state, keyword_reminder, xp_progression | [Level 3][>] I enter ready. |
| 4 | 1 | effect | keyword_modifier, stat_modifier, keyword_reminder, xp_progression | [Level 3][>] I have +1 :rb_might: and [Deflect]. |
| 5 | 1 | effect | keyword_modifier, movement_modifier, stat_modifier, keyword_reminder, xp_progression | [Level 3][>] I have +1 :rb_might: and [Ganking]. |
| 5 | 1 | effect | ready_exhaust_effect, entry_state, stat_modifier, keyword_reminder, xp_progression | [Level 3][>] I have +1 :rb_might: and enter ready. |
| 3 | 1 | effect | stat_modifier, keyword_reminder, xp_progression | [Level 3][>] I have an additional +1 :rb_might:. |
| 3 | 1 | activation_cost | keyword_reminder, xp_progression, cost_modifier | [Level 6][>] [>>][Reaction][>] :rb_exhaust: |
| 3 | 1 | effect | stun_effect, keyword_reminder, xp_progression | [Level 6][>] [Stun] an enemy unit. |
| 5 | 1 | effect | duration_modifier, replacement_effect, stat_modifier, keyword_reminder, xp_progression | [Level 6][>] Give it +3 :rb_might: this turn instead. |
| 4 | 1 | effect | replacement_effect, cost_modifier, keyword_reminder, xp_progression | [Level 6][>] I cost :rb_energy_4::rb_rune_calm::rb_rune_calm: less instead. |
| 3 | 1 | effect | stat_modifier, keyword_reminder, xp_progression | [Level 6][>] I have +1 :rb_might:. |
| 4 | 1 | effect | keyword_modifier, movement_modifier, keyword_reminder, xp_progression | [Level 6][>] I have [Deflect] and [Ganking]. |
| 3 | 1 | effect | cost_modifier, keyword_reminder, xp_progression | [Level 6][>] This costs :rb_energy_2: less. |
| 3 | 1 | effect | keyword_reminder, deck_manipulation, xp_progression | [Level 6][>] When you play me, draw 1. |
| 3 | 1 | effect | stat_modifier, keyword_reminder, xp_progression | [Level 6][>] Your units have +1 :rb_might:. |
| 4 | 1 | activation_cost | timing_window, keyword_reminder, removal_or_healing, cost_modifier | [Reaction][>] Kill this, :rb_exhaust: |
| 3 | 1 | effect | stun_effect, combat_modifier, keyword_reminder | [Stun] an attacking enemy unit. |
| 4 | 1 | effect | stun_effect, location_restriction, combat_modifier, keyword_reminder | [Stun] an enemy unit attacking here. |
| 3 | 1 | condition | tag_reference, cost_modifier, removal_or_healing | As an additional cost to play me, kill a Bird, Cat, Dog, or Poro you control. |
| 3 | 1 | condition | trait_identity, cost_modifier, removal_or_healing | As an additional cost to play this, kill a friendly [Mighty] unit. |
| 3 | 1 | condition | duration_modifier, copy_effect, attachment_modifier | As this is attached to a unit, copy that unit's text to this Equipment's effect text for as long as this is attached to it. |
| 3 | 1 | condition | target_selection, tag_reference, timing_window | As you play me, choose Bird, Cat, Dog, or Poro. |
| 3 | 1 | condition | cost_modifier, timing_window, deck_manipulation | As you play me, you may discard 1 as an additional cost. |
| 3 | 1 | condition | cost_modifier, timing_window, removal_or_healing | As you play me, you may kill any number of friendly units as an additional cost. |
| 3 | 1 | condition | buff_effect, cost_modifier, timing_window | As you play me, you may spend any number of buffs as an additional cost. |
| 3 | 1 | timing | duration_modifier, combat_modifier, timing_window | At the end of your turn, if I didn't conquer this turn, unattach this |
| 3 | 1 | timing | ready_exhaust_effect, location_restriction, timing_window | At the end of your turn, if I'm at a battlefield, ready up to 4 friendly runes. |
| 3 | 1 | timing | location_restriction, timing_window, damage_effect | At the start of each player's Beginning Phase, deal 1 to each unit here. |
| 3 | 1 | timing | location_restriction, timing_window, deck_manipulation | At the start of your Beginning Phase, if you control a facedown card at a battlefield, draw 1. |
| 4 | 1 | timing | location_restriction, timing_window, deck_manipulation, removal_or_healing | At the start of your Beginning Phase, you may kill a unit you control here to draw 1. |

## Complex Lines Decomposed


### Choose a battlefield (1 occurrences, 6 units)

Choose a battlefield. An opponent reveals their hand. You may choose a unit from it. They play that unit to that battlefield, ignoring any and all costs. When they do, [Stun] it. (It doesn't deal combat damage this turn.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | effect | target_selection | Choose a battlefield. |
| 1 | effect | deck_manipulation | An opponent reveals their hand. |
| 2 | effect | target_selection | You may choose a unit from it. |
| 3 | effect | cost_modifier | They play that unit to that battlefield, ignoring any and all costs. |
| 4 | timing | stun_effect, conditional_resolution | When they do, [Stun] it. |
| 5 | reminder | duration_modifier, combat_modifier, damage_effect | It doesn't deal combat damage this turn. |

### Discard 1 (1 occurrences, 6 units)

Discard 1, :rb_exhaust:: Choose a friendly unit. The next time it would die this turn, you may pay :rb_rune_fury: to heal it, exhaust it, and recall it instead. (Send it to base. This isn't a move.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | activation_cost | deck_manipulation, cost_modifier | Discard 1, :rb_exhaust: |
| 1 | effect | target_selection | Choose a friendly unit. |
| 2 | effect | ready_exhaust_effect, duration_modifier, replacement_effect, cost_modifier, removal_or_healing | The next time it would die this turn, you may pay :rb_rune_fury: to heal it, exhaust it |
| 3 | effect | movement_modifier, replacement_effect | recall it instead. |
| 4 | reminder | movement_modifier | Send it to base. |
| 5 | reminder | movement_modifier | This isn't a move. |

### :rb_energy_1::rb_rune_order (1 occurrences, 6 units)

:rb_energy_1::rb_rune_order:, :rb_exhaust:: Kill a friendly unit. Look at the top 5 cards of your Main Deck. You may banish a unit from among them that has Might up to 1 more than the killed unit and play it, ignoring its cost. Then recycle the rest.

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | activation_cost | cost_modifier | :rb_energy_1::rb_rune_order:, :rb_exhaust: |
| 1 | effect | removal_or_healing | Kill a friendly unit. |
| 2 | effect | deck_manipulation | Look at the top 5 cards of your Main Deck. |
| 3 | effect | banish_effect, stat_modifier, removal_or_healing | You may banish a unit from among them that has Might up to 1 more than the killed unit |
| 4 | effect | play_permission, cost_modifier | play it, ignoring its cost. |
| 5 | effect | deck_manipulation | Then recycle the rest. |

### When you play me (1 occurrences, 6 units)

When you play me, choose an opponent. They reveal their hand. Choose a card revealed this way and banish it. When they hold, return it to their hand (even if I'm no longer on the board).

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | timing | target_selection | When you play me, choose an opponent. |
| 1 | effect | deck_manipulation | They reveal their hand. |
| 2 | effect | target_selection | Choose a card revealed this way |
| 3 | effect | banish_effect | banish it. |
| 4 | timing | movement_modifier, combat_modifier | When they hold, return it to their hand |
| 5 | reminder | contextual_clarification | even if I'm no longer on the board |

### When you play me or when I hold (1 occurrences, 6 units)

When you play me or when I hold, look at the top 3 cards of your Main Deck. You may reveal a unit from among them and draw it. Recycle the rest. Then if you revealed a Bird, Cat, Dog, or Poro, do this: [Buff] a friendly unit. (Give it a +1 :rb_might: buff if it doesn't have one.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | timing | combat_modifier, deck_manipulation | When you play me or when I hold, look at the top 3 cards of your Main Deck. |
| 1 | effect | deck_manipulation | You may reveal a unit from among them |
| 2 | effect | deck_manipulation | draw it. |
| 3 | effect | deck_manipulation | Recycle the rest. |
| 4 | effect | buff_effect, tag_reference | Then if you revealed a Bird, Cat, Dog, or Poro, do this: [Buff] a friendly unit. |
| 5 | reminder | buff_effect, stat_modifier | Give it a +1 :rb_might: buff if it doesn't have one. |

### :rb_rune_calm:: [Action] (1 occurrences, 6 units)

:rb_rune_calm:: [Action] — Choose a unit you control. Move me to its location and it to my original location. If it's equipped, you may attach one of its Equipment to me. Use only once per turn.

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | activation_cost | symbol_option, cost_modifier | :rb_rune_calm: |
| 1 | timing | timing_window, keyword_reminder | [Action] |
| 2 | effect | target_selection | Choose a unit you control. |
| 3 | effect | movement_modifier | Move me to its location and it to my original location. |
| 4 | condition | attachment_modifier | If it's equipped, you may attach one of its Equipment to me. |
| 5 | restriction | usage_restriction | Use only once per turn. |

### Kill this (1 occurrences, 6 units)

Kill this, :rb_energy_1:, :rb_exhaust:: [Predict 2], then draw 1. Gain 1 XP. (To Predict 2, look at the top two cards of your Main Deck. Recycle any of them and put the rest back in any order.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | activation_cost | removal_or_healing, cost_modifier | Kill this, :rb_energy_1:, :rb_exhaust: |
| 1 | keyword_marker | keyword_reminder | [Predict 2] |
| 2 | effect | deck_manipulation | draw 1. |
| 3 | effect | resource_generation, xp_progression | Gain 1 XP. |
| 4 | reminder | deck_manipulation | To Predict 2, look at the top two cards of your Main Deck. |
| 5 | reminder | deck_manipulation | Recycle any of them and put the rest back in any order. |

### When a showdown begins here (1 occurrences, 6 units)

When a showdown begins here, you may pay :rb_energy_1:. If you do, [Predict], then reveal the top card of your Main Deck. If it's a spell, draw it. (To Predict, look at the top card of your Main Deck. You may recycle it.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | timing | location_restriction, cost_modifier | When a showdown begins here, you may pay :rb_energy_1:. |
| 1 | condition | conditional_resolution | If you do, [Predict] |
| 2 | effect | deck_manipulation | reveal the top card of your Main Deck. |
| 3 | condition | deck_manipulation | If it's a spell, draw it. |
| 4 | reminder | deck_manipulation | To Predict, look at the top card of your Main Deck. |
| 5 | reminder | deck_manipulation | You may recycle it. |

### Choose a unit (1 occurrences, 5 units)

Choose a unit. Play a ready Reflection unit token to your base. It becomes a copy of that unit. Give it [Temporary]. (Kill it at the start of its controller's Beginning Phase, before scoring.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | effect | target_selection | Choose a unit. |
| 1 | effect | ready_exhaust_effect, location_restriction, token_creation | Play a ready Reflection unit token to your base. |
| 2 | effect | trait_identity, effect_equivalence, copy_effect | It becomes a copy of that unit. |
| 3 | effect | keyword_modifier | Give it [Temporary]. |
| 4 | reminder | timing_window, removal_or_healing | Kill it at the start of its controller's Beginning Phase, before scoring. |

### [Deathknell][>] (1 occurrences, 5 units)

[Deathknell][>] Choose an opponent. They reveal their hand. You can look at their facedown cards this turn. Gain 1 XP. (When I die, get the effects.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | effect | target_selection, keyword_reminder | [Deathknell][>] Choose an opponent. |
| 1 | effect | deck_manipulation | They reveal their hand. |
| 2 | effect | duration_modifier | You can look at their facedown cards this turn. |
| 3 | effect | resource_generation, xp_progression | Gain 1 XP. |
| 4 | reminder | removal_or_healing | When I die, get the effects. |

### Choose a friendly unit (2 occurrences, 5 units)

Choose a friendly unit. The next time it would die this turn, heal it, exhaust it, and recall it instead. (Send it to base. This isn't a move.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | effect | target_selection | Choose a friendly unit. |
| 1 | effect | ready_exhaust_effect, duration_modifier, replacement_effect, removal_or_healing | The next time it would die this turn, heal it, exhaust it |
| 2 | effect | movement_modifier, replacement_effect | recall it instead. |
| 3 | reminder | movement_modifier | Send it to base. |
| 4 | reminder | movement_modifier | This isn't a move. |

### Each opponent reveals the top card of their Main Deck (1 occurrences, 5 units)

Each opponent reveals the top card of their Main Deck. Choose one and banish it, then play it, ignoring its cost. Then recycle the rest.

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | effect | deck_manipulation | Each opponent reveals the top card of their Main Deck. |
| 1 | choice_header | choice_modal, target_selection | Choose one |
| 2 | effect | banish_effect | banish it |
| 3 | effect | play_permission, cost_modifier | play it, ignoring its cost. |
| 4 | effect | deck_manipulation | Then recycle the rest. |

### When I attack (1 occurrences, 5 units)

When I attack, you may reveal the top 2 cards of your Main Deck. You may banish one, then play it. If it is a unit, you may play it here. Recycle the rest.

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | timing | combat_modifier, deck_manipulation | When I attack, you may reveal the top 2 cards of your Main Deck. |
| 1 | effect | banish_effect | You may banish one |
| 2 | effect | play_permission | play it. |
| 3 | condition | play_permission, trait_identity, location_restriction | If it is a unit, you may play it here. |
| 4 | effect | deck_manipulation | Recycle the rest. |

### When you play me (1 occurrences, 5 units)

When you play me, choose an opponent. They reveal their hand. You may pay 2 XP to choose a card from their hand. If you do, they discard that card and draw 1.

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | timing | target_selection | When you play me, choose an opponent. |
| 1 | effect | deck_manipulation | They reveal their hand. |
| 2 | effect | target_selection, cost_modifier, xp_progression | You may pay 2 XP to choose a card from their hand. |
| 3 | condition | conditional_resolution, deck_manipulation | If you do, they discard that card |
| 4 | effect | deck_manipulation | draw 1. |

### Choose an enemy unit at a battlefield (1 occurrences, 5 units)

Choose an enemy unit at a battlefield. Take control of it and recall it. (Send it to your base. This isn't a move.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | effect | target_selection, location_restriction | Choose an enemy unit at a battlefield. |
| 1 | effect | control_change | Take control of it |
| 2 | effect | movement_modifier | recall it. |
| 3 | reminder | location_restriction | Send it to your base. |
| 4 | reminder | movement_modifier | This isn't a move. |

### If a friendly unit would die (1 occurrences, 5 units)

If a friendly unit would die, kill this instead. Heal that unit, exhaust it, and recall it. (Send it to base. This isn't a move.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | condition | replacement_effect, removal_or_healing | If a friendly unit would die, kill this instead. |
| 1 | effect | ready_exhaust_effect, removal_or_healing | Heal that unit, exhaust it |
| 2 | effect | movement_modifier | recall it. |
| 3 | reminder | movement_modifier | Send it to base. |
| 4 | reminder | movement_modifier | This isn't a move. |

### :rb_exhaust:: [Reaction] (1 occurrences, 5 units)

:rb_exhaust:: [Reaction], [Legion] — [Add] :rb_energy_1:. (Abilities that add resources can't be reacted to. Get the effect if you've played a card this turn.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | activation_cost | symbol_option, cost_modifier | :rb_exhaust: |
| 1 | effect | timing_window, keyword_reminder | [Reaction], [Legion] |
| 2 | effect | resource_add_ability, keyword_reminder | [Add] :rb_energy_1:. |
| 3 | reminder | resource_add_ability | Abilities that add resources can't be reacted to. |
| 4 | reminder | duration_modifier, trigger_modifier | Get the effect if you've played a card this turn. |

### Kill a friendly unit or gear (1 occurrences, 5 units)

Kill a friendly unit or gear, :rb_exhaust:: [Action] — [Add] :rb_rune_rainbow::rb_rune_rainbow:. (Use on your turn or in showdowns. Abilities that add resources can't be reacted to.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | activation_cost | removal_or_healing, cost_modifier | Kill a friendly unit or gear, :rb_exhaust: |
| 1 | timing | timing_window, keyword_reminder | [Action] |
| 2 | effect | resource_add_ability, keyword_reminder | [Add] :rb_rune_rainbow::rb_rune_rainbow:. |
| 3 | reminder | timing_window | Use on your turn or in showdowns. |
| 4 | reminder | resource_add_ability | Abilities that add resources can't be reacted to. |

### :rb_exhaust:: [Reaction] (1 occurrences, 5 units)

:rb_exhaust:: [Reaction] — [Add] :rb_energy_2:. Use only to play spells. (Abilities that add resources can't be reacted to.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | activation_cost | symbol_option, cost_modifier | :rb_exhaust: |
| 1 | timing | timing_window, keyword_reminder | [Reaction] |
| 2 | effect | resource_add_ability, keyword_reminder | [Add] :rb_energy_2:. |
| 3 | restriction | usage_restriction | Use only to play spells. |
| 4 | reminder | resource_add_ability | Abilities that add resources can't be reacted to. |

### :rb_exhaust:: [Reaction] (1 occurrences, 5 units)

:rb_exhaust:: [Reaction] — [Add] :rb_rune_rainbow:. Use only to play gear or use gear abilities. (Abilities that add resources can't be reacted to.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | activation_cost | symbol_option, cost_modifier | :rb_exhaust: |
| 1 | timing | timing_window, keyword_reminder | [Reaction] |
| 2 | effect | resource_add_ability, keyword_reminder | [Add] :rb_rune_rainbow:. |
| 3 | restriction | usage_restriction | Use only to play gear or use gear abilities. |
| 4 | reminder | resource_add_ability | Abilities that add resources can't be reacted to. |

### :rb_exhaust:: [Reaction] (1 occurrences, 5 units)

:rb_exhaust:: [Reaction] — [Add] :rb_rune_rainbow:. Use only to play spells. (Abilities that add resources can't be reacted to.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | activation_cost | symbol_option, cost_modifier | :rb_exhaust: |
| 1 | timing | timing_window, keyword_reminder | [Reaction] |
| 2 | effect | resource_add_ability, keyword_reminder | [Add] :rb_rune_rainbow:. |
| 3 | restriction | usage_restriction | Use only to play spells. |
| 4 | reminder | resource_add_ability | Abilities that add resources can't be reacted to. |

### When you conquer or hold (1 occurrences, 4 units)

When you conquer or hold, you may discard 1 and exhaust me to play a ready Reflection unit token there. It becomes a copy of another unit there. Give it [Temporary].

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | timing | combat_modifier, deck_manipulation | When you conquer or hold, you may discard 1 |
| 1 | effect | ready_exhaust_effect, token_creation | exhaust me to play a ready Reflection unit token there. |
| 2 | effect | trait_identity, effect_equivalence, copy_effect | It becomes a copy of another unit there. |
| 3 | effect | keyword_modifier | Give it [Temporary]. |

### :rb_energy_1 (1 occurrences, 4 units)

:rb_energy_1:, :rb_exhaust:: Return a friendly unit at a battlefield to its owner's hand. Play a Gold gear token exhausted. (It has "[Reaction][>] Kill this, :rb_exhaust:: [Add] :rb_rune_rainbow:.")

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | activation_cost | cost_modifier | :rb_energy_1:, :rb_exhaust: |
| 1 | effect | location_restriction, movement_modifier | Return a friendly unit at a battlefield to its owner's hand. |
| 2 | effect | ready_exhaust_effect, token_creation | Play a Gold gear token exhausted. |
| 3 | reminder | resource_add_ability, keyword_modifier, removal_or_healing | It has "[Reaction][>] Kill this, :rb_exhaust:: [Add] :rb_rune_rainbow:." |

### Choose an enemy unit at a battlefield with 3 :rb_might: or less (1 occurrences, 4 units)

Choose an enemy unit at a battlefield with 3 :rb_might: or less. If you paid the additional cost, choose any enemy unit at a battlefield instead. Take control of it, exhaust it, and recall it.

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | effect | target_selection, location_restriction, cost_modifier | Choose an enemy unit at a battlefield with 3 :rb_might: or less. |
| 1 | condition | target_selection, location_restriction, replacement_effect, cost_modifier | If you paid the additional cost, choose any enemy unit at a battlefield instead. |
| 2 | effect | ready_exhaust_effect, control_change | Take control of it, exhaust it |
| 3 | effect | movement_modifier | recall it. |

### If another unit you control here would die (1 occurrences, 4 units)

If another unit you control here would die, if it has less Might than me, instead heal it, exhaust it, and recall it. (Send it to base. This isn't a move.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | condition | ready_exhaust_effect, location_restriction, replacement_effect, cost_modifier, stat_modifier, removal_or_healing | If another unit you control here would die, if it has less Might than me, instead heal it, exhaust it |
| 1 | effect | movement_modifier | recall it. |
| 2 | reminder | movement_modifier | Send it to base. |
| 3 | reminder | movement_modifier | This isn't a move. |

### If a buffed unit you control would die (1 occurrences, 4 units)

If a buffed unit you control would die, you may pay :rb_rune_rainbow:, exhaust me, and spend its buff to heal it, exhaust it, and recall it instead. (Send it to base. This isn't a move.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | condition | ready_exhaust_effect, buff_effect, replacement_effect, cost_modifier, removal_or_healing | If a buffed unit you control would die, you may pay :rb_rune_rainbow:, exhaust me, and spend its buff to heal it, exhaust it |
| 1 | effect | movement_modifier, replacement_effect | recall it instead. |
| 2 | reminder | movement_modifier | Send it to base. |
| 3 | reminder | movement_modifier | This isn't a move. |

### When I defend (1 occurrences, 4 units)

When I defend, choose an enemy unit here and reveal the top 5 cards of your Main Deck. Deal 1 to that unit for each card with [Hidden] revealed this way, then recycle the revealed cards.

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | timing | target_selection, location_restriction, combat_modifier | When I defend, choose an enemy unit here |
| 1 | effect | deck_manipulation | reveal the top 5 cards of your Main Deck. |
| 2 | effect | hide_modifier, damage_effect | Deal 1 to that unit for each card with [Hidden] revealed this way |
| 3 | effect | deck_manipulation | recycle the revealed cards. |

### When you play me (1 occurrences, 4 units)

When you play me, choose an enemy unit. If it is stunned, kill it. Otherwise, stun it. (It doesn't deal combat damage this turn.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | timing | target_selection | When you play me, choose an enemy unit. |
| 1 | condition | stun_effect, removal_or_healing | If it is stunned, kill it. |
| 2 | effect | stun_effect | Otherwise, stun it. |
| 3 | reminder | duration_modifier, combat_modifier, damage_effect | It doesn't deal combat damage this turn. |

### :rb_exhaust:: Play two :rb_energy_1: :rb_might: Bird unit tokens with [Deflect] (1 occurrences, 4 units)

:rb_exhaust:: Play two :rb_energy_1: :rb_might: Bird unit tokens with [Deflect]. Use this ability only while I'm at a battlefield. (Opponents must pay :rb_rune_rainbow: to choose a [Deflect] unit with a spell or ability.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | activation_cost | symbol_option, cost_modifier | :rb_exhaust: |
| 1 | effect | tag_reference, token_creation | Play two :rb_energy_1: :rb_might: Bird unit tokens with [Deflect]. |
| 2 | restriction | location_restriction | Use this ability only while I'm at a battlefield. |
| 3 | reminder | target_selection, cost_modifier | Opponents must pay :rb_rune_rainbow: to choose a [Deflect] unit with a spell or ability. |

### [Deathknell] (1 occurrences, 4 units)

[Deathknell] — Channel 2 runes exhausted and draw 1. (When I die, get the effect.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | keyword_marker | keyword_reminder | [Deathknell] |
| 1 | effect | ready_exhaust_effect | Channel 2 runes exhausted |
| 2 | effect | deck_manipulation | draw 1. |
| 3 | reminder | trigger_modifier, removal_or_healing | When I die, get the effect. |

### [Deathknell] (1 occurrences, 4 units)

[Deathknell] — If I died alone, draw 1. (When I die, get the effect. I'm alone if there are no other friendly units here.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | keyword_marker | keyword_reminder | [Deathknell] |
| 1 | condition | deck_manipulation | If I died alone, draw 1. |
| 2 | reminder | trigger_modifier, removal_or_healing | When I die, get the effect. |
| 3 | reminder | location_restriction | I'm alone if there are no other friendly units here. |

### [Deathknell] (1 occurrences, 4 units)

[Deathknell] — If I was [Mighty], draw 2. (When I die, get the effect. I'm Mighty while I have 5+ :rb_might:.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | keyword_marker | keyword_reminder | [Deathknell] |
| 1 | condition | trait_identity, deck_manipulation | If I was [Mighty], draw 2. |
| 2 | reminder | trigger_modifier, removal_or_healing | When I die, get the effect. |
| 3 | reminder | trait_identity | I'm Mighty while I have 5+ :rb_might:. |

### [Legion] (1 occurrences, 4 units)

[Legion] — When you play me, buff me. (If I don't have a buff, I get a +1 :rb_might: buff. Get the effect if you've played another card this turn.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | keyword_marker | keyword_reminder | [Legion] |
| 1 | timing | buff_effect | When you play me, buff me. |
| 2 | reminder | buff_effect, stat_modifier | If I don't have a buff, I get a +1 :rb_might: buff. |
| 3 | reminder | duration_modifier, trigger_modifier | Get the effect if you've played another card this turn. |

### Choose a friendly unit without [Temporary] (1 occurrences, 4 units)

Choose a friendly unit without [Temporary]. Give it [Temporary]. Draw 2. (Kill it at the start of its controller's Beginning Phase, before scoring.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | effect | target_selection | Choose a friendly unit without [Temporary]. |
| 1 | effect | keyword_modifier | Give it [Temporary]. |
| 2 | effect | deck_manipulation | Draw 2. |
| 3 | reminder | timing_window, removal_or_healing | Kill it at the start of its controller's Beginning Phase, before scoring. |

### Each player looks at the top 5 cards of their Main Deck (1 occurrences, 4 units)

Each player looks at the top 5 cards of their Main Deck, banishes one of them, then recycles the rest. Starting with the next player, each player plays those cards, ignoring Energy costs. (They must still pay Power costs.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | effect | banish_effect, deck_manipulation | Each player looks at the top 5 cards of their Main Deck, banishes one of them |
| 1 | effect | deck_manipulation | recycles the rest. |
| 2 | effect | turn_sequence, cost_modifier | Starting with the next player, each player plays those cards, ignoring Energy costs. |
| 3 | reminder | cost_modifier, stat_modifier | They must still pay Power costs. |

### When you conquer (1 occurrences, 4 units)

When you conquer, you may exhaust me to reveal the top 2 cards of your Main Deck. You may banish one, then play it. Recycle the rest.

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | timing | ready_exhaust_effect, combat_modifier, deck_manipulation | When you conquer, you may exhaust me to reveal the top 2 cards of your Main Deck. |
| 1 | effect | banish_effect | You may banish one |
| 2 | effect | play_permission | play it. |
| 3 | effect | deck_manipulation | Recycle the rest. |

### :rb_exhaust:: [Legion] (1 occurrences, 4 units)

:rb_exhaust:: [Legion] — The next unit you play this turn enters ready. (Get the effect if you've played another card this turn.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | activation_cost | symbol_option, cost_modifier | :rb_exhaust: |
| 1 | keyword_marker | keyword_reminder | [Legion] |
| 2 | effect | ready_exhaust_effect, duration_modifier, entry_state | The next unit you play this turn enters ready. |
| 3 | reminder | duration_modifier, trigger_modifier | Get the effect if you've played another card this turn. |

### [Deathknell] (1 occurrences, 4 units)

[Deathknell] — Discard 2, then draw 2. (When I die, get the effect.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | keyword_marker | keyword_reminder | [Deathknell] |
| 1 | effect | deck_manipulation | Discard 2 |
| 2 | effect | deck_manipulation | draw 2. |
| 3 | reminder | trigger_modifier, removal_or_healing | When I die, get the effect. |

### [Legion] (1 occurrences, 4 units)

[Legion] — When you play me, discard 2, then draw 2. (Get the effect if you've played another card this turn.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | keyword_marker | keyword_reminder | [Legion] |
| 1 | timing | deck_manipulation | When you play me, discard 2 |
| 2 | effect | deck_manipulation | draw 2. |
| 3 | reminder | duration_modifier, trigger_modifier | Get the effect if you've played another card this turn. |

### [Reaction][>] (1 occurrences, 4 units)

[Reaction][>] :rb_exhaust:: [Add] :rb_energy_1:. Spend this Energy only during showdowns. (Abilities that add resources can't be reacted to.)

| Index | Kind | Candidate families | Unit |
| --- | --- | --- | --- |
| 0 | activation_cost | timing_window, keyword_reminder, cost_modifier | [Reaction][>] :rb_exhaust: |
| 1 | effect | resource_add_ability, keyword_reminder | [Add] :rb_energy_1:. |
| 2 | restriction | usage_restriction | Spend this Energy only during showdowns. |
| 3 | reminder | resource_add_ability | Abilities that add resources can't be reacted to. |

## Lines With 4+ Candidate Families

| Family count | Occurrences | Opening | Candidate families | Original line |
| --- | --- | --- | --- | --- |
| 10 | 1 | Choose a unit | ready_exhaust_effect, target_selection, keyword_modifier, trait_identity, location_restriction, effect_equivalence, copy_effect, token_creation, timing_window, removal_or_healing | Choose a unit. Play a ready Reflection unit token to your base. It becomes a copy of that unit. Give it [Temporary]. (Kill it at the start of its controller's Beginning Phase, before scoring.) |
| 9 | 1 | [Deathknell][>] | target_selection, keyword_modifier, tag_reference, location_restriction, trigger_modifier, token_creation, cost_modifier, keyword_reminder, removal_or_healing | [Deathknell][>] Play a 1 :rb_might: Bird unit token with [Deflect] to your base. (When I die, get the effect. Opponents must pay :rb_rune_rainbow: to choose a [Deflect] unit with a spell or ability.) |
| 8 | 1 | Choose a battlefield | stun_effect, duration_modifier, target_selection, conditional_resolution, combat_modifier, cost_modifier, deck_manipulation, damage_effect | Choose a battlefield. An opponent reveals their hand. You may choose a unit from it. They play that unit to that battlefield, ignoring any and all costs. When they do, [Stun] it. (It doesn't deal combat damage this turn.) |
| 8 | 1 | Discard 1 | ready_exhaust_effect, duration_modifier, target_selection, movement_modifier, replacement_effect, cost_modifier, deck_manipulation, removal_or_healing | Discard 1, :rb_exhaust:: Choose a friendly unit. The next time it would die this turn, you may pay :rb_rune_fury: to heal it, exhaust it, and recall it instead. (Send it to base. This isn't a move.) |
| 8 | 1 | When you conquer or hold | ready_exhaust_effect, keyword_modifier, trait_identity, effect_equivalence, copy_effect, combat_modifier, token_creation, deck_manipulation | When you conquer or hold, you may discard 1 and exhaust me to play a ready Reflection unit token there. It becomes a copy of another unit there. Give it [Temporary]. |
| 7 | 1 | :rb_energy_1 | ready_exhaust_effect, resource_add_ability, keyword_modifier, location_restriction, movement_modifier, token_creation, removal_or_healing | :rb_energy_1:, :rb_exhaust:: Return a friendly unit at a battlefield to its owner's hand. Play a Gold gear token exhausted. (It has "[Reaction][>] Kill this, :rb_exhaust:: [Add] :rb_rune_rainbow:.") |
| 7 | 1 | [Action][>] | stun_effect, duration_modifier, location_restriction, combat_modifier, timing_window, keyword_reminder, damage_effect | [Action][>] :rb_energy_1::rb_rune_rainbow:, :rb_exhaust:: [Stun] an enemy unit attacking here. (It doesn't deal combat damage this turn.) |
| 7 | 1 | [Deathknell] | tag_reference, trait_identity, location_restriction, trigger_modifier, token_creation, keyword_reminder, removal_or_healing | [Deathknell] — Play two 3 :rb_might: Mech unit tokens to your base. (When I die, get the effect.) |
| 7 | 1 | [Deathknell][>] | duration_modifier, target_selection, resource_generation, keyword_reminder, deck_manipulation, removal_or_healing, xp_progression | [Deathknell][>] Choose an opponent. They reveal their hand. You can look at their facedown cards this turn. Gain 1 XP. (When I die, get the effects.) |
| 7 | 1 | [Level 3][>] | target_selection, keyword_modifier, trigger_modifier, cost_modifier, stat_modifier, keyword_reminder, xp_progression | [Level 3][>] I have +1 :rb_might: and [Deflect]. (While you have 3+ XP, get the effect. Opponents must pay :rb_rune_rainbow: to choose a [Deflect] unit with a spell or ability.) |
| 7 | 1 | [Level 6][>] | stun_effect, duration_modifier, combat_modifier, trigger_modifier, keyword_reminder, damage_effect, xp_progression | [Level 6][>] [Stun] an enemy unit. (While you have 6+ XP, get the effect. A stunned unit doesn't deal combat damage this turn.) |
| 7 | 1 | [Stun] | stun_effect, duration_modifier, movement_modifier, replacement_effect, combat_modifier, keyword_reminder, damage_effect | [Stun] an attacking enemy unit. If it's already stunned, return it to its owner's hand instead. (A stunned unit doesn't deal combat damage this turn.) |
| 7 | 1 | Choose a friendly unit and a battlefield | target_selection, location_restriction, movement_modifier, cost_modifier, resource_generation, stat_modifier, xp_progression | Choose a friendly unit and a battlefield. Move all enemy units at that battlefield with less Might than the chosen unit to their base. Gain 1 XP. |
| 7 | 1 | Choose an enemy unit at a battlefield with 3 :rb_might: or less | ready_exhaust_effect, target_selection, control_change, location_restriction, movement_modifier, replacement_effect, cost_modifier | Choose an enemy unit at a battlefield with 3 :rb_might: or less. If you paid the additional cost, choose any enemy unit at a battlefield instead. Take control of it, exhaust it, and recall it. |
| 7 | 1 | Deal 3 to an enemy unit | ready_exhaust_effect, resource_add_ability, duration_modifier, keyword_modifier, token_creation, damage_effect, removal_or_healing | Deal 3 to an enemy unit. When it dies this turn, play a Gold gear token exhausted. (It has "[Reaction][>] Kill this, :rb_exhaust:: [Add] :rb_rune_rainbow:.") |
| 7 | 1 | If a unit here would die during combat | ready_exhaust_effect, location_restriction, movement_modifier, replacement_effect, combat_modifier, cost_modifier, removal_or_healing | If a unit here would die during combat, its controller may pay :rb_rune_rainbow::rb_rune_rainbow::rb_rune_rainbow: to heal it, exhaust it, and recall it instead. |
| 7 | 1 | If another unit you control here would die | ready_exhaust_effect, location_restriction, movement_modifier, replacement_effect, cost_modifier, stat_modifier, removal_or_healing | If another unit you control here would die, if it has less Might than me, instead heal it, exhaust it, and recall it. (Send it to base. This isn't a move.) |
| 7 | 1 | When I attack while your units have all 4 tags | stun_effect, duration_modifier, keyword_modifier, tag_reference, location_restriction, combat_modifier, damage_effect | When I attack while your units have all 4 tags, [Stun] an enemy unit here. (It doesn't deal combat damage this turn.) |
| 7 | 1 | When I conquer | ready_exhaust_effect, resource_add_ability, keyword_modifier, combat_modifier, token_creation, damage_effect, removal_or_healing | When I conquer, if you assigned 3 or more excess damage, play two Gold gear tokens exhausted. (They have "[Reaction][>] Kill this, :rb_exhaust:: [Add] :rb_rune_rainbow:.") |
| 6 | 2 | Choose a friendly unit | ready_exhaust_effect, duration_modifier, target_selection, movement_modifier, replacement_effect, removal_or_healing | Choose a friendly unit. The next time it would die this turn, heal it, exhaust it, and recall it instead. (Send it to base. This isn't a move.) |
| 6 | 1 | :rb_energy_1::rb_rune_order | play_permission, banish_effect, cost_modifier, stat_modifier, deck_manipulation, removal_or_healing | :rb_energy_1::rb_rune_order:, :rb_exhaust:: Kill a friendly unit. Look at the top 5 cards of your Main Deck. You may banish a unit from among them that has Might up to 1 more than the killed unit and play it, ignoring its cost. Then recycle the rest. |
| 6 | 1 | [Deathknell][>] | location_restriction, trigger_modifier, cost_modifier, stat_modifier, keyword_reminder, removal_or_healing | [Deathknell][>] Play a unit from your hand to your base, ignoring its Energy cost. (When I die, get the effect. You must still pay its Power cost.) |
| 6 | 1 | [Level 3][>] | keyword_modifier, movement_modifier, trigger_modifier, stat_modifier, keyword_reminder, xp_progression | [Level 3][>] I have +1 :rb_might: and [Ganking]. (While you have 3+ XP, get the effect. A [Ganking] unit can move from battlefield to battlefield.) |
| 6 | 1 | [Level 3][>] | ready_exhaust_effect, entry_state, trigger_modifier, stat_modifier, keyword_reminder, xp_progression | [Level 3][>] I have +1 :rb_might: and enter ready. (While you have 3+ XP, get the effect.) |
| 6 | 1 | [Level 6][>] | duration_modifier, replacement_effect, trigger_modifier, stat_modifier, keyword_reminder, xp_progression | [Level 6][>] Give it +3 :rb_might: this turn instead. (While you have 6+ XP, get the effect.) |
| 6 | 1 | [Level 6][>] | target_selection, keyword_modifier, movement_modifier, cost_modifier, keyword_reminder, xp_progression | [Level 6][>] I have [Deflect] and [Ganking]. (While you have 6+ XP, opponents must pay :rb_rune_rainbow: to choose me with a spell or ability and I can move from battlefield to battlefield.) |
| 6 | 1 | Choose a friendly unit | target_selection, resource_generation, stat_modifier, damage_effect, removal_or_healing, xp_progression | Choose a friendly unit. It deals damage equal to its Might split among enemy units at battlefields. Then for each unit this kills, do this: Gain 1 XP. |
| 6 | 1 | Deal 3 to a unit at a battlefield | duration_modifier, banish_effect, location_restriction, replacement_effect, damage_effect, removal_or_healing | Deal 3 to a unit at a battlefield. If it would die this turn, banish it instead. |
| 6 | 1 | Each opponent reveals the top card of their Main Deck | choice_modal, play_permission, target_selection, banish_effect, cost_modifier, deck_manipulation | Each opponent reveals the top card of their Main Deck. Choose one and banish it, then play it, ignoring its cost. Then recycle the rest. |
| 6 | 1 | Give a friendly unit +1 :rb_might: this turn and [Stun] an enemy unit at its location | stun_effect, duration_modifier, keyword_modifier, combat_modifier, stat_modifier, damage_effect | Give a friendly unit +1 :rb_might: this turn and [Stun] an enemy unit at its location. (A stunned unit doesn't deal combat damage this turn.) |
| 6 | 1 | If a buffed unit you control would die | ready_exhaust_effect, buff_effect, movement_modifier, replacement_effect, cost_modifier, removal_or_healing | If a buffed unit you control would die, you may pay :rb_rune_rainbow:, exhaust me, and spend its buff to heal it, exhaust it, and recall it instead. (Send it to base. This isn't a move.) |
| 6 | 1 | Once each turn | ready_exhaust_effect, resource_add_ability, keyword_modifier, location_restriction, token_creation, removal_or_healing | Once each turn, when an enemy unit dies while I'm at a battlefield, play a Gold gear token exhausted. (It has "[Reaction][>] Kill this, :rb_exhaust:: [Add] :rb_rune_rainbow:.") |
| 6 | 1 | Spend 3 XP: Give your units here [Ganking] this turn | duration_modifier, keyword_modifier, location_restriction, movement_modifier, cost_modifier, xp_progression | Spend 3 XP: Give your units here [Ganking] this turn. (We can move from battlefield to battlefield.) |
| 6 | 1 | Stun an enemy unit at a battlefield | stun_effect, duration_modifier, location_restriction, movement_modifier, combat_modifier, damage_effect | Stun an enemy unit at a battlefield. You may move a friendly unit to that enemy unit's battlefield. (A stunned unit doesn't deal combat damage this turn.) |
| 6 | 1 | When an opponent plays a unit while I'm at a battlefield | stun_effect, duration_modifier, location_restriction, movement_modifier, combat_modifier, damage_effect | When an opponent plays a unit while I'm at a battlefield, [Stun] it. They can't move it this turn. (It doesn't deal combat damage this turn.) |
| 6 | 1 | When I attack or defend | duration_modifier, keyword_modifier, location_restriction, combat_modifier, stat_modifier, damage_effect | When I attack or defend, give one of your other units here +3 :rb_might: and [Tank] this turn. (It must be assigned combat damage first.) |
| 6 | 1 | When I attack or defend | duration_modifier, location_restriction, combat_modifier, resource_generation, stat_modifier, xp_progression | When I attack or defend, if an enemy unit is alone here, give me +2 :rb_might: this turn and gain 2 XP. |
| 6 | 1 | When I attack | ready_exhaust_effect, duration_modifier, trait_identity, location_restriction, combat_modifier, stat_modifier | When I attack, give me +2 :rb_might: this turn if there is a ready enemy unit here. |
| 6 | 1 | When I attack | play_permission, banish_effect, trait_identity, location_restriction, combat_modifier, deck_manipulation | When I attack, you may reveal the top 2 cards of your Main Deck. You may banish one, then play it. If it is a unit, you may play it here. Recycle the rest. |
| 6 | 1 | When I attack | location_restriction, combat_modifier, cost_modifier, stat_modifier, damage_effect, xp_progression | When I attack, you may spend 3 XP to deal damage equal to my Might to an enemy unit here. |
| 6 | 1 | When I conquer | play_permission, score_modifier, combat_modifier, cost_modifier, stat_modifier, deck_manipulation | When I conquer, you may play a spell from your trash with Energy cost less than your points without paying its Energy cost. Then recycle it. (You must still pay its Power cost.) |
| 6 | 1 | When I conquer | tag_reference, trait_identity, combat_modifier, cost_modifier, stat_modifier, deck_manipulation | When I conquer, you may recycle another friendly unit to play a Mech from your trash. Reduce its Energy cost by the Might of the unit you recycled. |
| 6 | 1 | When I defend | target_selection, location_restriction, hide_modifier, combat_modifier, deck_manipulation, damage_effect | When I defend, choose an enemy unit here and reveal the top 5 cards of your Main Deck. Deal 1 to that unit for each card with [Hidden] revealed this way, then recycle the revealed cards. |
| 6 | 1 | When I hold | ready_exhaust_effect, location_restriction, combat_modifier, token_creation, timing_window, removal_or_healing | When I hold, play a ready 3 :rb_might: Sprite unit token with [Temporary] here. (Kill it at the start of its controller's next Beginning Phase, before scoring.) |
| 6 | 1 | When you conquer here | conditional_resolution, location_restriction, movement_modifier, combat_modifier, token_creation, cost_modifier | When you conquer here, you may pay :rb_energy_1: and return a unit you control here to its owner's hand. If you do, play a 2 :rb_might: Sand Soldier unit token here. |
| 6 | 1 | When you conquer or hold | ready_exhaust_effect, score_modifier, tag_reference, combat_modifier, token_creation, stat_modifier | When you conquer or hold, you may exhaust me to replace that battlefield with a Brush battlefield token. (Bird, Cat, Dog, Poro, and Ivern units have +1 :rb_might: in Brush. It can be swapped back when scored.) |
| 6 | 1 | When you hold here | duration_modifier, keyword_modifier, location_restriction, combat_modifier, trigger_modifier, cost_modifier | When you hold here, give your next spell this turn [Repeat] equal to its base cost. (You may pay the additional cost to repeat the spell's effect.) |
| 6 | 1 | When you move an enemy unit | ready_exhaust_effect, stun_effect, duration_modifier, movement_modifier, combat_modifier, damage_effect | When you move an enemy unit, you may exhaust this to [Stun] it. (It doesn't deal combat damage this turn.) |
| 6 | 1 | When you play me | stun_effect, duration_modifier, target_selection, combat_modifier, damage_effect, removal_or_healing | When you play me, choose an enemy unit. If it is stunned, kill it. Otherwise, stun it. (It doesn't deal combat damage this turn.) |
| 6 | 1 | When you play me | target_selection, banish_effect, contextual_clarification, movement_modifier, combat_modifier, deck_manipulation | When you play me, choose an opponent. They reveal their hand. Choose a card revealed this way and banish it. When they hold, return it to their hand (even if I'm no longer on the board). |

## Candidate Family Examples


### keyword_reminder

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 73 | starts_with_bracketed_keyword | [Action] (Play on your turn or in showdowns.) |
| 53 | starts_with_bracketed_keyword | [Reaction] (Play any time, even before spells and abilities resolve.) |
| 32 | starts_with_bracketed_keyword | [Hidden] (Hide now for :rb_rune_rainbow: to react with later for :rb_energy_0:.) |
| 20 | starts_with_bracketed_keyword | [Deflect] (Opponents must pay :rb_rune_rainbow: to choose me with a spell or ability.) |
| 19 | starts_with_bracketed_keyword | [Tank] (I must be assigned combat damage first.) |
| 15 | starts_with_bracketed_keyword | [Ganking] (I can move from battlefield to battlefield.) |

### cost_modifier

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 20 | pay_word | [Deflect] (Opponents must pay :rb_rune_rainbow: to choose me with a spell or ability.) |
| 11 | cost_word, pay_word, additional_cost | [Repeat] :rb_energy_2: (You may pay the additional cost to repeat this spell's effect.) |
| 9 | cost_word, pay_word, additional_cost | [Accelerate] (You may pay :rb_energy_1::rb_rune_fury: as an additional cost to have me enter ready.) |
| 9 | less_word | [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less, even if it's already attached.) |
| 5 | cost_word, pay_word, additional_cost | [Accelerate] (You may pay :rb_energy_1::rb_rune_body: as an additional cost to have me enter ready.) |
| 4 | cost_word, pay_word, additional_cost | [Accelerate] (You may pay :rb_energy_1::rb_rune_mind: as an additional cost to have me enter ready.) |

### combat_modifier

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 19 | combat, combat_keyword | [Tank] (I must be assigned combat damage first.) |
| 9 | attack_defend, combat_keyword | [Shield] (+1 :rb_might: while I'm a defender.) |
| 8 | attack_defend, combat_keyword | [Assault 2] (+2 :rb_might: while I'm an attacker.) |
| 8 | attack_defend, combat_keyword | [Assault] (+1 :rb_might: while I'm an attacker.) |
| 7 | conquer_hold | [Hunt] (When I conquer or hold, gain 1 XP.) |
| 5 | conquer_hold | [Hunt 2] (When I conquer or hold, gain 2 XP.) |

### location_restriction

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 12 | battlefield_location | [Ambush] (You may play me as a [Reaction] to a battlefield where you have units.) |
| 3 | battlefield_location | [Reaction] (Play any time, even before spells and abilities resolve, including to a battlefield you control.) |
| 3 | battlefield_location | Deal 2 to a unit at a battlefield. |
| 2 | battlefield_location | Kill a unit at a battlefield. |
| 2 | here | Other friendly units have +1 :rb_might: here. |
| 1 | battlefield_location, base_location | :rb_energy_1:, :rb_exhaust:: Move a friendly unit at a battlefield to its base. |

### stat_modifier

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 9 | might_delta | [Shield] (+1 :rb_might: while I'm a defender.) |
| 8 | might_delta | [Assault 2] (+2 :rb_might: while I'm an attacker.) |
| 8 | might_delta | [Assault] (+1 :rb_might: while I'm an attacker.) |
| 5 | might_delta | [Shield 2] (+2 :rb_might: while I'm a defender.) |
| 2 | might_delta, give_delta | :rb_exhaust:: Give a unit +3 :rb_might: this turn. |
| 2 | might_delta | Other friendly units have +1 :rb_might: here. |

### deck_manipulation

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 6 | recycle, top_deck | [Vision] (When you play me, look at the top card of your Main Deck. You may recycle it.) |
| 6 | draw_discard | Draw 1. |
| 4 | draw_discard | [Quick-Draw] (This has [Reaction]. When you play it, attach it to a unit you control.) |
| 3 | draw_discard | Draw 2. |
| 2 | draw_discard | [Deathknell] — Draw 1. (When I die, get the effect.) |
| 2 | recycle, top_deck | [Predict]. (Look at the top card of your Main Deck. You may recycle it.) |

### ready_exhaust_effect

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 9 | ready_word | [Accelerate] (You may pay :rb_energy_1::rb_rune_fury: as an additional cost to have me enter ready.) |
| 6 | ready_word | I enter ready. |
| 5 | ready_word | [Accelerate] (You may pay :rb_energy_1::rb_rune_body: as an additional cost to have me enter ready.) |
| 4 | ready_word | [Accelerate] (You may pay :rb_energy_1::rb_rune_mind: as an additional cost to have me enter ready.) |
| 3 | ready_word | [Accelerate] (You may pay :rb_energy_1::rb_rune_chaos: as an additional cost to have me enter ready.) |
| 3 | exhaust_word | This enters exhausted. |

### timing_window

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 73 | action_reaction, play_timing | [Action] (Play on your turn or in showdowns.) |
| 53 | action_reaction, play_timing | [Reaction] (Play any time, even before spells and abilities resolve.) |
| 3 | action_reaction, play_timing | [Reaction] (Play any time, even before spells and abilities resolve, including to a battlefield you control.) |
| 3 | phase_timing | [Temporary] (Kill this at the start of its controller's Beginning Phase, before scoring.) |
| 2 | as_you_play | As you play this, you may spend a buff as an additional cost. If you do, ignore this spell's cost. |
| 1 | action_reaction | [Action][>] :rb_energy_1::rb_rune_rainbow:, :rb_exhaust:: [Stun] an enemy unit attacking here. (It doesn't deal combat damage this turn.) |

### duration_modifier

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 2 | this_turn | :rb_exhaust:: Give a unit +3 :rb_might: this turn. |
| 2 | this_turn, next_time | Choose a friendly unit. The next time it would die this turn, heal it, exhaust it, and recall it instead. (Send it to base. This isn't a move.) |
| 1 | this_turn | :rb_energy_1:, :rb_exhaust:: Play a 2 :rb_might: Sand Soldier unit token to your base. Use only if you've played an Equipment this turn. |
| 1 | this_turn | :rb_energy_2::rb_rune_fury:: Double my Might this turn. |
| 1 | this_turn | :rb_exhaust:: [Legion] — The next unit you play this turn enters ready. (Get the effect if you've played another card this turn.) |
| 1 | this_turn | :rb_exhaust:: [Reaction] — Draw 1. Use only if you've chosen enemy units and/or gear twice this turn with spells or unit abilities. |

### movement_modifier

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 15 | move_word, ganking_keyword | [Ganking] (I can move from battlefield to battlefield.) |
| 2 | move_word, recall_or_return, send_to_base | Choose a friendly unit. The next time it would die this turn, heal it, exhaust it, and recall it instead. (Send it to base. This isn't a move.) |
| 2 | move_word | Move an enemy unit. |
| 1 | move_word | :rb_energy_1:, :rb_exhaust:: Move a friendly unit at a battlefield to its base. |
| 1 | put_into_hand | :rb_energy_1:, :rb_exhaust:: Put a Teemo unit you own into your hand from your Champion Zone or the board. |
| 1 | recall_or_return | :rb_energy_1:, :rb_exhaust:: Return a friendly unit at a battlefield to its owner's hand. Play a Gold gear token exhausted. (It has "[Reaction][>] Kill this, :rb_exhaust:: [Add] :rb_rune_rainbow:.") |

### damage_effect

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 19 | deal_damage | [Tank] (I must be assigned combat damage first.) |
| 6 | deal_damage | Deal 2 to a unit. |
| 4 | deal_damage | [Backline] (I must be assigned combat damage last.) |
| 3 | deal_damage | Deal 2 to a unit at a battlefield. |
| 2 | deal_damage | Deal 3 to a unit. |
| 2 | deal_damage | I don't deal combat damage. |

### removal_or_healing

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 3 | kill_heal_die | [Temporary] (Kill this at the start of its controller's Beginning Phase, before scoring.) |
| 2 | kill_heal_die | [Deathknell] — Draw 1. (When I die, get the effect.) |
| 2 | kill_heal_die | Choose a friendly unit. The next time it would die this turn, heal it, exhaust it, and recall it instead. (Send it to base. This isn't a move.) |
| 2 | kill_heal_die | Kill a unit at a battlefield. |
| 1 | kill_heal_die | :rb_energy_1:, :rb_exhaust:: Return a friendly unit at a battlefield to its owner's hand. Play a Gold gear token exhausted. (It has "[Reaction][>] Kill this, :rb_exhaust:: [Add] :rb_rune_rainbow:.") |
| 1 | kill_heal_die | :rb_energy_1::rb_rune_calm:, :rb_exhaust:, Kill this: Draw 1. |

### target_selection

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 20 | choose_target | [Deflect] (Opponents must pay :rb_rune_rainbow: to choose me with a spell or ability.) |
| 3 | choose_target | [Deflect 2] (Opponents must pay :rb_rune_rainbow::rb_rune_rainbow: to choose me with a spell or Ability.) |
| 3 | choose_target | Choose one — |
| 2 | choose_target | Choose a friendly unit. The next time it would die this turn, heal it, exhaust it, and recall it instead. (Send it to base. This isn't a move.) |
| 1 | choose_target | :rb_exhaust:: Play two :rb_energy_1: :rb_might: Bird unit tokens with [Deflect]. Use this ability only while I'm at a battlefield. (Opponents must pay :rb_rune_rainbow: to choose a [Deflect] unit with a spell or ability.) |
| 1 | choose_target | :rb_rune_calm:: [Action] — Choose a unit you control. Move me to its location and it to my original location. If it's equipped, you may attach one of its Equipment to me. Use only once per turn. |

### token_creation

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 2 | token_word | When I conquer, play a Gold gear token exhausted. |
| 2 | token_word | When I hold, play two Gold gear tokens exhausted. |
| 1 | token_word | (You can't start the game with a token battlefield.) |
| 1 | token_word | :rb_energy_1:, :rb_exhaust:: Play a 1 :rb_might: Recruit unit token. |
| 1 | token_word | :rb_energy_1:, :rb_exhaust:: Play a 2 :rb_might: Sand Soldier unit token to your base. Use only if you've played an Equipment this turn. |
| 1 | token_word | :rb_energy_1:, :rb_exhaust:: Return a friendly unit at a battlefield to its owner's hand. Play a Gold gear token exhausted. (It has "[Reaction][>] Kill this, :rb_exhaust:: [Add] :rb_rune_rainbow:.") |

### trigger_modifier

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 11 | repeat | [Repeat] :rb_energy_2: (You may pay the additional cost to repeat this spell's effect.) |
| 2 | get_effect | [Deathknell] — Draw 1. (When I die, get the effect.) |
| 1 | get_effect | :rb_exhaust:: [Legion] — The next unit you play this turn enters ready. (Get the effect if you've played another card this turn.) |
| 1 | get_effect | :rb_exhaust:: [Reaction], [Legion] — [Add] :rb_energy_1:. (Abilities that add resources can't be reacted to. Get the effect if you've played a card this turn.) |
| 1 | repeat | :rb_rune_rainbow:, :rb_exhaust:: Give the next spell you play this turn [Repeat] equal to its cost. (You may pay the additional cost to repeat the spell's effect.) |
| 1 | get_effect | [Deathknell] — Banish me. (When I die, get the effect.) |

### attachment_modifier

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 9 | attach_word, equip_word | [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less, even if it's already attached.) |
| 5 | attach_word, equip_word | [Equip] :rb_rune_body: (:rb_rune_body:: Attach this to a unit you control.) |
| 5 | attach_word, equip_word | [Equip] :rb_rune_calm: (:rb_rune_calm:: Attach this to a unit you control.) |
| 4 | attach_word, equip_word | [Equip] :rb_rune_chaos: (:rb_rune_chaos:: Attach this to a unit you control.) |
| 4 | attach_word, equip_word | [Equip] :rb_rune_rainbow: (:rb_rune_rainbow:: Attach this to a unit you control.) |
| 4 | attach_word | [Quick-Draw] (This has [Reaction]. When you play it, attach it to a unit you control.) |

### xp_progression

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 7 | xp_word | [Hunt] (When I conquer or hold, gain 1 XP.) |
| 5 | xp_word | [Hunt 2] (When I conquer or hold, gain 2 XP.) |
| 2 | xp_word | Spend 2 XP: [Buff] me. (Give me a +1 :rb_might: buff if I don't have one.) |
| 1 | xp_word | [Deathknell][>] Choose an opponent. They reveal their hand. You can look at their facedown cards this turn. Gain 1 XP. (When I die, get the effects.) |
| 1 | xp_word | [Equip] — Spend 1 XP (Pay the cost: Attach this to a unit you control.) |
| 1 | xp_word | [Hunt 3] (When I conquer or hold, gain 3 XP.) |

### keyword_modifier

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 4 | grant_keyword | [Quick-Draw] (This has [Reaction]. When you play it, attach it to a unit you control.) |
| 1 | grant_keyword | :rb_energy_1:, :rb_exhaust:: Return a friendly unit at a battlefield to its owner's hand. Play a Gold gear token exhausted. (It has "[Reaction][>] Kill this, :rb_exhaust:: [Add] :rb_rune_rainbow:.") |
| 1 | grant_keyword | :rb_exhaust:: Give a unit [Ganking] this turn. (It can move from battlefield to battlefield.) |
| 1 | grant_keyword | :rb_rune_rainbow:, :rb_exhaust:: Give the next spell you play this turn [Repeat] equal to its cost. (You may pay the additional cost to repeat the spell's effect.) |
| 1 | grant_keyword | [Deathknell][>] Play a 1 :rb_might: Bird unit token with [Deflect] to your base. (When I die, get the effect. Opponents must pay :rb_rune_rainbow: to choose a [Deflect] unit with a spell or ability.) |
| 1 | grant_keyword | [Level 3][>] I have +1 :rb_might: and [Deflect]. (While you have 3+ XP, get the effect. Opponents must pay :rb_rune_rainbow: to choose a [Deflect] unit with a spell or ability.) |

### play_permission

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 12 | you_may_play_object | [Ambush] (You may play me as a [Reaction] to a battlefield where you have units.) |
| 4 | play_it | [Quick-Draw] (This has [Reaction]. When you play it, attach it to a unit you control.) |
| 3 | you_may_play_object, play_me_to_location | You may play me to an open battlefield. |
| 2 | you_may_play_object, play_me_to_location | You may play me to an occupied enemy battlefield. |
| 1 | play_it | :rb_energy_1::rb_rune_order:, :rb_exhaust:: Kill a friendly unit. Look at the top 5 cards of your Main Deck. You may banish a unit from among them that has Might up to 1 more than the killed unit and play it, ignoring its cost. Then recycle the rest. |
| 1 | you_may_play_object | :rb_exhaust:: Play three 1 :rb_might: Recruit unit tokens. (You may play them to different locations.) |

### entry_state

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 9 | enter_ready_or_exhausted, have_me_enter_ready | [Accelerate] (You may pay :rb_energy_1::rb_rune_fury: as an additional cost to have me enter ready.) |
| 6 | enter_ready_or_exhausted | I enter ready. |
| 5 | enter_ready_or_exhausted, have_me_enter_ready | [Accelerate] (You may pay :rb_energy_1::rb_rune_body: as an additional cost to have me enter ready.) |
| 4 | enter_ready_or_exhausted, have_me_enter_ready | [Accelerate] (You may pay :rb_energy_1::rb_rune_mind: as an additional cost to have me enter ready.) |
| 3 | enter_ready_or_exhausted, have_me_enter_ready | [Accelerate] (You may pay :rb_energy_1::rb_rune_chaos: as an additional cost to have me enter ready.) |
| 3 | enter_ready_or_exhausted | This enters exhausted. |

### buff_effect

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 2 | buff_word | As you play this, you may spend a buff as an additional cost. If you do, ignore this spell's cost. |
| 2 | buff_word | Spend 2 XP: [Buff] me. (Give me a +1 :rb_might: buff if I don't have one.) |
| 1 | buff_word | :rb_energy_1:, :rb_exhaust:: Buff a friendly unit. (If it doesn't have a buff, it gets a +1 :rb_might: buff.) |
| 1 | buff_word | :rb_exhaust:: Buff an exhausted friendly unit. (If it doesn't have a buff, it gets a +1 :rb_might: buff.) |
| 1 | buff_word | :rb_exhaust:: Buff me. (I get a +1 :rb_might: buff.) |
| 1 | buff_word | [Legion] — When you play me, buff me. (If I don't have a buff, I get a +1 :rb_might: buff. Get the effect if you've played another card this turn.) |

### resource_generation

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 7 | gain_xp | [Hunt] (When I conquer or hold, gain 1 XP.) |
| 5 | gain_xp | [Hunt 2] (When I conquer or hold, gain 2 XP.) |
| 1 | channel_rune | [Deathknell] — Channel 1 rune exhausted. (When I die, get the effect.) |
| 1 | channel_rune | [Deathknell][>] Channel 1 rune exhausted. (When I die, get the effect.) |
| 1 | gain_xp | [Deathknell][>] Choose an opponent. They reveal their hand. You can look at their facedown cards this turn. Gain 1 XP. (When I die, get the effects.) |
| 1 | gain_xp | [Hunt 3] (When I conquer or hold, gain 3 XP.) |

### hide_modifier

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 32 | hide_word | [Hidden] (Hide now for :rb_rune_rainbow: to react with later for :rb_energy_0:.) |
| 1 | hide_word | Hidden (Hide now for :rb_rune_rainbow: to react with later for :rb_energy_0:.) |
| 1 | hide_word | Return up to two cards with [Hidden] from your trash to your hand. You can hide cards ignoring costs this turn. |
| 1 | hide_word | When I attack, you may pay :rb_rune_mind: to play a card with [Hidden] from your hand, ignoring its cost. If it’s a unit, play it here. |
| 1 | hide_word | When I defend, choose an enemy unit here and reveal the top 5 cards of your Main Deck. Deal 1 to that unit for each card with [Hidden] revealed this way, then recycle the revealed cards. |
| 1 | hide_word | When you hide a card, ready me. |

### tag_reference

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 1 | known_tags | :rb_energy_1::rb_rune_fury:, Recycle a unit from your trash, :rb_exhaust:: Play a 3 :rb_might: Mech unit token to your base. |
| 1 | tag_word | :rb_exhaust:: Give a unit with the named tag -2 :rb_might: this turn. |
| 1 | known_tags | :rb_exhaust:: Play two :rb_energy_1: :rb_might: Bird unit tokens with [Deflect]. Use this ability only while I'm at a battlefield. (Opponents must pay :rb_rune_rainbow: to choose a [Deflect] unit with a spell or ability.) |
| 1 | known_tags | [Deathknell] — Play two 3 :rb_might: Mech unit tokens to your base. (When I die, get the effect.) |
| 1 | known_tags | [Deathknell][>] Play a 1 :rb_might: Bird unit token with [Deflect] to your base. (When I die, get the effect. Opponents must pay :rb_rune_rainbow: to choose a [Deflect] unit with a spell or ability.) |
| 1 | known_tags | As an additional cost to play me, kill a Bird, Cat, Dog, or Poro you control. You may play me to its battlefield (even if you don't have other units there). |

### replacement_effect

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 2 | instead, would | Choose a friendly unit. The next time it would die this turn, heal it, exhaust it, and recall it instead. (Send it to base. This isn't a move.) |
| 1 | instead | [Deathknell][>] Draw 1. If it's your Beginning Phase, draw 2 instead. (When I die, get the effect.) |
| 1 | instead | [Legion] — Kill it now instead. (Get the effect if you've played another card this turn.) |
| 1 | instead | [Level 11][>] I cost :rb_energy_6::rb_rune_calm::rb_rune_calm::rb_rune_calm: less instead. |
| 1 | instead | [Level 11][>] This costs :rb_energy_4: less instead. |
| 1 | instead | [Level 6][>] Give it +3 :rb_might: this turn instead. (While you have 6+ XP, get the effect.) |

### resource_add_ability

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 1 | add_resource_keyword | :rb_energy_1:, :rb_exhaust:: Return a friendly unit at a battlefield to its owner's hand. Play a Gold gear token exhausted. (It has "[Reaction][>] Kill this, :rb_exhaust:: [Add] :rb_rune_rainbow:.") |
| 1 | add_resource_keyword, add_resources_reminder | :rb_exhaust:: [Reaction] — [Add] :rb_energy_1:. (Abilities that add resources can't be reacted to.) |
| 1 | add_resource_keyword, add_resources_reminder | :rb_exhaust:: [Reaction] — [Add] :rb_energy_2:. Use only to play spells. (Abilities that add resources can't be reacted to.) |
| 1 | add_resource_keyword, add_resources_reminder | :rb_exhaust:: [Reaction] — [Add] :rb_rune_body:. (Abilities that add resources can't be reacted to.) |
| 1 | add_resource_keyword, add_resources_reminder | :rb_exhaust:: [Reaction] — [Add] :rb_rune_calm:. (Abilities that add resources can't be reacted to.) |
| 1 | add_resource_keyword, add_resources_reminder | :rb_exhaust:: [Reaction] — [Add] :rb_rune_chaos:. (Abilities that add resources can't be reacted to.) |

### stun_effect

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 1 | stun_word | :rb_rune_order: — Stun an enemy unit. |
| 1 | stun_keyword, stun_word | [Action][>] :rb_energy_1::rb_rune_rainbow:, :rb_exhaust:: [Stun] an enemy unit attacking here. (It doesn't deal combat damage this turn.) |
| 1 | stun_keyword, stun_word | [Level 6][>] [Stun] an enemy unit. (While you have 6+ XP, get the effect. A stunned unit doesn't deal combat damage this turn.) |
| 1 | stun_keyword, stun_word | [Stun] a unit. (It doesn't deal combat damage this turn.) |
| 1 | stun_keyword, stun_word | [Stun] an attacking enemy unit. If it's already stunned, return it to its owner's hand instead. (A stunned unit doesn't deal combat damage this turn.) |
| 1 | stun_keyword, stun_word | Choose a battlefield. An opponent reveals their hand. You may choose a unit from it. They play that unit to that battlefield, ignoring any and all costs. When they do, [Stun] it. (It doesn't deal combat damage this turn.) |

### trait_identity

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 1 | identity_statement | (I become a copy of something when played. I don't get that card's play effects.) |
| 1 | mech_trait | :rb_energy_1::rb_rune_fury:, Recycle a unit from your trash, :rb_exhaust:: Play a 3 :rb_might: Mech unit token to your base. |
| 1 | mighty_state | [Deathknell] — If I was [Mighty], draw 2. (When I die, get the effect. I'm Mighty while I have 5+ :rb_might:.) |
| 1 | mech_trait | [Deathknell] — Play two 3 :rb_might: Mech unit tokens to your base. (When I die, get the effect.) |
| 1 | mighty_state | As an additional cost to play this, kill a friendly [Mighty] unit. (A unit is Mighty while it has 5+ :rb_might:.) |
| 1 | identity_statement | Choose a unit. Play a ready Reflection unit token to your base. It becomes a copy of that unit. Give it [Temporary]. (Kill it at the start of its controller's Beginning Phase, before scoring.) |

### score_modifier

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 1 | score_points | :rb_energy_4::rb_rune_mind::rb_rune_mind::rb_rune_mind::rb_rune_mind:, :rb_exhaust:: Score 1 point. |
| 1 | score_points | At the start of each player's first Beginning Phase, that player gains 1 point. |
| 1 | score_points | I cost :rb_energy_2::rb_rune_calm: less for each point you scored from holding this turn. |
| 1 | score_points | If an opponent's score is within 3 points of the Victory Score, I enter ready. |
| 1 | score_points | If an opponent's score is within 3 points of the Victory Score, this costs :rb_energy_2: less. |
| 1 | score_points | Increase the points needed to win the game by 1. |

### banish_effect

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 1 | banish_word | :rb_energy_1::rb_rune_order:, :rb_exhaust:: Kill a friendly unit. Look at the top 5 cards of your Main Deck. You may banish a unit from among them that has Might up to 1 more than the killed unit and play it, ignoring its cost. Then recycle the rest. |
| 1 | banish_word | :rb_energy_3::rb_rune_mind:, Banish this: Play all units banished with this, ignoring their costs. (Use only if unattached.) |
| 1 | banish_word | :rb_exhaust:: Play a unit banished with this. (You must pay its costs.) |
| 1 | banish_word | [Deathknell] — Banish me. (When I die, get the effect.) |
| 1 | banish_word | As you look at or reveal me from the top of your deck, you may banish me. If you do, you may play me for :rb_rune_rainbow:. |
| 1 | banish_word | At the end of your turn, reveal cards from the top of your Main Deck until you reveal a unit and banish it. Play it, ignoring its cost, and recycle the rest. |

### conditional_resolution

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 2 | if_you_do | As you play this, you may spend a buff as an additional cost. If you do, ignore this spell's cost. |
| 1 | if_you_do | As an additional cost to play this, you may exhaust a friendly unit. If you do, draw 2. Otherwise, draw 1. |
| 1 | if_you_do | As you look at or reveal me from the top of your deck, you may banish me. If you do, you may play me for :rb_rune_rainbow:. |
| 1 | if_you_do | As you play me, add the Baron Pit battlefield token to the board if it's not there already. If you do, I enter there. (It has "Units can move here from anywhere.") |
| 1 | if_you_do | As you play me, you may discard 1 as an additional cost. If you do, reduce my cost by :rb_energy_2:. |
| 1 | when_they_do | Choose a battlefield. An opponent reveals their hand. You may choose a unit from it. They play that unit to that battlefield, ignoring any and all costs. When they do, [Stun] it. (It doesn't deal combat damage this turn.) |

### contextual_clarification

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 9 | even_if | [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less, even if it's already attached.) |
| 3 | including | [Reaction] (Play any time, even before spells and abilities resolve, including to a battlefield you control.) |
| 1 | even_if | As an additional cost to play me, kill a Bird, Cat, Dog, or Poro you control. You may play me to its battlefield (even if you don't have other units there). |
| 1 | even_if | I can be played to a battlefield where there are enemy units (even if you don't have units there). |
| 1 | including | Units here have +1 :rb_might:. (This includes attackers.) |
| 1 | even_if | When you play me, choose an opponent. They reveal their hand. Choose a card revealed this way and banish it. When they hold, return it to their hand (even if I'm no longer on the board). |

### choice_modal

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 3 | choose_one | Choose one — |
| 1 | choose_one | Choose one you haven't already chosen — |
| 1 | choose_up_to | Choose up to 3 cards from opponents' trashes. Their owners recycle them. |
| 1 | choose_one | Each opponent reveals the top card of their Main Deck. Choose one and banish it, then play it, ignoring its cost. Then recycle the rest. |
| 1 | choose_one | Spend my buff: Choose one you've not chosen this turn — |
| 1 | choose_one | When you attach an Equipment to me, choose one that hasn't been chosen this turn — |

### counter_effect

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 2 | counter_word | Counter a spell. |
| 1 | counter_word | Choose a friendly unit and a spell. Counter that spell and give that unit +:rb_might: equal to that spell's Energy cost this turn. |
| 1 | counter_word | Choose a friendly unit at a battlefield. Counter an enemy spell or ability that chooses it and no other friendly unit. |
| 1 | counter_word | Counter a spell that costs no more than :rb_energy_4: and no more than :rb_rune_rainbow:. |
| 1 | counter_word | Counter a spell unless its controller pays :rb_energy_2:. |
| 1 | counter_word | Counter a spell. Its controller can't play spells this turn. |

### usage_restriction

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 1 | use_only | :rb_energy_1:, :rb_exhaust:: Play a 2 :rb_might: Sand Soldier unit token to your base. Use only if you've played an Equipment this turn. |
| 1 | use_only | :rb_energy_3::rb_rune_mind:, Banish this: Play all units banished with this, ignoring their costs. (Use only if unattached.) |
| 1 | use_only | :rb_exhaust:: [Reaction] — [Add] :rb_energy_2:. Use only to play spells. (Abilities that add resources can't be reacted to.) |
| 1 | use_only | :rb_exhaust:: [Reaction] — [Add] :rb_rune_rainbow:. Use only to play gear or use gear abilities. (Abilities that add resources can't be reacted to.) |
| 1 | use_only | :rb_exhaust:: [Reaction] — [Add] :rb_rune_rainbow:. Use only to play spells. (Abilities that add resources can't be reacted to.) |
| 1 | use_only | :rb_exhaust:: [Reaction] — Draw 1. Use only if you've chosen enemy units and/or gear twice this turn with spells or unit abilities. |

### effect_equivalence

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 1 | becomes | (I become a copy of something when played. I don't get that card's play effects.) |
| 1 | becomes | Choose a unit. Play a ready Reflection unit token to your base. It becomes a copy of that unit. Give it [Temporary]. (Kill it at the start of its controller's Beginning Phase, before scoring.) |
| 1 | becomes | When a unit you control becomes [Mighty], you may pay :rb_rune_order: to ready it. (A unit is Mighty while it has 5+ :rb_might:.) |
| 1 | is_also | When I move to a battlefield, play a 1 :rb_might: Recruit unit token here. (It is also at the battlefield.) |
| 1 | becomes | When one of your units becomes [Mighty], you may exhaust me to channel 1 rune exhausted. (A unit is Mighty while it has 5+ :rb_might:.) |
| 1 | becomes | When you conquer or hold, you may discard 1 and exhaust me to play a ready Reflection unit token there. It becomes a copy of another unit there. Give it [Temporary]. |

### control_change

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 1 | take_control | Choose an enemy unit at a battlefield with 3 :rb_might: or less. If you paid the additional cost, choose any enemy unit at a battlefield instead. Take control of it, exhaust it, and recall it. |
| 1 | take_control | Choose an enemy unit at a battlefield. Take control of it and recall it. (Send it to your base. This isn't a move.) |
| 1 | gain_control, new_choices | Gain control of a spell. You may make new choices for it. |
| 1 | lose_control | Lose control of that unit and recall it at end of turn. (Send it to base. This isn't a move.) |
| 1 | take_control | Take control of an enemy unit at a battlefield. Ready it. (Start a combat if other enemies are there. Otherwise, conquer.) |
| 1 | control_until | When you play me, if you paid the additional cost, move an enemy gear to your base. You control it until I leave the board. If it's an Equipment, attach it to me. |

### copy_effect

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 1 | copy_word | (I become a copy of something when played. I don't get that card's play effects.) |
| 1 | copy_word | As this is attached to a unit, copy that unit's text to this Equipment's effect text for as long as this is attached to it. |
| 1 | copy_word | Choose a unit. Play a ready Reflection unit token to your base. It becomes a copy of that unit. Give it [Temporary]. (Kill it at the start of its controller's Beginning Phase, before scoring.) |
| 1 | copy_word | Once each turn, if you would play a token unit while I'm at a battlefield, you may play that token and an additional copy of it instead. |
| 1 | copy_word | When you conquer or hold, you may discard 1 and exhaust me to play a ready Reflection unit token there. It becomes a copy of another unit there. Give it [Temporary]. |
| 1 | copy_word | When you play me, play two Reflection unit tokens here. They become copies of me. |

### target_protection

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 2 | cant_be_chosen | I can't be chosen by enemy spells and abilities. |
| 1 | cant_be_chosen | [Level 16][>] I can't be chosen by enemy spells and abilities. |
| 1 | cant_be_chosen | Your units here with less Might than me can't be chosen by enemy spells and abilities. |

### turn_sequence

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 1 | turn_order | Each player looks at the top 5 cards of their Main Deck, banishes one of them, then recycles the rest. Starting with the next player, each player plays those cards, ignoring Energy costs. (They must still pay Power costs.) |
| 1 | turn_order | Starting with the next player, each other player chooses a unit you don't control that hasn't been chosen for this spell. Kill those units. |
| 1 | turn_order | Starting with the next player, each player may return a unit to its owner's hand. |
| 1 | extra_turn | Take a turn after this one. Banish this. |

### deckbuilding_restriction

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 3 | deck_can_have | [Unique] (Your deck can have only 1 card with this name.) |

### play_restriction

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 1 | cant_play | Counter a spell. Its controller can't play spells this turn. |
| 1 | cant_play | Play me only to a battlefield you conquered this turn. (You can't play me anywhere else.) |
| 1 | cant_play, play_lockout | When you play me, opponents can't play cards this turn. |

### modal_option

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 1 | following_options | When I attack, reveal the top rune of your rune deck, then recycle it. Do one of the following based on its domain: |
| 1 | following_options | When I move, draw 1, then discard 1. Then, do the following based on the discarded card's type: |

### type_exclusion

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 1 | not_battlefield | When an opponent moves to a battlefield other than mine, draw 1. (Bases are not battlefield.) |
| 1 | not_cards | When you recycle one or more cards to your Main Deck, buff a friendly unit. (If it doesn't have a buff, it gets a +1 :rb_might: buff. Runes aren't cards.) |

### ability_sharing

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 1 | have_all_abilities, exhaust_abilities | I have all :rb_exhaust: abilities of all friendly legends, units, and gear. |

### effect_suppression

| Occurrences | Reasons | Line |
| --- | --- | --- |
| 1 | no_play_effects, play_effects | (I become a copy of something when played. I don't get that card's play effects.) |
