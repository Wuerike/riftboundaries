# Cards Taxonomy Alignment

Bridge report from text inventory families/units to the target semantic contract.
This report does not read extracted facts or web relations.

## Summary

- Families: 47
- Mapped families: 47
- Unmapped families: 0
- Unique normalized units: 1209
- Mapped units: 1209
- Multi-role units: 896
- High-priority units: 1118
- Event-produced unit occurrences: 1422
- Trigger-observed unit occurrences: 886
- Payoff-output unit occurrences: 1004

## Family Alignment

| Family | Priority | Unit occ. | Unique units | Roles | Axes | Semantic targets |
| --- | --- | --- | --- | --- | --- | --- |
| cost_modifier | high | 347 | 221 | cost_or_requirement, restriction_or_permission | cost, resource, modality, amount | conditions, cost_patterns, numeric_patterns, symbols |
| timing_window | high | 326 | 43 | trigger_observed, restriction_or_permission | trigger, timing, modality | conditions, trigger_event_patterns, triggers |
| combat_modifier | high | 325 | 197 | event_produced, trigger_observed, state_or_modifier | event, action, object, stat, polarity | combat_patterns, triggers |
| deck_manipulation | high | 247 | 157 | event_produced, payoff_output | action, object, location, amount | actions, deck_patterns, zones |
| location_restriction | high | 246 | 217 | targeting_or_scope, restriction_or_permission | location, target, scope | targets, zones |
| stat_modifier | high | 227 | 161 | payoff_output, state_or_modifier | stat, amount, duration, target | combat_patterns, duration_patterns, numeric_patterns |
| movement_modifier | high | 203 | 140 | event_produced, state_or_modifier, targeting_or_scope | action, location, target | actions, movement_patterns, targets, zones |
| ready_exhaust_effect | high | 181 | 139 | event_produced, state_or_modifier, cost_or_requirement | action, cost, duration, polarity | actions, cost_patterns, symbols, trait_patterns |
| damage_effect | high | 147 | 86 | event_produced, payoff_output | action, object, amount, stat | actions, combat_patterns, numeric_patterns |
| removal_or_healing | high | 127 | 91 | event_produced, trigger_observed, payoff_output, state_or_modifier | action, event, object, polarity, duration | actions, conditions, removal_healing_patterns, trigger_event_patterns, trigger_modifier_patterns, triggers |
| attachment_modifier | high | 110 | 51 | event_produced, state_or_modifier, targeting_or_scope | action, object, target | actions, attachment_patterns, targets |
| trigger_modifier | high | 96 | 30 | trigger_observed, state_or_modifier | trigger, duration, amount | trigger_event_patterns, trigger_modifier_patterns, triggers |
| buff_effect | high | 87 | 59 | event_produced, payoff_output, state_or_modifier | action, stat, keyword, duration | actions, duration_patterns, numeric_patterns |
| xp_progression | high | 80 | 55 | trigger_observed, payoff_output, cost_or_requirement | resource, amount, trigger | conditions, numeric_patterns, resource_patterns |
| token_creation | high | 78 | 70 | event_produced, payoff_output | action, object, amount, identity, location | card_types, numeric_patterns, token_patterns, zones |
| hide_modifier | high | 75 | 12 | state_or_modifier, restriction_or_permission | keyword, cost, timing | conditions, keywords |
| keyword_modifier | high | 62 | 54 | event_produced, state_or_modifier, identity_or_descriptor | keyword, action, duration | keywords, trait_patterns |
| play_permission | high | 57 | 37 | restriction_or_permission, event_produced | action, location, modality | actions, conditions, permission_patterns, zones |
| entry_state | high | 52 | 27 | event_produced, state_or_modifier | event, action, duration | trait_patterns |
| resource_generation | high | 50 | 33 | event_produced, payoff_output | resource, action, amount | actions, numeric_patterns, resource_patterns, symbols |
| resource_add_ability | high | 44 | 17 | event_produced, payoff_output, cost_or_requirement | resource, action, cost, timing | actions, resource_patterns, symbols |
| stun_effect | high | 32 | 29 | event_produced, state_or_modifier, restriction_or_permission | keyword, polarity, duration, target | combat_patterns, keywords |
| replacement_effect | high | 31 | 26 | state_or_modifier, restriction_or_permission | polarity, trigger, duration | conditions, duration_patterns |
| banish_effect | high | 24 | 18 | event_produced, payoff_output, state_or_modifier | action, object, location | actions, banish_patterns, zones |
| counter_effect | high | 9 | 6 | event_produced, payoff_output, restriction_or_permission | action, object, polarity | actions |
| control_change | high | 7 | 7 | event_produced, state_or_modifier | action, target, duration, polarity | actions, targets |
| copy_effect | high | 6 | 6 | state_or_modifier, identity_or_descriptor | action, identity, object | copy_patterns |
| target_protection | high | 4 | 3 | restriction_or_permission, state_or_modifier | target, polarity, keyword | conditions, target_protection_patterns, targets |
| play_restriction | high | 3 | 3 | restriction_or_permission | polarity, action, duration | actions, conditions, permission_patterns |
| keyword_reminder | medium | 495 | 105 | identity_or_descriptor | keyword, extraction_seed | keywords |
| duration_modifier | medium | 168 | 138 | state_or_modifier | duration, modality | conditions, duration_patterns |
| target_selection | medium | 111 | 71 | targeting_or_scope | target, object, modality | card_types, targets |
| symbol_option | medium | 39 | 9 | cost_or_requirement, identity_or_descriptor | cost, resource, symbol | cost_patterns, symbols |
| tag_reference | medium | 35 | 32 | identity_or_descriptor, targeting_or_scope | identity, target | targets, trait_patterns |
| trait_identity | medium | 34 | 25 | identity_or_descriptor, state_or_modifier | identity, keyword, stat | trait_patterns |
| score_modifier | medium | 22 | 22 | event_produced, payoff_output | stat, amount, event | numeric_patterns, score_patterns |
| conditional_resolution | medium | 19 | 18 | trigger_observed, restriction_or_permission | trigger, modality | conditions |
| usage_restriction | medium | 8 | 7 | restriction_or_permission, cost_or_requirement | modality, timing, cost | conditions, permission_patterns |
| effect_equivalence | medium | 7 | 7 | state_or_modifier, identity_or_descriptor | identity, polarity | trait_patterns |
| turn_sequence | medium | 4 | 4 | event_produced, restriction_or_permission | timing, event | conditions, triggers |
| deckbuilding_restriction | medium | 3 | 1 | restriction_or_permission, identity_or_descriptor | modality, identity, amount | conditions |
| ability_sharing | medium | 1 | 1 | state_or_modifier | keyword, identity | trait_patterns |
| effect_suppression | medium | 1 | 1 | restriction_or_permission, state_or_modifier | polarity, action | conditions, copy_patterns |
| contextual_clarification | low | 17 | 7 | restriction_or_permission | modality, location, duration | conditions, zones |
| choice_modal | low | 9 | 7 | restriction_or_permission | modality, action | conditions |
| modal_option | low | 5 | 5 | restriction_or_permission | modality, object | card_types, conditions |
| type_exclusion | low | 2 | 2 | identity_or_descriptor, restriction_or_permission | identity, polarity | card_types, conditions |

## Role Summary

| Role | Unit occ. | Unique units | Top families |
| --- | --- | --- | --- |
| event_produced | 1422 | 899 | combat_modifier, deck_manipulation, location_restriction, movement_modifier, ready_exhaust_effect, cost_modifier, keyword_reminder, damage_effect, stat_modifier, removal_or_healing, attachment_modifier, duration_modifier |
| state_or_modifier | 1315 | 814 | combat_modifier, stat_modifier, movement_modifier, keyword_reminder, ready_exhaust_effect, cost_modifier, duration_modifier, location_restriction, removal_or_healing, attachment_modifier, trigger_modifier, buff_effect |
| restriction_or_permission | 1056 | 535 | cost_modifier, timing_window, location_restriction, keyword_reminder, combat_modifier, hide_modifier, movement_modifier, ready_exhaust_effect, target_selection, removal_or_healing, play_permission, stat_modifier |
| payoff_output | 1004 | 673 | deck_manipulation, stat_modifier, combat_modifier, damage_effect, location_restriction, removal_or_healing, duration_modifier, cost_modifier, buff_effect, ready_exhaust_effect, xp_progression, token_creation |
| trigger_observed | 886 | 395 | timing_window, combat_modifier, keyword_reminder, removal_or_healing, cost_modifier, trigger_modifier, location_restriction, xp_progression, stat_modifier, damage_effect, duration_modifier, ready_exhaust_effect |
| identity_or_descriptor | 659 | 218 | keyword_reminder, timing_window, combat_modifier, keyword_modifier, cost_modifier, symbol_option, attachment_modifier, tag_reference, trait_identity, hide_modifier, movement_modifier, location_restriction |
| targeting_or_scope | 629 | 437 | location_restriction, movement_modifier, target_selection, attachment_modifier, cost_modifier, combat_modifier, keyword_reminder, stat_modifier, damage_effect, duration_modifier, token_creation, tag_reference |
| cost_or_requirement | 597 | 397 | cost_modifier, ready_exhaust_effect, xp_progression, combat_modifier, location_restriction, entry_state, resource_generation, keyword_reminder, resource_add_ability, target_selection, removal_or_healing, symbol_option |

## Semantic Target Coverage

| Semantic target | Unit occ. | Unique units | Top families |
| --- | --- | --- | --- |
| actions | 1186 | 746 | deck_manipulation, movement_modifier, ready_exhaust_effect, combat_modifier, location_restriction, damage_effect, cost_modifier, removal_or_healing, attachment_modifier, keyword_reminder, buff_effect, stat_modifier |
| conditions | 1110 | 534 | cost_modifier, timing_window, keyword_reminder, duration_modifier, removal_or_healing, stat_modifier, location_restriction, combat_modifier, xp_progression, hide_modifier, ready_exhaust_effect, trigger_modifier |
| numeric_patterns | 876 | 589 | cost_modifier, stat_modifier, combat_modifier, damage_effect, location_restriction, duration_modifier, ready_exhaust_effect, buff_effect, xp_progression, token_creation, resource_generation, target_selection |
| triggers | 823 | 338 | timing_window, combat_modifier, keyword_reminder, removal_or_healing, trigger_modifier, location_restriction, cost_modifier, damage_effect, stat_modifier, duration_modifier, ready_exhaust_effect, deck_manipulation |
| zones | 740 | 528 | deck_manipulation, location_restriction, movement_modifier, combat_modifier, cost_modifier, token_creation, ready_exhaust_effect, play_permission, damage_effect, stat_modifier, duration_modifier, keyword_modifier |
| targets | 638 | 445 | location_restriction, movement_modifier, target_selection, attachment_modifier, cost_modifier, combat_modifier, keyword_reminder, stat_modifier, damage_effect, duration_modifier, token_creation, tag_reference |
| keywords | 623 | 190 | keyword_reminder, timing_window, combat_modifier, hide_modifier, keyword_modifier, attachment_modifier, movement_modifier, stun_effect, location_restriction, duration_modifier, trigger_modifier, cost_modifier |
| combat_patterns | 584 | 397 | combat_modifier, stat_modifier, damage_effect, duration_modifier, location_restriction, keyword_reminder, cost_modifier, buff_effect, deck_manipulation, ready_exhaust_effect, movement_modifier, stun_effect |
| symbols | 564 | 375 | cost_modifier, ready_exhaust_effect, combat_modifier, xp_progression, location_restriction, entry_state, resource_generation, resource_add_ability, target_selection, removal_or_healing, symbol_option, token_creation |
| trigger_event_patterns | 507 | 150 | timing_window, keyword_reminder, removal_or_healing, trigger_modifier, cost_modifier, location_restriction, duration_modifier, ready_exhaust_effect, xp_progression, combat_modifier, deck_manipulation, replacement_effect |
| cost_patterns | 489 | 339 | cost_modifier, ready_exhaust_effect, entry_state, location_restriction, target_selection, combat_modifier, symbol_option, token_creation, removal_or_healing, stat_modifier, duration_modifier, trigger_modifier |
| duration_patterns | 385 | 286 | stat_modifier, duration_modifier, combat_modifier, buff_effect, cost_modifier, location_restriction, damage_effect, replacement_effect, movement_modifier, ready_exhaust_effect, keyword_modifier, removal_or_healing |
| trait_patterns | 298 | 237 | ready_exhaust_effect, keyword_modifier, entry_state, cost_modifier, combat_modifier, token_creation, location_restriction, tag_reference, trait_identity, duration_modifier, movement_modifier, removal_or_healing |
| deck_patterns | 247 | 157 | deck_manipulation, combat_modifier, location_restriction, cost_modifier, ready_exhaust_effect, movement_modifier, removal_or_healing, keyword_reminder, timing_window, target_selection, trait_identity, stat_modifier |
| movement_patterns | 203 | 140 | movement_modifier, location_restriction, combat_modifier, keyword_reminder, keyword_modifier, cost_modifier, duration_modifier, stat_modifier, deck_manipulation, replacement_effect, token_creation, xp_progression |
| trigger_modifier_patterns | 202 | 119 | removal_or_healing, trigger_modifier, cost_modifier, keyword_reminder, timing_window, duration_modifier, location_restriction, xp_progression, ready_exhaust_effect, replacement_effect, combat_modifier, deck_manipulation |
| card_types | 196 | 148 | target_selection, token_creation, cost_modifier, location_restriction, ready_exhaust_effect, combat_modifier, tag_reference, choice_modal, movement_modifier, deck_manipulation, duration_modifier, modal_option |
| resource_patterns | 143 | 86 | xp_progression, resource_generation, resource_add_ability, keyword_reminder, combat_modifier, cost_modifier, ready_exhaust_effect, trigger_modifier, stat_modifier, keyword_modifier, movement_modifier, removal_or_healing |
| removal_healing_patterns | 127 | 91 | removal_or_healing, cost_modifier, trigger_modifier, timing_window, location_restriction, ready_exhaust_effect, replacement_effect, duration_modifier, deck_manipulation, combat_modifier, stat_modifier, resource_add_ability |
| attachment_patterns | 110 | 51 | attachment_modifier, keyword_reminder, cost_modifier, contextual_clarification, play_permission, duration_modifier, target_selection, stat_modifier, combat_modifier, deck_manipulation, keyword_modifier, copy_effect |
| token_patterns | 78 | 70 | token_creation, ready_exhaust_effect, location_restriction, combat_modifier, tag_reference, movement_modifier, trait_identity, removal_or_healing, duration_modifier, cost_modifier, timing_window, conditional_resolution |
| permission_patterns | 68 | 47 | play_permission, location_restriction, cost_modifier, usage_restriction, attachment_modifier, duration_modifier, combat_modifier, play_restriction, conditional_resolution, deck_manipulation, keyword_reminder, keyword_modifier |
| banish_patterns | 24 | 18 | banish_effect, cost_modifier, deck_manipulation, removal_or_healing, duration_modifier, replacement_effect, stat_modifier |
| score_patterns | 22 | 22 | score_modifier, combat_modifier, cost_modifier, location_restriction, ready_exhaust_effect, timing_window, duration_modifier, entry_state, stat_modifier, movement_modifier, damage_effect, tag_reference |
| copy_patterns | 7 | 7 | copy_effect, effect_equivalence, trait_identity, duration_modifier, attachment_modifier, effect_suppression, location_restriction, replacement_effect, token_creation |
| target_protection_patterns | 4 | 3 | target_protection, keyword_reminder, xp_progression, location_restriction, cost_modifier, stat_modifier |

## Web Use Coverage

| Web use | Unit occ. | Unique units | Top families |
| --- | --- | --- | --- |
| similarity | 2332 | 1206 | keyword_reminder, cost_modifier, timing_window, combat_modifier, deck_manipulation, location_restriction, stat_modifier, movement_modifier, ready_exhaust_effect, duration_modifier, damage_effect, removal_or_healing |
| deck_synergy | 2114 | 1118 | keyword_reminder, cost_modifier, timing_window, combat_modifier, deck_manipulation, location_restriction, stat_modifier, movement_modifier, ready_exhaust_effect, duration_modifier, damage_effect, removal_or_healing |
| filters | 1828 | 895 | keyword_reminder, cost_modifier, timing_window, combat_modifier, location_restriction, stat_modifier, duration_modifier, ready_exhaust_effect, target_selection, movement_modifier, damage_effect, trigger_modifier |
| enabled_by | 1621 | 863 | keyword_reminder, timing_window, combat_modifier, location_restriction, movement_modifier, cost_modifier, ready_exhaust_effect, damage_effect, stat_modifier, removal_or_healing, attachment_modifier, trigger_modifier |
| enables | 1259 | 812 | combat_modifier, movement_modifier, location_restriction, ready_exhaust_effect, keyword_reminder, cost_modifier, damage_effect, stat_modifier, removal_or_healing, attachment_modifier, buff_effect, duration_modifier |

## Semantic Target Seed Groups


### actions

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 42 | high | deck_manipulation | draw {number}. |
| 27 | high | keyword_reminder, attachment_modifier | [equip] {rb_symbol} |
| 27 | high | attachment_modifier | {rb_symbol}: attach this to a unit you control. |
| 24 | high | ready_exhaust_effect, entry_state, cost_modifier | you may pay {rb_symbol}{rb_symbol} as an additional cost to have me enter ready. |
| 20 | high | resource_add_ability | abilities that add resources can't be reacted to. |
| 20 | high | trigger_modifier, removal_or_healing | when i die, get the effect. |
| 20 | high | movement_modifier | i can move from battlefield to battlefield. |
| 19 | high | combat_modifier, damage_effect | i must be assigned combat damage first. |
| 15 | high | resource_add_ability, keyword_reminder | [add] {rb_symbol}. |
| 15 | high | movement_modifier, keyword_reminder | [ganking] |
| 13 | high | duration_modifier, combat_modifier, damage_effect | it doesn't deal combat damage this turn. |
| 13 | high | location_restriction, damage_effect | deal {number} to a unit at a battlefield. |

### conditions

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 76 | high | timing_window, keyword_reminder | [action] |
| 73 | high | timing_window | play on your turn or in showdowns. |
| 70 | high | timing_window, keyword_reminder | [reaction] |
| 53 | high | timing_window | play any time, even before spells and abilities resolve. |
| 36 | high | symbol_option, cost_modifier | {rb_symbol} |
| 33 | high | hide_modifier | hide now for {rb_symbol} to react with later for {rb_symbol}. |
| 32 | high | hide_modifier, keyword_reminder | [hidden] |
| 24 | high | ready_exhaust_effect, entry_state, cost_modifier | you may pay {rb_symbol}{rb_symbol} as an additional cost to have me enter ready. |
| 20 | high | trigger_modifier, removal_or_healing | when i die, get the effect. |
| 20 | high | target_selection, cost_modifier | opponents must pay {rb_symbol} to choose me with a spell or ability. |
| 18 | high | trigger_modifier, cost_modifier | you may pay the additional cost to repeat this spell's effect. |
| 13 | high | duration_modifier, combat_modifier, damage_effect | it doesn't deal combat damage this turn. |

### numeric_patterns

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 36 | high | symbol_option, cost_modifier | {rb_symbol} |
| 24 | high | ready_exhaust_effect, entry_state, cost_modifier | you may pay {rb_symbol}{rb_symbol} as an additional cost to have me enter ready. |
| 20 | high | target_selection, cost_modifier | opponents must pay {rb_symbol} to choose me with a spell or ability. |
| 19 | high | combat_modifier, stat_modifier | +{number} {rb_symbol} while i'm an attacker. |
| 19 | high | combat_modifier, damage_effect | i must be assigned combat damage first. |
| 18 | high | trigger_modifier, cost_modifier | you may pay the additional cost to repeat this spell's effect. |
| 16 | high | combat_modifier, stat_modifier | +{number} {rb_symbol} while i'm a defender. |
| 13 | high | duration_modifier, combat_modifier, damage_effect | it doesn't deal combat damage this turn. |
| 13 | high | trigger_modifier, xp_progression | while you have {number}+ xp, get the effect. |
| 13 | high | location_restriction, damage_effect | deal {number} to a unit at a battlefield. |
| 13 | high | combat_modifier, resource_generation, xp_progression | when i conquer or hold, gain {number} xp. |
| 12 | high | cost_modifier | {rb_symbol}, {rb_symbol} |

### triggers

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 76 | high | timing_window, keyword_reminder | [action] |
| 73 | high | timing_window | play on your turn or in showdowns. |
| 70 | high | timing_window, keyword_reminder | [reaction] |
| 53 | high | timing_window | play any time, even before spells and abilities resolve. |
| 20 | high | trigger_modifier, removal_or_healing | when i die, get the effect. |
| 19 | high | combat_modifier, stat_modifier | +{number} {rb_symbol} while i'm an attacker. |
| 19 | high | combat_modifier, keyword_reminder | [tank] |
| 19 | high | combat_modifier, damage_effect | i must be assigned combat damage first. |
| 18 | high | trigger_modifier, cost_modifier | you may pay the additional cost to repeat this spell's effect. |
| 16 | high | combat_modifier, stat_modifier | +{number} {rb_symbol} while i'm a defender. |
| 14 | high | trigger_modifier, keyword_reminder | [repeat] {rb_symbol} |
| 13 | high | duration_modifier, combat_modifier, damage_effect | it doesn't deal combat damage this turn. |

### zones

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 42 | high | deck_manipulation | draw {number}. |
| 20 | high | movement_modifier | i can move from battlefield to battlefield. |
| 15 | high | movement_modifier, keyword_reminder | [ganking] |
| 13 | high | location_restriction, damage_effect | deal {number} to a unit at a battlefield. |
| 13 | high | deck_manipulation | you may recycle it. |
| 12 | high | play_permission, location_restriction | you may play me as a [reaction] to a battlefield where you have units. |
| 9 | high | movement_modifier | this isn't a move. |
| 9 | high | contextual_clarification, cost_modifier, attachment_modifier | when you play me, you may [equip] one of your equipment to me for {rb_symbol} less, even if it's already attached. |
| 7 | high | deck_manipulation | recycle the rest. |
| 7 | high | movement_modifier | send it to base. |
| 6 | high | deck_manipulation | when you play me, look at the top card of your main deck. |
| 5 | high | deck_manipulation | draw it. |

### targets

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 27 | high | keyword_reminder, attachment_modifier | [equip] {rb_symbol} |
| 27 | high | attachment_modifier | {rb_symbol}: attach this to a unit you control. |
| 20 | high | movement_modifier | i can move from battlefield to battlefield. |
| 20 | high | target_selection, cost_modifier | opponents must pay {rb_symbol} to choose me with a spell or ability. |
| 15 | high | movement_modifier, keyword_reminder | [ganking] |
| 13 | high | location_restriction, damage_effect | deal {number} to a unit at a battlefield. |
| 12 | high | play_permission, location_restriction | you may play me as a [reaction] to a battlefield where you have units. |
| 9 | high | movement_modifier | this isn't a move. |
| 9 | high | contextual_clarification, cost_modifier, attachment_modifier | when you play me, you may [equip] one of your equipment to me for {rb_symbol} less, even if it's already attached. |
| 7 | high | movement_modifier | send it to base. |
| 5 | high | keyword_reminder, attachment_modifier | [equip] {rb_symbol}{rb_symbol} |
| 5 | high | movement_modifier, replacement_effect | recall it instead. |

### keywords

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 76 | high | timing_window, keyword_reminder | [action] |
| 70 | high | timing_window, keyword_reminder | [reaction] |
| 33 | high | hide_modifier | hide now for {rb_symbol} to react with later for {rb_symbol}. |
| 32 | high | hide_modifier, keyword_reminder | [hidden] |
| 27 | high | keyword_reminder, attachment_modifier | [equip] {rb_symbol} |
| 19 | high | combat_modifier, keyword_reminder | [tank] |
| 15 | high | resource_add_ability, keyword_reminder | [add] {rb_symbol}. |
| 15 | high | movement_modifier, keyword_reminder | [ganking] |
| 14 | high | trigger_modifier, keyword_reminder | [repeat] {rb_symbol} |
| 10 | high | combat_modifier, keyword_reminder | [assault {number}] |
| 9 | high | combat_modifier, keyword_reminder | [shield] |
| 8 | high | combat_modifier, keyword_reminder | [assault] |

### combat_patterns

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 19 | high | combat_modifier, stat_modifier | +{number} {rb_symbol} while i'm an attacker. |
| 19 | high | combat_modifier, keyword_reminder | [tank] |
| 19 | high | combat_modifier, damage_effect | i must be assigned combat damage first. |
| 16 | high | combat_modifier, stat_modifier | +{number} {rb_symbol} while i'm a defender. |
| 13 | high | duration_modifier, combat_modifier, damage_effect | it doesn't deal combat damage this turn. |
| 13 | high | location_restriction, damage_effect | deal {number} to a unit at a battlefield. |
| 13 | high | combat_modifier, resource_generation, xp_progression | when i conquer or hold, gain {number} xp. |
| 12 | high | damage_effect | deal {number} to a unit. |
| 10 | high | buff_effect, stat_modifier | if it doesn't have a buff, it gets a +{number} {rb_symbol} buff. |
| 10 | high | combat_modifier, keyword_reminder | [assault {number}] |
| 9 | high | duration_modifier, stat_modifier | give a unit +{number} {rb_symbol} this turn. |
| 9 | high | combat_modifier, keyword_reminder | [shield] |

### symbols

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 36 | high | symbol_option, cost_modifier | {rb_symbol} |
| 24 | high | ready_exhaust_effect, entry_state, cost_modifier | you may pay {rb_symbol}{rb_symbol} as an additional cost to have me enter ready. |
| 20 | high | resource_add_ability | abilities that add resources can't be reacted to. |
| 20 | high | target_selection, cost_modifier | opponents must pay {rb_symbol} to choose me with a spell or ability. |
| 18 | high | trigger_modifier, cost_modifier | you may pay the additional cost to repeat this spell's effect. |
| 15 | high | resource_add_ability, keyword_reminder | [add] {rb_symbol}. |
| 13 | high | combat_modifier, resource_generation, xp_progression | when i conquer or hold, gain {number} xp. |
| 12 | high | cost_modifier | {rb_symbol}, {rb_symbol} |
| 9 | high | contextual_clarification, cost_modifier, attachment_modifier | when you play me, you may [equip] one of your equipment to me for {rb_symbol} less, even if it's already attached. |
| 6 | high | ready_exhaust_effect, resource_generation | channel {number} rune exhausted. |
| 6 | high | cost_modifier, stat_modifier | you must still pay its power cost. |
| 6 | high | ready_exhaust_effect, entry_state | i enter ready. |

### trigger_event_patterns

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 76 | high | timing_window, keyword_reminder | [action] |
| 73 | high | timing_window | play on your turn or in showdowns. |
| 70 | high | timing_window, keyword_reminder | [reaction] |
| 53 | high | timing_window | play any time, even before spells and abilities resolve. |
| 20 | high | trigger_modifier, removal_or_healing | when i die, get the effect. |
| 18 | high | trigger_modifier, cost_modifier | you may pay the additional cost to repeat this spell's effect. |
| 14 | high | trigger_modifier, keyword_reminder | [repeat] {rb_symbol} |
| 13 | high | trigger_modifier, xp_progression | while you have {number}+ xp, get the effect. |
| 8 | high | duration_modifier, trigger_modifier | get the effect if you've played another card this turn. |
| 8 | high | timing_window, removal_or_healing | kill it at the start of its controller's beginning phase, before scoring. |
| 4 | high | trigger_modifier, keyword_reminder | [repeat] {rb_symbol}{rb_symbol} |
| 4 | high | location_restriction, removal_or_healing | kill a unit at a battlefield. |

### cost_patterns

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 36 | high | symbol_option, cost_modifier | {rb_symbol} |
| 24 | high | ready_exhaust_effect, entry_state, cost_modifier | you may pay {rb_symbol}{rb_symbol} as an additional cost to have me enter ready. |
| 20 | high | target_selection, cost_modifier | opponents must pay {rb_symbol} to choose me with a spell or ability. |
| 18 | high | trigger_modifier, cost_modifier | you may pay the additional cost to repeat this spell's effect. |
| 12 | high | cost_modifier | {rb_symbol}, {rb_symbol} |
| 9 | high | contextual_clarification, cost_modifier, attachment_modifier | when you play me, you may [equip] one of your equipment to me for {rb_symbol} less, even if it's already attached. |
| 6 | high | ready_exhaust_effect, resource_generation | channel {number} rune exhausted. |
| 6 | high | cost_modifier, stat_modifier | you must still pay its power cost. |
| 6 | high | ready_exhaust_effect, entry_state | i enter ready. |
| 5 | high | cost_modifier | you may pay {rb_symbol} as an additional cost to play me. |
| 4 | high | cost_modifier, attachment_modifier | pay the cost: attach this to a unit you control. |
| 4 | high | ready_exhaust_effect, token_creation | play a gold gear token exhausted. |

### duration_patterns

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 19 | high | combat_modifier, stat_modifier | +{number} {rb_symbol} while i'm an attacker. |
| 16 | high | combat_modifier, stat_modifier | +{number} {rb_symbol} while i'm a defender. |
| 13 | high | duration_modifier, combat_modifier, damage_effect | it doesn't deal combat damage this turn. |
| 10 | high | buff_effect, stat_modifier | if it doesn't have a buff, it gets a +{number} {rb_symbol} buff. |
| 9 | high | duration_modifier, stat_modifier | give a unit +{number} {rb_symbol} this turn. |
| 8 | high | duration_modifier, trigger_modifier | get the effect if you've played another card this turn. |
| 7 | high | buff_effect, stat_modifier | if i don't have a buff, i get a +{number} {rb_symbol} buff. |
| 6 | high | cost_modifier, stat_modifier | you must still pay its power cost. |
| 5 | high | duration_modifier, stat_modifier | give me +{number} {rb_symbol} this turn. |
| 5 | high | movement_modifier, replacement_effect | recall it instead. |
| 4 | high | combat_modifier, stat_modifier | +{number} {rb_symbol} while it's an attacker. |
| 4 | high | stun_effect, duration_modifier, combat_modifier, damage_effect | a stunned unit doesn't deal combat damage this turn. |

### trait_patterns

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 24 | high | ready_exhaust_effect, entry_state, cost_modifier | you may pay {rb_symbol}{rb_symbol} as an additional cost to have me enter ready. |
| 6 | high | ready_exhaust_effect, resource_generation | channel {number} rune exhausted. |
| 6 | high | ready_exhaust_effect, entry_state | i enter ready. |
| 4 | high | keyword_modifier | give it [temporary]. |
| 4 | high | ready_exhaust_effect, token_creation | play a gold gear token exhausted. |
| 4 | high | keyword_modifier | this has [reaction]. |
| 3 | high | duration_modifier, keyword_modifier, combat_modifier | give a unit [assault {number}] this turn. |
| 3 | high | resource_add_ability, keyword_modifier, removal_or_healing | it has "[reaction][>] kill this, {rb_symbol}: [add] {rb_symbol}." |
| 3 | high | ready_exhaust_effect | ready me. |
| 3 | high | ready_exhaust_effect | ready a unit. |
| 3 | high | ready_exhaust_effect, entry_state | this enters exhausted. |
| 2 | high | ready_exhaust_effect, token_creation | play a ready {number} {rb_symbol} sprite unit token with [temporary]. |

### deck_patterns

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 42 | high | deck_manipulation | draw {number}. |
| 13 | high | deck_manipulation | you may recycle it. |
| 7 | high | deck_manipulation | recycle the rest. |
| 6 | high | deck_manipulation | when you play me, look at the top card of your main deck. |
| 5 | high | deck_manipulation | draw it. |
| 5 | high | deck_manipulation | look at the top {number} cards of your main deck. |
| 5 | high | deck_manipulation | they reveal their hand. |
| 4 | high | keyword_reminder, deck_manipulation | [quick-draw] |
| 3 | high | deck_manipulation | discard {number} |
| 3 | high | deck_manipulation | draw {number} |
| 3 | high | deck_manipulation | then recycle the rest. |
| 3 | high | deck_manipulation | when you play me, discard {number} |

### movement_patterns

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 20 | high | movement_modifier | i can move from battlefield to battlefield. |
| 15 | high | movement_modifier, keyword_reminder | [ganking] |
| 9 | high | movement_modifier | this isn't a move. |
| 7 | high | movement_modifier | send it to base. |
| 5 | high | movement_modifier, replacement_effect | recall it instead. |
| 4 | high | movement_modifier | recall it. |
| 4 | high | movement_modifier | move an enemy unit. |
| 3 | high | movement_modifier | it can move from battlefield to battlefield. |
| 3 | high | movement_modifier | we can move from battlefield to battlefield. |
| 2 | high | movement_modifier | move a friendly unit |
| 2 | high | movement_modifier | move me to its location and it to my original location. |
| 1 | high | keyword_modifier, movement_modifier, stat_modifier, keyword_reminder, xp_progression | [level {number}][>] i have +{number} {rb_symbol} and [ganking]. |

### trigger_modifier_patterns

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 20 | high | trigger_modifier, removal_or_healing | when i die, get the effect. |
| 18 | high | trigger_modifier, cost_modifier | you may pay the additional cost to repeat this spell's effect. |
| 14 | high | trigger_modifier, keyword_reminder | [repeat] {rb_symbol} |
| 13 | high | trigger_modifier, xp_progression | while you have {number}+ xp, get the effect. |
| 8 | high | duration_modifier, trigger_modifier | get the effect if you've played another card this turn. |
| 8 | high | timing_window, removal_or_healing | kill it at the start of its controller's beginning phase, before scoring. |
| 4 | high | trigger_modifier, keyword_reminder | [repeat] {rb_symbol}{rb_symbol} |
| 4 | high | location_restriction, removal_or_healing | kill a unit at a battlefield. |
| 3 | high | resource_add_ability, keyword_modifier, removal_or_healing | it has "[reaction][>] kill this, {rb_symbol}: [add] {rb_symbol}." |
| 3 | high | trigger_modifier, cost_modifier | you may pay the additional cost to repeat the spell's effect. |
| 3 | high | timing_window, removal_or_healing | kill this at the start of its controller's beginning phase, before scoring. |
| 2 | high | trigger_modifier, keyword_reminder | [repeat] |

### card_types

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 20 | high | target_selection, cost_modifier | opponents must pay {rb_symbol} to choose me with a spell or ability. |
| 4 | high | ready_exhaust_effect, token_creation | play a gold gear token exhausted. |
| 3 | high | target_selection, cost_modifier | opponents must pay {rb_symbol} to choose a [deflect] unit with a spell or ability. |
| 3 | high | target_selection, cost_modifier | opponents must pay {rb_symbol}{rb_symbol} to choose me with a spell or ability. |
| 2 | high | target_selection, location_restriction | choose an enemy unit at a battlefield. |
| 2 | high | target_selection, cost_modifier | opponents must pay {rb_symbol} to choose it with a spell or ability. |
| 2 | high | target_selection, cost_modifier | opponents must pay {rb_symbol} to choose them with a spell or ability. |
| 2 | high | ready_exhaust_effect, token_creation | play a ready {number} {rb_symbol} sprite unit token with [temporary]. |
| 2 | high | tag_reference, trait_identity, location_restriction, token_creation | play a {number} {rb_symbol} mech unit token to your base. |
| 2 | high | token_creation | play a {number} {rb_symbol} sand soldier unit token. |
| 2 | high | ready_exhaust_effect, combat_modifier, token_creation | when i conquer, play a gold gear token exhausted. |
| 2 | high | ready_exhaust_effect, combat_modifier, token_creation | when i hold, play two gold gear tokens exhausted. |

### resource_patterns

| Occ. | Priority | Families | Parameterized unit |
| --- | --- | --- | --- |
| 20 | high | resource_add_ability | abilities that add resources can't be reacted to. |
| 15 | high | resource_add_ability, keyword_reminder | [add] {rb_symbol}. |
| 13 | high | trigger_modifier, xp_progression | while you have {number}+ xp, get the effect. |
| 13 | high | combat_modifier, resource_generation, xp_progression | when i conquer or hold, gain {number} xp. |
| 6 | high | ready_exhaust_effect, resource_generation | channel {number} rune exhausted. |
| 5 | high | resource_generation, xp_progression | gain {number} xp. |
| 4 | high | cost_modifier, xp_progression | spend {number} xp, {rb_symbol} |
| 4 | high | cost_modifier, xp_progression | spend {number} xp |
| 3 | high | resource_add_ability, keyword_modifier, removal_or_healing | it has "[reaction][>] kill this, {rb_symbol}: [add] {rb_symbol}." |
| 2 | high | resource_add_ability, keyword_reminder | [add] {rb_symbol}{rb_symbol}. |
| 2 | high | stat_modifier, keyword_reminder, xp_progression | [level {number}][>] i have +{number} {rb_symbol}. |
| 2 | high | resource_generation, xp_progression | when you play me, gain {number} xp. |

## High Priority Unit Examples

| Occ. | Kind | Roles | Families | Parameterized unit |
| --- | --- | --- | --- | --- |
| 76 | timing | identity_or_descriptor, restriction_or_permission, trigger_observed | timing_window, keyword_reminder | [action] |
| 73 | reminder | restriction_or_permission, trigger_observed | timing_window | play on your turn or in showdowns. |
| 70 | timing | identity_or_descriptor, restriction_or_permission, trigger_observed | timing_window, keyword_reminder | [reaction] |
| 53 | reminder | restriction_or_permission, trigger_observed | timing_window | play any time, even before spells and abilities resolve. |
| 33 | reminder | restriction_or_permission, state_or_modifier | hide_modifier | hide now for {rb_symbol} to react with later for {rb_symbol}. |
| 32 | keyword_marker | identity_or_descriptor, restriction_or_permission, state_or_modifier | hide_modifier, keyword_reminder | [hidden] |
| 32 | effect | event_produced, payoff_output | deck_manipulation | draw {number}. |
| 30 | activation_cost | cost_or_requirement, identity_or_descriptor, restriction_or_permission | symbol_option, cost_modifier | {rb_symbol} |
| 20 | reminder | cost_or_requirement, event_produced, payoff_output | resource_add_ability | abilities that add resources can't be reacted to. |
| 20 | reminder | event_produced, state_or_modifier, targeting_or_scope | movement_modifier | i can move from battlefield to battlefield. |
| 20 | reminder | cost_or_requirement, restriction_or_permission, targeting_or_scope | target_selection, cost_modifier | opponents must pay {rb_symbol} to choose me with a spell or ability. |
| 20 | reminder | event_produced, payoff_output, state_or_modifier, trigger_observed | trigger_modifier, removal_or_healing | when i die, get the effect. |
| 19 | keyword_marker | event_produced, identity_or_descriptor, state_or_modifier, trigger_observed | combat_modifier, keyword_reminder | [tank] |
| 19 | reminder | event_produced, payoff_output, state_or_modifier, trigger_observed | combat_modifier, damage_effect | i must be assigned combat damage first. |
| 18 | reminder | cost_or_requirement, restriction_or_permission, state_or_modifier, trigger_observed | trigger_modifier, cost_modifier | you may pay the additional cost to repeat this spell's effect. |
| 15 | keyword_marker | event_produced, identity_or_descriptor, state_or_modifier, targeting_or_scope | movement_modifier, keyword_reminder | [ganking] |
| 13 | reminder | event_produced, payoff_output, state_or_modifier, trigger_observed | duration_modifier, combat_modifier, damage_effect | it doesn't deal combat damage this turn. |
| 13 | reminder | event_produced, payoff_output | deck_manipulation | you may recycle it. |
| 12 | reminder | event_produced, restriction_or_permission, targeting_or_scope | play_permission, location_restriction | you may play me as a [reaction] to a battlefield where you have units. |
| 11 | effect | identity_or_descriptor, state_or_modifier, trigger_observed | trigger_modifier, keyword_reminder | [repeat] {rb_symbol} |
| 10 | reminder | event_produced, payoff_output, state_or_modifier | buff_effect, stat_modifier | if it doesn't have a buff, it gets a +{number} {rb_symbol} buff. |
| 9 | reminder | event_produced, payoff_output, state_or_modifier, trigger_observed | combat_modifier, stat_modifier | +{number} {rb_symbol} while i'm a defender. |
| 9 | reminder | event_produced, payoff_output, state_or_modifier, trigger_observed | combat_modifier, stat_modifier | +{number} {rb_symbol} while i'm an attacker. |
| 9 | keyword_marker | event_produced, identity_or_descriptor, state_or_modifier, trigger_observed | combat_modifier, keyword_reminder | [shield] |
| 9 | reminder | event_produced, state_or_modifier, targeting_or_scope | movement_modifier | this isn't a move. |
| 9 | reminder | cost_or_requirement, event_produced, restriction_or_permission, state_or_modifier, targeting_or_scope | contextual_clarification, cost_modifier, attachment_modifier | when you play me, you may [equip] one of your equipment to me for {rb_symbol} less, even if it's already attached. |
| 9 | reminder | cost_or_requirement, event_produced, restriction_or_permission, state_or_modifier | ready_exhaust_effect, entry_state, cost_modifier | you may pay {rb_symbol}{rb_symbol} as an additional cost to have me enter ready. |
| 8 | reminder | event_produced, payoff_output, state_or_modifier, trigger_observed | combat_modifier, stat_modifier | +{number} {rb_symbol} while i'm an attacker. |
| 8 | keyword_marker | event_produced, identity_or_descriptor, state_or_modifier, trigger_observed | combat_modifier, keyword_reminder | [assault {number}] |
| 8 | keyword_marker | event_produced, identity_or_descriptor, state_or_modifier, trigger_observed | combat_modifier, keyword_reminder | [assault] |
| 8 | effect | event_produced, payoff_output | deck_manipulation | draw {number}. |
| 8 | reminder | state_or_modifier, trigger_observed | duration_modifier, trigger_modifier | get the effect if you've played another card this turn. |
| 8 | reminder | event_produced, payoff_output, restriction_or_permission, state_or_modifier, trigger_observed | timing_window, removal_or_healing | kill it at the start of its controller's beginning phase, before scoring. |
| 7 | effect | event_produced, payoff_output | damage_effect | deal {number} to a unit. |
| 7 | reminder | event_produced, payoff_output, state_or_modifier | buff_effect, stat_modifier | if i don't have a buff, i get a +{number} {rb_symbol} buff. |
| 7 | effect | event_produced, payoff_output | deck_manipulation | recycle the rest. |
| 7 | reminder | event_produced, state_or_modifier, targeting_or_scope | movement_modifier | send it to base. |
| 7 | reminder | cost_or_requirement, event_produced, payoff_output, state_or_modifier, trigger_observed | combat_modifier, resource_generation, xp_progression | when i conquer or hold, gain {number} xp. |
| 7 | activation_cost | cost_or_requirement, restriction_or_permission | cost_modifier | {rb_symbol}, {rb_symbol} |
| 6 | effect | cost_or_requirement, event_produced, payoff_output, state_or_modifier | ready_exhaust_effect, resource_generation | channel {number} rune exhausted. |
