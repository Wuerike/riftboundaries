# Derived Semantic Index

## Use Policy

[derived-fact] This file is derived from official text. Use it for discovery and recall. Verify rules-sensitive answers against official card text and official rules.

## By Card

### [derived-fact] Abandon

- official_card: Abandon (`play:abandon:03e0b30c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `counter`; role `event_produced`; type `produced_event`; confidence 0.9; evidence: Counter a spell
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: You may recycle it
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: Return it to its owner's hand
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: Look at the top card of your Main Deck
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Predict]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos

### [derived-fact] Abandoned Hall

- official_card: Abandoned Hall (`play:abandoned-hall:d998c7f9`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When a player plays a spell
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give a unit they control here +1 :rb_might: this turn
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Acceptable Losses

- official_card: Acceptable Losses (`play:acceptable-losses:23e05503`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.86; evidence: Each player kills one of their gear
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Adaptatron

- official_card: Adaptatron (`play:adaptatron:64a9b2dd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: kill a gear
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff me
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mech
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Against the Odds

- official_card: Against the Odds (`play:against-the-odds:2a7b8a95`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a friendly unit at a battlefield +2 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Ahri, Alluring

- official_card: Ahri, Alluring (`play:ahri-alluring:9a14bc5e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I hold
- predicate `score`; role `payoff_output`; type `score_change`; confidence 0.8; evidence: score 1 point
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ahri
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Ahri, Inquisitive

- official_card: Ahri, Inquisitive (`play:ahri-inquisitive:d6396fae`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack or defend
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack or defend
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give an enemy unit here -2 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ahri
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3

### [derived-fact] Akshan, Mischievous

- official_card: Akshan, Mischievous (`play:akshan-mischievous:eb3bd896`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.9; evidence: You may pay :rb_rune_body::rb_rune_body: as an additional cost to play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: You may pay :rb_rune_body::rb_rune_body:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: attach it to me
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move an enemy gear to your base
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Weaponmaster]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body

### [derived-fact] Albus Ferros

- official_card: Albus Ferros (`play:albus-ferros:f4ea97a5`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff spent
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channel 1 rune exhausted
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Piltover

### [derived-fact] Allay, Eager Admirer

- official_card: Allay, Eager Admirer (`play:allay-eager-admirer:93df3922`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: While I'm at a battlefield, your other units here have [Deflect].
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Alpha Strike

- official_card: Alpha Strike (`play:alpha-strike:c82e3bcd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: Gain 1 XP
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Master Yi

### [derived-fact] Alpha Wildclaw

- official_card: Alpha Wildclaw (`play:alpha-wildclaw:d90d23e2`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: Your units here with less Might than me can't be chosen by enemy spells and abilities
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Cat
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:7
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Altar of Blood

- official_card: Altar of Blood (`play:altar-of-blood:da048a2d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: its controller may pay :rb_rune_rainbow::rb_rune_rainbow::rb_rune_rainbow: to heal it, exhaust it, and recall it instead
- predicate `prevent`; role `restriction_or_permission`; type `replacement_effect`; confidence 0.86; evidence: If a unit here would die during combat, its controller may pay :rb_rune_rainbow::rb_rune_rainbow::rb_rune_rainbow: to heal it, exhaust it, and recall it instead
- predicate `return_to_hand`; role `event_produced`; type `movement`; confidence 0.82; evidence: recall it instead
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Altar of Memories

- official_card: Altar of Memories (`play:altar-of-memories:2de88f83`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When a friendly unit dies
- predicate `exhaust`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.9; evidence: you may exhaust me
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `move`; role `payoff_output`; type `card_flow`; confidence 0.9; evidence: put a card from your hand on the top or bottom of your Main Deck
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Altar to Unity

- official_card: Altar to Unity (`play:altar-to-unity:410e54c7`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you hold here
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a 1 :rb_might: Recruit unit token in your base
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Amateur Recital

- official_card: Amateur Recital (`play:amateur-recital:8ba4ec50`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you hold here
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move a unit at a battlefield to its base
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Ancient Henge

- official_card: Ancient Henge (`play:ancient-henge:9117108a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Pay any amount of Energy to [Add] that much :rb_rune_rainbow:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] that much :rb_rune_rainbow:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Ancient Warmonger

- official_card: Ancient Warmonger (`play:ancient-warmonger:db8f6060`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_chaos:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Spirit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4

### [derived-fact] Angle Shot

- official_card: Angle Shot (`play:angle-shot:f8a4b638`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach that Equipment to that unit or
- predicate `detach`; role `event_produced`; type `produced_event`; confidence 0.82; evidence: detach that Equipment from that unit
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Angler Beast

- official_card: Angler Beast (`play:angler-beast:7a0d871f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: return all units with 2 :rb_might: or less to their owners' hands
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bilgewater

### [derived-fact] Anivia, Primal

- official_card: Anivia, Primal (`play:anivia-primal:6dbf1f76`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: deal 3 to all enemy units here
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bird
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Anivia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:8
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2

### [derived-fact] Annie, Fiery

- official_card: Annie, Fiery (`play:annie-fiery:a0afde4e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.88; evidence: Your spells and abilities deal 1 Bonus Damage
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Annie
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Annie, Stubborn

- official_card: Annie, Stubborn (`play:annie-stubborn:329d7cbc`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: play me, return a spell from your trash to your hand
- predicate `return_to_hand`; role `payoff_output`; type `card_flow`; confidence 0.82; evidence: return a spell from your trash to your hand
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Annie
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3

### [derived-fact] Aphelios, Exalted

- official_card: Aphelios, Exalted (`play:aphelios-exalted:b81e7f1f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you attach an Equipment to me
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: Buff a friendly unit
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: Channel 1 rune exhausted
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: Ready 2 runes
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Apprentice Smith

- official_card: Apprentice Smith (`play:apprentice-smith:170592f1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: recycle it
- predicate `reveal`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: reveal the top card of your Main Deck
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Freljord

### [derived-fact] Arachnoid Horror

- official_card: Arachnoid Horror (`play:arachnoid-horror:a077432b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `play`; role `restriction_or_permission`; type `permission`; confidence 0.82; evidence: I can be played to an occupied battlefield if an enemy unit is alone there
- predicate `play`; role `restriction_or_permission`; type `permission`; confidence 0.82; evidence: Friendly units can be played to an occupied battlefield if an enemy unit is alone there
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 2 XP
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hunt 2]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Arcane Shift

- official_card: Arcane Shift (`play:arcane-shift:448c90d0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 3 to an enemy unit at a battlefield
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: Banish this
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: Banish a friendly unit
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ezreal

### [derived-fact] Arena Bar

- official_card: Arena Bar (`play:arena-bar:3d632d6f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: Buff an exhausted friendly unit
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Arena Kingpin

- official_card: Arena Kingpin (`play:arena-kingpin:da01230d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit +3 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3

### [derived-fact] Arise!

- official_card: Arise! (`play:arise:e94046d9`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play a 2 :rb_might: Sand Soldier unit token
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: Ready up to two of them
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Azir
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Armed Assailant

- official_card: Armed Assailant (`play:armed-assailant:32d279bc`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_fury:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Equip]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Weaponmaster]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Ashe, Focused

- official_card: Ashe, Focused (`play:ashe-focused:8777394f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: banish it
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ashe
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Aspirant's Climb

- official_card: Aspirant's Climb (`play:aspirant-s-climb:341d79a2`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `score`; role `payoff_output`; type `score_change`; confidence 0.8; evidence: points needed to win the game by 1
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Aspiring Engineer

- official_card: Aspiring Engineer (`play:aspiring-engineer:bdb22107`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: play me, return a gear from your trash to your hand
- predicate `return_to_hand`; role `payoff_output`; type `card_flow`; confidence 0.82; evidence: return a gear from your trash to your hand
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Assembly Rig

- official_card: Assembly Rig (`play:assembly-rig:17b55441`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_energy_1::rb_rune_fury:, Recycle a unit from your trash, :rb_exhaust:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: Recycle a unit from your trash
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play a 3 :rb_might: Mech unit token to your base
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Atakhan

- official_card: Atakhan (`play:atakhan:a7ae219e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `kill`; role `cost_or_requirement`; type `additional_cost`; confidence 0.9; evidence: You may kill a friendly unit as an additional cost to play me
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: kill a friendly unit
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: kill one of their units
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_1: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_1: less
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ganking]

### [derived-fact] Ava Achiever

- official_card: Ava Achiever (`play:ava-achiever:59c46b4f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: play a card with [Hidden] from your hand, ignoring its cost
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Hidden]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Azir, Ascendant

- official_card: Azir, Ascendant (`play:azir-ascendant:82d12920`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_rune_calm:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: attach one of its Equipment to me
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move me to its location and it to my original location
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move me to its location and it to my original location
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bird

### [derived-fact] Azir, Sovereign

- official_card: Azir, Sovereign (`play:azir-sovereign:1df14401`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_order:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move any number of your token units to this battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bird
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Azir
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order

### [derived-fact] B.F. Sword

- official_card: B.F. Sword (`play:b-f-sword:41b0e711`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_order:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Equipment
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might_bonus:3

### [derived-fact] Back Off

- official_card: Back Off (`play:back-off:2778a448`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun] a unit
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Stun]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell

### [derived-fact] Back to Back

- official_card: Back to Back (`play:back-to-back:48c76121`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give two friendly units each +2 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Back-Alley Bar

- official_card: Back-Alley Bar (`play:back-alley-bar:1048a803`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give it +1 :rb_might: this turn
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Baited Hook

- official_card: Baited Hook (`play:baited-hook:e48e39f6`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_energy_1::rb_rune_order:, :rb_exhaust:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: recycle the rest
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: Kill a friendly unit
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: banish a unit from among them that has Might up to 1 more than the killed unit and play it
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: Look at the top 5 cards of your Main Deck
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Bandle Soldier

- official_card: Bandle Soldier (`play:bandle-soldier:b98a96f1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Level 3]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Bandle Tree

- official_card: Bandle Tree (`play:bandle-tree:1887131e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Bard, Mercurial

- official_card: Bard, Mercurial (`play:bard-mercurial:a8725232`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `exhaust`; role `cost_or_requirement`; type `additional_cost`; confidence 0.9; evidence: You may exhaust your legend as an additional cost to play me
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move any number of your units to an open battlefield
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bard
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Baron Nashor

- official_card: Baron Nashor (`play:baron-nashor:e67f7c30`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: Units can move here from anywhere
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: I can't be chosen by enemy spells and abilities
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: Other friendly units have +2 :rb_might:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:12
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: The Void

### [derived-fact] Baron Pit

- official_card: Baron Pit (`play:baron-pit:245edbb0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: Units can move here from anywhere
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Bashful Bloom

- official_card: Bashful Bloom (`play:bashful-bloom:a2a8b0d1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_energy_4:, :rb_exhaust:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play a ready 3 :rb_might: Sprite unit token with [Temporary]
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready 3 :rb_might: Sprite unit token with [Temporary]
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: This ability costs :rb_energy_1: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: This ability costs :rb_energy_1: less
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Temporary]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind

### [derived-fact] Battering Ram

- official_card: Battering Ram (`play:battering-ram:58f6f5bb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_1: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_1: less
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Trifarian

### [derived-fact] Battle Mistress

- official_card: Battle Mistress (`play:battle-mistress:72ac42f9`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you recycle a rune
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When one or more enemy units die
- predicate `exhaust`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.9; evidence: you may exhaust me
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a Gold gear token exhausted
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Sivir

### [derived-fact] Beast Below

- official_card: Beast Below (`play:beast-below:dc189fe5`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: return another friendly unit and an enemy unit to their owners' hands
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:8
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:7
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bilgewater

### [derived-fact] Bellows Breath

- official_card: Bellows Breath (`play:bellows-breath:59c3877f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_1::rb_rune_mind:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 1 to up to three units at the same location
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Bewitching Spirit

- official_card: Bewitching Spirit (`play:bewitching-spirit:07ca781e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: discard 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Spirit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shadow Isles

### [derived-fact] Bilgewater Bully

- official_card: Bilgewater Bully (`play:bilgewater-bully:8232ec7d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.84; evidence: While I'm buffed
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: While I'm buffed, I have [Ganking].
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bilgewater

### [derived-fact] Bird

- official_card: Bird (`play:bird:2d7d5f76`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bird
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless

### [derived-fact] Black Flame Altar

- official_card: Black Flame Altar (`play:black-flame-altar:32878e11`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Units here with [Temporary] have [Shield].
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Temporary]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Black Market Broker

- official_card: Black Market Broker (`play:black-market-broker:b85b2972`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a Gold gear token exhausted
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Black Rose Dignitary

- official_card: Black Rose Dignitary (`play:black-rose-dignitary:0e88417b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: Channel 1 rune exhausted
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault] (+1 :rb_might: while I'm an attacker.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order

### [derived-fact] Blade Dancer

- official_card: Blade Dancer (`play:blade-dancer:5986d065`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready it
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Irelia

### [derived-fact] Blade of the Ruined King

- official_card: Blade of the Ruined King (`play:blade-of-the-ruined-king:e4918c65`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] — :rb_rune_order:, Kill a friendly unit (Pay the cost
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: Kill a friendly unit
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Blast Cone

- official_card: Blast Cone (`play:blast-cone:55eeaf2f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play this
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you move an enemy unit
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move an enemy unit
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun] it
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Stun]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Blast Corps Cadet

- official_card: Blast Corps Cadet (`play:blast-corps-cadet:72d54e42`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.9; evidence: You may pay :rb_energy_1::rb_rune_fury: as an additional cost to play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: You may pay :rb_energy_1::rb_rune_fury:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: deal 2 to a unit at a battlefield
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Blast of Power

- official_card: Blast of Power (`play:blast-of-power:e64fc986`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.84; evidence: Kill a unit at a battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Blastcone Fae

- official_card: Blastcone Fae (`play:blastcone-fae:b3a25b27`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give a unit -2 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fae
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2

### [derived-fact] Blazing Scorcher

- official_card: Blazing Scorcher (`play:blazing-scorcher:5785a546`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_fury:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dragon
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Blighted Battleaxe

- official_card: Blighted Battleaxe (`play:blighted-battleaxe:a1e0de3c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_energy_1::rb_rune_fury:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: deal 4 to me
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Equipment

### [derived-fact] Blind Fury

- official_card: Blind Fury (`play:blind-fury:49808b2f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: recycle the rest
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: banish it
- predicate `reveal`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: reveals the top card of their Main Deck
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Blind Monk

- official_card: Blind Monk (`play:blind-monk:b2a14180`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_energy_1:, :rb_exhaust:
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: Buff a friendly unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Lee Sin

### [derived-fact] Blitzcrank, Impassive

- official_card: Blitzcrank, Impassive (`play:blitzcrank-impassive:19f338cd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I hold
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move an enemy unit to here
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: return me to my owner's hand
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mech

### [derived-fact] Block

- official_card: Block (`play:block:5af86e4a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while it's a defender
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: Give a unit [Shield 3] and [Tank] this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Blood Money

- official_card: Blood Money (`play:blood-money:744e0044`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.84; evidence: Kill a unit at a battlefield
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a Gold gear token exhausted
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play two Gold gear tokens exhausted
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Blood Rose

- official_card: Blood Rose (`play:blood-rose:91bf769b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play a unit
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Spend 3 XP, :rb_exhaust:
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 1 XP
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: Ready a unit
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Blood Rush

- official_card: Blood Rush (`play:blood-rush:6133a3d6`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_1:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while it's an attacker
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: Give a unit [Assault 2] this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell

### [derived-fact] Bloodharbor Ripper

- official_card: Bloodharbor Ripper (`play:bloodharbor-ripper:a9ea31a4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_energy_1:, :rb_exhaust:
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.88; evidence: Kill this
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_rune_rainbow:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play a Gold gear token exhausted
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: Return a friendly unit at a battlefield to its owner's hand
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Pyke
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos

### [derived-fact] Blue Sentinel

- official_card: Blue Sentinel (`play:blue-sentinel:1175ef0a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I hold
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm a defender
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_rune_rainbow:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Shield 2] (+2 :rb_might: while I'm a defender.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Shield 2]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4

### [derived-fact] Body Rune

- official_card: Body Rune (`play:body-rune:348edc32`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 1.0; evidence: basic_rune:body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: rune
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body

### [derived-fact] Bonds of Strength

- official_card: Bonds of Strength (`play:bonds-of-strength:d1ad2e5c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_2:
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give two friendly units each +1 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Bone Skewer

- official_card: Bone Skewer (`play:bone-skewer:34218ae3`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun] it
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun] it
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Stun]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Boneshiver

- official_card: Boneshiver (`play:boneshiver:b19621f8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_energy_1::rb_rune_body:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channel 1 rune exhausted
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Boots of Swiftness

- official_card: Boots of Swiftness (`play:boots-of-swiftness:aa5f3403`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_chaos:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ganking]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Bounty Hunter

- official_card: Bounty Hunter (`play:bounty-hunter:525b5606`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: Give a unit [Ganking] this turn
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Miss Fortune

### [derived-fact] Brazen Buccaneer

- official_card: Brazen Buccaneer (`play:brazen-buccaneer:02a9fc0c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: discard 1
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.78; evidence: reduce my cost by :rb_energy_2:
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.78; evidence: reduce my cost by :rb_energy_2:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Pirate
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Breakneck Mech

- official_card: Breakneck Mech (`play:breakneck-mech:858e6a03`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Your Mechs have [Deflect] and [Ganking]. (Opponents must pay :rb_rune_rainbow:
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Your Mechs have [Deflect] and [Ganking].
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mech
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:7

### [derived-fact] Brush

- official_card: Brush (`play:brush:6592ca65`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `replacement_effect`; confidence 0.8; evidence: you may replace this with the battlefield it replaced
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: Bird, Cat, Dog, Poro, and Ivern units here have +1 :rb_might:
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Brutalizer

- official_card: Brutalizer (`play:brutalizer:0ddb4008`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_calm:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.84; evidence: I have an additional +2 :rb_might:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Equipment

### [derived-fact] Brynhir Thundersong

- official_card: Brynhir Thundersong (`play:brynhir-thundersong:d93611b0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Freljord

### [derived-fact] Bubble Bot

- official_card: Bubble Bot (`play:bubble-bot:c07da9bb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready another friendly Mech
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mech
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Buhru Captain

- official_card: Buhru Captain (`play:buhru-captain:9f954111`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff me
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Bullet Time

- official_card: Bullet Time (`play:bullet-time:3b6dabf3`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Pay any amount of :rb_rune_rainbow:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Pay any amount of :rb_rune_rainbow: to deal that much damage to all enemy units at a battlefield
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: deal that much damage to all enemy units at a battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Bushwhack

- official_card: Bushwhack (`play:bushwhack:f068d201`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play a Gold gear token exhausted
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.84; evidence: Friendly units enter ready
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Caitlyn, Patrolling

- official_card: Caitlyn, Patrolling (`play:caitlyn-patrolling:4a8d3da6`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: Deal damage equal to my Might to a unit at a battlefield
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Caitlyn
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Call to Battle

- official_card: Call to Battle (`play:call-to-battle:704c873c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move a unit they control to the same battlefield
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move a unit you control to a battlefield you control
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Call to Glory

- official_card: Call to Glory (`play:call-to-glory:04a2a461`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff as an additional cost
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit +3 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Called Shot

- official_card: Called Shot (`play:called-shot:7475abbb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_rune_chaos:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: recycle the other
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: Look at the top 2 cards of your Main Deck
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos

### [derived-fact] Calm Rune

- official_card: Calm Rune (`play:calm-rune:ec9305ca`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 1.0; evidence: basic_rune:calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: rune
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm

### [derived-fact] Cannon Barrage

- official_card: Cannon Barrage (`play:cannon-barrage:bf1a6bbd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 2 to all enemy units in combat
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Captain Farron

- official_card: Captain Farron (`play:captain-farron:2a1432f4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Other friendly units here have [Assault].
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Trifarian

### [derived-fact] Card Sharp

- official_card: Card Sharp (`play:card-sharp:96709d6d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a Gold gear token exhausted
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bilgewater

### [derived-fact] Carnivorous Snapvine

- official_card: Carnivorous Snapvine (`play:carnivorous-snapvine:13a6fa94`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: We deal damage equal to our Mights to each other
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shadow Isles

### [derived-fact] Carrion Dredger

- official_card: Carrion Dredger (`play:carrion-dredger:a627978f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play a 1 :rb_might: Bird unit token with [Deflect] to your base
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Deflect]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mech
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order

### [derived-fact] Catalyst of Aeons

- official_card: Catalyst of Aeons (`play:catalyst-of-aeons:5c2af06a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channel 2 runes
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: Channel 2 runes exhausted
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Cemetery Attendant

- official_card: Cemetery Attendant (`play:cemetery-attendant:9c5ccc3c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: play me, return a unit from your trash to your hand
- predicate `return_to_hand`; role `payoff_output`; type `card_flow`; confidence 0.82; evidence: return a unit from your trash to your hand
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dog
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Chakram Dancer

- official_card: Chakram Dancer (`play:chakram-dancer:c6071e2c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: give your other units here [Shield] this turn
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ambush]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Challenge

- official_card: Challenge (`play:challenge:45139d35`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: They deal damage equal to their Mights to each other
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Chaos Rune

- official_card: Chaos Rune (`play:chaos-rune:a76048a5`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 1.0; evidence: basic_rune:chaos
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: rune
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos

### [derived-fact] Charm

- official_card: Charm (`play:charm:03e9c7ac`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move an enemy unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Chem-Baroness

- official_card: Chem-Baroness (`play:chem-baroness:c5c203e8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.88; evidence: When you or an ally hold
- predicate `exhaust`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.9; evidence: you may exhaust me
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a Gold gear token exhausted
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [ADD] an additional :rb_energy_1:
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Renata Glasc

### [derived-fact] Chemtech Cask

- official_card: Chemtech Cask (`play:chemtech-cask:5f987708`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play a spell
- predicate `exhaust`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.9; evidence: you may exhaust me
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a Gold gear token exhausted
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Chemtech Enforcer

- official_card: Chemtech Enforcer (`play:chemtech-enforcer:087a3142`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: discard 1
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault 2] (+2 :rb_might: while I'm an attacker.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault 2]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun

### [derived-fact] Cithria of Cloudfield

- official_card: Cithria of Cloudfield (`play:cithria-of-cloudfield:a24a7746`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff me
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Elite
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Clash of Giants

- official_card: Clash of Giants (`play:clash-of-giants:647c65cd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: They deal damage equal to their Mights to each other
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Cleave

- official_card: Cleave (`play:cleave:bb22004c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while it's an attacker
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: Give a unit [Assault 3] this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Clockwork Keeper

- official_card: Clockwork Keeper (`play:clockwork-keeper:9b488642`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.9; evidence: You may pay :rb_rune_calm: as an additional cost to play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: You may pay :rb_rune_calm:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shurima

### [derived-fact] Cloth Armor

- official_card: Cloth Armor (`play:cloth-armor:d5745d44`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play it
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_mind:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm a defender
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: attach it to a unit you control
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Shield 2] (+2 :rb_might: while I'm a defender.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Shield 2]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Quick-Draw]

### [derived-fact] Combat Chef

- official_card: Combat Chef (`play:combat-chef:404f2e45`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Equip]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Weaponmaster]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5

### [derived-fact] Combat Experience

- official_card: Combat Experience (`play:combat-experience:7766809d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit +1 :rb_might: this turn
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give it +3 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Level 6]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Commander Ledros

- official_card: Commander Ledros (`play:commander-ledros:f5eae405`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: As you play me, you may kill any number of friendly units as an additional cost. Reduce my cost by :rb_rune_order:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.86; evidence: kill any number of friendly units
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ganking]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order

### [derived-fact] Concentrate

- official_card: Concentrate (`play:concentrate:3e35ef4b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 2
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: This costs :rb_energy_2: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: This costs :rb_energy_2: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: This costs :rb_energy_4: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: This costs :rb_energy_4: less
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Level 6]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Level 11]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body

### [derived-fact] Confront

- official_card: Confront (`play:confront:dca66872`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.84; evidence: Units you play this turn enter ready
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Conscription

- official_card: Conscription (`play:conscription:8d398958`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `spend`; role `cost_or_requirement`; type `additional_cost`; confidence 0.9; evidence: You may spend 5 XP as an additional cost to play this
- predicate `gain_control`; role `event_produced`; type `control_change`; confidence 0.88; evidence: Take control of it
- predicate `return_to_hand`; role `event_produced`; type `movement`; confidence 0.82; evidence: recall it
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Consult the Past

- official_card: Consult the Past (`play:consult-the-past:468aa7bd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 2
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Convergent Mutation

- official_card: Convergent Mutation (`play:convergent-mutation:981352cf`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.8; evidence: This turn, increase its Might to the Might of another friendly unit
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Corina Veraza

- official_card: Corina Veraza (`play:corina-veraza:f73585ae`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move to a battlefield
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_order:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move to a battlefield
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play three 1 :rb_might: Recruit unit tokens
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order

### [derived-fact] Corrupt Enforcer

- official_card: Corrupt Enforcer (`play:corrupt-enforcer:e366a9f4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move to a battlefield
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I win a combat
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: discard 1
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move to a battlefield
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4

### [derived-fact] Counter Strike

- official_card: Counter Strike (`play:counter-strike:cfba558c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `prevent`; role `restriction_or_permission`; type `replacement_effect`; confidence 0.86; evidence: The next time that unit would be dealt damage this turn, prevent it
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Jax
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Crackshot Corsair

- official_card: Crackshot Corsair (`play:crackshot-corsair:60ea6f23`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: deal 1 to an enemy unit here
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Pirate
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bilgewater

### [derived-fact] Crescent Guardian

- official_card: Crescent Guardian (`play:crescent-guardian:200b640b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.9; evidence: you may pay :rb_rune_chaos: as an additional cost to play me
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mount Targon

### [derived-fact] Crescent Strike

- official_card: Crescent Strike (`play:crescent-strike:01c8f47c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 4 to that unit and 1 to each other enemy unit there
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Crimson Pigeons

- official_card: Crimson Pigeons (`play:crimson-pigeons:59ab8d4f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.84; evidence: I have +2 :rb_might:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bird
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Crowd Favorite

- official_card: Crowd Favorite (`play:crowd-favorite:59f362fc`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Spend 2 XP
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff if I don't have one
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 1 XP
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give me a +1 :rb_might:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Buff]

### [derived-fact] Cruel Patron

- official_card: Cruel Patron (`play:cruel-patron:0bf36a9b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: kill a friendly unit
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Cull

- official_card: Cull (`play:cull:92a7c8c6`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_chaos:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a Gold gear token exhausted
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Cull the Weak

- official_card: Cull the Weak (`play:cull-the-weak:b1b6d9ef`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.86; evidence: Each player kills one of their units
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Cursed Sarcophagus

- official_card: Cursed Sarcophagus (`play:cursed-sarcophagus:7d379e15`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play this
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: play this, banish all units from your trash
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: banish all units from your trash
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.82; evidence: Play a unit banished with this
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Curtain Call

- official_card: Curtain Call (`play:curtain-call:ca540b49`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] — :rb_energy_1:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 2 to a unit at a battlefield
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 3 to a unit at a base
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit at a battlefield -4 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury

### [derived-fact] Daisy!

- official_card: Daisy! (`play:daisy:9ac122ce`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun] an enemy unit here
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.78; evidence: Reduce my cost by :rb_energy_1: for each of the following tags among your units — Bird, Cat, Dog, and Poro
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.78; evidence: Reduce my cost by :rb_energy_1: for each of the following tags among your units — Bird, Cat, Dog, and Poro
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order

### [derived-fact] Dancing Grenade

- official_card: Dancing Grenade (`play:dancing-grenade:1ebb941d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 2 to a unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Danger Zone

- official_card: Danger Zone (`play:danger-zone:a4e1249a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_1::rb_rune_rainbow:
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give your Mechs +1 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell

### [derived-fact] Dangerous Duo

- official_card: Dangerous Duo (`play:dangerous-duo:5775a881`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give a unit +2 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Legion]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mech
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Daring Poro

- official_card: Daring Poro (`play:daring-poro:e2b0da0f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault] (+1 :rb_might: while I'm an attacker.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Poro
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Darius, Executioner

- official_card: Darius, Executioner (`play:darius-executioner:01ba8e9b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: Other friendly units have +1 :rb_might:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Legion]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Darius

### [derived-fact] Darius, Trifarian

- official_card: Darius, Trifarian (`play:darius-trifarian:1ca0261a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +2 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Darius
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Dark Child - Starter

- official_card: Dark Child - Starter (`play:dark-child-starter:4fef45da`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready up to 2 runes
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Annie
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Daughter of the Void

- official_card: Daughter of the Void (`play:daughter-of-the-void:41f2894f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_rune_rainbow:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Kai'Sa

### [derived-fact] Dauntless Vanguard

- official_card: Dauntless Vanguard (`play:dauntless-vanguard:e92d0334`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play`; role `restriction_or_permission`; type `permission`; confidence 0.82; evidence: You may play me to an occupied enemy battlefield
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Elite
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Dazzling Aurora

- official_card: Dazzling Aurora (`play:dazzling-aurora:64b46d3a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: recycle the rest
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: banish it
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:9

### [derived-fact] Deadbloom Predator

- official_card: Deadbloom Predator (`play:deadbloom-predator:a7cbbb92`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `play`; role `restriction_or_permission`; type `permission`; confidence 0.82; evidence: You may play me to an occupied enemy battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:8
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:8

### [derived-fact] Deadly Flourish

- official_card: Deadly Flourish (`play:deadly-flourish:c7f1dfd1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Deal 3 to an enemy unit. When it dies this turn, play a Gold gear token exhausted. (It has "[Reaction][>] Kill this, :rb_exhaust:
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.88; evidence: Kill this
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 3 to an enemy unit
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_rune_rainbow:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a Gold gear token exhausted
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Death from Below

- official_card: Death from Below (`play:death-from-below:42c6117d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: you may play this from your trash for :rb_rune_rainbow:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.84; evidence: Kill a unit at a battlefield
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Pyke
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Deathgrip

- official_card: Deathgrip (`play:deathgrip:bcba5fad`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: Kill a friendly unit
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.82; evidence: give +:rb_might: equal to its Might to another friendly unit this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Deceiver

- official_card: Deceiver (`play:deceiver:5673f5c7`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer or hold
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: discard 1
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a ready Reflection unit token
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: Give it [Temporary]
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready Reflection unit token there
- predicate `copy`; role `state_or_modifier`; type `copy_effect`; confidence 0.82; evidence: It becomes a copy of another unit there
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind

### [derived-fact] Decisive Strike

- official_card: Decisive Strike (`play:decisive-strike:61220af1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give friendly units +2 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Garen
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Defiant Dance

- official_card: Defiant Dance (`play:defiant-dance:02d8df0e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit +2 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Irelia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Defy

- official_card: Defy (`play:defy:8cd6b1c5`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `cost_cap_constraint`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: costs no more than :rb_energy_4: and
- predicate `counter`; role `event_produced`; type `produced_event`; confidence 0.9; evidence: Counter a spell that costs no more than :rb_energy_4: and no more than :rb_rune_rainbow:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Demacian Diplomat

- official_card: Demacian Diplomat (`play:demacian-diplomat:5b2bcdcd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 1 XP
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Desert's Call

- official_card: Desert's Call (`play:desert-s-call:c06bad0a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_2:
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play a 2 :rb_might: Sand Soldier unit token
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Determined Sentry

- official_card: Determined Sentry (`play:determined-sentry:5260ee97`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: I can't move to base
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bandle City

### [derived-fact] Detonate

- official_card: Detonate (`play:detonate:d574479a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: Kill a gear
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draws 2
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Diana, Lunari

- official_card: Diana, Lunari (`play:diana-lunari:4a172786`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: You may recycle it
- predicate `reveal`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: reveal the top card of your Main Deck
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: look at the top card of your Main Deck
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Predict]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Diana
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3

### [derived-fact] Diana, No Longer Human

- official_card: Diana, No Longer Human (`play:diana-no-longer-human:605ae03c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play a spell
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +2 :rb_might: this turn
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ambush]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Diana
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3

### [derived-fact] Direwing

- official_card: Direwing (`play:direwing:dfba301e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dragon
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:7
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:7

### [derived-fact] Disarming Rake

- official_card: Disarming Rake (`play:disarming-rake:f7ebe3d0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: kill a gear
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Discipline

- official_card: Discipline (`play:discipline:0e5bd863`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit +2 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Disintegrate

- official_card: Disintegrate (`play:disintegrate:729c1066`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 3 to a unit at a battlefield
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Disposal Order

- official_card: Disposal Order (`play:disposal-order:68d05fb8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: recycle them
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: Their owners recycle them
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Divine Judgment

- official_card: Divine Judgment (`play:divine-judgment:b2235a4a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: Recycle the rest
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:7

### [derived-fact] Divining Shells

- official_card: Divining Shells (`play:divining-shells:0ea6d1ad`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play this
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Action][>] Kill this, :rb_exhaust:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: You may recycle it
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.88; evidence: Kill this
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: look at the top card of your Main Deck
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit +2 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Vision]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]

### [derived-fact] Doran's Blade

- official_card: Doran's Blade (`play:doran-s-blade:509fc310`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_body:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Equipment
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might_bonus:2

### [derived-fact] Doran's Ring

- official_card: Doran's Ring (`play:doran-s-ring:2a7933d5`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_chaos:
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: discard 1
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos

### [derived-fact] Doran's Shield

- official_card: Doran's Shield (`play:doran-s-shield:f2c53949`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_calm:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Equipment

### [derived-fact] Double Trouble

- official_card: Double Trouble (`play:double-trouble:070df0c2`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_2:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: Recycle the rest
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: Look at the top 3 cards of your Main Deck
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Downstage Dramatics

- official_card: Downstage Dramatics (`play:downstage-dramatics:c596ab3d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_2:
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Downwell

- official_card: Downwell (`play:downwell:9c91c53a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: Return all units and gear to their owners' hands
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:8

### [derived-fact] Dr. Mundo, Expert

- official_card: Dr. Mundo, Expert (`play:dr-mundo-expert:88e3fed0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: recycle 3 from your trash
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.8; evidence: My Might is increased by the number of cards in your trash
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:8

### [derived-fact] Drag Under

- official_card: Drag Under (`play:drag-under:7ee8ab92`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.84; evidence: Kill a unit at a battlefield
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_2: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_2: less
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Dragon's Rage

- official_card: Dragon's Rage (`play:dragon-s-rage:35c349cc`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move an enemy unit
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: They deal damage equal to their Mights to each other
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Lee Sin
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Dragonsoul Sage

- official_card: Dragonsoul Sage (`play:dragonsoul-sage:b494c74b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Reaction][>] :rb_exhaust:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_energy_1:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Dramatic Visionary

- official_card: Dramatic Visionary (`play:dramatic-visionary:2074f413`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: Recycle any of them
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: look at the top two cards of your Main Deck
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Predict 2]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia

### [derived-fact] Draven, Audacious

- official_card: Draven, Audacious (`play:draven-audacious:cd128e4e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `score`; role `payoff_output`; type `score_change`; confidence 0.8; evidence: score 1 point
- predicate `score`; role `payoff_output`; type `score_change`; confidence 0.8; evidence: score 1 point
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus

### [derived-fact] Draven, Showboat

- official_card: Draven, Showboat (`play:draven-showboat:21b20369`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.8; evidence: My Might is increased by your points
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Draven
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Draven, Vanquisher

- official_card: Draven, Vanquisher (`play:draven-vanquisher:0b326b1d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I win a combat
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack or defend
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack or defend
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a Gold gear token exhausted
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +2 :rb_might: this turn
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +2 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury

### [derived-fact] Dropboarder

- official_card: Dropboarder (`play:dropboarder:0700f5e8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Dune Drake

- official_card: Dune Drake (`play:dune-drake:982e5804`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +2 :rb_might: this turn
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready enemy unit here
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dragon
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shurima

### [derived-fact] Dunebreaker

- official_card: Dunebreaker (`play:dunebreaker:625e592f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I hold
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 2
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:7
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:7

### [derived-fact] Dusk Rose Lab

- official_card: Dusk Rose Lab (`play:dusk-rose-lab:4a845850`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.84; evidence: kill a unit
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Eager Apprentice

- official_card: Eager Apprentice (`play:eager-apprentice:76904ad8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.78; evidence: reduced by :rb_energy_1:, to a minimum of :rb_energy_1:
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.78; evidence: reduced by :rb_energy_1:, to a minimum of :rb_energy_1:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Piltover

### [derived-fact] Eager Drakehound

- official_card: Eager Drakehound (`play:eager-drakehound:3c6551e8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dog
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dragon
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Eclipse

- official_card: Eclipse (`play:eclipse:e147d1e4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: You may recycle it
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: Look at the top card of your Main Deck
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit -4 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Predict]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Eclipse Herald

- official_card: Eclipse Herald (`play:eclipse-herald:2fb84a48`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: stun an enemy unit
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +1 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bird
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:7
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Edge of Night

- official_card: Edge of Night (`play:edge-of-night:c0d34156`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play this
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_chaos:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: attach it to a unit you control (here)
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear

### [derived-fact] Ekko, Recurrent

- official_card: Ekko, Recurrent (`play:ekko-recurrent:f62e9dd9`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_mind:
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready your runes
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ekko

### [derived-fact] Elder Dragon

- official_card: Elder Dragon (`play:elder-dragon:30236914`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 1 to them
- predicate `damage`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: Any amount of your damage is enough to kill enemy units
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dragon
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia

### [derived-fact] Ember Monk

- official_card: Ember Monk (`play:ember-monk:c2ff3a3a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +2 :rb_might: this turn
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Hidden]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bandle City

### [derived-fact] Eminent Benefactor

- official_card: Eminent Benefactor (`play:eminent-benefactor:fbbcebf2`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I hold
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play two Gold gear tokens exhausted
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Piltover

### [derived-fact] Emperor of the Sands

- official_card: Emperor of the Sands (`play:emperor-of-the-sands:122152ab`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_energy_1:, :rb_exhaust:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play a 2 :rb_might: Sand Soldier unit token to your base
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Sand Soldiers you play have [Weaponmaster].
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Equip]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Azir
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Emperor's Dais

- official_card: Emperor's Dais (`play:emperor-s-dais:06f8de89`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer here
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a 2 :rb_might: Sand Soldier unit token
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: return a unit you control here to its owner's hand
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Emperor's Divide

- official_card: Emperor's Divide (`play:emperor-s-divide:2de8389b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move any number of friendly units at a battlefield to their base
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] En Garde

- official_card: En Garde (`play:en-garde:cf258ddf`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a friendly unit +1 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Energy Conduit

- official_card: Energy Conduit (`play:energy-conduit:e3a1b101`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_energy_1:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Enthralling Protector

- official_card: Enthralling Protector (`play:enthralling-protector:ca6c0c98`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Spend 2 XP
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff if I don't have one
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 1 XP
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give me a +1 :rb_might:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Buff]

### [derived-fact] Enthusiastic Promoter

- official_card: Enthusiastic Promoter (`play:enthusiastic-promoter:954cad7e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I hold
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff if it doesn't have one
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give each a +1 :rb_might:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Buff]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Backline]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle

### [derived-fact] Evelynn, Entrancing

- official_card: Evelynn, Entrancing (`play:evelynn-entrancing:346fcb78`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move an enemy unit at a different location to my battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Backline]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demon

### [derived-fact] Evershade Stalker

- official_card: Evershade Stalker (`play:evershade-stalker:d88ce50c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: discard 1
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shadow Isles

### [derived-fact] Existential Dread

- official_card: Existential Dread (`play:existential-dread:bb56494b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_2:
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun] an attacking enemy unit
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: return it to its owner's hand
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Stun]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell

### [derived-fact] Experimental Hexplate

- official_card: Experimental Hexplate (`play:experimental-hexplate:cb371eec`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_mind:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Equipment
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might_bonus:1

### [derived-fact] Eye of the Herald

- official_card: Eye of the Herald (`play:eye-of-the-herald:00bc346d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_order:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a 1 :rb_might: Recruit unit token
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Ezreal, Dashing

- official_card: Ezreal, Dashing (`play:ezreal-dashing:293244ee`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack or defend
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack or defend
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_rune_mind:
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: I don't deal combat damage
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: deal damage equal to my Might to an enemy unit here
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move me to your base
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Ezreal, Prodigy

- official_card: Ezreal, Prodigy (`play:ezreal-prodigy:c63a1193`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Optional additional costs you pay cost :rb_energy_1:
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: discard 1
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 2
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ezreal
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3

### [derived-fact] Facebreaker

- official_card: Facebreaker (`play:facebreaker:081d95f6`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: They don't deal combat damage this turn
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun a friendly unit and an enemy unit at the same battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Factory Recall

- official_card: Factory Recall (`play:factory-recall:41b004aa`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: Return a gear to its owner's hand
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Fading Memories

- official_card: Fading Memories (`play:fading-memories:c9a46092`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: Give a unit at a battlefield or a gear [Temporary]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Fae Dragon

- official_card: Fae Dragon (`play:fae-dragon:cf42d079`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff if it doesn't have one
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff up to four friendly units
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a Gold gear token exhausted
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give each a +1 :rb_might:
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fae
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body

### [derived-fact] Fae Porter

- official_card: Fae Porter (`play:fae-porter:f176ff7f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move to a battlefield
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move to a battlefield
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move to a battlefield
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move a unit you control to the same battlefield
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fae
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia

### [derived-fact] Faithful Manufactor

- official_card: Faithful Manufactor (`play:faithful-manufactor:00a39ff2`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a 1 :rb_might: Recruit unit token
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Piltover

### [derived-fact] Falling Comet

- official_card: Falling Comet (`play:falling-comet:43cec82c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 6 to a unit at a battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Falling Star

- official_card: Falling Star (`play:falling-star:2e10bc4d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 3 to a unit
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 3 to a unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Fate Weaver

- official_card: Fate Weaver (`play:fate-weaver:82a0d8ae`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `cost_threshold`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: cost :rb_energy_4: or more
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: Recycle the rest
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: look at the top 4 cards of your Main Deck
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4

### [derived-fact] Feral Strength

- official_card: Feral Strength (`play:feral-strength:6627d2a6`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_2:
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit +2 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Ferrous Forerunner

- official_card: Ferrous Forerunner (`play:ferrous-forerunner:5957090a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play two 3 :rb_might: Mech unit tokens to your base
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mech
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6

### [derived-fact] Fight or Flight

- official_card: Fight or Flight (`play:fight-or-flight:489143ff`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move a unit from a battlefield to its base
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Final Spark

- official_card: Final Spark (`play:final-spark:c076b01b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 8 to a unit
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Lux
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:8

### [derived-fact] Find Your Center

- official_card: Find Your Center (`play:find-your-center:38e81e4f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channel 1 rune exhausted
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: this costs :rb_energy_2: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: this costs :rb_energy_2: less
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Fiora, Peerless

- official_card: Fiora, Peerless (`play:fiora-peerless:f8a59eeb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack or defend
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack or defend
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.82; evidence: double my Might this combat
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fiora
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Fiora, Victorious

- official_card: Fiora, Victorious (`play:fiora-victorious:92559485`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: While I'm [Mighty], I have [Deflect], [Ganking], and [Shield].
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Mighty]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fiora
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Fiora, Worthy

- official_card: Fiora, Worthy (`play:fiora-worthy:e3105fbc`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready it
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Mighty]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fiora
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Fire Below the Mountain

- official_card: Fire Below the Mountain (`play:fire-below-the-mountain:2b9c0e7f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_rune_rainbow:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ornn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Firestorm

- official_card: Firestorm (`play:firestorm:2522be6e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 3 to all enemy units at a battlefield
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] First Mate

- official_card: First Mate (`play:first-mate:62e97859`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready another unit
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Pirate
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bilgewater

### [derived-fact] Fizz, Trickster

- official_card: Fizz, Trickster (`play:fizz-trickster:3e947e55`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `cost_cap_constraint`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: cost no more than :rb_energy_3:
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: play me, you may play a spell from your trash with Energy cost no more than :rb_energy_3:, ignoring its Energy cost
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fizz
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3

### [derived-fact] Flame Chompers

- official_card: Flame Chompers (`play:flame-chompers:a6e26638`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.88; evidence: When you discard me
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: you may pay :rb_rune_fury: to play me
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Flash

- official_card: Flash (`play:flash:571eba20`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move up to 2 friendly units to base
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move up to 2 friendly units to base
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Flurry of Blades

- official_card: Flurry of Blades (`play:flurry-of-blades:0ee9173f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 1 to all units at battlefields
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Flurry of Feathers

- official_card: Flurry of Feathers (`play:flurry-of-feathers:ab222324`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `counter`; role `event_produced`; type `produced_event`; confidence 0.9; evidence: Counter a spell
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play four 1 :rb_might: Bird unit tokens with [Deflect]
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Deflect]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Forbidding Waste

- official_card: Forbidding Waste (`play:forbidding-waste:0c19865c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.8; evidence: a unit here is defending alone, it has -2 :rb_might:
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Forecaster

- official_card: Forecaster (`play:forecaster:72b635df`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: You may recycle it
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: look at the top card of your Main Deck
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Your Mechs have [Vision].
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mech
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2

### [derived-fact] Forge of the Fluft

- official_card: Forge of the Fluft (`play:forge-of-the-fluft:4ea8d456`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: While you control this battlefield
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Forge of the Future

- official_card: Forge of the Future (`play:forge-of-the-future:eb7442f4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play this
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Kill this
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.88; evidence: Kill this
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a 1 :rb_might: Recruit unit token at your base
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Forgefire Cape

- official_card: Forgefire Cape (`play:forgefire-cape:bbfe1354`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack or defend
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack or defend
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_rainbow:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: deal 2 to all enemy units here
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Unique]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear

### [derived-fact] Forgotten Library

- official_card: Forgotten Library (`play:forgotten-library:f1e10333`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: when you play a spell
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: While you control this battlefield
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: You may recycle it
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: Look at the top card of your Main Deck
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Predict]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Forgotten Monument

- official_card: Forgotten Monument (`play:forgotten-monument:5c511235`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: Players can't score here until their third turn
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Forgotten Signpost

- official_card: Forgotten Signpost (`play:forgotten-signpost:85046b6c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Action][>] Exhaust a unit you control, :rb_exhaust:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move a different unit you control to the location of the unit you exhausted to pay for this ability
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Fortified Position

- official_card: Fortified Position (`play:fortified-position:31bb26b4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while it's a defender
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: It gains [Shield 2] this combat
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Fox-Fire

- official_card: Fox-Fire (`play:fox-fire:551c2553`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.84; evidence: Kill any number of units at a battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ahri
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell

### [derived-fact] Fresh Beans

- official_card: Fresh Beans (`play:fresh-beans:e1294ad8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play a unit
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Friendship

- official_card: Friendship (`play:friendship:eecf0310`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give it +1 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Frigid Jewel

- official_card: Frigid Jewel (`play:frigid-jewel:575481e6`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give a friendly unit +2 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Frigid Touch

- official_card: Frigid Touch (`play:frigid-touch:28f36f21`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_2:
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit -2 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Frisky Hunter

- official_card: Frisky Hunter (`play:frisky-hunter:a3ac8a1f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a 1 :rb_might: Bird unit token with [Deflect]
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Deflect]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Cat
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3

### [derived-fact] Frostcoat Cub

- official_card: Frostcoat Cub (`play:frostcoat-cub:a17f0dcf`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.9; evidence: You may pay :rb_rune_mind: as an additional cost to play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: You may pay :rb_rune_mind:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give a unit -2 :rb_might: this turn
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dog
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3

### [derived-fact] Frozen Fortress

- official_card: Frozen Fortress (`play:frozen-fortress:c20dc712`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: deal 1 to each unit here
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Fury Rune

- official_card: Fury Rune (`play:fury-rune:ec493974`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 1.0; evidence: basic_rune:fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: rune
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury

### [derived-fact] Galio, Indefatigable

- official_card: Galio, Indefatigable (`play:galio-indefatigable:d6728973`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: I don't deal combat damage
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Galio
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6

### [derived-fact] Garbage Grabber

- official_card: Garbage Grabber (`play:garbage-grabber:cf950167`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Recycle 3 from your trash, :rb_energy_1:, :rb_exhaust:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: Recycle 3 from your trash
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Gardens of Becoming

- official_card: Gardens of Becoming (`play:gardens-of-becoming:9dca0acf`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Units here have ":rb_exhaust:
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: Gain 1 XP
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Garen, Commander

- official_card: Garen, Commander (`play:garen-commander:a262e66d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: Other friendly units have +1 :rb_might:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Elite
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Garen
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia

### [derived-fact] Garen, Rugged

- official_card: Garen, Rugged (`play:garen-rugged:397ab8eb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault 2], [Shield 2] (+2 :rb_might: while I'm an attacker or defender.)
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Shield 2]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault 2]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Elite
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Garen

### [derived-fact] Gearhead

- official_card: Gearhead (`play:gearhead:a59c38ca`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_mind:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Gem Jammer

- official_card: Gem Jammer (`play:gem-jammer:84d20dc4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: give a unit [Ganking] this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mech
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bandle City

### [derived-fact] Gemcraft Seer

- official_card: Gemcraft Seer (`play:gemcraft-seer:5378ef68`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: You may recycle it
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: look at the top card of your Main Deck
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Other friendly units have [Vision].
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Vision]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3

### [derived-fact] Gemhand Hunter

- official_card: Gemhand Hunter (`play:gemhand-hunter:66eb2764`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 1 XP
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.84; evidence: I have +1 :rb_might:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hunt]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Level 6]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Gentle Gemdragon

- official_card: Gentle Gemdragon (`play:gentle-gemdragon:20c4d777`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready up to 2 runes
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dragon
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:8
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:8
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mount Targon

### [derived-fact] Gentlemen's Duel

- official_card: Gentlemen's Duel (`play:gentlemen-s-duel:a2bd8048`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: They deal damage equal to their Mights to each other
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a friendly unit +3 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Get Excited!

- official_card: Get Excited! (`play:get-excited:06a9f254`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: Discard 1
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: Deal its Energy cost as damage to a unit at a battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Glasc Mixologist

- official_card: Glasc Mixologist (`play:glasc-mixologist:76c5e377`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `cost_cap_constraint`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: cost no more than :rb_energy_3: and
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: You may play a unit with cost no more than :rb_energy_3: and no more than :rb_rune_rainbow: from your trash, ignoring its cost
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5

### [derived-fact] Gloomist

- official_card: Gloomist (`play:gloomist:c2b23126`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.88; evidence: When you or an ally hold
- predicate `exhaust`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.9; evidence: you may exhaust me
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Vex
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Glorious Executioner

- official_card: Glorious Executioner (`play:glorious-executioner:c8e2e2b2`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you win a combat
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Draven

### [derived-fact] Gold

- official_card: Gold (`play:gold:6cfbe394`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Reaction][>] Kill this, :rb_exhaust:
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.88; evidence: Kill this
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_rune_rainbow:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless

### [derived-fact] Grand Duelist

- official_card: Grand Duelist (`play:grand-duelist:53b0f72b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `exhaust`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.9; evidence: you may exhaust me
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channel 1 rune exhausted
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Mighty]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fiora
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Grand Strategem

- official_card: Grand Strategem (`play:grand-strategem:18df7b02`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give friendly units +5 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Grandmaster at Arms

- official_card: Grandmaster at Arms (`play:grandmaster-at-arms:117140a0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_energy_1:, :rb_exhaust:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach a detached Equipment you control to a unit you control
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach an attached Equipment you control to a unit you control
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Jax
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Green Father

- official_card: Green Father (`play:green-father:0015a332`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer or hold
- predicate `exhaust`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.9; evidence: you may exhaust me
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: Bird, Cat, Dog, Poro, and Ivern units have +1 :rb_might:
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: Bird, Cat, Dog, Poro, and Ivern units have +1 :rb_might:
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ivern

### [derived-fact] Grim Apothecary

- official_card: Grim Apothecary (`play:grim-apothecary:4c23e812`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: return a friendly unit at a battlefield to its owner's hand
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ambush]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3

### [derived-fact] Grim Resolve

- official_card: Grim Resolve (`play:grim-resolve:c91ccdb1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 2 XP
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a friendly unit +3 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Grove of the God-Willow

- official_card: Grove of the God-Willow (`play:grove-of-the-god-willow:c5ac9741`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you hold here
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Guardian Angel

- official_card: Guardian Angel (`play:guardian-angel:3a0c3bdc`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_calm:
- predicate `prevent`; role `restriction_or_permission`; type `replacement_effect`; confidence 0.88; evidence: If I would die, kill Guardian Angel instead. Heal me, exhaust me, and recall me
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `return_to_hand`; role `event_produced`; type `movement`; confidence 0.82; evidence: recall me
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Guardian of the Passage

- official_card: Guardian of the Passage (`play:guardian-of-the-passage:f481a2e7`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I hold
- predicate `return_to_hand`; role `payoff_output`; type `card_flow`; confidence 0.82; evidence: return a unit or gear from your trash to your hand
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Spirit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shadow Isles

### [derived-fact] Guards!

- official_card: Guards! (`play:guards:c3487335`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play a 2 :rb_might: Sand Soldier unit token
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready it
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Guerilla Warfare

- official_card: Guerilla Warfare (`play:guerilla-warfare:5df47749`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `return_to_hand`; role `payoff_output`; type `card_flow`; confidence 0.82; evidence: Return up to two cards with [Hidden] from your trash to your hand
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Hidden]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Teemo
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Gust

- official_card: Gust (`play:gust:9fa07ad4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: Return a unit at a battlefield with 3 :rb_might: or less to its owner's hand
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Gustwalker

- official_card: Gustwalker (`play:gustwalker:e1514be6`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 2 XP
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.84; evidence: I have +1 :rb_might:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Ganking]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hunt 2]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Level 3]

### [derived-fact] Gutter Palace

- official_card: Gutter Palace (`play:gutter-palace:2fb2b882`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Discard 1, :rb_exhaust:
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: Discard 1
- predicate `score`; role `payoff_output`; type `score_change`; confidence 0.82; evidence: you win the game
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play a 1 :rb_might: Bird unit token with [Deflect]
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Deflect]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Hall of Legends

- official_card: Hall of Legends (`play:hall-of-legends:1624bde5`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer here
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready your legend
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Hallowed Tomb

- official_card: Hallowed Tomb (`play:hallowed-tomb:15d30261`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you hold here
- predicate `return_to_hand`; role `payoff_output`; type `card_flow`; confidence 0.8; evidence: return your Chosen Champion from your trash to your Champion Zone
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Hand of Noxus

- official_card: Hand of Noxus (`play:hand-of-noxus:7ff0f47b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_energy_1:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Legion]
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Darius

### [derived-fact] Hard Bargain

- official_card: Hard Bargain (`play:hard-bargain:a33b0166`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_2:
- predicate `counter`; role `event_produced`; type `produced_event`; confidence 0.9; evidence: Counter a spell unless its controller pays :rb_energy_2:
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Harnessed Dragon

- official_card: Harnessed Dragon (`play:harnessed-dragon:c4bb02f1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: kill an enemy unit
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dragon
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia

### [derived-fact] Harpoon Squad

- official_card: Harpoon Squad (`play:harpoon-squad:f103bb9d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move from a battlefield
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +2 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Pirate
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Heart of Dark Ice

- official_card: Heart of Dark Ice (`play:heart-of-dark-ice:37e59fb7`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit +3 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Heedless Resurrection

- official_card: Heedless Resurrection (`play:heedless-resurrection:663d7dfc`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: kill a friendly unit
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: Play a unit from your trash that costs no more Energy and no more Power than the killed unit, ignoring its cost
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Heimerdinger, Inventor

- official_card: Heimerdinger, Inventor (`play:heimerdinger-inventor:2b2dc5bb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Piltover
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Heimerdinger

### [derived-fact] Herald of Scales

- official_card: Herald of Scales (`play:herald-of-scales:be4c3df8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.78; evidence: reduced by :rb_energy_2:, to a minimum of :rb_energy_1:
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.78; evidence: reduced by :rb_energy_2:, to a minimum of :rb_energy_1:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mount Targon

### [derived-fact] Herald of Spring

- official_card: Herald of Spring (`play:herald-of-spring:4439e8b0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 1 XP
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 2 XP
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hunt]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Herald of the Arcane

- official_card: Herald of the Arcane (`play:herald-of-the-arcane:2782794e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_energy_1:, :rb_exhaust:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play a 1 :rb_might: Recruit unit token
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Viktor

### [derived-fact] Here to Help

- official_card: Here to Help (`play:here-to-help:21d9f335`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: You may play a unit from hand to a battlefield you control, reducing its cost by :rb_energy_3:
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.78; evidence: reducing its cost by :rb_energy_3:
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.78; evidence: reducing its cost by :rb_energy_3:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell

### [derived-fact] Heroic Charge

- official_card: Heroic Charge (`play:heroic-charge:9df18b52`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun] an enemy unit at its location
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a friendly unit +1 :rb_might: this turn
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Stun]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Hexdrinker

- official_card: Hexdrinker (`play:hexdrinker:9f5d3e37`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_body:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Hextech Anomaly

- official_card: Hextech Anomaly (`play:hextech-anomaly:bf2a39e8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Pay any amount of :rb_rune_rainbow: to [Add] that much Energy
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] that much Energy
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Hextech Gauntlets

- official_card: Hextech Gauntlets (`play:hextech-gauntlets:f041973f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_energy_3::rb_rune_rainbow:. This ability's Energy cost is reduced by the Might of the unit you choose. (Pay the cost
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Vi
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury

### [derived-fact] Hextech Ray

- official_card: Hextech Ray (`play:hextech-ray:32239197`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 3 to a unit at a battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Hidden Blade

- official_card: Hidden Blade (`play:hidden-blade:0c12ff93`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.84; evidence: Kill a unit at a battlefield
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draws 2
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Highlander

- official_card: Highlander (`play:highlander:fa089001`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `prevent`; role `restriction_or_permission`; type `replacement_effect`; confidence 0.88; evidence: The next time it would die this turn, heal it, exhaust it, and recall it instead
- predicate `return_to_hand`; role `event_produced`; type `movement`; confidence 0.82; evidence: recall it instead
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Master Yi

### [derived-fact] Honest Broker

- official_card: Honest Broker (`play:honest-broker:d68f4e69`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play a Gold gear token exhausted
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Honeyfruit

- official_card: Honeyfruit (`play:honeyfruit:51dd9a16`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Reaction][>] :rb_exhaust:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Level 6][>] [>>][Reaction][>] :rb_exhaust:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_rune_rainbow:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_energy_1::rb_rune_rainbow:
- predicate `enter_exhausted`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: This enters exhausted
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Level 6]

### [derived-fact] Hostile Takeover

- official_card: Hostile Takeover (`play:hostile-takeover:a5a73bd7`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `gain_control`; role `event_produced`; type `control_change`; confidence 0.88; evidence: Take control of an enemy unit at a battlefield
- predicate `lose_control`; role `event_produced`; type `control_change`; confidence 0.88; evidence: Lose control of that unit
- predicate `return_to_hand`; role `event_produced`; type `movement`; confidence 0.82; evidence: recall it at end of turn
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: Ready it
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell

### [derived-fact] Hunter's Machete

- official_card: Hunter's Machete (`play:hunter-s-machete:968edf6e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_body:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 1 XP
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hunt]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]

### [derived-fact] Hwei, Brooding Painter

- official_card: Hwei, Brooding Painter (`play:hwei-brooding-painter:d202bc8d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: discard 1
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: Ready up to 2 runes
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give me +3 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind

### [derived-fact] Iascylla

- official_card: Iascylla (`play:iascylla:4a5f7dcf`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I hold
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move an enemy unit to this battlefield
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:7
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bilgewater

### [derived-fact] Icathian Rain

- official_card: Icathian Rain (`play:icathian-rain:7fcc4497`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 2 to a unit
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 2 to a unit
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 2 to a unit
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 2 to a unit
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 2 to a unit
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 2 to a unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind

### [derived-fact] Icevale Archer

- official_card: Icevale Archer (`play:icevale-archer:a3da7537`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give a unit here -1 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Freljord

### [derived-fact] Immortal Phoenix

- official_card: Immortal Phoenix (`play:immortal-phoenix:47e509a7`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: play me from your trash
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.84; evidence: kill a unit
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: you may pay :rb_energy_1::rb_rune_fury: to play me
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault 2] (+2 :rb_might: while I'm an attacker.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault 2]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury

### [derived-fact] Imperial Decree

- official_card: Imperial Decree (`play:imperial-decree:aa7e7d60`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.82; evidence: When any unit takes damage this turn, kill it
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Imposing Challenger

- official_card: Imposing Challenger (`play:imposing-challenger:41a9c601`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move an enemy unit here with less Might than me to a different battlefield
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Incinerate

- official_card: Incinerate (`play:incinerate:07b208ea`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 2 to a unit at a battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Inferna

- official_card: Inferna (`play:inferna:389a2508`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault 2] (+2 :rb_might: while I'm an attacker.)
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ambush]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault 2]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1

### [derived-fact] Insightful Investigator

- official_card: Insightful Investigator (`play:insightful-investigator:2f88bdb6`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: they discard that card
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Piltover

### [derived-fact] Invert Timelines

- official_card: Invert Timelines (`play:invert-timelines:7a3cc22a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: Each player discards their hand
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draws 4
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Inviolus Vox

- official_card: Inviolus Vox (`play:inviolus-vox:722201ee`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give a friendly unit +8 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dragon
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:8
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:8

### [derived-fact] Irelia, Fervent

- official_card: Irelia, Fervent (`play:irelia-fervent:422771c3`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +1 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Irelia

### [derived-fact] Irelia, Graceful

- official_card: Irelia, Graceful (`play:irelia-graceful:e8452ca1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: Your spells that choose me cost :rb_energy_1: or :rb_rune_rainbow: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: Your spells that choose me cost :rb_energy_1: or :rb_rune_rainbow: less
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Irelia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Iron Ballista

- official_card: Iron Ballista (`play:iron-ballista:6d1b61ac`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 2 to a unit at a battlefield
- predicate `enter_exhausted`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: This enters exhausted
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Irresistible Faefolk

- official_card: Irresistible Faefolk (`play:irresistible-faefolk:413b57a0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move to a battlefield
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move to a battlefield
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move to a battlefield
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move an enemy unit to that battlefield
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fae
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia

### [derived-fact] Isolate

- official_card: Isolate (`play:isolate:d9a1ea34`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move an enemy unit from a battlefield to its base
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Ivern, Friend to All

- official_card: Ivern, Friend to All (`play:ivern-friend-to-all:297d8432`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `score`; role `payoff_output`; type `score_change`; confidence 0.8; evidence: score 1 point
- predicate `gain_keyword`; role `state_or_modifier`; type `state_modifier`; confidence 0.78; evidence: I gain that tag
- predicate `choose`; role `targeting_or_scope`; type `target_scope`; confidence 0.78; evidence: choose Bird, Cat, Dog, or Poro
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order

### [derived-fact] Ivern, Nurturer

- official_card: Ivern, Nurturer (`play:ivern-nurturer:d2c1e478`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: when I hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: Recycle the rest
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: look at the top 3 cards of your Main Deck
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Buff]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ivern

### [derived-fact] Jae Medarda

- official_card: Jae Medarda (`play:jae-medarda:55ee217a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Janna, Savior

- official_card: Janna, Savior (`play:janna-savior:3e9ef70d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move up to one enemy unit from here to its base
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move up to one enemy unit from here to its base
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Janna

### [derived-fact] Jaull-Fish

- official_card: Jaull-Fish (`play:jaull-fish:d95a8327`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_body:
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_2: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_2: less
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Mighty]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6

### [derived-fact] Jax, Unmatched

- official_card: Jax, Unmatched (`play:jax-unmatched:d5bc89ec`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play it
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: attach it to a unit you control
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Your Equipment everywhere have [Quick-Draw].
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Jax
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm

### [derived-fact] Jax, Unrelenting

- official_card: Jax, Unrelenting (`play:jax-unrelenting:8670f403`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you attach an Equipment to me
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Equip]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Weaponmaster]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Jax

### [derived-fact] Jayce, Man of Progress

- official_card: Jayce, Man of Progress (`play:jayce-man-of-progress:7c07d54d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `cost_cap_constraint`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: cost no more than :rb_energy_7: from
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: you may play a gear with Energy cost no more than :rb_energy_7: from hand this turn, ignoring its Energy cost
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Jayce
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Jeweled Colossus

- official_card: Jeweled Colossus (`play:jeweled-colossus:6f7edc11`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm a defender
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: You may recycle it
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: look at the top card of your Main Deck
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Shield] (+1 :rb_might: while I'm a defender.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Vision]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Shield]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Jhin, Meticulous Killer

- official_card: Jhin, Meticulous Killer (`play:jhin-meticulous-killer:f3b20bd0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `play`; role `restriction_or_permission`; type `permission`; confidence 0.82; evidence: you may play me for :rb_rune_mind:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: You may recycle it
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: look at the top card of your Main Deck
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Vision]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Jhin

### [derived-fact] Jhin, Murderous Artist

- official_card: Jhin, Murderous Artist (`play:jhin-murderous-artist:dbecef0c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_energy_1::rb_rune_rainbow:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ganking]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury

### [derived-fact] Jinx, Demolitionist

- official_card: Jinx, Demolitionist (`play:jinx-demolitionist:ae7f20ef`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_fury:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: discard 2
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault 2] (+2 :rb_might: while I'm an attacker.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault 2]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Jinx, Rebel

- official_card: Jinx, Rebel (`play:jinx-rebel:b85a0cca`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +1 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Jinx
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Kadregrin the Infernal

- official_card: Kadregrin the Infernal (`play:kadregrin-the-infernal:fcefe851`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1 for each of your [Mighty] units
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Mighty]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dragon
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:9
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2

### [derived-fact] Kai'Sa, Evolutionary

- official_card: Kai'Sa, Evolutionary (`play:kai-sa-evolutionary:4e7c39e8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: recycle it
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: Then recycle it
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: you may play a spell from your trash with Energy cost less than your points without paying its Energy cost
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ganking]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind

### [derived-fact] Kai'Sa, Survivor

- official_card: Kai'Sa, Survivor (`play:kai-sa-survivor:5a507ebb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_fury:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Kai'Sa
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4

### [derived-fact] Karma, Channeler

- official_card: Karma, Channeler (`play:karma-channeler:7a5457ee`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you recycle one or more cards to your Main Deck
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: You may recycle it
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff a friendly unit
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: look at the top card of your Main Deck
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Vision]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Vi
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Karthus, Eternal

- official_card: Karthus, Eternal (`play:karthus-eternal:bc9cc407`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Spirit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Karthus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Katarina, Reckless

- official_card: Katarina, Reckless (`play:katarina-reckless:5ac00445`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: deal 2 to an enemy unit
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Kato the Arm

- official_card: Kato the Arm (`play:kato-the-arm:6a8e198a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move to a battlefield
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move to a battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3

### [derived-fact] Kayn, Unleashed

- official_card: Kayn, Unleashed (`play:kayn-unleashed:c3689dd0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.84; evidence: I don't take damage
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ganking]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Kayn
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6

### [derived-fact] Keeper of Masks

- official_card: Keeper of Masks (`play:keeper-of-masks:536d4ae5`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play two Reflection unit tokens
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Temporary]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia

### [derived-fact] Keeper of the Hammer

- official_card: Keeper of the Hammer (`play:keeper-of-the-hammer:9c0dda8e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you hold
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Spend 3 XP, :rb_exhaust:
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 1 XP
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Poppy
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Keeper's Verdict

- official_card: Keeper's Verdict (`play:keeper-s-verdict:9e4e390e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `payoff_output`; type `movement`; confidence 0.84; evidence: Its owner places it on the top or bottom of their Main Deck
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Poppy
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Kha'Zix, Evolving Hunter

- official_card: Kha'Zix, Evolving Hunter (`play:kha-zix-evolving-hunter:5af6b733`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: deal damage equal to my Might to an enemy unit here
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 1 XP
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hunt]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Kha'Zix, Mutating Horror

- official_card: Kha'Zix, Mutating Horror (`play:kha-zix-mutating-horror:fdcc125e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack or defend
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack or defend
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 2 XP
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +2 :rb_might: this turn
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ambush]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos

### [derived-fact] King's Edict

- official_card: King's Edict (`play:king-s-edict:9f9dcab4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.82; evidence: Kill those units
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Kinkou Initiate

- official_card: Kinkou Initiate (`play:kinkou-initiate:7721dda2`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Kinkou Monk

- official_card: Kinkou Monk (`play:kinkou-monk:f647011d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff gets a +1 :rb_might: buff
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff up to two other friendly units
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Kog'Maw, Caustic

- official_card: Kog'Maw, Caustic (`play:kog-maw-caustic:c071c167`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 4 to all units at my battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Kog'Maw

### [derived-fact] Kraken Hunter

- official_card: Kraken Hunter (`play:kraken-hunter:2fc675cc`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_body:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: As you play me, you may spend any number of buffs as an additional cost. Reduce my cost by :rb_rune_body:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff you spend
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault] (+1 :rb_might: while I'm an attacker.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Lady of Luminosity - Starter

- official_card: Lady of Luminosity - Starter (`play:lady-of-luminosity-starter:b8a50096`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play a spell
- predicate `cost_threshold`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: costs :rb_energy_5: or more
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Lux
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Last Breath

- official_card: Last Breath (`play:last-breath:d2989c2f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: It deals damage equal to its Might to an enemy unit at a battlefield
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: Ready a friendly unit
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yasuo
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2

### [derived-fact] Last Rites

- official_card: Last Rites (`play:last-rites:0eda9816`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] — :rb_rune_chaos:, Recycle 2 cards from your trash (Pay the cost
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: you may play a unit from your trash
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: Recycle 2 cards from your trash
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]

### [derived-fact] Last Stand

- official_card: Last Stand (`play:last-stand:480fa5eb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: Give it [Temporary]
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.82; evidence: Double a friendly unit's Might this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Laurent Bladekeeper

- official_card: Laurent Bladekeeper (`play:laurent-bladekeeper:31152886`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.94; evidence: Ganking
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Laurent Duelist

- official_card: Laurent Duelist (`play:laurent-duelist:e5adff59`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault 2] (+2 :rb_might: while I'm an attacker.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault 2]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] LeBlanc, Everywhere at Once

- official_card: LeBlanc, Everywhere at Once (`play:leblanc-everywhere-at-once:e9986ee4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Temporary]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Backline]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: LeBlanc
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] LeBlanc, Fragmented

- official_card: LeBlanc, Fragmented (`play:leblanc-fragmented:d5d94cdb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 2
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault] (+1 :rb_might: while I'm an attacker.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Lecturing Yordle

- official_card: Lecturing Yordle (`play:lecturing-yordle:aa6faa7d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Lee Sin, Ascetic

- official_card: Lee Sin, Ascetic (`play:lee-sin-ascetic:5a1ebe30`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm a defender
- predicate `buff`; role `restriction_or_permission`; type `permission`; confidence 0.84; evidence: I can have any number of buffs
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: Buff me
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Shield] (+1 :rb_might: while I'm a defender.)
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.82; evidence: I get a +1 :rb_might: buff
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Shield]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Lee Sin, Centered

- official_card: Lee Sin, Centered (`play:lee-sin-centered:ae9804ba`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_body:
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: Other buffed friendly units at my battlefield have +2 :rb_might:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Lee Sin

### [derived-fact] Legion Quartermaster

- official_card: Legion Quartermaster (`play:legion-quartermaster:b4ecf31e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: return a friendly gear to its owner's hand
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Trifarian

### [derived-fact] Legion Rearguard

- official_card: Legion Rearguard (`play:legion-rearguard:4407c3c1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_fury:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Trifarian

### [derived-fact] Leona, Determined

- official_card: Leona, Determined (`play:leona-determined:e94bda80`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm a defender
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: stun an enemy unit here
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Shield] (+1 :rb_might: while I'm a defender.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Shield]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Leona

### [derived-fact] Leona, Zealot

- official_card: Leona, Zealot (`play:leona-zealot:b7f55ff4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: Stunned enemy units here have -8 :rb_might:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Leona
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Lillia, Fae Fawn

- official_card: Lillia, Fae Fawn (`play:lillia-fae-fawn:c29d3e8d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_mind:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move from a location
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a 3 :rb_might: Sprite unit token with [Temporary]
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Temporary]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fae
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Lillia, Protector of Dreams

- official_card: Lillia, Protector of Dreams (`play:lillia-protector-of-dreams:21163b7d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +1 :rb_might: this turn
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Your token units have [Tank].
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fae
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Lillia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4

### [derived-fact] Lilting Lullaby

- official_card: Lilting Lullaby (`play:lilting-lullaby:b386575d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `counter`; role `event_produced`; type `produced_event`; confidence 0.9; evidence: Counter a spell
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Lillia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Lonely Poro

- official_card: Lonely Poro (`play:lonely-poro:b23f71bc`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Poro
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Long Sword

- official_card: Long Sword (`play:long-sword:29d3a400`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play it
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_fury:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: attach it to a unit you control
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Quick-Draw]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury

### [derived-fact] Loose Cannon

- official_card: Loose Cannon (`play:loose-cannon:029aa9b6`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Jinx
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Lord Broadmane

- official_card: Lord Broadmane (`play:lord-broadmane:9143ae2d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: give your other units here [Assault] this turn
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ambush]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5

### [derived-fact] Lotus Trap

- official_card: Lotus Trap (`play:lotus-trap:63db23f4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: Double all damage that would be dealt to it this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Loyal Poro

- official_card: Loyal Poro (`play:loyal-poro:385fae03`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Poro
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Loyal Pup

- official_card: Loyal Pup (`play:loyal-pup:4ee3d1da`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move me there
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dog
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bandle City

### [derived-fact] Lucian, Gunslinger

- official_card: Lucian, Gunslinger (`play:lucian-gunslinger:6cdb974d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: deal damage equal to my [Assault] to an enemy unit here
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault] (+1 :rb_might: while I'm an attacker.)
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Assault]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury

### [derived-fact] Lucian, Merciless

- official_card: Lucian, Merciless (`play:lucian-merciless:297dd867`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Equip]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Weaponmaster]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body

### [derived-fact] Lunar Boon

- official_card: Lunar Boon (`play:lunar-boon:5f74324a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: Discard 1
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 2
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Lux, Crownguard

- official_card: Lux, Crownguard (`play:lux-crownguard:7b9e26a1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_energy_2:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Lux
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia

### [derived-fact] Lux, Illuminated

- official_card: Lux, Illuminated (`play:lux-illuminated:145673bb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play a spell
- predicate `cost_threshold`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: costs :rb_energy_5: or more
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +3 :rb_might: this turn
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Lux
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Machine Evangel

- official_card: Machine Evangel (`play:machine-evangel:3bc0f8ca`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play three 1 :rb_might: Recruit unit tokens into your base
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Maddened Marauder

- official_card: Maddened Marauder (`play:maddened-marauder:4686fbbf`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move a unit from a battlefield to its base
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Pirate
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Maduli the Gatekeeper

- official_card: Maduli the Gatekeeper (`play:maduli-the-gatekeeper:29bfb45b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_rune_chaos:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move me to an occupied enemy battlefield if my Might is greater than the total Might of enemy units there
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:7
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bandle City

### [derived-fact] Mageseeker Investigator

- official_card: Mageseeker Investigator (`play:mageseeker-investigator:0a40e923`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Opponents must pay :rb_rune_rainbow:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move multiple units to my battlefield at the same time
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Mageseeker Warden

- official_card: Mageseeker Warden (`play:mageseeker-warden:f27157dd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: opponents can only play units to their base
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: spells and abilities can't ready enemy units and gear
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Magma Wurm

- official_card: Magma Wurm (`play:magma-wurm:37e34ff6`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.84; evidence: Other friendly units enter ready
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:8
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:8
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Freljord

### [derived-fact] Malzahar, Fanatic

- official_card: Malzahar, Fanatic (`play:malzahar-fanatic:e463fe1c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Kill a friendly unit or gear, :rb_exhaust:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: Kill a friendly unit
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_rune_rainbow::rb_rune_rainbow:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Marai Spire

- official_card: Marai Spire (`play:marai-spire:25523469`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: While you control this battlefield
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: friendly [Repeat] costs cost :rb_energy_1: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: friendly [Repeat] costs cost :rb_energy_1: less
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Repeat]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Marching Orders

- official_card: Marching Orders (`play:marching-orders:57b91f18`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_3:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: They deal damage equal to their Mights to each other
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Mask of Foresight

- official_card: Mask of Foresight (`play:mask-of-foresight:42a36574`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give it +1 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Master Bingwen

- official_card: Master Bingwen (`play:master-bingwen:dc2575fe`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Equip]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Weaponmaster]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia

### [derived-fact] Master Yi, Tempered

- official_card: Master Yi, Tempered (`play:master-yi-tempered:d4d91114`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Level 6][>] I have [Deflect] and [Ganking]. (While you have 6+ XP, opponents must pay :rb_rune_rainbow:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 2 XP
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Level 6][>] I have [Deflect] and [Ganking].
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hunt 2]

### [derived-fact] Master Yi, Unstoppable

- official_card: Master Yi, Unstoppable (`play:master-yi-unstoppable:9fcd6a63`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: I can't be chosen by enemy spells and abilities
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_2::rb_rune_calm: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_2::rb_rune_calm: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_4::rb_rune_calm::rb_rune_calm: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_4::rb_rune_calm::rb_rune_calm: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_6::rb_rune_calm::rb_rune_calm::rb_rune_calm: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_6::rb_rune_calm::rb_rune_calm::rb_rune_calm: less
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Level 3]

### [derived-fact] Mechanized Menace

- official_card: Mechanized Menace (`play:mechanized-menace:1869431c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Your Mechs have [Shield].
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Rumble

### [derived-fact] Meditation

- official_card: Meditation (`play:meditation:11bb62cb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 2
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Mega-Mech

- official_card: Mega-Mech (`play:mega-mech:15c0c127`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mech
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:8
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:7
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bandle City

### [derived-fact] Megatusk

- official_card: Megatusk (`play:megatusk:c62a8b9c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Spend 3 XP
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: Give your units here [Ganking] this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bilgewater

### [derived-fact] Might of Demacia - Starter

- official_card: Might of Demacia - Starter (`play:might-of-demacia-starter:2872a00c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 2
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Garen
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Mind Rune

- official_card: Mind Rune (`play:mind-rune:63eb0fd3`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 1.0; evidence: basic_rune:mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: rune
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind

### [derived-fact] Mindsplitter

- official_card: Mindsplitter (`play:mindsplitter:79ffbec8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: they discard that card
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dragon
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:7
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:7

### [derived-fact] Minefield

- official_card: Minefield (`play:minefield:74a8186e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer here
- predicate `move`; role `payoff_output`; type `movement`; confidence 0.84; evidence: put the top 2 cards of your Main Deck into your trash
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Minotaur Reckoner

- official_card: Minotaur Reckoner (`play:minotaur-reckoner:97352b34`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: Units can't move to base
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Mirror Image

- official_card: Mirror Image (`play:mirror-image:287b0704`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play a ready Reflection unit token to your base
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: Give it [Temporary]
- predicate `copy`; role `state_or_modifier`; type `copy_effect`; confidence 0.82; evidence: It becomes a copy of that unit
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready Reflection unit token to your base
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2

### [derived-fact] Mischievous Marai

- official_card: Mischievous Marai (`play:mischievous-marai:ab1a997e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: deal 2 to an enemy unit here
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Miss Fortune, Buccaneer

- official_card: Miss Fortune, Buccaneer (`play:miss-fortune-buccaneer:462cb81d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play`; role `restriction_or_permission`; type `permission`; confidence 0.82; evidence: You may play me to an open battlefield
- predicate `play`; role `restriction_or_permission`; type `permission`; confidence 0.82; evidence: Friendly units may be played to open battlefields
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Pirate
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Miss Fortune, Captain

- official_card: Miss Fortune, Captain (`play:miss-fortune-captain:a4b3cce5`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_body:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move each turn
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move each turn
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready something else that's exhausted
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ganking]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Mister Root

- official_card: Mister Root (`play:mister-root:b65462c8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move to a battlefield
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_chaos:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move to a battlefield
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 2 XP
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fae
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos

### [derived-fact] Mistfall

- official_card: Mistfall (`play:mistfall:a211d6c8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you buff a friendly unit
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff a friendly unit
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready it
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Mobilize

- official_card: Mobilize (`play:mobilize:4c17ccd4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: Channel 1 rune exhausted
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Monastery of Hirana

- official_card: Monastery of Hirana (`play:monastery-of-hirana:65d270f0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer here
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff to draw 1
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Monch

- official_card: Monch (`play:monch:c2f3fc08`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: unit, I cost :rb_energy_2: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: unit, I cost :rb_energy_2: less
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bandle City

### [derived-fact] Monster Harpoon

- official_card: Monster Harpoon (`play:monster-harpoon:bc55b276`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: deal 4 to it instead
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 2 to a unit at a battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Moonfall

- official_card: Moonfall (`play:moonfall:a866b85d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move up to one enemy unit to that battlefield
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move up to one enemy unit to that battlefield
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give enemy units there -2 :rb_might: this turn
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give enemy units there -2 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos

### [derived-fact] Moonlight Affliction

- official_card: Moonlight Affliction (`play:moonlight-affliction:e327504d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit -10 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:7

### [derived-fact] Morbid Return

- official_card: Morbid Return (`play:morbid-return:977585d2`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `return_to_hand`; role `payoff_output`; type `card_flow`; confidence 0.82; evidence: Return a unit from your trash to your hand
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Mosstomper

- official_card: Mosstomper (`play:mosstomper:24625ebf`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 2 XP
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.84; evidence: I have +1 :rb_might:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Deflect]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hunt 2]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Level 3]

### [derived-fact] Mountain Drake

- official_card: Mountain Drake (`play:mountain-drake:24c1bdea`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dragon
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:9
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:10

### [derived-fact] Mushroom Pouch

- official_card: Mushroom Pouch (`play:mushroom-pouch:c4fd2119`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Mutated Mouser

- official_card: Mutated Mouser (`play:mutated-mouser:40a8b20e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm a defender
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Shield 2] (+2 :rb_might: while I'm a defender.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Shield 2]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Cat
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1

### [derived-fact] Mystic Poro

- official_card: Mystic Poro (`play:mystic-poro:6bc281be`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: You may recycle it
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: look at the top card of your Main Deck
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Vision]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Poro
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2

### [derived-fact] Mystic Reversal

- official_card: Mystic Reversal (`play:mystic-reversal:81f30bae`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `gain_control`; role `event_produced`; type `control_change`; confidence 0.88; evidence: Gain control of a spell
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Nami, Headstrong

- official_card: Nami, Headstrong (`play:nami-headstrong:35c45fd5`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I hold
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.9; evidence: You may pay :rb_rune_calm: as an additional cost to play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: You may pay :rb_rune_calm:
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun] an enemy unit
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready it and [Buff] it
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Stun]
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Buff]

### [derived-fact] Navori Fighting Pit

- official_card: Navori Fighting Pit (`play:navori-fighting-pit:dec2874f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you hold here
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff a unit here
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Navori Scout

- official_card: Navori Scout (`play:navori-scout:fd798736`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Needlessly Large Yordle

- official_card: Needlessly Large Yordle (`play:needlessly-large-yordle:350b3a71`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm a defender
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Shield 5] (+5 :rb_might: while I'm a defender.)
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_2::rb_rune_calm: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_2::rb_rune_calm: less
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Shield 5]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm

### [derived-fact] Nidalee, Cat Form

- official_card: Nidalee, Cat Form (`play:nidalee-cat-form:2d013fb5`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I win a combat
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ambush]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Cat
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ixtal

### [derived-fact] Nilah, Joyful Ascetic

- official_card: Nilah, Joyful Ascetic (`play:nilah-joyful-ascetic:0fc34ea4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_body:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 1 XP
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ganking]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body

### [derived-fact] Nine-Tailed Fox

- official_card: Nine-Tailed Fox (`play:nine-tailed-fox:79e9450e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give it -1 :rb_might: this turn
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ahri
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Nocturne, Horrifying

- official_card: Nocturne, Horrifying (`play:nocturne-horrifying:f83ad418`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `play`; role `restriction_or_permission`; type `permission`; confidence 0.82; evidence: you may play me for :rb_rune_rainbow:
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: you may banish me
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ganking]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Not So Fast

- official_card: Not So Fast (`play:not-so-fast:dd41c965`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `counter`; role `event_produced`; type `produced_event`; confidence 0.9; evidence: Counter an enemy spell or ability that chooses a friendly unit or gear
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Noxian Drummer

- official_card: Noxian Drummer (`play:noxian-drummer:4b6056e8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move to a battlefield
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move to a battlefield
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a 1 :rb_might: Recruit unit token
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Noxian Guillotine

- official_card: Noxian Guillotine (`play:noxian-guillotine:ce06bc82`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.82; evidence: Kill it the next time it takes damage this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Legion]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Darius
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Noxus Hopeful

- official_card: Noxus Hopeful (`play:noxus-hopeful:56b06268`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_2: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_2: less
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Legion]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Noxus Saboteur

- official_card: Noxus Saboteur (`play:noxus-saboteur:d07cbafa`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Hidden]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Trifarian

### [derived-fact] Obelisk of Power

- official_card: Obelisk of Power (`play:obelisk-of-power:32cddf26`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channels 1 rune
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] On the Hunt

- official_card: On the Hunt (`play:on-the-hunt:8a713a40`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: Ready your units
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Sivir
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Orb of Regret

- official_card: Orb of Regret (`play:orb-of-regret:ce5bc32b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit -1 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Order Rune

- official_card: Order Rune (`play:order-rune:0b77d967`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 1.0; evidence: basic_rune:order
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: rune
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order

### [derived-fact] Ornn's Forge

- official_card: Ornn's Forge (`play:ornn-s-forge:0b5db274`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: While you control this battlefield
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.9; evidence: the first friendly non-token gear played each turn costs :rb_energy_1: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: the first friendly non-token gear played each turn costs :rb_energy_1: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: the first friendly non-token gear played each turn costs :rb_energy_1: less
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Ornn, Blacksmith

- official_card: Ornn, Blacksmith (`play:ornn-blacksmith:19ac6d02`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: when I hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: recycle the rest
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: look at the top 4 cards of your Main Deck
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ornn
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5

### [derived-fact] Ornn, Forge God

- official_card: Ornn, Forge God (`play:ornn-forge-god:01d7efe1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect 2] (Opponents must pay :rb_rune_rainbow::rb_rune_rainbow:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.82; evidence: I have +1 :rb_might: for each friendly gear
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Equip]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect 2]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Weaponmaster]

### [derived-fact] Overt Operation

- official_card: Overt Operation (`play:overt-operation:05e09d85`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff to ready it
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff all friendly units
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff gets a +1 :rb_might: buff
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready it
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2

### [derived-fact] Overzealous Fan

- official_card: Overzealous Fan (`play:overzealous-fan:a535bbee`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move an attacking unit to its base
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Pack of Wonders

- official_card: Pack of Wonders (`play:pack-of-wonders:76466a22`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: Return another friendly gear, unit, or facedown card to its owner's hand
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Pakaa Cub

- official_card: Pakaa Cub (`play:pakaa-cub:155110ae`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Cat
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ixtal
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Party Favors

- official_card: Party Favors (`play:party-favors:7ecec395`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channel 1 rune exhausted
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Peak Guardian

- official_card: Peak Guardian (`play:peak-guardian:8e776480`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff me
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff all other friendly units there
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Perched Grimwyrm

- official_card: Perched Grimwyrm (`play:perched-grimwyrm:900974bd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play`; role `restriction_or_permission`; type `permission`; confidence 0.82; evidence: Play me only to a battlefield you conquered this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dragon
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shadow Isles

### [derived-fact] Petal Pixie

- official_card: Petal Pixie (`play:petal-pixie:f551a78c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.82; evidence: I have +1 :rb_might: for each of your units with [Temporary] at my battlefield
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Temporary]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fae
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Petricite Monument

- official_card: Petricite Monument (`play:petricite-monument:5883f7b0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Friendly units have [Deflect]. (Opponents must pay :rb_rune_rainbow:
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.9; evidence: Kill this at the start of its controller's Beginning Phase, before scoring
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.88; evidence: Kill this
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Friendly units have [Deflect].
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Temporary]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Petty Officer

- official_card: Petty Officer (`play:petty-officer:10250d91`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault] (+1 :rb_might: while I'm an attacker.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Pirate
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Pickpocket

- official_card: Pickpocket (`play:pickpocket:98c5987f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `cost_cap_constraint`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: cost no more than :rb_energy_1:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: kill a gear
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a Gold gear token exhausted
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3

### [derived-fact] Piercing Light

- official_card: Piercing Light (`play:piercing-light:93716c6f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_2::rb_rune_fury:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 2 to a unit at a battlefield, then deal 2 to up to one other unit
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Piltover Enforcer

- official_card: Piltover Enforcer (`play:piltover-enforcer:e232b8fc`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer
- predicate `exhaust`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.9; evidence: you may exhaust me
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready a unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Vi
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Pirate's Haven

- official_card: Pirate's Haven (`play:pirate-s-haven:5b01a495`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give it +1 :rb_might: this turn
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready a friendly unit
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Pit Crew

- official_card: Pit Crew (`play:pit-crew:a6eddd77`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bandle City

### [derived-fact] Pit Rookie

- official_card: Pit Rookie (`play:pit-rookie:2e44b9f4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff another friendly unit
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bilgewater

### [derived-fact] Playful Phantom

- official_card: Playful Phantom (`play:playful-phantom:de775024`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Spirit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shadow Isles

### [derived-fact] Plundering Poro

- official_card: Plundering Poro (`play:plundering-poro:3de16b4c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a Gold gear token exhausted
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Poro
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Pirate
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Poppy, Defender of the Meek

- official_card: Poppy, Defender of the Meek (`play:poppy-defender-of-the-meek:689e74c0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `spend`; role `cost_or_requirement`; type `additional_cost`; confidence 0.9; evidence: You may spend 3 XP as an additional cost to play me
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_3: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_3: less
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ambush]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order

### [derived-fact] Poppy, Paragon

- official_card: Poppy, Paragon (`play:poppy-paragon:1f712391`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 3 XP
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Poppy

### [derived-fact] Poro Herder

- official_card: Poro Herder (`play:poro-herder:e38bcca1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff me and draw 1
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Poro Snax

- official_card: Poro Snax (`play:poro-snax:089d7772`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play this
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_energy_1::rb_rune_calm:, :rb_exhaust:, Kill this
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.88; evidence: Kill this
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Portal Rescue

- official_card: Portal Rescue (`play:portal-rescue:bc79c8d4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: Banish a friendly unit
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Possession

- official_card: Possession (`play:possession:3fc2de2b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `gain_control`; role `event_produced`; type `control_change`; confidence 0.88; evidence: Take control of it
- predicate `return_to_hand`; role `event_produced`; type `movement`; confidence 0.82; evidence: recall it
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:8

### [derived-fact] Pouty Poro

- official_card: Pouty Poro (`play:pouty-poro:f8eb50fa`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Poro
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Power Nexus

- official_card: Power Nexus (`play:power-nexus:9604775f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you hold here
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: you may pay :rb_rune_rainbow::rb_rune_rainbow::rb_rune_rainbow::rb_rune_rainbow: to score 1 point
- predicate `score`; role `payoff_output`; type `score_change`; confidence 0.8; evidence: score 1 point
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Premonition

- official_card: Premonition (`play:premonition:af8850f1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 3
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Prepared Neophyte

- official_card: Prepared Neophyte (`play:prepared-neophyte:249233d1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.84; evidence: I have +4 :rb_might:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shadow Isles

### [derived-fact] Pridestalker

- official_card: Pridestalker (`play:pridestalker:fefa8e34`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play a unit
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give a unit +1 :rb_might: this turn
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Rengar

### [derived-fact] Primal Strength

- official_card: Primal Strength (`play:primal-strength:a912a58a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit +7 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Prize of Progress

- official_card: Prize of Progress (`play:prize-of-progress:d5af5239`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +1 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mech
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Piltover

### [derived-fact] Prodigal Explorer

- official_card: Prodigal Explorer (`play:prodigal-explorer:2af5627e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ezreal

### [derived-fact] Production Surge

- official_card: Production Surge (`play:production-surge:6779c2e5`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play a 3 :rb_might: Mech unit token to your base
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: This costs :rb_energy_2: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: This costs :rb_energy_2: less
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Progress Day

- official_card: Progress Day (`play:progress-day:28a28b70`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 4
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Promising Future

- official_card: Promising Future (`play:promising-future:8627cbfb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: recycles the rest
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: banishes one of them
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.8; evidence: each player plays those cards, ignoring Energy costs
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: Each player looks at the top 5 cards of their Main Deck
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Punch First

- official_card: Punch First (`play:punch-first:02f59b2e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit +5 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Purifier

- official_card: Purifier (`play:purifier:3e9bbd4c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.8; evidence: Your Equipment each give [Assault]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Lucian

### [derived-fact] Pyke, Dockside Butcher

- official_card: Pyke, Dockside Butcher (`play:pyke-dockside-butcher:0a7bbbac`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.9; evidence: You may pay :rb_rune_fury: as an additional cost to play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: You may pay :rb_rune_fury:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +2 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]

### [derived-fact] Pyke, Returned

- official_card: Pyke, Returned (`play:pyke-returned:a5329bf7`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Once each turn, when an enemy unit dies while I'm at a battlefield, play a Gold gear token exhausted. (It has "[Reaction][>] Kill this, :rb_exhaust:
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.88; evidence: Kill this
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_rune_rainbow:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a Gold gear token exhausted
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Backline]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Qiyana, Victorious

- official_card: Qiyana, Victorious (`play:qiyana-victorious:ee9243cc`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channel 1 rune exhausted
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ixtal

### [derived-fact] Rabadon's Deathcrown

- official_card: Rabadon's Deathcrown (`play:rabadon-s-deathcrown:2161f7df`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_rainbow:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.88; evidence: Your spells and abilities deal 3 Bonus Damage
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Unique]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind

### [derived-fact] Radiant Dawn

- official_card: Radiant Dawn (`play:radiant-dawn:65ab942b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you stun one or more enemy units
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: stun one or more enemy units
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff a friendly unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Leona
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Raging Firebrand

- official_card: Raging Firebrand (`play:raging-firebrand:0fe72c50`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: the next spell you play this turn costs :rb_energy_5: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: the next spell you play this turn costs :rb_energy_5: less
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dragon
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Raging Soul

- official_card: Raging Soul (`play:raging-soul:8491dead`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: If you've discarded a card this turn, I have [Assault] and [Ganking].
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Spirit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Rally the Troops

- official_card: Rally the Troops (`play:rally-the-troops:bca132d2`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff it
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Ravenbloom Conservatory

- official_card: Ravenbloom Conservatory (`play:ravenbloom-conservatory:388622e7`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: recycle it
- predicate `reveal`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: reveal the top card of your Main Deck
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Ravenbloom Student

- official_card: Ravenbloom Student (`play:ravenbloom-student:ffb7fe9a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play a spell
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +1 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Ravenborn Tome

- official_card: Ravenborn Tome (`play:ravenborn-tome:f46fe953`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.84; evidence: The next spell you play this turn deals 1 Bonus Damage
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Reaver's Row

- official_card: Reaver's Row (`play:reaver-s-row:ba381762`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move a friendly unit here to base
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Rebuke

- official_card: Rebuke (`play:rebuke:5a0612af`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: Return a unit at a battlefield to its owner's hand
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Reckoner's Arena

- official_card: Reckoner's Arena (`play:reckoner-s-arena:0bab9bba`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you hold here
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Recruit (DE)

- official_card: Recruit (DE) (`play:recruit-de:1ce0d3f2`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Recruit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless

### [derived-fact] Recruit (NX)

- official_card: Recruit (NX) (`play:recruit-nx:c7a669c6`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Recruit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless

### [derived-fact] Recruit (ZN)

- official_card: Recruit (ZN) (`play:recruit-zn:24ea9161`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Recruit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless

### [derived-fact] Recruit the Vanguard

- official_card: Recruit the Vanguard (`play:recruit-the-vanguard:bf2595dd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play four 1 :rb_might: Recruit unit tokens
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Recurve Bow

- official_card: Recurve Bow (`play:recurve-bow:e246988b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack or defend
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack or defend
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_fury:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: deal 2 to an enemy unit here
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury

### [derived-fact] Red Brambleback

- official_card: Red Brambleback (`play:red-brambleback:5b4a4085`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_fury:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Buff]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4

### [derived-fact] Reflection

- official_card: Reflection (`play:reflection:46cdd3cb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `copy`; role `state_or_modifier`; type `copy_effect`; confidence 0.82; evidence: I become a copy of something when played
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:0
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless

### [derived-fact] Reinforce

- official_card: Reinforce (`play:reinforce:617f08c4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: Recycle the remaining cards
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: banish a unit from among them
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: Look at the top 5 cards of your Main Deck
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.78; evidence: reducing its cost by :rb_energy_5:
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.78; evidence: reducing its cost by :rb_energy_5:
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Rek'Sai, Breacher

- official_card: Rek'Sai, Breacher (`play:rek-sai-breacher:4e6bb84f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_fury:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault] (+1 :rb_might: while I'm an attacker.)
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Friendly units played from anywhere other than a player's hand have [Accelerate].
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury

### [derived-fact] Rek'Sai, Swarm Queen

- official_card: Rek'Sai, Swarm Queen (`play:rek-sai-swarm-queen:25292fb1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: Recycle the rest
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: banish one
- predicate `reveal`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: reveal the top 2 cards of your Main Deck
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Relentless Pursuit

- official_card: Relentless Pursuit (`play:relentless-pursuit:b9a3c835`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move me to my base
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move a friendly unit
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move a friendly unit
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell

### [derived-fact] Relentless Storm

- official_card: Relentless Storm (`play:relentless-storm:48cdbb7c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `exhaust`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.9; evidence: you may exhaust me
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channel 1 rune exhausted
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Mighty]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Volibear

### [derived-fact] Rell, Magnetic

- official_card: Rell, Magnetic (`play:rell-magnetic:519be01a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `cost_cap_constraint`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: cost no more than :rb_energy_2:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach it to me
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Rell
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus

### [derived-fact] Renata Glasc, Industrialist

- official_card: Renata Glasc, Industrialist (`play:renata-glasc-industrialist:8a112b17`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.94; evidence: Your tokens enter ready
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Renata Glasc

### [derived-fact] Renata Glasc, Mastermind

- official_card: Renata Glasc, Mastermind (`play:renata-glasc-mastermind:fa1087ce`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_energy_1::rb_rune_mind:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_energy_4::rb_rune_mind::rb_rune_mind::rb_rune_mind::rb_rune_mind:, :rb_exhaust:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `score`; role `payoff_output`; type `score_change`; confidence 0.8; evidence: Score 1 point
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4

### [derived-fact] Rengar, Pouncing

- official_card: Rengar, Pouncing (`play:rengar-pouncing:fad9971b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `play`; role `restriction_or_permission`; type `permission`; confidence 0.82; evidence: I can be played to a battlefield you're attacking
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault 2] (+2 :rb_might: while I'm an attacker.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault 2]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Cat
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury

### [derived-fact] Rengar, Trophy Hunter

- official_card: Rengar, Trophy Hunter (`play:rengar-trophy-hunter:70f5a34d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play`; role `restriction_or_permission`; type `permission`; confidence 0.82; evidence: I can be played to a battlefield where there are enemy units (even if you don't have units there)
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ambush]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Cat
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ixtal
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Rengar

### [derived-fact] Rengar, Unseen

- official_card: Rengar, Unseen (`play:rengar-unseen:d346fcc8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_fury:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault 2] (+2 :rb_might: while I'm an attacker.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault 2]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]

### [derived-fact] Repulse

- official_card: Repulse (`play:repulse:d0c3e7ae`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `counter`; role `event_produced`; type `produced_event`; confidence 0.9; evidence: Counter an enemy spell or ability that chooses it and no other friendly unit
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Retreat

- official_card: Retreat (`play:retreat:3a2bb4a4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channels 1 rune exhausted
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: Return a friendly unit to its owner's hand
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Revna the Lorekeeper

- official_card: Revna the Lorekeeper (`play:revna-the-lorekeeper:ee7db6c9`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play a spell
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ganking]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:7
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Rhasa the Sunderer

- official_card: Rhasa the Sunderer (`play:rhasa-the-sunderer:f5bfd950`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_1: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_1: less
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Spirit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:10

### [derived-fact] Ribbon Dancer

- official_card: Ribbon Dancer (`play:ribbon-dancer:c38eb9af`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move to a battlefield
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move to a battlefield
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give another friendly unit +1 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Ride the Wind

- official_card: Ride the Wind (`play:ride-the-wind:67b5c5a2`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move a friendly unit and ready it
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready it
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Rift Herald

- official_card: Rift Herald (`play:rift-herald:22b30b86`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move to a battlefield
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: Recycle the rest
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move to a battlefield
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move to a battlefield
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: Play a unit from your hand to your base, ignoring its Energy cost
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: look at the top 3 cards of your Main Deck
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]

### [derived-fact] Right of Conquest

- official_card: Right of Conquest (`play:right-of-conquest:87ead7a5`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1 for each battlefield you or allies control
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Riposte

- official_card: Riposte (`play:riposte:d8988aaf`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `counter`; role `event_produced`; type `produced_event`; confidence 0.9; evidence: Counter that spell
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fiora
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Ripper's Bay

- official_card: Ripper's Bay (`play:ripper-s-bay:de3af236`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channel 1 rune exhausted
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Riptide Rex

- official_card: Riptide Rex (`play:riptide-rex:56869e3e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: deal 6 to an enemy unit at a battlefield
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Pirate
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Rocket Barrage

- official_card: Rocket Barrage (`play:rocket-barrage:1ee001f2`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_4::rb_rune_mind:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 4 to a unit in a base
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: Kill a gear
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Rockfall Path

- official_card: Rockfall Path (`play:rockfall-path:f690a406`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.88; evidence: Units can't be played here
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Royal Entourage

- official_card: Royal Entourage (`play:royal-entourage:05b1f43c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready or exhaust a legend
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shurima
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Royal Guard

- official_card: Royal Guard (`play:royal-guard:0ffb616a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a 2 :rb_might: Sand Soldier unit token
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shurima
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Ruin Runner

- official_card: Ruin Runner (`play:ruin-runner:64ad7ee0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: I can't be chosen by enemy spells and abilities
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shurima
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Ruined Rex

- official_card: Ruined Rex (`play:ruined-rex:6ba10a89`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 4 to an enemy unit
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Rumble, Hotheaded

- official_card: Rumble, Hotheaded (`play:rumble-hotheaded:118ba12c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: play a Mech from your trash
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: recycle another friendly unit
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Your Mechs each have [Assault].
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.78; evidence: Reduce its Energy cost by the Might of the unit you recycled
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mech

### [derived-fact] Rumble, Scrapper

- official_card: Rumble, Scrapper (`play:rumble-scrapper:c635249a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I hold
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a 3 :rb_might: Mech unit token to your base
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mech
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Rumble
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4

### [derived-fact] Rune Prison

- official_card: Rune Prison (`play:rune-prison:bbbc1f6b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun a unit
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Sabotage

- official_card: Sabotage (`play:sabotage:5555f7cd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: recycle that card
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Sacred Shears

- official_card: Sacred Shears (`play:sacred-shears:c89b9046`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_order:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order

### [derived-fact] Sacrifice

- official_card: Sacrifice (`play:sacrifice:76764d53`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 2
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channel 1 rune exhausted
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Mighty]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Safety Inspector

- official_card: Safety Inspector (`play:safety-inspector:f2278612`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `spend`; role `cost_or_requirement`; type `additional_cost`; confidence 0.9; evidence: You may spend 3 XP as an additional cost to play me
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.9; evidence: If you paid my additional cost, you don't kill a unit this way
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: kill one of their units
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: each player must kill one of their units
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle

### [derived-fact] Sai Scout

- official_card: Sai Scout (`play:sai-scout:7e379c86`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `play`; role `restriction_or_permission`; type `permission`; confidence 0.82; evidence: You may play me to an open battlefield
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: You may recycle it
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: look at the top card of your Main Deck
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Vision]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5

### [derived-fact] Salvage

- official_card: Salvage (`play:salvage:52f03a91`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: kill up to one gear
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Sandshifter

- official_card: Sandshifter (`play:sandshifter:aab43494`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: kill an enemy unit
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shurima
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Scorchclaw

- official_card: Scorchclaw (`play:scorchclaw:d9cf795e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 2 XP
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.84; evidence: I have +1 :rb_might:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hunt 2]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Level 3]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dog

### [derived-fact] Scorn of the Moon

- official_card: Scorn of the Moon (`play:scorn-of-the-moon:16134ae5`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Reaction][>] :rb_exhaust:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_energy_1:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Diana
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Scrapheap

- official_card: Scrapheap (`play:scrapheap:8f6489fe`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Scrapyard Champion

- official_card: Scrapyard Champion (`play:scrapyard-champion:c4c51482`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: discard 2
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 2
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Legion]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mech
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5

### [derived-fact] Scrutinizing Sergeant

- official_card: Scrutinizing Sergeant (`play:scrutinizing-sergeant:c62ab577`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 1 XP
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Elite
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Scryer's Bloom

- official_card: Scryer's Bloom (`play:scryer-s-bloom:cf6902d1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Kill this, :rb_energy_1:, :rb_exhaust:
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.88; evidence: Kill this
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: Recycle any of them
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: Gain 1 XP
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: look at the top two cards of your Main Deck
- predicate `enter_exhausted`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: This enters exhausted
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Predict 2]

### [derived-fact] Scuttle Crab

- official_card: Scuttle Crab (`play:scuttle-crab:8c3955ab`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: Gain 1 XP
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:0

### [derived-fact] Sea Monkey

- official_card: Sea Monkey (`play:sea-monkey:7534b7be`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.9; evidence: You may pay :rb_energy_1: as an additional cost to play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: You may pay :rb_energy_1:
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff me
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff if I don't already have one
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give me a +1 :rb_might:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body

### [derived-fact] Seal of Discord

- official_card: Seal of Discord (`play:seal-of-discord:2f1c93d8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_rune_chaos:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:0

### [derived-fact] Seal of Focus

- official_card: Seal of Focus (`play:seal-of-focus:46cd31aa`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_rune_calm:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:0

### [derived-fact] Seal of Insight

- official_card: Seal of Insight (`play:seal-of-insight:50c75766`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_rune_mind:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:0

### [derived-fact] Seal of Rage

- official_card: Seal of Rage (`play:seal-of-rage:066d5ae8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_rune_fury:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:0

### [derived-fact] Seal of Strength

- official_card: Seal of Strength (`play:seal-of-strength:57429223`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_rune_body:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:0

### [derived-fact] Seal of Unity

- official_card: Seal of Unity (`play:seal-of-unity:f6d58275`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_rune_order:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:0

### [derived-fact] Seat of Power

- official_card: Seat of Power (`play:seat-of-power:d76f503a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer here
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1 for each other battlefield you or allies control
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Sentinel Adept

- official_card: Sentinel Adept (`play:sentinel-adept:7a25c078`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Equip]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Weaponmaster]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3

### [derived-fact] Serrated Dirk

- official_card: Serrated Dirk (`play:serrated-dirk:eb284704`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_fury:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault 2] (+2 :rb_might: while I'm an attacker.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault 2]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury

### [derived-fact] Sett, Brawler

- official_card: Sett, Brawler (`play:sett-brawler:24087646`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: when I conquer
- predicate `spend`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.84; evidence: Spend my buff:
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff me
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give me +4 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Sett
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia

### [derived-fact] Sett, Kingpin

- official_card: Sett, Kingpin (`play:sett-kingpin:72c3c44d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.82; evidence: I get +1 :rb_might: for each buffed friendly unit at my battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Sett
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Shadow

- official_card: Shadow (`play:shadow:c3ae12be`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Action][>] :rb_energy_1::rb_rune_rainbow:, :rb_exhaust:
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun] an enemy unit attacking here
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Stun]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Vex
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm

### [derived-fact] Shadow Watcher

- official_card: Shadow Watcher (`play:shadow-watcher:b8aac470`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Shadow's Call

- official_card: Shadow's Call (`play:shadow-s-call:21fa8205`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 2
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: Give it [Temporary]
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Temporary]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Shakedown

- official_card: Shakedown (`play:shakedown:3fd894ed`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 6 to it unless its controller has you draw 2
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 2
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Shard of Undoing

- official_card: Shard of Undoing (`play:shard-of-undoing:0663c06c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: kill one of their units
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Sharkling

- official_card: Sharkling (`play:sharkling:001032ef`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_fury:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault 4] (+4 :rb_might: while I'm an attacker.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault 4]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1

### [derived-fact] Shen, Kinkou

- official_card: Shen, Kinkou (`play:shen-kinkou:e3f28633`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm a defender
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Shield 2] (+2 :rb_might: while I'm a defender.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Shield 2]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shen
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order

### [derived-fact] Shepherd's Heirloom

- official_card: Shepherd's Heirloom (`play:shepherd-s-heirloom:2c7879d8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play this
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] — Spend 1 XP (Pay the cost
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 1 XP
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Shipyard Skulker

- official_card: Shipyard Skulker (`play:shipyard-skulker:1221f795`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Pirate
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bilgewater

### [derived-fact] Show of Strength

- official_card: Show of Strength (`play:show-of-strength:08603631`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1 for each of your [Mighty] units
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Mighty]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Showstopper

- official_card: Showstopper (`play:showstopper:ebd23267`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: Buff a friendly unit in your base
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move it to a battlefield
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Sett
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Shurelya's Requiem

- official_card: Shurelya's Requiem (`play:shurelya-s-requiem:0ba2de39`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play this
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_rainbow:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Your units here have [Ganking].
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready your units
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Unique]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear

### [derived-fact] Sigil of the Storm

- official_card: Sigil of the Storm (`play:sigil-of-the-storm:49065044`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer here
- predicate `recycle`; role `event_produced`; type `resource_change`; confidence 0.84; evidence: recycle one of your runes
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Simian Ancestor

- official_card: Simian Ancestor (`play:simian-ancestor:001a8a1c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff me
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Singularity

- official_card: Singularity (`play:singularity:10e85634`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 6 to each of up to two units
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Sinister Poro

- official_card: Sinister Poro (`play:sinister-poro:97b02b86`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move an enemy unit here to its base
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Poro
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Siphon Power

- official_card: Siphon Power (`play:siphon-power:95a5bede`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give friendly units there +1 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Viktor
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Sivir, Ambitious

- official_card: Sivir, Ambitious (`play:sivir-ambitious:74068514`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect 2] (Opponents must pay :rb_rune_rainbow::rb_rune_rainbow:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: deal that much to an enemy unit
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect 2]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Sivir
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:7

### [derived-fact] Sivir, Mercenary

- official_card: Sivir, Mercenary (`play:sivir-mercenary:c937a7c0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_chaos:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.84; evidence: I have +2 :rb_might:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Ganking]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Sivir

### [derived-fact] Sky Splitter

- official_card: Sky Splitter (`play:sky-splitter:98da3e56`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 5 to a unit at a battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:8

### [derived-fact] Skyfall of Areion

- official_card: Skyfall of Areion (`play:skyfall-of-areion:91394768`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_energy_1::rb_rune_fury:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Equipment
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might_bonus:2

### [derived-fact] Skyward Strike

- official_card: Skyward Strike (`play:skyward-strike:06248a21`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move an enemy unit
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun] an enemy unit
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Stun]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Level 6]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Smite

- official_card: Smite (`play:smite:c152afc9`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 3 to a unit at a battlefield
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: banish it instead
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Smoke and Mirrors

- official_card: Smoke and Mirrors (`play:smoke-and-mirrors:e4d957f9`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move each to the other's location
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Smoke Screen

- official_card: Smoke Screen (`play:smoke-screen:213b4638`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit -4 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Sneaky Deckhand

- official_card: Sneaky Deckhand (`play:sneaky-deckhand:dc110592`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play`; role `restriction_or_permission`; type `permission`; confidence 0.82; evidence: You may play me to an open battlefield
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Pirate
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bilgewater

### [derived-fact] Soaring Scout

- official_card: Soaring Scout (`play:soaring-scout:76203084`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: Channel 1 rune exhausted
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bird
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Solari Chief

- official_card: Solari Chief (`play:solari-chief:feb4c25c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: stun it
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mount Targon

### [derived-fact] Solari Shieldbearer

- official_card: Solari Shieldbearer (`play:solari-shieldbearer:04893dcd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: stun a unit
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mount Targon

### [derived-fact] Solari Shrine

- official_card: Solari Shrine (`play:solari-shrine:78018cfd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Sona, Harmonious

- official_card: Sona, Harmonious (`play:sona-harmonious:0b54e635`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready up to 4 friendly runes
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Sona
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Soraka, Wanderer

- official_card: Soraka, Wanderer (`play:soraka-wanderer:81c0ff4a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `prevent`; role `restriction_or_permission`; type `replacement_effect`; confidence 0.86; evidence: If another unit you control here would die, if it has less Might than me, instead heal it, exhaust it, and recall it
- predicate `return_to_hand`; role `event_produced`; type `movement`; confidence 0.82; evidence: recall it
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Soraka
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Soul Harvest

- official_card: Soul Harvest (`play:soul-harvest:0f4643e7`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.84; evidence: Kill a unit at a battlefield
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Soul Shepherd

- official_card: Soul Shepherd (`play:soul-shepherd:b54f4f22`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: Your token units have +1 :rb_might:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shadow Isles

### [derived-fact] Soul Sword

- official_card: Soul Sword (`play:soul-sword:60beff9b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_calm:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.84; evidence: I have an additional +1 :rb_might:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Level 3]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Soulgorger

- official_card: Soulgorger (`play:soulgorger:4d8dee62`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: play me, you may play a unit from your trash, ignoring its Energy cost
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Spirit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:8

### [derived-fact] Spectral Centaur

- official_card: Spectral Centaur (`play:spectral-centaur:11503a54`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When another friendly unit dies
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +2 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Spirit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shadow Isles

### [derived-fact] Spectral Matron

- official_card: Spectral Matron (`play:spectral-matron:4cee4063`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `cost_cap_constraint`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: costing no more than :rb_energy_3: and
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: play me, you may play a unit costing no more than :rb_energy_3: and no more than :rb_rune_rainbow: from your trash, ignoring its cost
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Spirit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2

### [derived-fact] Spinning Axe

- official_card: Spinning Axe (`play:spinning-axe:54c823a0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play it
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_rainbow:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: attach it to a unit you control
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Quick-Draw]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Temporary]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear

### [derived-fact] Spirit Wheel

- official_card: Spirit Wheel (`play:spirit-wheel:ff23b094`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Spirit's Refuge

- official_card: Spirit's Refuge (`play:spirit-s-refuge:319db174`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play this
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Friendly buffed units have [Deflect] if they didn't already. (Opponents must pay :rb_rune_rainbow:
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff a friendly unit
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Friendly buffed units have [Deflect] if they didn't already.
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Spoils of War

- official_card: Spoils of War (`play:spoils-of-war:8bed8853`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 2
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: enemy unit has died this turn, this costs :rb_energy_2: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: enemy unit has died this turn, this costs :rb_energy_2: less
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Sprite

- official_card: Sprite (`play:sprite:6f9e6c49`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.9; evidence: Kill me at the start of your Beginning Phase, before scoring
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Temporary]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fae
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless

### [derived-fact] Sprite Burst

- official_card: Sprite Burst (`play:sprite-burst:2dd1c3cb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play two ready 3 :rb_might: Sprite unit tokens with [Temporary]
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready 3 :rb_might: Sprite unit tokens with [Temporary]
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Temporary]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Sprite Call

- official_card: Sprite Call (`play:sprite-call:160152fa`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play a ready 3 :rb_might: Sprite unit token with [Temporary]
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready 3 :rb_might: Sprite unit token with [Temporary]
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Temporary]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell

### [derived-fact] Sprite Fountain

- official_card: Sprite Fountain (`play:sprite-fountain:c26beabb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play this
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When this dies
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.9; evidence: Kill this at the start of its controller's Beginning Phase, before scoring
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.88; evidence: Kill this
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a ready 3 :rb_might: Sprite unit token with [Temporary] to your base
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: Repeat this gear's play effect
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready 3 :rb_might: Sprite unit token with [Temporary] to your base
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Temporary]

### [derived-fact] Sprite Mother

- official_card: Sprite Mother (`play:sprite-mother:ff918cbf`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a ready 3 :rb_might: Sprite unit token with [Temporary]
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready 3 :rb_might: Sprite unit token with [Temporary] here
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Temporary]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fae
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3

### [derived-fact] Sprite Queen

- official_card: Sprite Queen (`play:sprite-queen:2c1926cf`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a ready 3 :rb_might: Sprite unit token with [Temporary] to your base
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready 3 :rb_might: Sprite unit token with [Temporary] to your base
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Temporary]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fae
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia

### [derived-fact] Square Up

- official_card: Square Up (`play:square-up:eba28c69`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while it's an attacker
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: Discard 1
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: Give a unit [Assault 4] this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Stacked Deck

- official_card: Stacked Deck (`play:stacked-deck:c3510c3a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: recycle the rest
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: Look at the top 3 cards of your Main Deck
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Stalking Wolf

- official_card: Stalking Wolf (`play:stalking-wolf:39c96cca`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play`; role `restriction_or_permission`; type `permission`; confidence 0.82; evidence: You may play me to its battlefield (even if you don't have other units there)
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ambush]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dog
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Stalwart Poro

- official_card: Stalwart Poro (`play:stalwart-poro:657971c8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm a defender
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Shield] (+1 :rb_might: while I'm a defender.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Shield]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Poro
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Stand United

- official_card: Stand United (`play:stand-united:ae922aa1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: Buff a friendly unit
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give an additional +1 :rb_might:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Star Spring

- official_card: Star Spring (`play:star-spring:2d2df5e8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move another unit they control here to its base
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Star-Crossed

- official_card: Star-Crossed (`play:star-crossed:1c3f4923`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: Return a friendly unit and an enemy unit to their owners' hands
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Stare Down

- official_card: Stare Down (`play:stare-down:9a0e9249`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move all enemy units at that battlefield with less Might than the chosen unit to their base
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: Gain 1 XP
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Starhound

- official_card: Starhound (`play:starhound:5953bff7`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: play me, return a Bird, Cat, Dog, or Poro from your trash to your hand
- predicate `return_to_hand`; role `payoff_output`; type `card_flow`; confidence 0.82; evidence: return a Bird, Cat, Dog, or Poro from your trash to your hand
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dog
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Startipped Peak

- official_card: Startipped Peak (`play:startipped-peak:4c2100db`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you hold here
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channel 1 rune exhausted
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Stealthy Pursuer

- official_card: Stealthy Pursuer (`play:stealthy-pursuer:6eff10d8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.8; evidence: I may be moved with it
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shurima
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Stellacorn Herder

- official_card: Stellacorn Herder (`play:stellacorn-herder:cf7a132c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mount Targon

### [derived-fact] Sterak's Gage

- official_card: Sterak's Gage (`play:sterak-s-gage:c69f5b35`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play it
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_calm:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: attach it to a unit you control
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Quick-Draw]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm

### [derived-fact] Stormbringer

- official_card: Stormbringer (`play:stormbringer:1439dc92`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move your unit there
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: Deal damage equal to its Might to all enemy units at a battlefield, then move your unit there
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Volibear

### [derived-fact] Stormclaw Ursine

- official_card: Stormclaw Ursine (`play:stormclaw-ursine:c5c9f433`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channel 1 rune exhausted
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:7
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Freljord

### [derived-fact] Strike Down

- official_card: Strike Down (`play:strike-down:ba0c50a1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `detach`; role `event_produced`; type `produced_event`; confidence 0.82; evidence: detach an Equipment from it
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: It deals damage equal to its Might to an enemy unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Stupefy

- official_card: Stupefy (`play:stupefy:4d766719`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit -1 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Sudden Storm

- official_card: Sudden Storm (`play:sudden-storm:d2a1f0ab`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: deal 4 to it instead
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 2 to a unit at a battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Sumpworks Map

- official_card: Sumpworks Map (`play:sumpworks-map:0062f880`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.9; evidence: Kill this at the start of its controller's Beginning Phase, before scoring
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.88; evidence: Kill this
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Temporary]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Sun Disc

- official_card: Sun Disc (`play:sun-disc:348149db`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Legion]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Sunken Temple

- official_card: Sunken Temple (`play:sunken-temple:689eb488`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer here
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Mighty]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Sunlit Guardian

- official_card: Sunlit Guardian (`play:sunlit-guardian:aa43e5b3`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm a defender
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Shield] (+1 :rb_might: while I'm a defender.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Shield]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shurima

### [derived-fact] Super Mega Death Rocket!

- official_card: Super Mega Death Rocket! (`play:super-mega-death-rocket:c9c9b003`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 5 to a unit
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: discard 1
- predicate `return_to_hand`; role `payoff_output`; type `card_flow`; confidence 0.82; evidence: return this from your trash to your hand
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Jinx
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos

### [derived-fact] Svellsongur

- official_card: Svellsongur (`play:svellsongur:fe56614e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_energy_1::rb_rune_calm:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `copy`; role `state_or_modifier`; type `copy_effect`; confidence 0.84; evidence: As this is attached to a unit, copy that unit's text to this Equipment's effect text for as long as this is attached to it
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Swift Scout

- official_card: Swift Scout (`play:swift-scout:66b43574`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: You may pay :rb_energy_1:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_energy_1:, :rb_exhaust:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Hidden]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Teemo
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Switcheroo

- official_card: Switcheroo (`play:switcheroo:fd706962`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.82; evidence: Swap the Might of two units at the same battlefield this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Symbol of the Solari

- official_card: Symbol of the Solari (`play:symbol-of-the-solari:94d6b92b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `return_to_hand`; role `event_produced`; type `movement`; confidence 0.82; evidence: recall ALL units instead
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Syndra, Transcendent

- official_card: Syndra, Transcendent (`play:syndra-transcendent:61065ad6`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: While I'm in a showdown, your spells have [Repeat] :rb_energy_2::rb_rune_chaos:.
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Syndra
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Tactical Retreat

- official_card: Tactical Retreat (`play:tactical-retreat:de2f7365`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `prevent`; role `restriction_or_permission`; type `replacement_effect`; confidence 0.88; evidence: The next time it would die this turn, heal it, exhaust it, and recall it instead
- predicate `return_to_hand`; role `event_produced`; type `movement`; confidence 0.82; evidence: recall it instead
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Targon's Peak

- official_card: Targon's Peak (`play:targon-s-peak:d664116d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer here
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready up to 2 runes at the end of this turn
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Targonian Visionary

- official_card: Targonian Visionary (`play:targonian-visionary:c86c8a64`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.84; evidence: I have +4 :rb_might:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Level 11]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Mount Targon

### [derived-fact] Taric, Protector

- official_card: Taric, Protector (`play:taric-protector:4997197e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm a defender
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Shield] (+1 :rb_might: while I'm a defender.)
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Other friendly units here have [Shield].
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Shield]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Taric

### [derived-fact] Tasty Faefolk

- official_card: Tasty Faefolk (`play:tasty-faefolk:1c477fea`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_calm:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: Channel 2 runes exhausted
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fae
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Teemo, Scout

- official_card: Teemo, Scout (`play:teemo-scout:a39da794`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give me +3 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Teemo
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle

### [derived-fact] Teemo, Strategist

- official_card: Teemo, Strategist (`play:teemo-strategist:6c7b5feb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 1 to that unit for each card with [Hidden] revealed this way, then recycle the revealed cards
- predicate `reveal`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: reveal the top 5 cards of your Main Deck
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Teemo

### [derived-fact] Temporal Portal

- official_card: Temporal Portal (`play:temporal-portal:f09c14c4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_rune_rainbow:, :rb_exhaust:
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: Give the next spell you play this turn [Repeat] equal to its cost
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Temptation

- official_card: Temptation (`play:temptation:3963c47d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_2:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move an enemy unit to a location where there's a unit with the same controller
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] The Academy

- official_card: The Academy (`play:the-academy:f9fe7741`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you hold here
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: give your next spell this turn [Repeat] equal to its base cost
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] The Arena's Greatest

- official_card: The Arena's Greatest (`play:the-arena-s-greatest:96ce67dc`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `score`; role `payoff_output`; type `score_change`; confidence 0.8; evidence: gains 1 point
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] The Boss

- official_card: The Boss (`play:the-boss:0851aa4f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff to heal it
- predicate `return_to_hand`; role `event_produced`; type `movement`; confidence 0.82; evidence: recall it instead
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Sett
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] The Candlelit Sanctum

- official_card: The Candlelit Sanctum (`play:the-candlelit-sanctum:c79c6213`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer here
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: You may recycle one or both of them
- predicate `look`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: look at the top two cards of your Main Deck
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] The Dreaming Tree

- official_card: The Dreaming Tree (`play:the-dreaming-tree:fa3a09f4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] The Grand Plaza

- official_card: The Grand Plaza (`play:the-grand-plaza:ac961395`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you hold here
- predicate `score`; role `payoff_output`; type `score_change`; confidence 0.82; evidence: you win the game
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] The Harrowing

- official_card: The Harrowing (`play:the-harrowing:f22276b9`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: Play a unit from your trash, ignoring its Energy cost
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] The List

- official_card: The List (`play:the-list:dc6594e5`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give a unit with the named tag -2 :rb_might: this turn
- predicate `choose`; role `targeting_or_scope`; type `target_scope`; confidence 0.82; evidence: As you play this, name a tag
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] The Papertree

- official_card: The Papertree (`play:the-papertree:aa75cb67`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you hold here
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channels 1 rune exhausted
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] The Ruination

- official_card: The Ruination (`play:the-ruination:ae33fee4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.84; evidence: Kill all units
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:9

### [derived-fact] The Syren

- official_card: The Syren (`play:the-syren:f02b2bcf`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_energy_1:, :rb_exhaust:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move a friendly unit at a battlefield to its base
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] The Zero Drive

- official_card: The Zero Drive (`play:the-zero-drive:0051e34a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_energy_1::rb_rune_mind:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_energy_3::rb_rune_mind:, Banish this
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: Banish this: Play all units banished with this
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear

### [derived-fact] Thermo Beam

- official_card: Thermo Beam (`play:thermo-beam:55f7b6b8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.84; evidence: Kill all gear
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Thousand-Tailed Watcher

- official_card: Thousand-Tailed Watcher (`play:thousand-tailed-watcher:a53ad2a2`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Accelerate] (You may pay :rb_energy_1::rb_rune_mind:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give enemy units -3 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Accelerate]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:7

### [derived-fact] Thrill of the Hunt

- official_card: Thrill of the Hunt (`play:thrill-of-the-hunt:9a0bd883`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: Banish a friendly unit
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Rengar
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Thwonk!

- official_card: Thwonk! (`play:thwonk:9757af12`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_2:
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun an attacking unit
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Tianna Crownguard

- official_card: Tianna Crownguard (`play:tianna-crownguard:2a0d765b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: opponents can't gain points
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Elite
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2

### [derived-fact] Tibbers

- official_card: Tibbers (`play:tibbers:9ea97f77`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: deal 3 to all units at battlefields
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Annie
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:7
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2

### [derived-fact] Tideturner

- official_card: Tideturner (`play:tideturner:2cc456e0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move me to its location and it to my original location
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move me to its location and it to my original location
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2

### [derived-fact] Time Warp

- official_card: Time Warp (`play:time-warp:c0318408`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: Banish this
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:10

### [derived-fact] Towering Combatant

- official_card: Towering Combatant (`play:towering-combatant:dfd72478`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm a defender
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Shield 2] (+2 :rb_might: while I'm a defender.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Shield 2]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shurima

### [derived-fact] Towering Pairofant

- official_card: Towering Pairofant (`play:towering-pairofant:4a9bbd1a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault] (+1 :rb_might: while I'm an attacker.)
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shurima

### [derived-fact] Trapping Grounds

- official_card: Trapping Grounds (`play:trapping-grounds:0c4aa341`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer here
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a 1 :rb_might: Bird unit token with [Deflect]
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Deflect]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Traveling Merchant

- official_card: Traveling Merchant (`play:traveling-merchant:1df2cfdb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: discard 1
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bilgewater

### [derived-fact] Treasure Hoard

- official_card: Treasure Hoard (`play:treasure-hoard:8ac85843`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer here
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a Gold gear token exhausted
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Treasure Hunter

- official_card: Treasure Hunter (`play:treasure-hunter:37ac77e5`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I move
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a Gold gear token exhausted
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shurima
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Treasure Trove

- official_card: Treasure Trove (`play:treasure-trove:b3c54260`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When this leaves the board
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_rune_chaos:, :rb_exhaust:
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.88; evidence: Kill this
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channel 1 rune exhausted
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Trevor Snoozebottom

- official_card: Trevor Snoozebottom (`play:trevor-snoozebottom:e87e027c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I hold
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm a defender
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a ready 3 :rb_might: Sprite unit token with [Temporary]
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Shield] (+1 :rb_might: while I'm a defender.)
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready 3 :rb_might: Sprite unit token with [Temporary] here
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Temporary]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Shield]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Tricksy Tentacles

- official_card: Tricksy Tentacles (`play:tricksy-tentacles:121533c8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move any number of enemy units with the same controller and a total Might of 8 or less to a single location
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Trifarian Gloryseeker

- official_card: Trifarian Gloryseeker (`play:trifarian-gloryseeker:4d4b10a3`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff me
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Legion]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Trifarian War Camp

- official_card: Trifarian War Camp (`play:trifarian-war-camp:2be76ba5`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: Units here have +1 :rb_might:
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Trinity Force

- official_card: Trinity Force (`play:trinity-force:4d00eede`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I hold
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_body:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `score`; role `payoff_output`; type `score_change`; confidence 0.8; evidence: score 1 point
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Trove Golem

- official_card: Trove Golem (`play:trove-golem:51aaa475`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play four Gold gear tokens exhausted
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:9
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:8
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Freljord

### [derived-fact] Trusty Ramhound

- official_card: Trusty Ramhound (`play:trusty-ramhound:37e5523b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.84; evidence: I have +1 :rb_might:
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: While you have another unit here, I have +1 :rb_might:
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dog
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Elite
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia

### [derived-fact] Tryndamere, Barbarian

- official_card: Tryndamere, Barbarian (`play:tryndamere-barbarian:18a0571c`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `score`; role `payoff_output`; type `score_change`; confidence 0.8; evidence: score 1 point
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:8
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:7
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Freljord

### [derived-fact] Turn to Dust

- official_card: Turn to Dust (`play:turn-to-dust:4f8c78cc`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: Give a gear [Temporary]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Twisted Fate, Gambler

- official_card: Twisted Fate, Gambler (`play:twisted-fate-gambler:045bbc7b`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_rune_fury:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_rune_mind:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_rune_order:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: recycle it
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: then recycle it
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 2 to an enemy unit here and 1 to all other enemy units here
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun an enemy unit

### [derived-fact] Udyr, Wildman

- official_card: Udyr, Wildman (`play:udyr-wildman:2c26ef78`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `spend`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.84; evidence: Spend my buff:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 2 to a unit at a battlefield
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun a unit at a battlefield
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: Ready me
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: Give me [Ganking] this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Udyr

### [derived-fact] Ultrasoft Poro

- official_card: Ultrasoft Poro (`play:ultrasoft-poro:31a30f68`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Deflect]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Poro
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Freljord

### [derived-fact] Unchecked Power

- official_card: Unchecked Power (`play:unchecked-power:7ccc1c77`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: deal 12 to ALL units at battlefields
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:7

### [derived-fact] Undercover Agent

- official_card: Undercover Agent (`play:undercover-agent:dc3b994e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: Discard 2
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 2
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Undertitan

- official_card: Undertitan (`play:undertitan:8a0db123`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_energy_2:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give your other units +2 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Undying Legion

- official_card: Undying Legion (`play:undying-legion:a4cbdc79`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: You may play me from your trash for :rb_energy_3::rb_rune_fury:
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: You may play me from your trash for :rb_energy_3::rb_rune_fury:
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Legion]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Spirit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Undying Loyalty

- official_card: Undying Loyalty (`play:undying-loyalty:2cf4bd34`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `cost_cap_constraint`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: cost no more than :rb_energy_2: and
- predicate `play`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: Play a unit with cost no more than :rb_energy_2: and no more than :rb_rune_rainbow: from your trash, ignoring its cost
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: This costs :rb_energy_2: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: This costs :rb_energy_2: less
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Unforgiven

- official_card: Unforgiven (`play:unforgiven:86e82c99`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_energy_2:, :rb_exhaust:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move a friendly unit to or from its base
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yasuo
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Unlicensed Armory

- official_card: Unlicensed Armory (`play:unlicensed-armory:c5b38ea1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Discard 1, :rb_exhaust:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: you may pay :rb_rune_fury: to heal it, exhaust it, and recall it instead
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: Discard 1
- predicate `return_to_hand`; role `event_produced`; type `movement`; confidence 0.82; evidence: recall it instead
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Unsung Hero

- official_card: Unsung Hero (`play:unsung-hero:12083b84`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 2
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Mighty]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Elite
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2

### [derived-fact] Unyielding Spirit

- official_card: Unyielding Spirit (`play:unyielding-spirit:672c2b35`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.9; evidence: Prevent all spell and ability damage this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Upstage Comedy

- official_card: Upstage Comedy (`play:upstage-comedy:5d2e4c5f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `additional_cost`; confidence 0.88; evidence: [Repeat] :rb_energy_2:
- predicate `repeat_effect`; role `payoff_output`; type `payoff`; confidence 0.88; evidence: repeat this spell's effect
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: Ready a unit
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Repeat]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Valley of Idols

- official_card: Valley of Idols (`play:valley-of-idols:988d52df`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When a player plays a unit
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: they may pay :rb_energy_1: to [Buff] it
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Buff]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Vanguard Armory

- official_card: Vanguard Armory (`play:vanguard-armory:e2e15b83`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_exhaust:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play three 1 :rb_might: Recruit unit tokens
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:7

### [derived-fact] Vanguard Attendant

- official_card: Vanguard Attendant (`play:vanguard-attendant:326a457a`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Elite
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6

### [derived-fact] Vanguard Captain

- official_card: Vanguard Captain (`play:vanguard-captain:c9c1c80f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play two 1 :rb_might: Recruit unit tokens
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Legion]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Elite
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Vanguard Helm

- official_card: Vanguard Helm (`play:vanguard-helm:a8fd6126`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When a buffed friendly unit dies
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff another friendly unit
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Vanguard Sergeant

- official_card: Vanguard Sergeant (`play:vanguard-sergeant:646780d9`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Elite
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Vault Breaker

- official_card: Vault Breaker (`play:vault-breaker:77a4fa2f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while it's an attacker
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: Give a unit [Assault 2] and [Ganking] this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Vaults of Helia

- official_card: Vaults of Helia (`play:vaults-of-helia:1e3f93ce`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you hold here
- predicate `increase_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: cost :rb_energy_1: more to play this turn
- predicate `increase_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: cost :rb_energy_1: more to play this turn
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Vayne, Hunter

- official_card: Vayne, Hunter (`play:vayne-hunter:37b5d160`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm an attacker
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: return me to my owner's hand
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Assault 3] (+3 :rb_might: while I'm an attacker.)
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Assault 3]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury

### [derived-fact] Veiled Temple

- official_card: Veiled Temple (`play:veiled-temple:c24f22f7`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer here
- predicate `detach`; role `event_produced`; type `produced_event`; confidence 0.82; evidence: detach it
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: ready a friendly gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Vengeance

- official_card: Vengeance (`play:vengeance:6fcfb218`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.84; evidence: Kill a unit
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Veteran Poro

- official_card: Veteran Poro (`play:veteran-poro:472d879f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Equip]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Weaponmaster]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Poro

### [derived-fact] Vex, Apathetic

- official_card: Vex, Apathetic (`play:vex-apathetic:e6442530`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun] it
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Stun]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Vex
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle

### [derived-fact] Vex, Cheerless

- official_card: Vex, Cheerless (`play:vex-cheerless:13c868ee`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `increase_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: cost :rb_energy_1::rb_rune_rainbow: more
- predicate `increase_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: cost :rb_energy_1::rb_rune_rainbow: more
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: friendly spells cost :rb_energy_1::rb_rune_rainbow: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: friendly spells cost :rb_energy_1::rb_rune_rainbow: less
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Vex
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle

### [derived-fact] Vex, Mocking

- official_card: Vex, Mocking (`play:vex-mocking:7c8d3aaf`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm a defender
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun] an enemy unit at a battlefield
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun] an enemy unit at a battlefield
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move me to that battlefield
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Shield] (+1 :rb_might: while I'm a defender.)
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Stun]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Shield]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]

### [derived-fact] Vi, Destructive

- official_card: Vi, Destructive (`play:vi-destructive:4ca9bbda`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Recycle 1 from your trash
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: Recycle 1 from your trash
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: Give me +1 :rb_might: this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ganking]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Vi
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury

### [derived-fact] Vi, Hotheaded

- official_card: Vi, Hotheaded (`play:vi-hotheaded:1cec02b3`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_energy_2::rb_rune_fury:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.82; evidence: Double my Might this turn
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Vi
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun

### [derived-fact] Vi, Peacekeeper

- official_card: Vi, Peacekeeper (`play:vi-peacekeeper:0bac4fbd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun] an enemy unit here
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Stun]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ambush]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Vi
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order

### [derived-fact] Vicious Snapjaws

- official_card: Vicious Snapjaws (`play:vicious-snapjaws:65db1c63`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When another friendly unit dies
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 1 XP
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bilgewater

### [derived-fact] Viktor, Innovator

- official_card: Viktor, Innovator (`play:viktor-innovator:5e94d05f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a 1 :rb_might: Recruit unit token in your base
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Viktor
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Viktor, Leader

- official_card: Viktor, Leader (`play:viktor-leader:e3392ab2`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When another non-Recruit unit you control dies
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a 1 :rb_might: Recruit unit token into your base
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Viktor
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Vilemaw

- official_card: Vilemaw (`play:vilemaw:b50133f8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I hold
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.82; evidence: Enemy units here with less Might than me don't deal combat damage
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Reaction]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ambush]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Spider

### [derived-fact] Vilemaw's Lair

- official_card: Vilemaw's Lair (`play:vilemaw-s-lair:d12d78ce`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `prevent`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: Units can't move from here to base
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Virtuoso

- official_card: Virtuoso (`play:virtuoso:45a055f3`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play a spell
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: banish it
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channel 4 runes
- predicate `channel`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: channel 4 runes
- predicate `move`; role `payoff_output`; type `movement`; confidence 0.8; evidence: put each in its trash
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind

### [derived-fact] Void Assault

- official_card: Void Assault (`play:void-assault:f1ca3280`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move an enemy unit
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move a friendly unit
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move to a battlefield you don't control
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Kha'Zix

### [derived-fact] Void Burrower

- official_card: Void Burrower (`play:void-burrower:a1700d73`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer
- predicate `exhaust`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.9; evidence: you may exhaust me
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: Recycle the rest
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: banish one
- predicate `reveal`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: reveal the top 2 cards of your Main Deck
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend

### [derived-fact] Void Drone

- official_card: Void Drone (`play:void-drone:2f0d2066`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_2: less
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.8; evidence: I cost :rb_energy_2: less
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: The Void

### [derived-fact] Void Gate

- official_card: Void Gate (`play:void-gate:ed74c390`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.88; evidence: Spells and abilities deal 1 Bonus Damage
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Void Hatchling

- official_card: Void Hatchling (`play:void-hatchling:c5d8edbf`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `recycle`; role `event_produced`; type `card_flow`; confidence 0.88; evidence: You may recycle it
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: The Void

### [derived-fact] Void Rush

- official_card: Void Rush (`play:void-rush:b39bb761`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `banish`; role `event_produced`; type `card_flow`; confidence 0.82; evidence: banish one
- predicate `reveal`; role `payoff_output`; type `card_flow`; confidence 0.84; evidence: Reveal the top 2 cards of your Main Deck
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.78; evidence: reducing its cost by :rb_energy_2:
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.78; evidence: reducing its cost by :rb_energy_2:
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Void Seeker

- official_card: Void Seeker (`play:void-seeker:bc7932ee`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 4 to a unit at a battlefield
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Voidreaver

- official_card: Voidreaver (`play:voidreaver:32676f4e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you win a combat
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Spend 1 XP, :rb_exhaust:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Spend 2 XP, :rb_exhaust:
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: Move an exhausted friendly unit from a battlefield to its base
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 1 XP
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Buff]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos

### [derived-fact] Volibear, Furious

- official_card: Volibear, Furious (`play:volibear-furious:674baee2`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect 2] (Opponents must pay :rb_rune_rainbow::rb_rune_rainbow:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.82; evidence: deal 5 damage split among any number of enemy units here
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect 2]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:9
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2

### [derived-fact] Volibear, Imposing

- official_card: Volibear, Imposing (`play:volibear-imposing:c4557b21`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm a defender
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Shield 3] (+3 :rb_might: while I'm a defender.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Shield 3]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2

### [derived-fact] Voracious Gromp

- official_card: Voracious Gromp (`play:voracious-gromp:a4c3deac`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 3 XP
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hunt 3]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5

### [derived-fact] Wages of Pain

- official_card: Wages of Pain (`play:wages-of-pain:467613d0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 3 to a unit at a battlefield
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: Play a Gold gear token exhausted
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Walking Roost

- official_card: Walking Roost (`play:walking-roost:fcaad4c2`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Deflect] (Opponents must pay :rb_rune_rainbow:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play a 1 :rb_might: Bird unit token with [Deflect]
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Deflect]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deflect]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6

### [derived-fact] Wallop

- official_card: Wallop (`play:wallop:c46e72d1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff as an additional cost
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.82; evidence: Ready a unit
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Warmog's Armor

- official_card: Warmog's Armor (`play:warmog-s-armor:ebdffb67`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_body:
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff me
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:1

### [derived-fact] Warwick, Hunter

- official_card: Warwick, Hunter (`play:warwick-hunter:2d515067`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dog
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Watchful Sentry

- official_card: Watchful Sentry (`play:watchful-sentry:998537f7`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I die
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: Draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Deathknell]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Freljord

### [derived-fact] Whirlwind

- official_card: Whirlwind (`play:whirlwind:70daa021`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: return a unit to its owner's hand
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Whiteflame Protector

- official_card: Whiteflame Protector (`play:whiteflame-protector:b5b5f61d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give a unit +8 :rb_might: this turn
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Dragon
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:8
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:8

### [derived-fact] Wielder of Water

- official_card: Wielder of Water (`play:wielder-of-water:c1eb5f5e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.84; evidence: I have +2 :rb_might:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Wildclaw Shaman

- official_card: Wildclaw Shaman (`play:wildclaw-shaman:400058cd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `buff`; role `event_produced`; type `state_modifier`; confidence 0.84; evidence: buff to buff me and ready me
- predicate `ready`; role `state_or_modifier`; type `state_modifier`; confidence 0.92; evidence: ready me
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Freljord

### [derived-fact] Wily Newtfish

- official_card: Wily Newtfish (`play:wily-newtfish:1f09fb9e`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.84; evidence: I have +1 :rb_might:
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Ganking]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bilgewater

### [derived-fact] Wind Wall

- official_card: Wind Wall (`play:wind-wall:96af2272`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `counter`; role `event_produced`; type `produced_event`; confidence 0.9; evidence: Counter a spell
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Reaction]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Windsinger

- official_card: Windsinger (`play:windsinger:ed5dbfe9`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: Hidden (Hide now for :rb_rune_rainbow:
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: return another unit at a battlefield with 3 :rb_might: or less to its owner's hand
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.94; evidence: Hidden
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:1

### [derived-fact] Windswept Hillock

- official_card: Windswept Hillock (`play:windswept-hillock:b550f6df`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.82; evidence: Units here have [Ganking].
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Wizened Elder

- official_card: Wizened Elder (`play:wizened-elder:a54d19e4`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.84; evidence: While I'm buffed
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.84; evidence: I have an additional +1 :rb_might:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] World Atlas

- official_card: World Atlas (`play:world-atlas:878c1917`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I hold
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Equip] :rb_rune_mind:
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.84; evidence: Attach this to a unit you control
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play two Gold gear tokens exhausted
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Equip]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Wraith of Echoes

- official_card: Wraith of Echoes (`play:wraith-of-echoes:971f1307`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Spirit
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:6
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shadow Isles

### [derived-fact] Wuju Apprentice

- official_card: Wuju Apprentice (`play:wuju-apprentice:6c78caaf`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer or hold
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `gain_xp`; role `payoff_output`; type `resource_change`; confidence 0.9; evidence: gain 1 XP
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hunt]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Level 6]

### [derived-fact] Wuju Bladesman - Starter

- official_card: Wuju Bladesman - Starter (`play:wuju-bladesman-starter:17a1e7bb`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Master Yi

### [derived-fact] Wuju Master

- official_card: Wuju Master (`play:wuju-master:a46122c1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `static_modifier`; confidence 0.82; evidence: Level 6][>] Your units have +1 :rb_might:
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.84; evidence: Your units enter ready
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Level 6]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Level 11]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: legend
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Master Yi

### [derived-fact] Xerath, Freed

- official_card: Xerath, Freed (`play:xerath-freed:6ba44b83`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: :rb_rune_fury:, :rb_exhaust:
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.86; evidence: Deal 3 to a unit
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Xerath
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Shurima
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

### [derived-fact] Xin Zhao, Vigilant

- official_card: Xin Zhao, Vigilant (`play:xin-zhao-vigilant:8a1bb57d`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Tank]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Demacia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Yasuo, Remorseful

- official_card: Yasuo, Remorseful (`play:yasuo-remorseful:174cb5c8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: deal damage equal to my Might to an enemy unit here
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yasuo
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2

### [derived-fact] Yasuo, Windrider

- official_card: Yasuo, Windrider (`play:yasuo-windrider:f5853ca9`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move in a turn
- predicate `score`; role `payoff_output`; type `score_change`; confidence 0.8; evidence: score 1 point
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ganking]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yasuo
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia

### [derived-fact] Yeti Brawler

- official_card: Yeti Brawler (`play:yeti-brawler:f6514c72`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.88; evidence: Kill this
- predicate `add_resource`; role `payoff_output`; type `resource_change`; confidence 0.88; evidence: [Add] :rb_rune_rainbow:
- predicate `play_token`; role `payoff_output`; type `token_creation`; confidence 0.88; evidence: play two Gold gear tokens exhausted
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: fury
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Noxus
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6

### [derived-fact] Yi, Honed

- official_card: Yi, Honed (`play:yi-honed:4fd3e4bd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `move`; role `restriction_or_permission`; type `permission`; confidence 0.78; evidence: I can move from battlefield to battlefield
- predicate `enter_ready`; role `state_or_modifier`; type `entry_state`; confidence 0.93; evidence: I enter ready
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Ganking]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1

### [derived-fact] Yi, Meditative

- official_card: Yi, Meditative (`play:yi-meditative:7f9eebc0`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.84; evidence: I have +4 :rb_might:
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Master Yi

### [derived-fact] Yone, Blademaster

- official_card: Yone, Blademaster (`play:yone-blademaster:252edf76`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I conquer
- predicate `attach`; role `event_produced`; type `produced_event`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `damage`; role `event_produced`; type `damage`; confidence 0.78; evidence: deal damage equal to my Might to an enemy unit in a base
- predicate `reduce_cost`; role `state_or_modifier`; type `static_modifier`; confidence 0.86; evidence: [Weaponmaster] (When you play me, you may [Equip] one of your Equipment to me for :rb_rune_rainbow: less
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Equip]
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Weaponmaster]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit

### [derived-fact] Yordle Explorer

- official_card: Yordle Explorer (`play:yordle-explorer:d89e21bd`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: body
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Yordle
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:4
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bandle City

### [derived-fact] Yuumi, Magical Cat

- official_card: Yuumi, Magical Cat (`play:yuumi-magical-cat:14e752b1`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack or defend
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When I attack or defend
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give one of your other units here +3 :rb_might:
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.86; evidence: give one of your other units here +3 :rb_might: and [Tank] this turn
- predicate `gain_keyword`; role `state_or_modifier`; type `keyword_grant`; confidence 0.84; evidence: give one of your other units here +3 :rb_might: and [Tank] this turn
- predicate `reference_keyword`; role `targeting_or_scope`; type `keyword_reference`; confidence 0.86; evidence: [Tank]
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Fae
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Cat

### [derived-fact] Zaun Punk

- official_card: Zaun Punk (`play:zaun-punk:e7c2786f`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `kill`; role `cost_or_requirement`; type `additional_cost`; confidence 0.9; evidence: You may kill a friendly gear as an additional cost to play me
- predicate `kill`; role `event_produced`; type `removal`; confidence 0.88; evidence: kill a gear
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:3
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:3

### [derived-fact] Zaun Warrens

- official_card: Zaun Warrens (`play:zaun-warrens:6bce52a8`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you conquer here
- predicate `discard`; role `event_produced`; type `card_flow`; confidence 0.84; evidence: discard 1
- predicate `draw`; role `payoff_output`; type `card_flow`; confidence 0.94; evidence: draw 1
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: colorless
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: battlefield

### [derived-fact] Zaunite Bouncer

- official_card: Zaunite Bouncer (`play:zaunite-bouncer:74e7de55`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `observe_event`; role `trigger_observed`; type `event_trigger`; confidence 0.9; evidence: When you play me
- predicate `return_to_hand`; role `payoff_output`; type `movement`; confidence 0.86; evidence: return another unit at a battlefield to its owner's hand
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zaun
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: chaos
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:2
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:4

### [derived-fact] Zenith Blade

- official_card: Zenith Blade (`play:zenith-blade:d4644f37`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun an enemy unit at a battlefield
- predicate `stun`; role `event_produced`; type `state_modifier`; confidence 0.86; evidence: Stun an enemy unit at a battlefield
- predicate `move`; role `event_produced`; type `movement`; confidence 0.82; evidence: move a friendly unit to that enemy unit's battlefield
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Action]
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: spell
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: order
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Leona

### [derived-fact] Zephyr Sage

- official_card: Zephyr Sage (`play:zephyr-sage:af0ed2cf`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `require`; role `restriction_or_permission`; type `restriction`; confidence 0.86; evidence: while I'm a defender
- predicate `modify_stat`; role `state_or_modifier`; type `stat_change`; confidence 0.88; evidence: [Shield] (+1 :rb_might: while I'm a defender.)
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Shield]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Bird
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Ionia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:6

### [derived-fact] Zhonya's Hourglass

- official_card: Zhonya's Hourglass (`play:zhonya-s-hourglass:fcfa3dbc`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `pay`; role `cost_or_requirement`; type `activated_ability_cost`; confidence 0.88; evidence: [Hidden] (Hide now for :rb_rune_rainbow:
- predicate `prevent`; role `restriction_or_permission`; type `replacement_effect`; confidence 0.88; evidence: If a friendly unit would die, kill this instead. Heal that unit, exhaust it, and recall it
- predicate `kill`; role `event_produced`; type `produced_event`; confidence 0.88; evidence: kill this
- predicate `return_to_hand`; role `event_produced`; type `movement`; confidence 0.82; evidence: recall it
- predicate `has_keyword`; role `identity_or_descriptor`; type `keyword_marker`; confidence 0.96; evidence: [Hidden]
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: gear
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: calm
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:2

### [derived-fact] Zilean, Time Mage

- official_card: Zilean, Time Mage (`play:zilean-time-mage:8fb4d0e9`)
- authority_note: extracted from official card text or normalized official fields; verify against official card and official rules.

Derived facts:
- predicate `copy`; role `state_or_modifier`; type `replacement_effect`; confidence 0.82; evidence: if you would play a token unit while I'm at a battlefield, you may play that token and an additional copy of it instead
- predicate `has_card_type`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: unit
- predicate `has_domain`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: mind
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Zilean
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: might:5
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: power:1
- predicate `has_tag`; role `identity_or_descriptor`; type `identity_reference`; confidence 1.0; evidence: Icathia
- predicate `has_stat`; role `identity_or_descriptor`; type `stat_change`; confidence 1.0; evidence: energy:5

## By Semantic Role

### [derived-fact] cost_or_requirement

- fact_count: 265
- example_cards: Pyke, Dockside Butcher (3), Twisted Fate, Gambler (3), Akshan, Mischievous (2), Ancient Henge (2), Blast Corps Cadet (2), Bullet Time (2), Clockwork Keeper (2), Commander Ledros (2), Edge of Night (2), Frostcoat Cub (2), Grandmaster at Arms (2), Hexdrinker (2), Hextech Anomaly (2), Honeyfruit (2), Kraken Hunter (2), Nami, Headstrong (2), Pyke, Returned (2), Renata Glasc, Mastermind (2), Rengar, Unseen (2), Sea Monkey (2), Swift Scout (2), The Zero Drive (2), Unlicensed Armory (2), Vi, Hotheaded (2), Voidreaver (2), Allay, Eager Admirer (1), Altar of Blood (1), Altar of Memories (1), Ancient Warmonger (1), Arena Bar (1)

### [derived-fact] event_produced

- fact_count: 477
- example_cards: Icathian Rain (6), Rift Herald (4), Twisted Fate, Gambler (4), Arcane Shift (3), Azir, Ascendant (3), Baited Hook (3), Cursed Sarcophagus (3), Fae Porter (3), Hostile Takeover (3), Immortal Phoenix (3), Irresistible Faefolk (3), Kai'Sa, Evolutionary (3), Last Rites (3), Overt Operation (3), Promising Future (3), Relentless Pursuit (3), Vex, Mocking (3), Void Assault (3), Zenith Blade (3), Abandon (2), Adaptatron (2), Akshan, Mischievous (2), Angle Shot (2), Atakhan (2), Blade of the Ruined King (2), Blast Cone (2), Blighted Battleaxe (2), Blind Fury (2), Bone Skewer (2), Call to Battle (2)

### [derived-fact] identity_or_descriptor

- fact_count: 4247
- example_cards: Rengar, Unseen (12), Master Yi, Unstoppable (11), Spinning Axe (11), Forgefire Cape (10), Miss Fortune, Captain (10), Nilah, Joyful Ascetic (10), Poppy, Defender of the Meek (10), Rabadon's Deathcrown (10), Rengar, Pouncing (10), Shen, Kinkou (10), Shurelya's Requiem (10), Vex, Mocking (10), Blitzcrank, Impassive (9), Commander Ledros (9), Darius, Executioner (9), Ekko, Recurrent (9), Ferrous Forerunner (9), Galio, Indefatigable (9), Garen, Rugged (9), Gustwalker (9), Jhin, Murderous Artist (9), Jinx, Demolitionist (9), Kraken Hunter (9), LeBlanc, Fragmented (9), Mosstomper (9), Needlessly Large Yordle (9), Nidalee, Cat Form (9), Rengar, Trophy Hunter (9), Rumble, Scrapper (9), Scorchclaw (9)

### [derived-fact] payoff_output

- fact_count: 357
- example_cards: Virtuoso (4), Bloodharbor Ripper (3), Catalyst of Aeons (3), Scryer's Bloom (3), Abandon (2), Altar of Memories (2), Blood Money (2), Called Shot (2), Chem-Baroness (2), Curtain Call (2), Deadly Flourish (2), Desert's Call (2), Diana, Lunari (2), Double Trouble (2), Downstage Dramatics (2), Draven, Audacious (2), Emperor's Dais (2), Existential Dread (2), Find Your Center (2), Gutter Palace (2), Herald of Spring (2), Honeyfruit (2), Hwei, Brooding Painter (2), Keeper of the Hammer (2), LeBlanc, Fragmented (2), Meditation (2), Mobilize (2), Party Favors (2), Poro Snax (2), Production Surge (2)

### [derived-fact] restriction_or_permission

- fact_count: 125
- example_cards: Arachnoid Horror (2), Baron Nashor (2), Bilgewater Bully (2), Kayn, Unleashed (2), Lee Sin, Ascetic (2), Mageseeker Warden (2), Miss Fortune, Buccaneer (2), Nocturne, Horrifying (2), Raging Soul (2), Rengar, Pouncing (2), Rengar, Unseen (2), Alpha Wildclaw (1), Altar of Blood (1), Ancient Warmonger (1), Atakhan (1), Baron Pit (1), Black Rose Dignitary (1), Block (1), Blood Rush (1), Blue Sentinel (1), Boots of Swiftness (1), Chemtech Enforcer (1), Cleave (1), Cloth Armor (1), Commander Ledros (1), Counter Strike (1), Daring Poro (1), Dauntless Vanguard (1), Deadbloom Predator (1), Defy (1)

### [derived-fact] state_or_modifier

- fact_count: 373
- example_cards: Master Yi, Unstoppable (6), Concentrate (4), Vex, Cheerless (4), Bashful Bloom (3), Daisy! (3), Deceiver (3), Mirror Image (3), Needlessly Large Yordle (3), Ornn's Forge (3), Yuumi, Magical Cat (3), Arena Kingpin (2), Atakhan (2), Battering Ram (2), Blade Dancer (2), Brazen Buccaneer (2), Breakneck Mech (2), Combat Experience (2), Crescent Guardian (2), Darius, Executioner (2), Darius, Trifarian (2), Drag Under (2), Draven, Vanquisher (2), Dune Drake (2), Eager Apprentice (2), Eclipse Herald (2), Find Your Center (2), Green Father (2), Herald of Scales (2), Here to Help (2), Hwei, Brooding Painter (2)

### [derived-fact] targeting_or_scope

- fact_count: 109
- example_cards: Hand of Noxus (2), Nami, Headstrong (2), Vi, Peacekeeper (2), Ancient Henge (1), Armed Assailant (1), Ava Achiever (1), Azir, Ascendant (1), Bashful Bloom (1), Black Flame Altar (1), Blast Cone (1), Bone Skewer (1), Carrion Dredger (1), Chakram Dancer (1), Combat Chef (1), Crowd Favorite (1), Daughter of the Void (1), Diana, Lunari (1), Diana, No Longer Human (1), Dramatic Visionary (1), Ember Monk (1), Emperor of the Sands (1), Energy Conduit (1), Enthralling Protector (1), Enthusiastic Promoter (1), Ezreal, Dashing (1), Fiora, Victorious (1), Fiora, Worthy (1), Fire Below the Mountain (1), Flurry of Feathers (1), Forgotten Library (1)

### [derived-fact] trigger_observed

- fact_count: 358
- example_cards: Herald of Spring (4), Kha'Zix, Evolving Hunter (4), Wuju Apprentice (4), Arachnoid Horror (3), Crowd Favorite (3), Draven, Vanquisher (3), Enthralling Protector (3), Gemhand Hunter (3), Gustwalker (3), Hunter's Machete (3), Ivern, Friend to All (3), Last Rites (3), Master Yi, Tempered (3), Mosstomper (3), Scorchclaw (3), Voracious Gromp (3), Ahri, Inquisitive (2), Battle Mistress (2), Blast Cone (2), Blitzcrank, Impassive (2), Corrupt Enforcer (2), Deceiver (2), Ezreal, Dashing (2), Fiora, Peerless (2), Forgefire Cape (2), Green Father (2), Ivern, Nurturer (2), Jax, Unrelenting (2), Karma, Channeler (2), Kha'Zix, Mutating Horror (2)
