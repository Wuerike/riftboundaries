# Card Explorer Quality Report

Audit for the sharded card explorer dataset rooted at `data/processed/web/card_explorer_index.json`.

## Summary

- card_count: 767
- fact_count: 6311
- relation_count: 14590
- cards_without_relations: 42
- cards_with_only_broad_relations: 0
- cards_with_uncovered_relational_lines: 0
- broad_relation_count: 4889
- high_signal_relation_count: 9701
- broad_relation_share: 0.3351
- high_degree_threshold_p95: 95
- cards_with_rule_variants: 44

## Snapshot

- date: 2026-05-13
- broad_relation_count_threshold: 500
- high_degree_threshold_p95: 95
- legacy_rule_count_max: 650

## Relation Types

- enables: 2325
- enabled_by: 2325
- similar_effect: 6634
- deck_synergy: 3306

## Degree Distribution

| Scope | Min | P50 | P90 | P95 | P99 | Max | Mean | Zero |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| total | 0 | 28 | 69 | 95 | 400 | 508 | 38.044 | 42 |
| outgoing | 0 | 12 | 34 | 61 | 200 | 254 | 19.022 | 58 |
| incoming | 0 | 13 | 37 | 50 | 200 | 254 | 19.022 | 43 |
| enables | 0 | 0 | 9 | 15 | 199 | 200 | 6.063 | 389 |
| enabled_by | 0 | 0 | 9 | 15 | 199 | 200 | 6.063 | 389 |
| similar_effect | 0 | 14 | 38 | 48 | 94 | 134 | 17.299 | 75 |
| deck_synergy | 0 | 0 | 24 | 40 | 121 | 178 | 8.621 | 444 |

## Diagnostics

- ok: 701
- missing_relation_rule: 24
- front_scoring_issue: 18
- likely_vanilla_or_low_relational_text: 18
- weak_fact: 6

## Broad Relation Reasons

| Reason | Count | Share | Sources |
| --- | --- | --- | --- |
| spell_card_can_be_countered | 3438 | 0.2356 | ["explicit_default", "match_flag", "threshold"] |
| cost:rune:any | 1451 | 0.0995 | ["match_flag", "threshold"] |

## Cards Without Relations By Bucket

- other: 7
- vanilla/no_text: 7
- card_flow: 6
- cost/resource: 5
- stat/buff/damage_modifier: 5
- movement/location: 5
- kill/heal/replacement: 3
- permission/restriction: 2
- damage: 1
- stun: 1

## Top Hubs

| Card | Degree | Broad | High Signal | Broad Share | Diagnostic |
| --- | --- | --- | --- | --- | --- |
| Abandon | 508 | 398 | 110 | 0.7835 | front_scoring_issue |
| Hard Bargain | 432 | 398 | 34 | 0.9213 | front_scoring_issue |
| Flurry of Feathers | 422 | 398 | 24 | 0.9431 | front_scoring_issue |
| Defy | 410 | 398 | 12 | 0.9707 | front_scoring_issue |
| Lilting Lullaby | 410 | 398 | 12 | 0.9707 | front_scoring_issue |
| Riposte | 410 | 398 | 12 | 0.9707 | front_scoring_issue |
| Wind Wall | 410 | 398 | 12 | 0.9707 | front_scoring_issue |
| Not So Fast | 400 | 398 | 2 | 0.995 | front_scoring_issue |
| Repulse | 400 | 398 | 2 | 0.995 | front_scoring_issue |
| Bloodharbor Ripper | 267 | 121 | 146 | 0.4532 | ok |

## Manual Review Samples


### No Relations With Relational Text

| Card | Diagnostic | Bucket | Degree | High Signal | Missing | Weak | Text |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ravenborn Tome | missing_relation_rule | stat/buff/damage_modifier | 0 | 0 | 0 | 0 | :rb_exhaust:: The next spell you play this turn deals 1 Bonus Damage. (Each instance of damage the spell deals is increased by 1.) |
| Volibear, Imposing | missing_relation_rule | movement/location | 0 | 0 | 0 | 0 | [Shield 3] (+3 :rb_might: while I'm a defender.) \| [Tank] (I must be assigned combat damage first.) \| When an opponent moves to a battlefield other than mine, draw 1. (Bases are not battlefield.) |
| Mushroom Pouch | missing_relation_rule | movement/location | 0 | 0 | 0 | 0 | At the start of your Beginning Phase, if you control a facedown card at a battlefield, draw 1. |
| Nine-Tailed Fox | missing_relation_rule | movement/location | 0 | 0 | 0 | 0 | When an enemy unit attacks a battlefield you control, give it -1 :rb_might: this turn, to a minimum of 1 :rb_might:. |
| Windswept Hillock | missing_relation_rule | movement/location | 0 | 0 | 0 | 0 | Units here have [Ganking]. (They can move from battlefield to battlefield.) |
| Ava Achiever | missing_relation_rule | cost/resource | 0 | 0 | 0 | 0 | When I attack, you may pay :rb_rune_mind: to play a card with [Hidden] from your hand, ignoring its cost. If it’s a unit, play it here. |
| Spirit Wheel | missing_relation_rule | cost/resource | 0 | 0 | 0 | 0 | When you choose a friendly unit, you may pay :rb_energy_1: and exhaust this to draw 1. |
| Yordle Explorer | missing_relation_rule | cost/resource | 0 | 0 | 0 | 0 | When you play a card with Power cost :rb_rune_rainbow::rb_rune_rainbow: or more, draw 1. |
| Prodigal Explorer | missing_relation_rule | card_flow | 0 | 0 | 0 | 0 | :rb_exhaust:: [Reaction] — Draw 1. Use only if you've chosen enemy units and/or gear twice this turn with spells or unit abilities. |
| Fresh Beans | missing_relation_rule | card_flow | 0 | 0 | 0 | 0 | When you play a unit during a showdown, you may exhaust this to draw 1. |

### Only Broad Relations

No cards found.

### Uncovered Relational Lines

No cards found.

### Unlinked Relation Candidate Facts

| Card | Diagnostic | Bucket | Degree | High Signal | Missing | Weak | Text |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ava Achiever | missing_relation_rule | cost/resource | 0 | 0 | 0 | 0 | When I attack, you may pay :rb_rune_mind: to play a card with [Hidden] from your hand, ignoring its cost. If it’s a unit, play it here. |
| Jayce, Man of Progress | missing_relation_rule | kill/heal/replacement | 0 | 0 | 0 | 0 | When you play me, you may kill a friendly gear. If you do, you may play a gear with Energy cost no more than :rb_energy_7: from hand this turn, ignoring its Energy cost. (You must still pay its Power cost.) |
| Prodigal Explorer | missing_relation_rule | card_flow | 0 | 0 | 0 | 0 | :rb_exhaust:: [Reaction] — Draw 1. Use only if you've chosen enemy units and/or gear twice this turn with spells or unit abilities. |
| Sivir, Ambitious | missing_relation_rule | damage | 0 | 0 | 0 | 0 | [Deflect 2] (Opponents must pay :rb_rune_rainbow::rb_rune_rainbow: to choose me with a spell or Ability.) \| When I conquer after an attack, if you assigned 5 or more excess damage to enemy units, you may deal that much to an enemy unit. |
| Volibear, Imposing | missing_relation_rule | movement/location | 0 | 0 | 0 | 0 | [Shield 3] (+3 :rb_might: while I'm a defender.) \| [Tank] (I must be assigned combat damage first.) \| When an opponent moves to a battlefield other than mine, draw 1. (Bases are not battlefield.) |
| Fresh Beans | missing_relation_rule | card_flow | 0 | 0 | 0 | 0 | When you play a unit during a showdown, you may exhaust this to draw 1. |
| Grove of the God-Willow | missing_relation_rule | card_flow | 0 | 0 | 0 | 0 | When you hold here, draw 1. |
| Hallowed Tomb | missing_relation_rule | other | 0 | 0 | 0 | 0 | When you hold here, you may return your Chosen Champion from your trash to your Champion Zone if it is empty. |
| Ravenborn Tome | missing_relation_rule | stat/buff/damage_modifier | 0 | 0 | 0 | 0 | :rb_exhaust:: The next spell you play this turn deals 1 Bonus Damage. (Each instance of damage the spell deals is increased by 1.) |
| Sun Disc | missing_relation_rule | other | 0 | 0 | 0 | 0 | :rb_exhaust:: [Legion] — The next unit you play this turn enters ready. (Get the effect if you've played another card this turn.) |

## Facts Not Becoming Relations

- relation_candidate_fact_count: 2064
- unlinked_relation_candidate_fact_count: 501
- actionable_unlinked_relation_candidate_fact_count: 232
- needs_relation_rule_fact_count: 220

### Classification Counts

- intentional_ignored: 269
- needs_relation_rule: 220
- weak_fact: 11
- needs_extraction_fix: 1

### Classification Matrix By Family

- observe_event: intentional_ignored=137, needs_relation_rule=2
- reference_keyword: needs_relation_rule=107
- cost/resource: intentional_ignored=49, needs_relation_rule=17
- card_flow: intentional_ignored=45, needs_relation_rule=7, weak_fact=2
- require: intentional_ignored=36, needs_extraction_fix=1
- stat/buff/damage_modifier: needs_relation_rule=32
- movement/location: needs_relation_rule=17
- ready: needs_relation_rule=17
- repeat_effect: weak_fact=8
- kill/heal/replacement: needs_relation_rule=7
- banish: needs_relation_rule=3
- channel: needs_relation_rule=3
- damage: needs_relation_rule=3
- exhaust: intentional_ignored=2, needs_relation_rule=1
- attachment/copy: needs_relation_rule=1
- choose: needs_relation_rule=1
- control_change: needs_relation_rule=1
- enter_ready: needs_relation_rule=1
- score: weak_fact=1

### Example Facts By Family

- card_flow:
  - intentional_ignored: Angle Shot [draw] Draw 1; Back Off [draw] draw 1; Catalyst of Aeons [draw] draw 1
  - needs_relation_rule: Buhru Captain [draw] draw 1; Dusk Rose Lab [draw] draw 1; Fresh Beans [draw] draw 1
  - weak_fact: Teemo, Strategist [reveal] reveal the top 5 cards of your Main Deck; Void Rush [reveal] Reveal the top 2 cards of your Main Deck
- cost/resource:
  - intentional_ignored: Allay, Eager Admirer [pay] [Deflect] (Opponents must pay :rb_rune_rainbow:; Ancient Henge [pay] :rb_exhaust:; Arena Bar [pay] :rb_exhaust:
  - needs_relation_rule: Defy [cost_cap_constraint] costs no more than :rb_energy_4: and; Fate Weaver [cost_threshold] cost :rb_energy_4: or more; Forge of the Future [pay] Kill this
- observe_event:
  - intentional_ignored: Ahri, Alluring [observe_event] When I hold; Ahri, Inquisitive [observe_event] When I attack or defend; Ahri, Inquisitive [observe_event] When I attack or defend
  - needs_relation_rule: Draven, Vanquisher [observe_event] When I win a combat; Voidreaver [observe_event] When you win a combat
- require:
  - needs_extraction_fix: Ancient Warmonger [require] while I'm an attacker
  - intentional_ignored: Black Rose Dignitary [require] while I'm an attacker; Blue Sentinel [require] while I'm a defender; Chemtech Enforcer [require] while I'm an attacker
- kill/heal/replacement:
  - needs_relation_rule: Altar of Blood [prevent] If a unit here would die during combat, its controller may pay :rb_rune_rainbow::rb_rune_rainbow::rb_rune_rainbow: to heal it, exhaust it, and recall it instead; Atakhan [kill] You may kill a friendly unit as an additional cost to play me; Guardian Angel [prevent] If I would die, kill Guardian Angel instead. Heal me, exhaust me, and recall me
- movement/location:
  - needs_relation_rule: Aspiring Engineer [play] play me, return a gear from your trash to your hand; Ava Achiever [play] play a card with [Hidden] from your hand, ignoring its cost; Boots of Swiftness [move] I can move from battlefield to battlefield
- ready:
  - needs_relation_rule: Arise! [ready] Ready up to two of them; Battle Mistress [ready] ready me; Blade Dancer [ready] ready me
- reference_keyword:
  - needs_relation_rule: Ancient Henge [reference_keyword] [Reaction]; Armed Assailant [reference_keyword] [Equip]; Ava Achiever [reference_keyword] [Hidden]
- repeat_effect:
  - weak_fact: Bellows Breath [repeat_effect] repeat this spell's effect; Called Shot [repeat_effect] repeat this spell's effect; Danger Zone [repeat_effect] repeat this spell's effect
- stat/buff/damage_modifier:
  - needs_relation_rule: Abandoned Hall [modify_stat] give a unit they control here +1 :rb_might: this turn; Breakneck Mech [gain_keyword] Your Mechs have [Deflect] and [Ganking].; Captain Farron [gain_keyword] Other friendly units here have [Assault].
- banish:
  - needs_relation_rule: Cursed Sarcophagus [banish] banish all units from your trash; Promising Future [banish] banishes one of them; The Zero Drive [banish] Banish this: Play all units banished with this
- channel:
  - needs_relation_rule: Boneshiver [channel] channel 1 rune exhausted; Virtuoso [channel] channel 4 runes; Virtuoso [channel] channel 4 runes

### Vanilla / Intentionally Isolated Allowlist

- play:mountain-drake:24c1bdea
- play:playful-phantom:de775024
- play:recruit-de:1ce0d3f2
- play:recruit-nx:c7a669c6
- play:recruit-zn:24ea9161
- play:shipyard-skulker:1221f795
- play:vanguard-sergeant:646780d9

### Top Unlinked Predicates

- observe_event: 139
- reference_keyword: 107
- pay: 53
- draw: 51
- require: 37
- ready: 17
- gain_keyword: 16
- modify_stat: 15
- move: 9
- repeat_effect: 8
- play: 6
- reduce_cost: 6
- prevent: 5
- cost_cap_constraint: 4
- exhaust: 3
- damage: 3
- channel: 3
- banish: 3
- kill: 2
- return_to_hand: 2
- spend: 2
- reveal: 2
- enter_ready: 1
- cost_threshold: 1
- lose_control: 1
- discard: 1
- buff: 1
- copy: 1
- choose: 1
- score: 1

### Top Actionable Unlinked Predicates

- reference_keyword: 107
- ready: 17
- gain_keyword: 16
- modify_stat: 15
- move: 9
- repeat_effect: 8
- play: 6
- draw: 6
- reduce_cost: 6
- prevent: 5
- cost_cap_constraint: 4
- pay: 4
- damage: 3
- channel: 3
- banish: 3
- kill: 2
- observe_event: 2
- return_to_hand: 2
- spend: 2
- reveal: 2
- require: 1
- exhaust: 1
- enter_ready: 1
- cost_threshold: 1
- lose_control: 1
- discard: 1
- buff: 1
- copy: 1
- choose: 1
- score: 1

### Top Needs Relation Rule Predicates

- reference_keyword: 107
- ready: 17
- gain_keyword: 16
- modify_stat: 15
- move: 9
- play: 6
- draw: 6
- reduce_cost: 6
- prevent: 5
- cost_cap_constraint: 4
- pay: 4
- damage: 3
- channel: 3
- banish: 3
- kill: 2
- observe_event: 2
- return_to_hand: 2
- spend: 2
- exhaust: 1
- enter_ready: 1
- cost_threshold: 1
- lose_control: 1
- discard: 1
- buff: 1
- copy: 1
- choose: 1

## Backtrace Samples


### Ravenborn Tome

- diagnostic: missing_relation_rule
- bucket: stat/buff/damage_modifier
- relation_count: 0 (high_signal=0, broad=0)
- rules: :rb_exhaust:: The next spell you play this turn deals 1 Bonus Damage. (Each instance of damage the spell deals is increased by 1.)
| Line | Role | Predicate | Events | Outputs | Evidence |
| --- | --- | --- | --- | --- | --- |
| rules_lines:0 | state_or_modifier | modify_stat |  | bonus_damage_added | The next spell you play this turn deals 1 Bonus Damage |
| rules_lines:0 | cost_or_requirement | pay |  |  | :rb_exhaust: |

### Volibear, Imposing

- diagnostic: missing_relation_rule
- bucket: movement/location
- relation_count: 0 (high_signal=0, broad=0)
- rules: [Shield 3] (+3 :rb_might: while I'm a defender.) | [Tank] (I must be assigned combat damage first.) | When an opponent moves to a battlefield other than mine, draw 1. (Bases are not battlefield.)
| Line | Role | Predicate | Events | Outputs | Evidence |
| --- | --- | --- | --- | --- | --- |
| rules_lines:0 | identity_or_descriptor | has_keyword |  |  | [Shield 3] |
| rules_lines:0 | state_or_modifier | modify_stat |  | might_modified | [Shield 3] (+3 :rb_might: while I'm a defender.) |
| rules_lines:0 | restriction_or_permission | require |  |  | while I'm a defender |
| rules_lines:1 | identity_or_descriptor | has_keyword |  |  | [Tank] |
| rules_lines:2 | payoff_output | draw |  | card_drawn | draw 1 |

### Mushroom Pouch

- diagnostic: missing_relation_rule
- bucket: movement/location
- relation_count: 0 (high_signal=0, broad=0)
- rules: At the start of your Beginning Phase, if you control a facedown card at a battlefield, draw 1.
| Line | Role | Predicate | Events | Outputs | Evidence |
| --- | --- | --- | --- | --- | --- |
| rules_lines:0 | payoff_output | draw |  | card_drawn | draw 1 |

### Nine-Tailed Fox

- diagnostic: missing_relation_rule
- bucket: movement/location
- relation_count: 0 (high_signal=0, broad=0)
- rules: When an enemy unit attacks a battlefield you control, give it -1 :rb_might: this turn, to a minimum of 1 :rb_might:.
| Line | Role | Predicate | Events | Outputs | Evidence |
| --- | --- | --- | --- | --- | --- |
| rules_lines:0 | state_or_modifier | modify_stat |  | might_modified | give it -1 :rb_might: this turn |

### Windswept Hillock

- diagnostic: missing_relation_rule
- bucket: movement/location
- relation_count: 0 (high_signal=0, broad=0)
- rules: Units here have [Ganking]. (They can move from battlefield to battlefield.)
| Line | Role | Predicate | Events | Outputs | Evidence |
| --- | --- | --- | --- | --- | --- |
| rules_lines:0 | state_or_modifier | gain_keyword |  | keyword_granted | Units here have [Ganking]. |

### Ava Achiever

- diagnostic: missing_relation_rule
- bucket: cost/resource
- relation_count: 0 (high_signal=0, broad=0)
- rules: When I attack, you may pay :rb_rune_mind: to play a card with [Hidden] from your hand, ignoring its cost. If it’s a unit, play it here.
| Line | Role | Predicate | Events | Outputs | Evidence |
| --- | --- | --- | --- | --- | --- |
| rules_lines:0 | trigger_observed | observe_event | self_attacks |  | When I attack |
| rules_lines:0 | event_produced | play | card_played | card_played | play a card with [Hidden] from your hand, ignoring its cost |
| rules_lines:0 | targeting_or_scope | reference_keyword |  |  | [Hidden] |

### Spirit Wheel

- diagnostic: missing_relation_rule
- bucket: cost/resource
- relation_count: 0 (high_signal=0, broad=0)
- rules: When you choose a friendly unit, you may pay :rb_energy_1: and exhaust this to draw 1.
| Line | Role | Predicate | Events | Outputs | Evidence |
| --- | --- | --- | --- | --- | --- |
| rules_lines:0 | payoff_output | draw |  | card_drawn | draw 1 |

### Yordle Explorer

- diagnostic: missing_relation_rule
- bucket: cost/resource
- relation_count: 0 (high_signal=0, broad=0)
- rules: When you play a card with Power cost :rb_rune_rainbow::rb_rune_rainbow: or more, draw 1.
| Line | Role | Predicate | Events | Outputs | Evidence |
| --- | --- | --- | --- | --- | --- |
| rules_lines:0 | payoff_output | draw |  | card_drawn | draw 1 |

### Prodigal Explorer

- diagnostic: missing_relation_rule
- bucket: card_flow
- relation_count: 0 (high_signal=0, broad=0)
- rules: :rb_exhaust:: [Reaction] — Draw 1. Use only if you've chosen enemy units and/or gear twice this turn with spells or unit abilities.
| Line | Role | Predicate | Events | Outputs | Evidence |
| --- | --- | --- | --- | --- | --- |
| rules_lines:0 | payoff_output | draw |  | card_drawn | Draw 1 |
| rules_lines:0 | targeting_or_scope | reference_keyword |  |  | [Reaction] |
| rules_lines:0 | cost_or_requirement | pay |  |  | :rb_exhaust: |

### Fresh Beans

- diagnostic: missing_relation_rule
- bucket: card_flow
- relation_count: 0 (high_signal=0, broad=0)
- rules: When you play a unit during a showdown, you may exhaust this to draw 1.
| Line | Role | Predicate | Events | Outputs | Evidence |
| --- | --- | --- | --- | --- | --- |
| rules_lines:0 | trigger_observed | observe_event | unit_played |  | When you play a unit |
| rules_lines:0 | payoff_output | draw |  | card_drawn | draw 1 |
