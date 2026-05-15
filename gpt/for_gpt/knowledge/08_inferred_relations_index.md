# Inferred Relations Index

## Use Policy

[inferred-relation] Relations are pipeline inferences. Use them for discovery, synergy, comparison, and list-building suggestions. Verify rules-sensitive answers against official cards and official rules.

## Relation Types

### [inferred-relation] deck_synergy

- label: Deck Synergy
- count: 3306
- lane: experimental
- default_visible: False
- experimental: True

### [inferred-relation] enabled_by

- label: Enablers
- count: 2325
- lane: high_signal
- default_visible: True
- experimental: False

### [inferred-relation] enables

- label: Enabled Cards
- count: 2325
- lane: high_signal
- default_visible: True
- experimental: False

### [inferred-relation] similar_effect

- label: Similar Effects
- count: 6634
- lane: high_signal
- default_visible: True
- experimental: False

## High-Signal Relations By Card

### [inferred-relation] Abandon

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- in: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- in: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- in: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- in: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`
- in: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- in: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`

### [inferred-relation] Abandoned Hall

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Annie, Stubborn; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Fizz, Trickster; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Kai'Sa, Evolutionary; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Annie, Stubborn; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Fizz, Trickster; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Kai'Sa, Evolutionary; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`

### [inferred-relation] Acceptable Losses

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Detonate; type `similar_effect`; strength 0.72; reason `secondary:removal:gear_dies:gear:required:active`
- in: Rocket Barrage; type `similar_effect`; strength 0.72; reason `secondary:removal:gear_dies:gear:required:active`
- in: Thermo Beam; type `similar_effect`; strength 0.72; reason `secondary:removal:gear_dies:gear:required:active`
- in: Zaun Punk; type `similar_effect`; strength 0.72; reason `secondary:removal:gear_dies:gear:required:active`
- out: Detonate; type `similar_effect`; strength 0.72; reason `secondary:removal:gear_dies:gear:required:active`
- out: Rocket Barrage; type `similar_effect`; strength 0.72; reason `secondary:removal:gear_dies:gear:required:active`
- out: Thermo Beam; type `similar_effect`; strength 0.72; reason `secondary:removal:gear_dies:gear:required:active`
- out: Zaun Punk; type `similar_effect`; strength 0.72; reason `secondary:removal:gear_dies:gear:required:active`

### [inferred-relation] Adaptatron

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- in: Salvage; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::optional`
- in: Sett, Brawler; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_conquers`
- out: Salvage; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::optional`
- out: Sett, Brawler; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_conquers`

### [inferred-relation] Against the Odds

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Siphon Power; type `similar_effect`; strength 0.72; reason `secondary:stat_no_location:might_modified:might:positive:unit[controller=friendly]:this...`
- in: Yuumi, Magical Cat; type `similar_effect`; strength 0.72; reason `secondary:stat_no_location:might_modified:might:positive:unit[controller=friendly]:this...`
- out: Siphon Power; type `similar_effect`; strength 0.72; reason `secondary:stat_no_location:might_modified:might:positive:unit[controller=friendly]:this...`
- out: Yuumi, Magical Cat; type `similar_effect`; strength 0.72; reason `secondary:stat_no_location:might_modified:might:positive:unit[controller=friendly]:this...`

### [inferred-relation] Ahri, Alluring

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aspirant's Climb; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Draven, Audacious; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Ivern, Friend to All; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Power Nexus; type `similar_effect`; strength 0.72; reason `secondary:score_amount:1:point:active`
- in: Renata Glasc, Mastermind; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: The Arena's Greatest; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Tryndamere, Barbarian; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Yasuo, Windrider; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`

### [inferred-relation] Ahri, Inquisitive

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- in: Forbidding Waste; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- in: Icevale Archer; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- in: Leona, Zealot; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- in: Moonfall; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:-2:might:unit[controlle...`
- in: Moonfall; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- in: Moonlight Affliction; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`

### [inferred-relation] Akshan, Mischievous

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:card:active`
- in: Cloth Armor; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:when=self_played`
- in: Edge of Night; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:when=self_played`
- in: Ezreal, Dashing; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base[controller=friendly]:active`

### [inferred-relation] Albus Ferros

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- in: Stormclaw Ursine; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required:when=sel...`
- out: Stormclaw Ursine; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required:when=sel...`

### [inferred-relation] Allay, Eager Admirer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Petricite Monument; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:deflect:unit:ongoing:required:active`
- in: Petricite Monument; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:deflect:unit:ongoing:required:active`
- in: Spirit's Refuge; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:deflect:unit:ongoing:required:active`
- in: Spirit's Refuge; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:deflect:unit:ongoing:required:active`
- out: Petricite Monument; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:deflect:unit:ongoing:required:active`
- out: Petricite Monument; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:deflect:unit:ongoing:required:active`
- out: Spirit's Refuge; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:deflect:unit:ongoing:required:active`
- out: Spirit's Refuge; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:deflect:unit:ongoing:required:active`

### [inferred-relation] Alpha Strike

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Gardens of Becoming; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Keeper of the Hammer; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Nilah, Joyful Ascetic; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Scryer's Bloom; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Scuttle Crab; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Stare Down; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Vicious Snapjaws; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Voidreaver; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`

### [inferred-relation] Alpha Wildclaw

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Baron Nashor; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:active`
- in: Baron Nashor; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:::active`
- in: Master Yi, Unstoppable; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:::active`
- in: Master Yi, Unstoppable; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:active`
- in: Ruin Runner; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:::active`
- in: Ruin Runner; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:active`
- out: Baron Nashor; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:::active`
- out: Baron Nashor; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:active`

### [inferred-relation] Altar of Blood

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Relentless Pursuit; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:card:base:optional:active`
- in: Symbol of the Solari; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:base:active`
- in: The Boss; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::optional`
- in: Unlicensed Armory; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::optional`
- out: Relentless Pursuit; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:card:base:optional:active`
- out: Symbol of the Solari; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:base:active`
- out: The Boss; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::optional`
- out: Unlicensed Armory; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::optional`

### [inferred-relation] Altar of Memories

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Baited Hook; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Deathgrip; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`

### [inferred-relation] Altar to Unity

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Forge of the Future; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- in: Machine Evangel; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- in: Recruit the Vanguard; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- in: Viktor, Innovator; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- in: Viktor, Leader; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- out: Forge of the Future; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- out: Machine Evangel; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- out: Recruit the Vanguard; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`

### [inferred-relation] Amateur Recital

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Emperor's Divide; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Fight or Flight; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Flash; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Isolate; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Overzealous Fan; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Overzealous Fan; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:optional:active`
- in: Overzealous Fan; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:base:optional:active`
- in: Overzealous Fan; type `similar_effect`; strength 0.72; reason `secondary:move:unit:base:optional:active`

### [inferred-relation] Angle Shot

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Boneshiver; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`
- in: Grandmaster at Arms; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`
- in: Hextech Gauntlets; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`
- in: Last Rites; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`

### [inferred-relation] Angler Beast

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Beast Below; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active:when=self_played`
- in: Beast Below; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`
- in: Beast Below; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active:when=self_played`
- in: Beast Below; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active:when=self_played`
- in: Grim Apothecary; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`
- in: Windsinger; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`
- in: Zaunite Bouncer; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active:when=self_played`
- in: Zaunite Bouncer; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`

### [inferred-relation] Anivia, Primal

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Arcane Shift; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Crackshot Corsair; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=here]::required:active:when...`
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Disintegrate; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Falling Star; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Firestorm; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Hextech Ray; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`

### [inferred-relation] Annie, Fiery

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Void Gate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:bonus_damage_added:1:bonus_damage:...`
- out: Void Gate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:bonus_damage_added:1:bonus_damage:...`

### [inferred-relation] Annie, Stubborn

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Abandoned Hall; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Chemtech Cask; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Diana, No Longer Human; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Forgotten Library; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Lady of Luminosity - Starter; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Lux, Illuminated; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Ravenbloom Student; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Revna the Lorekeeper; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`

### [inferred-relation] Aphelios, Exalted

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Akshan, Mischievous; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Angle Shot; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Armed Assailant; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Azir, Ascendant; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: B.F. Sword; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`

### [inferred-relation] Apprentice Smith

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- in: Blind Fury; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`
- in: Diana, Lunari; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`
- in: Ravenbloom Conservatory; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`
- in: Rift Herald; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::required:w...`
- out: Blind Fury; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`
- out: Diana, Lunari; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`

### [inferred-relation] Arachnoid Horror

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Dauntless Vanguard; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- in: Dauntless Vanguard; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:battlefield[controller=opponent]:play:active`
- in: Deadbloom Predator; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- in: Deadbloom Predator; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:battlefield[controller=opponent]:play:active`
- in: Gustwalker; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required:when=self_conqu...`
- in: Jhin, Meticulous Killer; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- in: Mageseeker Warden; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`
- in: Master Yi, Tempered; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required:when=self_conqu...`

### [inferred-relation] Arcane Shift

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Ashe, Focused; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- in: Blind Fury; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Dazzling Aurora; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- in: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Firestorm; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:3:damage:unit[controller=opponent;locat...`

### [inferred-relation] Arena Bar

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- in: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- in: Blind Monk; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- in: Karma, Channeler; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- in: Mistfall; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- in: Overt Operation; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`

### [inferred-relation] Arena Kingpin

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Crescent Guardian; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Daisy!; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Direwing; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Dunebreaker; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Eager Drakehound; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Green Father; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:positive:active:cost=action=exhaust:self`

### [inferred-relation] Arise!

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Desert's Call; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sand_soldier_unit_token_created::::requi...`
- in: Guards!; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sand_soldier_unit_token_created::::requi...`
- out: Desert's Call; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sand_soldier_unit_token_created::::requi...`
- out: Guards!; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sand_soldier_unit_token_created::::requi...`

### [inferred-relation] Armed Assailant

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Combat Chef; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=g...`
- in: Combat Chef; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:gear_cost_reduced:1:rune:gear[cont...`
- in: Jax, Unrelenting; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=g...`
- in: Jax, Unrelenting; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:gear_cost_reduced:1:rune:gear[cont...`

### [inferred-relation] Ashe, Focused

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arcane Shift; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- in: Arcane Shift; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- in: Blind Fury; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- in: Dazzling Aurora; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- in: Smite; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- in: Time Warp; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- out: Blind Fury; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- out: Dazzling Aurora; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`

### [inferred-relation] Aspirant's Climb

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Ahri, Alluring; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Ahri, Alluring; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Draven, Audacious; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Ivern, Friend to All; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Power Nexus; type `similar_effect`; strength 0.72; reason `secondary:score_amount:1:point:active`
- in: Renata Glasc, Mastermind; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: The Arena's Greatest; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Tryndamere, Barbarian; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`

### [inferred-relation] Aspiring Engineer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Annie, Stubborn; type `similar_effect`; strength 0.72; reason `secondary:move:hand[controller=friendly;zone=hand]:hand[controller=friendly]:required:a...`
- out: Annie, Stubborn; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active:when=self_...`
- out: Annie, Stubborn; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:required:active:w...`
- out: Annie, Stubborn; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand[controller=friendly]:required:active:when=self_played`
- in: Annie, Stubborn; type `similar_effect`; strength 0.72; reason `secondary:move:hand[controller=friendly;zone=hand]:hand[controller=friendly]:required:a...`
- in: Annie, Stubborn; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active:when=self_...`
- in: Annie, Stubborn; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:required:active:w...`
- in: Annie, Stubborn; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand[controller=friendly]:required:active:when=self_played`

### [inferred-relation] Assembly Rig

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- in: Ferrous Forerunner; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:mech_unit_token_created:your_base[locati...`
- in: Production Surge; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:mech_unit_token_created:your_base[locati...`
- in: Rumble, Scrapper; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:mech_unit_token_created:your_base[locati...`
- out: Ferrous Forerunner; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:mech_unit_token_created:your_base[locati...`
- out: Production Surge; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:mech_unit_token_created:your_base[locati...`
- out: Rumble, Scrapper; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:mech_unit_token_created:your_base[locati...`

### [inferred-relation] Atakhan

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Altar of Memories; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Spectral Centaur; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Vanguard Helm; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Vicious Snapjaws; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Viktor, Leader; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Altar of Memories; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Spectral Centaur; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Vanguard Helm; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`

### [inferred-relation] Azir, Ascendant

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:card:active`
- in: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:card:active`
- in: Brutalizer; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=calm`
- in: Doran's Shield; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=calm`

### [inferred-relation] Azir, Sovereign

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Call to Battle; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- in: Evelynn, Entrancing; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:optional:active`
- in: Evelynn, Entrancing; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:battlefield:optional:active`
- in: Fae Porter; type `similar_effect`; strength 0.72; reason `secondary:move:unit[controller=friendly]:battlefield:optional:active`
- in: Iascylla; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- in: Iascylla; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:optional:active`
- in: Iascylla; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:battlefield:optional:active`
- in: Mageseeker Investigator; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`

### [inferred-relation] B.F. Sword

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Blade of the Ruined King; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- in: Blade of the Ruined King; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=order`
- in: Blade of the Ruined King; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=order`
- in: Eye of the Herald; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`

### [inferred-relation] Back Off

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- in: Rune Prison; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`
- in: Solari Shieldbearer; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`
- in: Thwonk!; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`
- out: Rune Prison; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`
- out: Solari Shieldbearer; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`
- out: Thwonk!; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`

### [inferred-relation] Back to Back

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Decisive Strike; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit[controller...`
- in: Frigid Jewel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit[controller...`
- in: Grand Strategem; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- in: Inviolus Vox; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- in: Undertitan; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Decisive Strike; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit[controller...`
- out: Frigid Jewel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit[controller...`
- out: Grand Strategem; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`

### [inferred-relation] Back-Alley Bar

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Friendship; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Irelia, Fervent; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Jinx, Rebel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Lillia, Protector of Dreams; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Mask of Foresight; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Pirate's Haven; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Prize of Progress; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`

### [inferred-relation] Baited Hook

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Altar of Memories; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Spectral Centaur; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Vanguard Helm; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Vicious Snapjaws; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Viktor, Leader; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Altar of Memories; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Spectral Centaur; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Vanguard Helm; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`

### [inferred-relation] Bandle Soldier

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Crescent Guardian; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Daisy!; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Direwing; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Dunebreaker; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Eager Drakehound; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`

### [inferred-relation] Bard, Mercurial

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Call to Battle; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:required:active`
- in: Call to Battle; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:battlefield:required:active`
- in: Call to Battle; type `similar_effect`; strength 0.72; reason `secondary:move:unit[controller=friendly]:battlefield:required:active`
- in: Evelynn, Entrancing; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active:when=self_played`
- in: Mageseeker Investigator; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:required:active`
- in: Mageseeker Investigator; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:battlefield:required:active`
- in: Showstopper; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:required:active`
- out: Call to Battle; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:required:active`

### [inferred-relation] Baron Nashor

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Alpha Wildclaw; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:active`
- out: Alpha Wildclaw; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:::active`
- in: Alpha Wildclaw; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:::active`
- in: Alpha Wildclaw; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:active`
- in: Baron Pit; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:unit:here[location=here]:::source=a...`
- in: Darius, Executioner; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]::static:active`
- in: Garen, Commander; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]::static:active`
- in: Master Yi, Unstoppable; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:restriction:prevent:card::::prevented=choose`

### [inferred-relation] Baron Pit

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Baron Nashor; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:unit:here[location=here]:::source=a...`
- in: Baron Nashor; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:unit:here[location=here]:::source=a...`

### [inferred-relation] Bashful Bloom

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- in: Atakhan; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- in: Battering Ram; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- in: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Dune Drake; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Eager Apprentice; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- in: Lillia, Fae Fawn; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created::::required:ob...`
- in: Piltover Enforcer; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`

### [inferred-relation] Battering Ram

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- out: Bashful Bloom; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- in: Atakhan; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- in: Bashful Bloom; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- in: Eager Apprentice; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- in: Rhasa the Sunderer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- out: Eager Apprentice; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- out: Rhasa the Sunderer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`

### [inferred-relation] Battle Mistress

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Harnessed Dragon; type `enabled_by`; strength 0.95; reason `enemy_unit_dies_enables_enemy_unit_dies`
- out: Sandshifter; type `enabled_by`; strength 0.95; reason `enemy_unit_dies_enables_enemy_unit_dies`
- in: Harnessed Dragon; type `enables`; strength 0.95; reason `enemy_unit_dies_enables_enemy_unit_dies`
- in: Sandshifter; type `enables`; strength 0.95; reason `enemy_unit_dies_enables_enemy_unit_dies`
- out: Sigil of the Storm; type `enabled_by`; strength 0.9; reason `rune_recycled_enables_rune_recycled`
- in: Sigil of the Storm; type `enables`; strength 0.9; reason `rune_recycled_enables_rune_recycled`
- in: Chem-Baroness; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::optional:obje...`
- in: Chemtech Cask; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::optional:obje...`

### [inferred-relation] Beast Below

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Angler Beast; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active:when=self_played`
- out: Angler Beast; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`
- out: Angler Beast; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active:when=self_played`
- out: Angler Beast; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active:when=self_played`
- in: Angler Beast; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active:when=self_played`
- in: Angler Beast; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`
- in: Angler Beast; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active:when=self_played`
- in: Angler Beast; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active:when=self_played`

### [inferred-relation] Bellows Breath

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Crackshot Corsair; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Elder Dragon; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Final Spark; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- in: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Frozen Fortress; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Singularity; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- in: Super Mega Death Rocket!; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- in: Teemo, Strategist; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:1:damage:unit:::required`

### [inferred-relation] Bewitching Spirit

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- in: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- in: Evershade Stalker; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- in: Ezreal, Prodigy; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- out: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- out: Evershade Stalker; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- out: Ezreal, Prodigy; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`

### [inferred-relation] Bilgewater Bully

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- in: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- in: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- in: Fiora, Victorious; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:card:ongoing:required:active`
- in: Fiora, Victorious; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:card:ongoing:required:active`
- in: Jhin, Murderous Artist; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- in: Kai'Sa, Evolutionary; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- in: Kayn, Unleashed; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`

### [inferred-relation] Black Flame Altar

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Taric, Protector; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:shield:unit:ongoing:required:active:require=duration...`
- in: Taric, Protector; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:shield:unit:ongoing:required:active:require=duration=while,stat...`
- out: Taric, Protector; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:shield:unit:ongoing:required:active:require=duration...`
- out: Taric, Protector; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:shield:unit:ongoing:required:active:require=duration=while,stat...`

### [inferred-relation] Black Market Broker

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Blood Money; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Bushwhack; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Draven, Vanquisher; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Eminent Benefactor; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Fae Dragon; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Honest Broker; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Treasure Hunter; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`

### [inferred-relation] Black Rose Dignitary

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Blade Dancer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Fiora, Worthy; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- in: Guards!; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- in: Mistfall; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- in: Overt Operation; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- out: Fiora, Worthy; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- out: Guards!; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- out: Mistfall; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- out: Overt Operation; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`

### [inferred-relation] Blade of the Ruined King

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Altar of Memories; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Spectral Centaur; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Vanguard Helm; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Vicious Snapjaws; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Viktor, Leader; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Altar of Memories; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Spectral Centaur; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Vanguard Helm; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`

### [inferred-relation] Blast Cone

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- in: Bone Skewer; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:card::this_turn:optional`
- in: Charm; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:unit[controller=opponent]:active`
- in: Dragon's Rage; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:unit[controller=opponent]:active`
- in: Skyward Strike; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:unit[controller=opponent]:active`
- in: Void Assault; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:unit[controller=opponent]:active`
- out: Bone Skewer; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:card::this_turn:optional`

### [inferred-relation] Blast Corps Cadet

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- in: Incinerate; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- in: Iron Ballista; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- in: Monster Harpoon; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- in: Piercing Light; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- in: Sudden Storm; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- in: Udyr, Wildman; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`

### [inferred-relation] Blast of Power

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Blood Money; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- in: Cull the Weak; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- in: Drag Under; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- in: Fox-Fire; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- in: Hidden Blade; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- in: Imperial Decree; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- in: King's Edict; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- in: Noxian Guillotine; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`

### [inferred-relation] Blastcone Fae

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Frostcoat Cub; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:-2:might:unit::this_tur...`
- in: Thousand-Tailed Watcher; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active:when=self_played`
- out: Frostcoat Cub; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:-2:might:unit::this_tur...`
- out: Thousand-Tailed Watcher; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active:when=self_played`

### [inferred-relation] Blighted Battleaxe

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Skyfall of Areion; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- in: Skyfall of Areion; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=energy=1,rune=fury`
- in: Skyfall of Areion; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=energy=1,rune=fury`
- out: Skyfall of Areion; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`

### [inferred-relation] Blind Fury

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Apprentice Smith; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`
- out: Arcane Shift; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- out: Ashe, Focused; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- in: Apprentice Smith; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`
- in: Arcane Shift; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- in: Ashe, Focused; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`

### [inferred-relation] Blind Monk

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- out: Arena Bar; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- in: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- in: Arena Bar; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- in: Karma, Channeler; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- in: Mistfall; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`

### [inferred-relation] Blitzcrank, Impassive

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`
- in: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- in: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- in: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- in: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`

### [inferred-relation] Block

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Chakram Dancer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:shield:unit:temporary:required:active:require=durati...`
- in: Chakram Dancer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:shield:unit:this_turn:required:active:require=duration=while,st...`
- in: Fortified Position; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:shield:unit:temporary:required:active:require=durati...`
- in: Yuumi, Magical Cat; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:tank:unit:temporary:required:active`
- in: Yuumi, Magical Cat; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:tank:unit:this_turn:required:active`
- out: Chakram Dancer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:shield:unit:temporary:required:active:require=durati...`
- out: Chakram Dancer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:shield:unit:this_turn:required:active:require=duration=while,st...`
- out: Fortified Position; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:shield:unit:temporary:required:active:require=durati...`

### [inferred-relation] Blood Money

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Black Market Broker; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Blast of Power; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- in: Black Market Broker; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Blast of Power; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- in: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Bushwhack; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Cull the Weak; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- in: Drag Under; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`

### [inferred-relation] Blood Rose

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Dune Drake; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: First Mate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit:::required`
- in: Piltover Enforcer; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Upstage Comedy; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit:::required`
- in: Wallop; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit:::required`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Dune Drake; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`

### [inferred-relation] Blood Rush

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Cleave; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:unit::this_turn:req...`
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=1`
- in: Lord Broadmane; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:assault:unit:this_turn:required:active:require=duration=while,s...`
- in: Lord Broadmane; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:assault:unit:temporary:required:active:require=durat...`
- in: Square Up; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:unit::this_turn:req...`
- in: Vault Breaker; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:assault:unit:this_turn:required:active:require=duration=while,s...`
- in: Vault Breaker; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:assault:unit:temporary:required:active:require=durat...`
- out: Cleave; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:unit::this_turn:req...`

### [inferred-relation] Bloodharbor Ripper

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`
- out: Black Market Broker; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`

### [inferred-relation] Blue Sentinel

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required`
- in: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required`
- in: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_defender:active`
- in: Mutated Mouser; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Shen, Kinkou; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Towering Combatant; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Yeti Brawler; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required`
- out: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_defender:active`

### [inferred-relation] Body Rune

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Calm Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Chaos Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Fury Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Mind Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Order Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- out: Calm Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- out: Chaos Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- out: Fury Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`

### [inferred-relation] Bonds of Strength

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Desert's Call; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Double Trouble; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Downstage Dramatics; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: En Garde; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:unit[controller...`
- in: Existential Dread; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Feral Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Frigid Touch; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Grand Strategem; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`

### [inferred-relation] Bone Skewer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Blast Cone; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:card::this_turn:optional`
- in: Blast Cone; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:card::this_turn:optional`
- in: Solari Chief; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:card::this_turn:required`
- in: Vex, Apathetic; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:card::this_turn:required`
- out: Solari Chief; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:card::this_turn:required`
- out: Vex, Apathetic; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:card::this_turn:required`

### [inferred-relation] Boneshiver

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Angle Shot; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`
- in: Angle Shot; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`
- in: Grandmaster at Arms; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- in: Grandmaster at Arms; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`

### [inferred-relation] Boots of Swiftness

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Cull; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- in: Cull; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=chaos`
- in: Cull; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=chaos`
- in: Doran's Ring; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`

### [inferred-relation] Bounty Hunter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Gem Jammer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:unit::this_turn:req...`
- in: Megatusk; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:unit:temporary:required:active`
- in: Megatusk; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:unit:this_turn:required:active`
- in: Vault Breaker; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:unit:temporary:required:active`
- in: Vault Breaker; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:unit:this_turn:required:active`
- out: Gem Jammer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:unit::this_turn:req...`
- out: Megatusk; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:unit:temporary:required:active`
- out: Megatusk; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:unit:this_turn:required:active`

### [inferred-relation] Brazen Buccaneer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- in: Concentrate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Deceiver; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::optional`
- in: Drag Under; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Find Your Center; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Herald of Scales; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Jaull-Fish; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`

### [inferred-relation] Breakneck Mech

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Crescent Guardian; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Daisy!; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Direwing; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Dunebreaker; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`

### [inferred-relation] Brush

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Trifarian War Camp; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:might_modified:1:might:unit[locati...`
- in: Trusty Ramhound; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:might_modified:1:might:unit[locati...`
- out: Trifarian War Camp; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:might_modified:1:might:unit[locati...`
- out: Trusty Ramhound; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:might_modified:1:might:unit[locati...`

### [inferred-relation] Brutalizer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=calm`
- in: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=calm`
- in: Doran's Shield; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- in: Doran's Shield; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=calm`

### [inferred-relation] Buhru Captain

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- in: Wildclaw Shaman; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::optional:when=self_played`
- out: Wildclaw Shaman; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::optional:when=self_played`

### [inferred-relation] Bullet Time

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Last Breath; type `similar_effect`; strength 0.72; reason `secondary:damage:variable:unit[controller=opponent;location=battlefield]::required:active`
- out: Last Breath; type `similar_effect`; strength 0.72; reason `secondary:damage:variable:unit[controller=opponent;location=battlefield]::required:active`

### [inferred-relation] Bushwhack

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Black Market Broker; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Blood Money; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Black Market Broker; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Blood Money; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Draven, Vanquisher; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Eminent Benefactor; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`

### [inferred-relation] Caitlyn, Patrolling

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Ezreal, Dashing; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_my_might:damage::required:active`
- in: Get Excited!; type `similar_effect`; strength 0.72; reason `secondary:damage:variable:unit[location=battlefield]::required:active`
- in: Yasuo, Remorseful; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_my_might:damage::required:active`
- in: Yone, Blademaster; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_my_might:damage::required:active`
- out: Ezreal, Dashing; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_my_might:damage::required:active`
- out: Get Excited!; type `similar_effect`; strength 0.72; reason `secondary:damage:variable:unit[location=battlefield]::required:active`
- out: Yasuo, Remorseful; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_my_might:damage::required:active`
- out: Yone, Blademaster; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_my_might:damage::required:active`

### [inferred-relation] Call to Battle

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- out: Bard, Mercurial; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:required:active`
- out: Bard, Mercurial; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:battlefield:required:active`
- out: Bard, Mercurial; type `similar_effect`; strength 0.72; reason `secondary:move:unit[controller=friendly]:battlefield:required:active`
- in: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- in: Bard, Mercurial; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:required:active`
- in: Bard, Mercurial; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:battlefield:required:active`
- in: Bard, Mercurial; type `similar_effect`; strength 0.72; reason `secondary:move:unit[controller=friendly]:battlefield:required:active`

### [inferred-relation] Call to Glory

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- in: Primal Strength; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- in: Punch First; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- in: Wallop; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:as an additional cost:::optional`
- out: Primal Strength; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Punch First; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Wallop; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:as an additional cost:::optional`

### [inferred-relation] Called Shot

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- in: Dramatic Visionary; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:2:card::::required:object=card[location=top;zone...`
- in: Scryer's Bloom; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:2:card::::required:object=card[location=top;zone...`
- in: The Candlelit Sanctum; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:2:card::::required:object=card[location=top;zone...`
- out: Dramatic Visionary; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:2:card::::required:object=card[location=top;zone...`
- out: Scryer's Bloom; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:2:card::::required:object=card[location=top;zone...`
- out: The Candlelit Sanctum; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:2:card::::required:object=card[location=top;zone...`

### [inferred-relation] Calm Rune

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Body Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Body Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Chaos Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Fury Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Mind Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Order Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- out: Chaos Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- out: Fury Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`

### [inferred-relation] Cannon Barrage

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent]::required:active`
- in: Katarina, Reckless; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[controller=opponent]:::re...`
- in: Ruined Rex; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent]::required:active`
- out: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent]::required:active`
- out: Katarina, Reckless; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[controller=opponent]:::re...`
- out: Ruined Rex; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent]::required:active`

### [inferred-relation] Card Sharp

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Pickpocket; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Trove Golem; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Pickpocket; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Trove Golem; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`

### [inferred-relation] Carnivorous Snapvine

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Challenge; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- in: Clash of Giants; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- in: Dragon's Rage; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- in: Gentlemen's Duel; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- in: Marching Orders; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- out: Challenge; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- out: Clash of Giants; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- out: Dragon's Rage; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`

### [inferred-relation] Carrion Dredger

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Catalyst of Aeons

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Tasty Faefolk; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:2:rune::::required`
- out: Tasty Faefolk; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:2:rune::::required`

### [inferred-relation] Cemetery Attendant

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Annie, Stubborn; type `similar_effect`; strength 0.72; reason `secondary:move:hand[controller=friendly;zone=hand]:hand[controller=friendly]:required:a...`
- out: Annie, Stubborn; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active:when=self_...`
- out: Annie, Stubborn; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:required:active:w...`
- out: Annie, Stubborn; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand[controller=friendly]:required:active:when=self_played`
- out: Aspiring Engineer; type `similar_effect`; strength 0.72; reason `secondary:move:hand[controller=friendly;zone=hand]:hand[controller=friendly]:required:a...`
- out: Aspiring Engineer; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active:when=self_...`
- out: Aspiring Engineer; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:required:active:w...`
- out: Aspiring Engineer; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand[controller=friendly]:required:active:when=self_played`

### [inferred-relation] Chakram Dancer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Block; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:shield:unit:temporary:required:active:require=durati...`
- out: Block; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:shield:unit:this_turn:required:active:require=duration=while,st...`
- in: Block; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:shield:unit:temporary:required:active:require=durati...`
- in: Block; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:shield:unit:this_turn:required:active:require=duration=while,st...`
- in: Fortified Position; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:shield:unit:temporary:required:active:require=durati...`
- out: Fortified Position; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:shield:unit:temporary:required:active:require=durati...`

### [inferred-relation] Challenge

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Carnivorous Snapvine; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- in: Carnivorous Snapvine; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- in: Clash of Giants; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- in: Dragon's Rage; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- in: Gentlemen's Duel; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- in: Marching Orders; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- out: Clash of Giants; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- out: Dragon's Rage; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`

### [inferred-relation] Chaos Rune

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Body Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- out: Calm Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Body Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Calm Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Fury Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Mind Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Order Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- out: Fury Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`

### [inferred-relation] Charm

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast Cone; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:unit[controller=opponent]:active`
- in: Blast Cone; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:unit[controller=opponent]:active`
- in: Dragon's Rage; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:::required`
- in: Skyward Strike; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:::required`
- in: Void Assault; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:::required`
- out: Dragon's Rage; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:::required`
- out: Skyward Strike; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:::required`
- out: Void Assault; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:::required`

### [inferred-relation] Chem-Baroness

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Battle Mistress; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::optional:obje...`
- in: Battle Mistress; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::optional:obje...`
- in: Chemtech Cask; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::optional:obje...`
- in: Jhin, Murderous Artist; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required`
- out: Chemtech Cask; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::optional:obje...`
- out: Jhin, Murderous Artist; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required`

### [inferred-relation] Chemtech Cask

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Annie, Stubborn; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Fizz, Trickster; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Kai'Sa, Evolutionary; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Annie, Stubborn; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Fizz, Trickster; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Kai'Sa, Evolutionary; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Battle Mistress; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::optional:obje...`
- out: Chem-Baroness; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::optional:obje...`

### [inferred-relation] Chemtech Enforcer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Bewitching Spirit; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- in: Bewitching Spirit; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- in: Evershade Stalker; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- in: Ezreal, Prodigy; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- in: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_attacker:active`
- in: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`

### [inferred-relation] Cithria of Cloudfield

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- in: Enthusiastic Promoter; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- in: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- in: Rally the Troops; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- in: Simian Ancestor; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- out: Enthusiastic Promoter; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- out: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`

### [inferred-relation] Clash of Giants

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Carnivorous Snapvine; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- out: Challenge; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- in: Carnivorous Snapvine; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- in: Challenge; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- in: Dragon's Rage; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- in: Gentlemen's Duel; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- in: Marching Orders; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- out: Dragon's Rage; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`

### [inferred-relation] Cleave

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blood Rush; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:unit::this_turn:req...`
- in: Blood Rush; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:unit::this_turn:req...`
- in: Lord Broadmane; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:assault:unit:this_turn:required:active:require=duration=while,s...`
- in: Lord Broadmane; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:assault:unit:temporary:required:active:require=durat...`
- in: Square Up; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:unit::this_turn:req...`
- in: Vault Breaker; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:assault:unit:this_turn:required:active:require=duration=while,s...`
- in: Vault Breaker; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:assault:unit:temporary:required:active:require=durat...`
- out: Lord Broadmane; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:assault:unit:this_turn:required:active:require=duration=while,s...`

### [inferred-relation] Clockwork Keeper

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Evershade Stalker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Insightful Investigator; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Kinkou Initiate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Lecturing Yordle; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Poro Herder; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Poro Snax; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Scuttle Crab; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Wuju Apprentice; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`

### [inferred-relation] Cloth Armor

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:when=self_played`
- in: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:when=self_played`
- in: Edge of Night; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:when=self_played`
- in: Edge of Night; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:when=self_played`

### [inferred-relation] Combat Chef

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Armed Assailant; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=g...`
- out: Armed Assailant; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:gear_cost_reduced:1:rune:gear[cont...`
- in: Armed Assailant; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=g...`
- in: Armed Assailant; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:gear_cost_reduced:1:rune:gear[cont...`

### [inferred-relation] Combat Experience

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Hwei, Brooding Painter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:card::this_turn...`
- in: Lux, Illuminated; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:card::this_turn...`
- in: Pridestalker; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:unit::this_turn...`
- in: Primal Strength; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- in: Punch First; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- in: Teemo, Scout; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:card::this_turn...`
- out: Hwei, Brooding Painter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:card::this_turn...`
- out: Lux, Illuminated; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:card::this_turn...`

### [inferred-relation] Commander Ledros

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Altar of Memories; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Spectral Centaur; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Vanguard Helm; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Vicious Snapjaws; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Viktor, Leader; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Altar of Memories; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Spectral Centaur; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Vanguard Helm; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`

### [inferred-relation] Concentrate

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Consult the Past; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Detonate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Drag Under; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Dunebreaker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Find Your Center; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Herald of Scales; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`

### [inferred-relation] Confront

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Wuju Master; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:entry_state:enter_ready:token_enters_ready:unit[controller=you...`
- out: Wuju Master; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:entry_state:enter_ready:token_enters_ready:unit[controller=you...`

### [inferred-relation] Conscription

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Highlander; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- in: Hostile Takeover; type `similar_effect`; strength 0.72; reason `output:event_produced:control_change:gain_control:control_gained:unit[controller=oppone...`
- in: Hostile Takeover; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- in: Mystic Reversal; type `similar_effect`; strength 0.72; reason `secondary:control_change:gain_control:gain:active`
- in: Possession; type `similar_effect`; strength 0.72; reason `output:event_produced:control_change:gain_control:control_gained:unit[controller=oppone...`
- in: Possession; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- in: Soraka, Wanderer; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- in: Symbol of the Solari; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:base:active`

### [inferred-relation] Consult the Past

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Concentrate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Detonate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Dunebreaker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Hidden Blade; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Lunar Boon; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Meditation; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Might of Demacia - Starter; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`

### [inferred-relation] Convergent Mutation

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Deathgrip; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:variable:active`
- in: Switcheroo; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:variable:active`
- out: Deathgrip; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:variable:active`
- out: Switcheroo; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:variable:active`

### [inferred-relation] Corina Veraza

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Corrupt Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Fae Porter; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Irresistible Faefolk; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Kato the Arm; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Mister Root; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Noxian Drummer; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Noxian Drummer; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:here[location...`
- in: Ribbon Dancer; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`

### [inferred-relation] Corrupt Enforcer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Corina Veraza; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Corina Veraza; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Fae Porter; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Glorious Executioner; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=combat_won`
- in: Hwei, Brooding Painter; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_moves`
- in: Irresistible Faefolk; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`

### [inferred-relation] Counter Strike

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Kayn, Unleashed; type `similar_effect`; strength 0.72; reason `secondary:prevent:damage_dealt:active`
- in: Unyielding Spirit; type `similar_effect`; strength 0.72; reason `secondary:prevent:damage_dealt:active`
- out: Kayn, Unleashed; type `similar_effect`; strength 0.72; reason `secondary:prevent:damage_dealt:active`
- out: Unyielding Spirit; type `similar_effect`; strength 0.72; reason `secondary:prevent:damage_dealt:active`

### [inferred-relation] Crackshot Corsair

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=here]::required:active:when...`
- out: Bellows Breath; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=here]::required:active:when...`
- in: Bellows Breath; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Elder Dragon; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Frozen Fortress; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Teemo, Strategist; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`

### [inferred-relation] Crescent Guardian

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Daisy!; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Direwing; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`

### [inferred-relation] Crescent Strike

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mischievous Marai; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=here]::required:active`
- in: Monster Harpoon; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:4:damage::required:active`
- in: Rocket Barrage; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:4:damage::required:active`
- in: Sudden Storm; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:4:damage::required:active`
- in: Twisted Fate, Gambler; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=here]::required:active`
- in: Void Seeker; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:4:damage::required:active`
- out: Mischievous Marai; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=here]::required:active`
- out: Monster Harpoon; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:4:damage::required:active`

### [inferred-relation] Crimson Pigeons

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Sivir, Mercenary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card:::required`
- in: Wielder of Water; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card:::required`
- out: Sivir, Mercenary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card:::required`
- out: Wielder of Water; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card:::required`

### [inferred-relation] Crowd Favorite

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- in: Enthralling Protector; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:cost=xp=2`
- in: Enthralling Protector; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- in: Enthralling Protector; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required...`
- in: Gemhand Hunter; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- in: Herald of Spring; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- in: Kha'Zix, Evolving Hunter; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`

### [inferred-relation] Cruel Patron

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Altar of Memories; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Spectral Centaur; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Vanguard Helm; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Vicious Snapjaws; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Viktor, Leader; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Altar of Memories; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Spectral Centaur; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Vanguard Helm; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`

### [inferred-relation] Cull

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Boots of Swiftness; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Boots of Swiftness; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=chaos`
- out: Boots of Swiftness; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=chaos`
- in: Boots of Swiftness; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`

### [inferred-relation] Cull the Weak

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- out: Blast of Power; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- out: Blood Money; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- in: Atakhan; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- in: Blast of Power; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- in: Blood Money; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- in: Drag Under; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- in: Fox-Fire; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`

### [inferred-relation] Cursed Sarcophagus

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Starhound; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::required:when=...`
- out: Starhound; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::required:when=...`

### [inferred-relation] Curtain Call

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Ahri, Inquisitive; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Arcane Shift; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Blast Corps Cadet; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Blood Rush; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=1`
- in: Ahri, Inquisitive; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- in: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Arcane Shift; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`

### [inferred-relation] Daisy!

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Crescent Guardian; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`

### [inferred-relation] Dancing Grenade

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Final Spark; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- in: Icathian Rain; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit:::required`
- in: Singularity; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- in: Super Mega Death Rocket!; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Final Spark; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Icathian Rain; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit:::required`
- out: Singularity; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Super Mega Death Rocket!; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`

### [inferred-relation] Dangerous Duo

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Defiant Dance; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- in: Discipline; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- in: Divining Shells; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- in: Feral Strength; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- in: Undertitan; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:positive:active:when=self_played`
- in: Whiteflame Protector; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:positive:active:when=self_played`
- in: Whiteflame Protector; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active:when=self_p...`
- out: Defiant Dance; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`

### [inferred-relation] Daring Poro

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Black Rose Dignitary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Black Rose Dignitary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Kraken Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: LeBlanc, Fragmented; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Lucian, Gunslinger; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Petty Officer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Rek'Sai, Breacher; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Towering Pairofant; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`

### [inferred-relation] Darius, Executioner

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Baron Nashor; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]::static:active`
- in: Baron Nashor; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]::static:active`
- in: Dropboarder; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`
- in: Garen, Commander; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:might_modified:1:might:unit[contro...`
- in: Poppy, Paragon; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`
- in: Pyke, Dockside Butcher; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`
- in: Wuju Master; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]::static:active`
- out: Dropboarder; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`

### [inferred-relation] Darius, Trifarian

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Diana, No Longer Human; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Dune Drake; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Ember Monk; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Harpoon Squad; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Pyke, Dockside Butcher; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Spectral Centaur; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- out: Diana, No Longer Human; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- out: Dune Drake; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`

### [inferred-relation] Dark Child - Starter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune::required:active`
- in: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- in: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune::required:active`
- in: Ekko, Recurrent; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- in: Gentle Gemdragon; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:up to 2 runes:::required`
- in: Hwei, Brooding Painter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:up to 2 runes:::required`
- in: Sona, Harmonious; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`

### [inferred-relation] Daughter of the Void

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Fire Below the Mountain; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Seal of Discord; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Seal of Focus; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Seal of Insight; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Seal of Rage; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Seal of Strength; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Seal of Unity; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`

### [inferred-relation] Dauntless Vanguard

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:battlefield[controller=opponent]:play:active`
- in: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- in: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:battlefield[controller=opponent]:play:active`
- in: Deadbloom Predator; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:play:card:battlefield[controller=opponen...`
- in: Rengar, Trophy Hunter; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- in: Rengar, Trophy Hunter; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:battlefield[controller=opponent]:play:active`
- in: Stalking Wolf; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`

### [inferred-relation] Dazzling Aurora

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Arcane Shift; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- out: Ashe, Focused; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- out: Blind Fury; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- in: Arcane Shift; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- in: Ashe, Focused; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- in: Blind Fury; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`

### [inferred-relation] Deadbloom Predator

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:battlefield[controller=opponent]:play:active`
- out: Dauntless Vanguard; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:play:card:battlefield[controller=opponen...`
- in: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- in: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:battlefield[controller=opponent]:play:active`
- in: Dauntless Vanguard; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:play:card:battlefield[controller=opponen...`
- in: Rengar, Trophy Hunter; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- in: Rengar, Trophy Hunter; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:battlefield[controller=opponent]:play:active`

### [inferred-relation] Deadly Flourish

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Arcane Shift; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Cannon Barrage; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent]::required:active`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Arcane Shift; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Cannon Barrage; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent]::required:active`
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`

### [inferred-relation] Death from Below

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Dusk Rose Lab; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::optional`
- in: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::optional`
- in: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`
- in: Rumble, Hotheaded; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`
- in: Undying Legion; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`
- out: Dusk Rose Lab; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::optional`
- out: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::optional`
- out: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`

### [inferred-relation] Deathgrip

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Altar of Memories; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Spectral Centaur; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Vanguard Helm; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Vicious Snapjaws; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Viktor, Leader; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Altar of Memories; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Spectral Centaur; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Vanguard Helm; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`

### [inferred-relation] Deceiver

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Bashful Bloom; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Blood Rose; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::optional`
- in: Bashful Bloom; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Blood Rose; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::optional`

### [inferred-relation] Decisive Strike

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Back to Back; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit[controller...`
- in: Back to Back; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit[controller...`
- in: Frigid Jewel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit[controller...`
- in: Grand Strategem; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- in: Inviolus Vox; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- in: Undertitan; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Frigid Jewel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit[controller...`
- out: Grand Strategem; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`

### [inferred-relation] Defiant Dance

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Dangerous Duo; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- in: Dangerous Duo; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- in: Discipline; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- in: Divining Shells; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- in: Feral Strength; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- in: Primal Strength; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- in: Punch First; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Discipline; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`

### [inferred-relation] Defy

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Abandon; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Flurry of Feathers; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Hard Bargain; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Lilting Lullaby; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Riposte; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Wind Wall; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- out: Flurry of Feathers; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`

### [inferred-relation] Demacian Diplomat

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Scrutinizing Sergeant; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_played`
- in: Shepherd's Heirloom; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_played`
- out: Scrutinizing Sergeant; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_played`
- out: Shepherd's Heirloom; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_played`

### [inferred-relation] Desert's Call

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arise!; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sand_soldier_unit_token_created::::requi...`
- out: Bonds of Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Arise!; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sand_soldier_unit_token_created::::requi...`
- in: Bonds of Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Double Trouble; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Downstage Dramatics; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Existential Dread; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Feral Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`

### [inferred-relation] Determined Sentry

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Minotaur Reckoner; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:restriction:prevent:unit:base:::prevented=move`
- in: Vilemaw's Lair; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:active`
- in: Vilemaw's Lair; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:::active`
- in: Vilemaw's Lair; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:unit:::active`
- out: Minotaur Reckoner; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:restriction:prevent:unit:base:::prevented=move`
- out: Vilemaw's Lair; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:::active`
- out: Vilemaw's Lair; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:active`
- out: Vilemaw's Lair; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:unit:::active`

### [inferred-relation] Detonate

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Acceptable Losses; type `similar_effect`; strength 0.72; reason `secondary:removal:gear_dies:gear:required:active`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Consult the Past; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Acceptable Losses; type `similar_effect`; strength 0.72; reason `secondary:removal:gear_dies:gear:required:active`
- in: Concentrate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Consult the Past; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Dunebreaker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Hidden Blade; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`

### [inferred-relation] Diana, Lunari

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Abandon; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- out: Apprentice Smith; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`
- out: Blind Fury; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`
- in: Abandon; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- in: Apprentice Smith; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`
- in: Blind Fury; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`

### [inferred-relation] Diana, No Longer Human

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Annie, Stubborn; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Fizz, Trickster; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Kai'Sa, Evolutionary; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Annie, Stubborn; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Fizz, Trickster; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Kai'Sa, Evolutionary; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Darius, Trifarian; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Darius, Trifarian; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`

### [inferred-relation] Direwing

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Crescent Guardian; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Daisy!; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`

### [inferred-relation] Disarming Rake

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Pickpocket; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::optional:when=self_played`
- out: Pickpocket; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::optional:when=self_played`

### [inferred-relation] Discipline

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Dangerous Duo; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- out: Defiant Dance; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- in: Dangerous Duo; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- in: Defiant Dance; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- in: Divining Shells; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- in: Feral Strength; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- in: Primal Strength; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- in: Punch First; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`

### [inferred-relation] Disintegrate

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- in: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`

### [inferred-relation] Disposal Order

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`

### [inferred-relation] Divine Judgment

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`

### [inferred-relation] Divining Shells

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Dangerous Duo; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- out: Deadly Flourish; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required:cost=action=exhaust:...`
- out: Defiant Dance; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- out: Discipline; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- in: Dangerous Duo; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- in: Deadly Flourish; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required:cost=action=exhaust:...`

### [inferred-relation] Doran's Blade

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Hexdrinker; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- in: Hexdrinker; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=body`
- in: Hexdrinker; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=body`
- in: Hunter's Machete; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`

### [inferred-relation] Doran's Ring

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Boots of Swiftness; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Boots of Swiftness; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=chaos`

### [inferred-relation] Doran's Shield

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=calm`
- out: Brutalizer; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Brutalizer; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=calm`
- out: Brutalizer; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=calm`

### [inferred-relation] Double Trouble

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Bonds of Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Desert's Call; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Bonds of Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Desert's Call; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Downstage Dramatics; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Existential Dread; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`

### [inferred-relation] Downstage Dramatics

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bonds of Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Desert's Call; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Double Trouble; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Bonds of Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Desert's Call; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Double Trouble; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Existential Dread; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- in: Feral Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`

### [inferred-relation] Downwell

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`

### [inferred-relation] Dr. Mundo, Expert

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- in: Draven, Showboat; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- in: Draven, Showboat; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:variable:active`
- in: Garbage Grabber; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:3:card:card[zone=trash]:::required`
- in: Ornn, Forge God; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- in: Petal Pixie; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- in: Sett, Kingpin; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`

### [inferred-relation] Drag Under

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast of Power; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Blood Money; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Cull the Weak; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- in: Blast of Power; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- in: Blood Money; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- in: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`

### [inferred-relation] Dragon's Rage

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast Cone; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:unit[controller=opponent]:active`
- out: Carnivorous Snapvine; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- out: Challenge; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- out: Charm; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:::required`
- out: Clash of Giants; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- in: Blast Cone; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:unit[controller=opponent]:active`
- in: Carnivorous Snapvine; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- in: Challenge; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`

### [inferred-relation] Dragonsoul Sage

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Energy Conduit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Hand of Noxus; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Scorn of the Moon; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- out: Energy Conduit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- out: Hand of Noxus; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- out: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- out: Scorn of the Moon; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`

### [inferred-relation] Dramatic Visionary

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Draven, Audacious

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Draven, Showboat

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Dr. Mundo, Expert; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- out: Dr. Mundo, Expert; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:variable:active`
- in: Dr. Mundo, Expert; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- in: Dr. Mundo, Expert; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:variable:active`
- in: Ornn, Forge God; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- in: Petal Pixie; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- in: Sett, Kingpin; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- out: Ornn, Forge God; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`

### [inferred-relation] Draven, Vanquisher

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Black Market Broker; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Blood Money; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Bushwhack; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Black Market Broker; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Blood Money; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Bushwhack; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`

### [inferred-relation] Dropboarder

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Darius, Executioner; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`
- in: Darius, Executioner; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`
- in: Poppy, Paragon; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`
- in: Pyke, Dockside Butcher; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`
- out: Poppy, Paragon; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`
- out: Pyke, Dockside Butcher; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`

### [inferred-relation] Dune Drake

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bashful Bloom; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Blood Rose; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Darius, Trifarian; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Diana, No Longer Human; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Bashful Bloom; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Blood Rose; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Darius, Trifarian; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`

### [inferred-relation] Dunebreaker

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Consult the Past; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Crescent Guardian; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Daisy!; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Detonate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`

### [inferred-relation] Dusk Rose Lab

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Death from Below; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::optional`
- in: Death from Below; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::optional`
- in: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::optional`
- out: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::optional`
- in: Altar of Memories; type `enabled_by`; strength 0.7; reason `generic_unit_death_enables_friendly_unit_dies`
- in: Battle Mistress; type `enabled_by`; strength 0.7; reason `generic_unit_death_enables_enemy_unit_dies`
- in: Spectral Centaur; type `enabled_by`; strength 0.7; reason `generic_unit_death_enables_friendly_unit_dies`
- in: Vanguard Helm; type `enabled_by`; strength 0.7; reason `generic_unit_death_enables_friendly_unit_dies`

### [inferred-relation] Eager Apprentice

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- out: Bashful Bloom; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- out: Battering Ram; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- in: Atakhan; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- in: Bashful Bloom; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- in: Battering Ram; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- in: Rhasa the Sunderer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- out: Rhasa the Sunderer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`

### [inferred-relation] Eager Drakehound

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Crescent Guardian; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Daisy!; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Direwing; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Dunebreaker; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- in: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`

### [inferred-relation] Eclipse

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Abandon; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Diana, Lunari; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- in: Abandon; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- in: Diana, Lunari; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`

### [inferred-relation] Eclipse Herald

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Back-Alley Bar; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Back-Alley Bar; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Existential Dread; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent]::this_...`
- in: Friendship; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Heroic Charge; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent]::this_...`
- in: Irelia, Fervent; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`

### [inferred-relation] Edge of Night

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:when=self_played`
- out: Boots of Swiftness; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Boots of Swiftness; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=chaos`
- out: Boots of Swiftness; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=chaos`

### [inferred-relation] Ekko, Recurrent

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Elder Dragon

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bellows Breath; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- out: Crackshot Corsair; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Bellows Breath; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Crackshot Corsair; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Frozen Fortress; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Teemo, Strategist; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- out: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`

### [inferred-relation] Ember Monk

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Darius, Trifarian; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- out: Diana, No Longer Human; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- out: Dune Drake; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Darius, Trifarian; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Diana, No Longer Human; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Dune Drake; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Harpoon Squad; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Pyke, Dockside Butcher; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`

### [inferred-relation] Eminent Benefactor

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Black Market Broker; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Blood Money; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Bushwhack; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Draven, Vanquisher; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Black Market Broker; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Blood Money; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`

### [inferred-relation] Emperor's Dais

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Downwell; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- in: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- in: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- in: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- in: Downwell; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`

### [inferred-relation] Emperor's Divide

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Overzealous Fan; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Reaver's Row; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Relentless Pursuit; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Sinister Poro; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Star Spring; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Symbol of the Solari; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:base:required:active`

### [inferred-relation] En Garde

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bonds of Strength; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:unit[controller...`
- in: Bonds of Strength; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:unit[controller...`
- in: Grand Strategem; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- in: Heroic Charge; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:unit[controller...`
- in: Inviolus Vox; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- in: Ribbon Dancer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:unit[controller...`
- in: Undertitan; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Grand Strategem; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`

### [inferred-relation] Energy Conduit

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Dragonsoul Sage; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Dragonsoul Sage; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Hand of Noxus; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Scorn of the Moon; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- out: Hand of Noxus; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- out: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- out: Scorn of the Moon; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`

### [inferred-relation] Enthralling Protector

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Crowd Favorite; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:cost=xp=2`
- out: Crowd Favorite; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- out: Crowd Favorite; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required...`
- in: Crowd Favorite; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:cost=xp=2`
- in: Crowd Favorite; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- in: Crowd Favorite; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required...`

### [inferred-relation] Enthusiastic Promoter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Cithria of Cloudfield; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- in: Cithria of Cloudfield; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- in: Fae Dragon; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:each a:::required`
- in: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- in: Rally the Troops; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- in: Simian Ancestor; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`

### [inferred-relation] Evelynn, Entrancing

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:optional:active`
- out: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:battlefield:optional:active`
- out: Bard, Mercurial; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active:when=self_played`
- in: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:optional:active`
- in: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:battlefield:optional:active`
- in: Bard, Mercurial; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active:when=self_played`
- in: Iascylla; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:battlefield::o...`
- in: Irresistible Faefolk; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:battlefield::o...`

### [inferred-relation] Evershade Stalker

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Bewitching Spirit; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- out: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- out: Clockwork Keeper; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Bewitching Spirit; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- in: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- in: Clockwork Keeper; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`

### [inferred-relation] Existential Dread

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Abandon; type `similar_effect`; strength 0.72; reason `output:payoff_output:movement:return_to_hand:unit_recalled:hand[zone=hand]:::required:o...`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`

### [inferred-relation] Experimental Hexplate

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Cloth Armor; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Cloth Armor; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=mind`
- out: Cloth Armor; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=mind`
- in: Cloth Armor; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`

### [inferred-relation] Eye of the Herald

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: B.F. Sword; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: B.F. Sword; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=order`
- out: B.F. Sword; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=order`
- out: Blade of the Ruined King; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`

### [inferred-relation] Ezreal, Dashing

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base[controller=friendly]:active`
- out: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base[controller=friendly]:required:active`
- out: Caitlyn, Patrolling; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_my_might:damage::required:active`
- in: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base[controller=friendly]:active`
- in: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base[controller=friendly]:required:active`
- in: Caitlyn, Patrolling; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_my_might:damage::required:active`
- in: Flash; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base[controller=friendly]:active`
- in: Flash; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base[controller=friendly]:required:active`

### [inferred-relation] Ezreal, Prodigy

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Bewitching Spirit; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- out: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- out: Evershade Stalker; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- in: Bewitching Spirit; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- in: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`
- in: Evershade Stalker; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_played`

### [inferred-relation] Facebreaker

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- in: Vilemaw; type `similar_effect`; strength 0.72; reason `secondary:prevent:deal_combat_damage:active`
- in: Vilemaw; type `similar_effect`; strength 0.72; reason `secondary:prevent:deal_combat_damage:::active`
- out: Vilemaw; type `similar_effect`; strength 0.72; reason `secondary:prevent:deal_combat_damage:active`
- out: Vilemaw; type `similar_effect`; strength 0.72; reason `secondary:prevent:deal_combat_damage:::active`

### [inferred-relation] Factory Recall

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`

### [inferred-relation] Fading Memories

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:temporary:unit:ongoing:required:active`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:temporary:unit:ongoing:required:active`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:temporary_grant:unit:ongoing:required:active`
- in: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:temporary:unit:ongoing:required:active`
- in: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:temporary:unit:ongoing:required:active`
- in: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:temporary_grant:unit:ongoing:required:active`
- in: Mirror Image; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:temporary:unit:ongoing:required:active`
- in: Mirror Image; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:temporary:unit:ongoing:required:active`

### [inferred-relation] Fae Dragon

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Black Market Broker; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Blood Money; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Bushwhack; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Draven, Vanquisher; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Eminent Benefactor; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`

### [inferred-relation] Fae Porter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move:unit[controller=friendly]:battlefield:optional:active`
- out: Corina Veraza; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Corrupt Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move:unit[controller=friendly]:battlefield:optional:active`
- in: Corina Veraza; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Corrupt Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Imposing Challenger; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active:when=self_moves`
- in: Imposing Challenger; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:optional:active:when=self_moves`

### [inferred-relation] Faithful Manufactor

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Vanguard Captain; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:here[location...`
- out: Vanguard Captain; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:here[location...`

### [inferred-relation] Falling Comet

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Disintegrate; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- in: Disintegrate; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- in: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- in: Hextech Ray; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- in: Incinerate; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- in: Iron Ballista; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`

### [inferred-relation] Falling Star

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Final Spark; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- in: Singularity; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`

### [inferred-relation] Fate Weaver

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- in: Ornn, Blacksmith; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:4:card::::required:object=card[location=top;zone...`
- out: Ornn, Blacksmith; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:4:card::::required:object=card[location=top;zone...`

### [inferred-relation] Feral Strength

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bonds of Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Dangerous Duo; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- out: Defiant Dance; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- out: Desert's Call; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Discipline; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- out: Divining Shells; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit::this_turn...`
- out: Double Trouble; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Downstage Dramatics; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`

### [inferred-relation] Ferrous Forerunner

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Fight or Flight

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Maddened Marauder; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit:base::required`
- in: Overzealous Fan; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Reaver's Row; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Relentless Pursuit; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Sinister Poro; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Star Spring; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`

### [inferred-relation] Final Spark

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bellows Breath; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Dancing Grenade; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Falling Star; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- in: Bellows Breath; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- in: Dancing Grenade; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- in: Falling Star; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- in: Icathian Rain; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- in: Singularity; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`

### [inferred-relation] Find Your Center

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Drag Under; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Concentrate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Drag Under; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`

### [inferred-relation] Fiora, Peerless

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Last Stand; type `similar_effect`; strength 0.72; reason `secondary:stat_multiplier:might:2:active`
- in: Vi, Hotheaded; type `similar_effect`; strength 0.72; reason `secondary:stat_multiplier:might:2:active`
- out: Last Stand; type `similar_effect`; strength 0.72; reason `secondary:stat_multiplier:might:2:active`
- out: Vi, Hotheaded; type `similar_effect`; strength 0.72; reason `secondary:stat_multiplier:might:2:active`

### [inferred-relation] Fiora, Victorious

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:card:ongoing:required:active`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:card:ongoing:required:active`
- in: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:card:ongoing:required:active`
- in: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:card:ongoing:required:active`
- in: Master Yi, Tempered; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:deflect:card:ongoing:required:active`
- in: Master Yi, Tempered; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:card:ongoing:required:active`
- in: Master Yi, Tempered; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:deflect:card:ongoing:required:active`
- in: Master Yi, Tempered; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:card:ongoing:required:active`

### [inferred-relation] Fiora, Worthy

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blade Dancer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- in: Blade Dancer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- in: Guards!; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- in: Mistfall; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- in: Overt Operation; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- out: Guards!; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- out: Mistfall; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- out: Overt Operation; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`

### [inferred-relation] Fire Below the Mountain

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Daughter of the Void; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Daughter of the Void; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Seal of Discord; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Seal of Focus; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Seal of Insight; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Seal of Rage; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Seal of Strength; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`

### [inferred-relation] Firestorm

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Arcane Shift; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:3:damage:unit[controller=opponent;locat...`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Arcane Shift; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:3:damage:unit[controller=opponent;locat...`
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`

### [inferred-relation] First Mate

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blood Rose; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit:::required`
- in: Blood Rose; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit:::required`
- in: Upstage Comedy; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit:::required`
- in: Wallop; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit:::required`
- out: Upstage Comedy; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit:::required`
- out: Wallop; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit:::required`

### [inferred-relation] Fizz, Trickster

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Abandoned Hall; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Chemtech Cask; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Diana, No Longer Human; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Forgotten Library; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Lady of Luminosity - Starter; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Lux, Illuminated; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Ravenbloom Student; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Revna the Lorekeeper; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`

### [inferred-relation] Flame Chompers

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bewitching Spirit; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Brazen Buccaneer; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Chemtech Enforcer; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Corrupt Enforcer; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Deceiver; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Doran's Ring; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Evershade Stalker; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Ezreal, Prodigy; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`

### [inferred-relation] Flash

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base[controller=friendly]:active`
- out: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base[controller=friendly]:required:active`
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Ezreal, Dashing; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base[controller=friendly]:active`
- out: Ezreal, Dashing; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base[controller=friendly]:required:active`
- out: Ezreal, Dashing; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:card:base[controller=friendly]:required:active`
- in: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base[controller=friendly]:active`
- in: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base[controller=friendly]:required:active`

### [inferred-relation] Flurry of Blades

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bellows Breath; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- out: Crackshot Corsair; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Disintegrate; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Elder Dragon; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- out: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- in: Bellows Breath; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Crackshot Corsair; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`

### [inferred-relation] Flurry of Feathers

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- out: Defy; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Abandon; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Defy; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Gutter Palace; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:bird_unit_token_created::::required:obje...`
- in: Hard Bargain; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Lilting Lullaby; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Riposte; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`

### [inferred-relation] Forbidding Waste

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Ahri, Inquisitive; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Eclipse; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- in: Ahri, Inquisitive; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- in: Eclipse; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- in: Frigid Touch; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- in: Icevale Archer; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`

### [inferred-relation] Forecaster

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Abandon; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- out: Diana, Lunari; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- out: Eclipse; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- in: Abandon; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- in: Diana, Lunari; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- in: Eclipse; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`

### [inferred-relation] Forge of the Fluft

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Forgotten Library; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`
- in: Marai Spire; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`
- in: Ornn's Forge; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`
- out: Forgotten Library; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`
- out: Marai Spire; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`
- out: Ornn's Forge; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`

### [inferred-relation] Forge of the Future

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Altar to Unity; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- in: Altar to Unity; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- in: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- in: Machine Evangel; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- in: Petricite Monument; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- in: Poro Snax; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- in: Recruit the Vanguard; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`

### [inferred-relation] Forgefire Cape

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Rabadon's Deathcrown; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- in: Rabadon's Deathcrown; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=any`
- in: Rabadon's Deathcrown; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=any`
- in: Recurve Bow; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[controller=opponent;locat...`

### [inferred-relation] Forgotten Library

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Annie, Stubborn; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Fizz, Trickster; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Kai'Sa, Evolutionary; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Annie, Stubborn; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Fizz, Trickster; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Kai'Sa, Evolutionary; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`

### [inferred-relation] Forgotten Monument

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Tianna Crownguard; type `similar_effect`; strength 0.72; reason `secondary:prevent:score:active`
- out: Tianna Crownguard; type `similar_effect`; strength 0.72; reason `secondary:prevent:score:active`

### [inferred-relation] Forgotten Signpost

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:active`
- out: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:required:active`
- in: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:active`
- in: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:required:active`
- in: Smoke and Mirrors; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:active`
- in: Smoke and Mirrors; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:required:active`
- in: Temptation; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:active`
- in: Temptation; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:required:active`

### [inferred-relation] Fortified Position

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Block; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:shield:unit:temporary:required:active:require=durati...`
- out: Chakram Dancer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:shield:unit:temporary:required:active:require=durati...`
- in: Block; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:shield:unit:temporary:required:active:require=durati...`
- in: Chakram Dancer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:shield:unit:temporary:required:active:require=durati...`

### [inferred-relation] Fox-Fire

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast of Power; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Blood Money; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Cull the Weak; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- out: Drag Under; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- in: Blast of Power; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- in: Blood Money; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- in: Cull the Weak; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- in: Drag Under; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`

### [inferred-relation] Friendship

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Back-Alley Bar; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Back-Alley Bar; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Irelia, Fervent; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Jinx, Rebel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Lillia, Protector of Dreams; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Mask of Foresight; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`

### [inferred-relation] Frigid Jewel

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Back to Back; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit[controller...`
- out: Decisive Strike; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit[controller...`
- in: Back to Back; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit[controller...`
- in: Decisive Strike; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:unit[controller...`
- in: Grand Strategem; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- in: Inviolus Vox; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- in: Undertitan; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Grand Strategem; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`

### [inferred-relation] Frigid Touch

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bonds of Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Desert's Call; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Double Trouble; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Downstage Dramatics; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Existential Dread; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Feral Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Forbidding Waste; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`

### [inferred-relation] Frostcoat Cub

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blastcone Fae; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:-2:might:unit::this_tur...`
- in: Blastcone Fae; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:-2:might:unit::this_tur...`
- in: Thousand-Tailed Watcher; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active:when=self_played`
- out: Thousand-Tailed Watcher; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active:when=self_played`

### [inferred-relation] Frozen Fortress

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bellows Breath; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- out: Crackshot Corsair; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- out: Elder Dragon; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- out: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Bellows Breath; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Crackshot Corsair; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Elder Dragon; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- in: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`

### [inferred-relation] Fury Rune

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Body Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- out: Calm Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- out: Chaos Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Body Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Calm Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Chaos Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Mind Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Order Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`

### [inferred-relation] Galio, Indefatigable

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Ezreal, Dashing; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:restriction:prevent:damage::::polarity=prevention`
- in: Ezreal, Dashing; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:restriction:prevent:damage::::polarity=prevention`

### [inferred-relation] Garbage Grabber

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Dr. Mundo, Expert; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:3:card:card[zone=trash]:::required`
- in: Dr. Mundo, Expert; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:3:card:card[zone=trash]:::required`

### [inferred-relation] Gardens of Becoming

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Alpha Strike; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Alpha Strike; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Keeper of the Hammer; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Nilah, Joyful Ascetic; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Scryer's Bloom; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Scuttle Crab; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Stare Down; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Vicious Snapjaws; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`

### [inferred-relation] Garen, Commander

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Baron Nashor; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]::static:active`
- out: Darius, Executioner; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:might_modified:1:might:unit[contro...`
- in: Baron Nashor; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]::static:active`
- in: Darius, Executioner; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:might_modified:1:might:unit[contro...`
- in: Wuju Master; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]::static:active`
- out: Wuju Master; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]::static:active`

### [inferred-relation] Garen, Rugged

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blue Sentinel; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_defender:active`
- out: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_attacker:active`
- in: Blue Sentinel; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_defender:active`
- in: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_attacker:active`
- in: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_attacker:active`
- in: Inferna; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_attacker:active`
- in: Jinx, Demolitionist; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_attacker:active`
- in: Laurent Duelist; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_attacker:active`

### [inferred-relation] Gem Jammer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bounty Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:unit::this_turn:req...`
- in: Bounty Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:unit::this_turn:req...`
- in: Megatusk; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:unit:temporary:required:active`
- in: Megatusk; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:unit:this_turn:required:active`
- in: Vault Breaker; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:unit:temporary:required:active`
- in: Vault Breaker; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:unit:this_turn:required:active`
- out: Megatusk; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:unit:temporary:required:active`
- out: Megatusk; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:unit:this_turn:required:active`

### [inferred-relation] Gemcraft Seer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Divining Shells; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional:w...`
- out: Divining Shells; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- in: Divining Shells; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional:w...`
- in: Divining Shells; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- in: Jeweled Colossus; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional:w...`
- in: Jeweled Colossus; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`

### [inferred-relation] Gemhand Hunter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Crowd Favorite; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- out: Enthralling Protector; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- in: Crowd Favorite; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- in: Enthralling Protector; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- in: Gustwalker; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- in: Herald of Spring; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- in: Kha'Zix, Evolving Hunter; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- in: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`

### [inferred-relation] Gentle Gemdragon

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune::required:active`
- out: Dark Child - Starter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:up to 2 runes:::required`
- out: Ekko, Recurrent; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- in: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- in: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune::required:active`
- in: Dark Child - Starter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:up to 2 runes:::required`
- in: Ekko, Recurrent; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`

### [inferred-relation] Gentlemen's Duel

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Carnivorous Snapvine; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- out: Challenge; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- out: Clash of Giants; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- out: Dragon's Rage; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- in: Carnivorous Snapvine; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- in: Challenge; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- in: Clash of Giants; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- in: Dragon's Rage; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`

### [inferred-relation] Get Excited!

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Caitlyn, Patrolling; type `similar_effect`; strength 0.72; reason `secondary:damage:variable:unit[location=battlefield]::required:active`
- in: Caitlyn, Patrolling; type `similar_effect`; strength 0.72; reason `secondary:damage:variable:unit[location=battlefield]::required:active`
- in: Gutter Palace; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- in: Lunar Boon; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- in: Square Up; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- in: Unlicensed Armory; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`

### [inferred-relation] Glasc Mixologist

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Gloomist

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Altar of Memories; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::optional:cost=action=exhaust:self`
- in: Altar of Memories; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::optional:cost=action=exhaust:self`

### [inferred-relation] Glorious Executioner

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Corrupt Enforcer; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=combat_won`
- in: Corrupt Enforcer; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=combat_won`
- in: Nidalee, Cat Form; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=combat_won`
- out: Nidalee, Cat Form; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=combat_won`

### [inferred-relation] Gold

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Deadly Flourish; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required:cost=action=exhaust:...`
- out: Deadly Flourish; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Divining Shells; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required:cost=action=exhaust:...`
- in: Deadly Flourish; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required:cost=action=exhaust:...`
- in: Deadly Flourish; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Divining Shells; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required:cost=action=exhaust:...`
- in: Pyke, Returned; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required:cost=action=exhaust:...`
- in: Pyke, Returned; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`

### [inferred-relation] Grand Duelist

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Relentless Storm; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::optional:cost=act...`
- out: Relentless Storm; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::optional:cost=act...`

### [inferred-relation] Grand Strategem

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Back to Back; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Bonds of Strength; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Decisive Strike; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: En Garde; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Frigid Jewel; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Gentlemen's Duel; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- in: Back to Back; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- in: Bonds of Strength; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`

### [inferred-relation] Grandmaster at Arms

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Angle Shot; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`
- out: Boneshiver; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Boneshiver; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`
- out: Boneshiver; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active`

### [inferred-relation] Green Father

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:positive:active:cost=action=exhaust:self`
- in: Arena Kingpin; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:positive:active:cost=action=exhaust:self`
- in: Heart of Dark Ice; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:positive:active:cost=action=exhaust:self`
- out: Heart of Dark Ice; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:positive:active:cost=action=exhaust:self`

### [inferred-relation] Grim Apothecary

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Angler Beast; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`
- out: Beast Below; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`
- in: Angler Beast; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`
- in: Beast Below; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`
- in: Windsinger; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:optional:active:when=self_played`
- in: Windsinger; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`
- in: Windsinger; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:optional:active:when=self_played`
- in: Windsinger; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:optional:active:when=self_played`

### [inferred-relation] Grim Resolve

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Gentlemen's Duel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:unit[controller...`
- out: Grand Strategem; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- in: Gentlemen's Duel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:unit[controller...`
- in: Grand Strategem; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- in: Herald of Spring; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required`
- in: Inviolus Vox; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- in: Kha'Zix, Mutating Horror; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required`
- in: Mister Root; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required`

### [inferred-relation] Guardian Angel

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=calm`
- out: Brutalizer; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Brutalizer; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=calm`
- out: Brutalizer; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=calm`

### [inferred-relation] Guardian of the Passage

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Guerilla Warfare; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active`
- in: Morbid Return; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active`
- in: Super Mega Death Rocket!; type `similar_effect`; strength 0.72; reason `secondary:move:hand[controller=friendly;zone=hand]:hand[controller=friendly]:optional:a...`
- in: Super Mega Death Rocket!; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active`
- in: Super Mega Death Rocket!; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:optional:active`
- in: Super Mega Death Rocket!; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand[controller=friendly]:optional:active`
- out: Guerilla Warfare; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active`
- out: Morbid Return; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active`

### [inferred-relation] Guards!

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arise!; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sand_soldier_unit_token_created::::requi...`
- out: Blade Dancer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- out: Desert's Call; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sand_soldier_unit_token_created::::requi...`
- out: Fiora, Worthy; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- in: Arise!; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sand_soldier_unit_token_created::::requi...`
- in: Blade Dancer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- in: Desert's Call; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sand_soldier_unit_token_created::::requi...`
- in: Fiora, Worthy; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`

### [inferred-relation] Guerilla Warfare

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Guardian of the Passage; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active`
- in: Guardian of the Passage; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active`
- in: Morbid Return; type `similar_effect`; strength 0.72; reason `secondary:move:hand[controller=friendly;zone=hand]:hand[controller=friendly]:required:a...`
- in: Morbid Return; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active`
- in: Morbid Return; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:required:active`
- in: Morbid Return; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand[controller=friendly]:required:active`
- in: Super Mega Death Rocket!; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active`
- out: Morbid Return; type `similar_effect`; strength 0.72; reason `secondary:move:hand[controller=friendly;zone=hand]:hand[controller=friendly]:required:a...`

### [inferred-relation] Gust

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`

### [inferred-relation] Gustwalker

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required:when=self_conqu...`
- out: Gemhand Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- in: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required:when=self_conqu...`
- in: Gemhand Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- in: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- in: Master Yi, Tempered; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required:when=self_conqu...`
- in: Mosstomper; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required:when=self_conqu...`
- in: Mosstomper; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`

### [inferred-relation] Gutter Palace

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flurry of Feathers; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:bird_unit_token_created::::required:obje...`
- out: Get Excited!; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- in: Flurry of Feathers; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:bird_unit_token_created::::required:obje...`
- in: Get Excited!; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- in: Lunar Boon; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- in: Square Up; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`

### [inferred-relation] Hall of Legends

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Royal Entourage; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:legend:active`
- out: Royal Entourage; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:legend:active`

### [inferred-relation] Hand of Noxus

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Dragonsoul Sage; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- out: Energy Conduit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Dragonsoul Sage; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Energy Conduit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Scorn of the Moon; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- out: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- out: Scorn of the Moon; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`

### [inferred-relation] Hard Bargain

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- out: Bonds of Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Defy; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- out: Desert's Call; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Double Trouble; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Downstage Dramatics; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Existential Dread; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Feral Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`

### [inferred-relation] Harnessed Dragon

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Battle Mistress; type `enabled_by`; strength 0.95; reason `enemy_unit_dies_enables_enemy_unit_dies`
- out: Battle Mistress; type `enables`; strength 0.95; reason `enemy_unit_dies_enables_enemy_unit_dies`
- in: Sandshifter; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:enemy_unit_dies:unit[controller=opponent]:::required:...`
- out: Sandshifter; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:enemy_unit_dies:unit[controller=opponent]:::required:...`

### [inferred-relation] Harpoon Squad

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Darius, Trifarian; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- out: Diana, No Longer Human; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- out: Dune Drake; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- out: Ember Monk; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Darius, Trifarian; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Diana, No Longer Human; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Dune Drake; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Ember Monk; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`

### [inferred-relation] Heart of Dark Ice

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:unit::this_turn...`
- out: Green Father; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:positive:active:cost=action=exhaust:self`
- in: Arena Kingpin; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:unit::this_turn...`
- in: Green Father; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:positive:active:cost=action=exhaust:self`

### [inferred-relation] Heedless Resurrection

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Altar of Memories; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Spectral Centaur; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Vanguard Helm; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Vicious Snapjaws; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Viktor, Leader; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Altar of Memories; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Spectral Centaur; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Vanguard Helm; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`

### [inferred-relation] Herald of Scales

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Drag Under; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Find Your Center; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Concentrate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Drag Under; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Find Your Center; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`

### [inferred-relation] Herald of Spring

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Crowd Favorite; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- out: Enthralling Protector; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- out: Gemhand Hunter; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- out: Grim Resolve; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required`
- in: Crowd Favorite; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- in: Enthralling Protector; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- in: Gemhand Hunter; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- in: Grim Resolve; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required`

### [inferred-relation] Herald of the Arcane

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Vanguard Armory; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created::::required:o...`
- out: Vanguard Armory; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created::::required:o...`

### [inferred-relation] Here to Help

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Concentrate; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:card:active`
- in: Concentrate; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- in: Concentrate; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:card:active`
- in: Master Yi, Unstoppable; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- in: Master Yi, Unstoppable; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:card:active`
- in: Poppy, Defender of the Meek; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- in: Poppy, Defender of the Meek; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:card:active`

### [inferred-relation] Heroic Charge

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Bonds of Strength; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:unit[controller...`
- out: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent]::this_...`
- out: En Garde; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:unit[controller...`
- out: Existential Dread; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent]::this_...`
- out: Grand Strategem; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- in: Bonds of Strength; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:unit[controller...`

### [inferred-relation] Hexdrinker

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Doran's Blade; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Doran's Blade; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=body`
- out: Doran's Blade; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=body`
- in: Doran's Blade; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`

### [inferred-relation] Hextech Gauntlets

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Angle Shot; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`
- out: Boneshiver; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Boneshiver; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`
- out: Boneshiver; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active`

### [inferred-relation] Hextech Ray

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Disintegrate; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:3:damage:unit[location=battlefield]:::r...`
- out: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- in: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`

### [inferred-relation] Hidden Blade

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast of Power; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Blood Money; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Consult the Past; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Cull the Weak; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- out: Detonate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Drag Under; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Dunebreaker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`

### [inferred-relation] Highlander

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Conscription; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- in: Conscription; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- in: Hostile Takeover; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- in: Possession; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- in: Soraka, Wanderer; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- in: Soraka, Wanderer; type `similar_effect`; strength 0.72; reason `secondary:replacement:unit_dies:heal_exhaust_recall:active`
- in: Soraka, Wanderer; type `similar_effect`; strength 0.72; reason `secondary:replacement:unit_dies:heal_exhaust_recall:unit:active`
- in: Symbol of the Solari; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:base:active`

### [inferred-relation] Honest Broker

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Honeyfruit

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Daughter of the Void; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Dragonsoul Sage; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- out: Energy Conduit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- out: Fire Below the Mountain; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Hand of Noxus; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Daughter of the Void; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Dragonsoul Sage; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Energy Conduit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`

### [inferred-relation] Hostile Takeover

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Conscription; type `similar_effect`; strength 0.72; reason `output:event_produced:control_change:gain_control:control_gained:unit[controller=oppone...`
- out: Conscription; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- out: Highlander; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- in: Conscription; type `similar_effect`; strength 0.72; reason `output:event_produced:control_change:gain_control:control_gained:unit[controller=oppone...`
- in: Conscription; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- in: Highlander; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- in: Mystic Reversal; type `similar_effect`; strength 0.72; reason `secondary:control_change:gain_control:gain:active`
- in: Nami, Headstrong; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::required`

### [inferred-relation] Hunter's Machete

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Doran's Blade; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Doran's Blade; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=body`
- out: Doran's Blade; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=body`
- out: Hexdrinker; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`

### [inferred-relation] Hwei, Brooding Painter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune::required:active`
- out: Combat Experience; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:card::this_turn...`
- out: Corrupt Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_moves`
- out: Dark Child - Starter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:up to 2 runes:::required`
- out: Ekko, Recurrent; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`

### [inferred-relation] Iascylla

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- out: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:optional:active`
- out: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:battlefield:optional:active`
- out: Call to Battle; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- out: Evelynn, Entrancing; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:battlefield::o...`
- in: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- in: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:optional:active`
- in: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:battlefield:optional:active`

### [inferred-relation] Icathian Rain

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Dancing Grenade; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit:::required`
- out: Final Spark; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- in: Dancing Grenade; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit:::required`
- in: Final Spark; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- in: Singularity; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- in: Super Mega Death Rocket!; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Singularity; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Super Mega Death Rocket!; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`

### [inferred-relation] Icevale Archer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Ahri, Inquisitive; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Eclipse; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Forbidding Waste; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Frigid Touch; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- in: Ahri, Inquisitive; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- in: Eclipse; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`

### [inferred-relation] Immortal Phoenix

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Death from Below; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::optional`
- out: Death from Below; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`
- out: Dusk Rose Lab; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::optional`
- out: Flame Chompers; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card:::optional`
- out: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_attacker:active`
- in: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Death from Below; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::optional`

### [inferred-relation] Imperial Decree

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast of Power; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Blood Money; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Cull the Weak; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- out: Drag Under; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Fox-Fire; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Hidden Blade; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- in: Blast of Power; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- in: Blood Money; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`

### [inferred-relation] Imposing Challenger

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Fae Porter; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active:when=self_moves`
- out: Fae Porter; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:optional:active:when=self_moves`
- out: Fae Porter; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:battlefield:optional:active:when=self_moves`
- in: Fae Porter; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active:when=self_moves`
- in: Fae Porter; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:optional:active:when=self_moves`
- in: Fae Porter; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:battlefield:optional:active:when=self_moves`
- in: Irresistible Faefolk; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active:when=self_moves`
- in: Irresistible Faefolk; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:optional:active:when=self_moves`

### [inferred-relation] Incinerate

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast Corps Cadet; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- in: Blast Corps Cadet; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- in: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- in: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`

### [inferred-relation] Inferna

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_attacker:active`
- out: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_attacker:active`
- in: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Jinx, Demolitionist; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Laurent Duelist; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`

### [inferred-relation] Insightful Investigator

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Clockwork Keeper; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Evershade Stalker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Clockwork Keeper; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Evershade Stalker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Kinkou Initiate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Lecturing Yordle; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Mindsplitter; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:card[zone=hand]:::required:when=...`
- in: Poro Herder; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`

### [inferred-relation] Invert Timelines

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Premonition; type `similar_effect`; strength 0.72; reason `secondary:draw_cards:multi::required:active`
- in: Progress Day; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:4:card::::required`
- out: Premonition; type `similar_effect`; strength 0.72; reason `secondary:draw_cards:multi::required:active`
- out: Progress Day; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:4:card::::required`

### [inferred-relation] Inviolus Vox

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Back to Back; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Bonds of Strength; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Decisive Strike; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: En Garde; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Frigid Jewel; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Gentlemen's Duel; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Grand Strategem; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Grim Resolve; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`

### [inferred-relation] Irelia, Fervent

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Back-Alley Bar; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Friendship; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Back-Alley Bar; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Friendship; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Jinx, Rebel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Lillia, Protector of Dreams; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`

### [inferred-relation] Irelia, Graceful

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Vex, Cheerless; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction_exact:play_cost_reduced:energy:1:spell:active`
- out: Vex, Cheerless; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction_exact:play_cost_reduced:energy:1:spell:active`

### [inferred-relation] Iron Ballista

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast Corps Cadet; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Honeyfruit; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_exhausted:self_enters:card:::required`
- out: Incinerate; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- in: Blast Corps Cadet; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`

### [inferred-relation] Irresistible Faefolk

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Corina Veraza; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Corrupt Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Evelynn, Entrancing; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:battlefield::o...`
- out: Fae Porter; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::optional:when=self_moves`
- out: Fae Porter; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Fae Porter; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active:when=self_moves`
- out: Fae Porter; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:optional:active:when=self_moves`
- out: Fae Porter; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:battlefield:optional:active:when=self_moves`

### [inferred-relation] Isolate

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Janna, Savior; type `similar_effect`; strength 0.72; reason `secondary:move:unit[controller=opponent]:base:required:active`
- in: Overzealous Fan; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Reaver's Row; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Relentless Pursuit; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Sinister Poro; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- in: Star Spring; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`

### [inferred-relation] Ivern, Friend to All

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Ahri, Alluring; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Aspirant's Climb; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Draven, Audacious; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Ahri, Alluring; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Aspirant's Climb; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Draven, Audacious; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Power Nexus; type `similar_effect`; strength 0.72; reason `secondary:score_amount:1:point:active`
- in: Renata Glasc, Mastermind; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`

### [inferred-relation] Ivern, Nurturer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Double Trouble; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:3:card::::required:object=card[location=top;zone...`
- in: Double Trouble; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:3:card::::required:object=card[location=top;zone...`
- in: Ornn, Blacksmith; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::required:w...`
- in: Rift Herald; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:3:card::::required:object=card[location=top;zone...`
- in: Stacked Deck; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:3:card::::required:object=card[location=top;zone...`
- out: Ornn, Blacksmith; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::required:w...`

### [inferred-relation] Janna, Savior

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Isolate; type `similar_effect`; strength 0.72; reason `secondary:move:unit[controller=opponent]:base:required:active`
- in: Isolate; type `similar_effect`; strength 0.72; reason `secondary:move:unit[controller=opponent]:base:required:active`
- in: Maddened Marauder; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active:when=self_played`
- in: Maddened Marauder; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:required:active:when=self_played`
- in: Maddened Marauder; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:base:required:active:when=self_played`
- in: Stare Down; type `similar_effect`; strength 0.72; reason `secondary:move:unit[controller=opponent]:base:required:active`
- out: Maddened Marauder; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active:when=self_played`
- out: Maddened Marauder; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:required:active:when=self_played`

### [inferred-relation] Jaull-Fish

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Drag Under; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Find Your Center; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Herald of Scales; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Concentrate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Drag Under; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`

### [inferred-relation] Jax, Unmatched

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:when=self_played`
- out: Cloth Armor; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Cloth Armor; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:when=self_played`
- out: Cloth Armor; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:when=self_played`

### [inferred-relation] Jax, Unrelenting

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Akshan, Mischievous; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Angle Shot; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Armed Assailant; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Azir, Ascendant; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: B.F. Sword; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Blighted Battleaxe; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Boneshiver; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`

### [inferred-relation] Jeweled Colossus

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Divining Shells; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional:w...`
- out: Divining Shells; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- out: Gemcraft Seer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional:w...`
- out: Gemcraft Seer; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- in: Divining Shells; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional:w...`
- in: Divining Shells; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`

### [inferred-relation] Jhin, Meticulous Killer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Divining Shells; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional:w...`
- out: Divining Shells; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- out: Gemcraft Seer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional:w...`
- out: Gemcraft Seer; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- out: Jeweled Colossus; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional:w...`

### [inferred-relation] Jhin, Murderous Artist

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Chem-Baroness; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required`
- out: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- in: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- in: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- in: Chem-Baroness; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required`
- in: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`

### [inferred-relation] Jinx, Demolitionist

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_attacker:active`
- out: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Inferna; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_attacker:active`

### [inferred-relation] Jinx, Rebel

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Back-Alley Bar; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Friendship; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Irelia, Fervent; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Back-Alley Bar; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Friendship; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Irelia, Fervent; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`

### [inferred-relation] Kadregrin the Infernal

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Show of Strength; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:per=your [Mighty] units`
- out: Show of Strength; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:per=your [Mighty] units`

### [inferred-relation] Kai'Sa, Evolutionary

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- in: Abandoned Hall; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Chemtech Cask; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Diana, No Longer Human; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Forgotten Library; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Lady of Luminosity - Starter; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Lux, Illuminated; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`

### [inferred-relation] Kai'Sa, Survivor

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Qiyana, Victorious; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_conquers`
- out: Qiyana, Victorious; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_conquers`

### [inferred-relation] Karma, Channeler

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Apprentice Smith; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Assembly Rig; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Baited Hook; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Blind Fury; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Called Shot; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Dazzling Aurora; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Diana, Lunari; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`

### [inferred-relation] Katarina, Reckless

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Cannon Barrage; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[controller=opponent]:::re...`
- out: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent]::required:active`
- in: Cannon Barrage; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[controller=opponent]:::re...`
- in: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent]::required:active`
- in: Ruined Rex; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent]::required:active`
- out: Ruined Rex; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent]::required:active`

### [inferred-relation] Kato the Arm

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Corina Veraza; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Corrupt Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Fae Porter; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Irresistible Faefolk; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Corina Veraza; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Corrupt Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Fae Porter; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Irresistible Faefolk; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`

### [inferred-relation] Kayn, Unleashed

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Counter Strike; type `similar_effect`; strength 0.72; reason `secondary:prevent:damage_dealt:active`
- out: Jhin, Murderous Artist; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Kai'Sa, Evolutionary; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- in: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- in: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`

### [inferred-relation] Keeper of the Hammer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Alpha Strike; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- out: Gardens of Becoming; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Alpha Strike; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Gardens of Becoming; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Nilah, Joyful Ascetic; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Scryer's Bloom; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Scuttle Crab; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- in: Stare Down; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`

### [inferred-relation] Keeper's Verdict

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Altar of Memories; type `similar_effect`; strength 0.72; reason `secondary:move_output:deck_card_put_top_or_bottom:main_deck:active`
- in: Altar of Memories; type `similar_effect`; strength 0.72; reason `secondary:move_output:deck_card_put_top_or_bottom:main_deck:active`

### [inferred-relation] Kha'Zix, Evolving Hunter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Crowd Favorite; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- out: Enthralling Protector; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- out: Gemhand Hunter; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- out: Herald of Spring; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- in: Crowd Favorite; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- in: Enthralling Protector; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- in: Gemhand Hunter; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- in: Herald of Spring; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`

### [inferred-relation] Kha'Zix, Mutating Horror

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Draven, Vanquisher; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- out: Draven, Vanquisher; type `similar_effect`; strength 0.72; reason `secondary:stat_self:might_modified:might:positive:2:this_turn:active:when=self_attacks,...`
- out: Grim Resolve; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required`
- out: Herald of Spring; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required`
- in: Draven, Vanquisher; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- in: Draven, Vanquisher; type `similar_effect`; strength 0.72; reason `secondary:stat_self:might_modified:might:positive:2:this_turn:active:when=self_attacks,...`
- in: Grim Resolve; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required`
- in: Herald of Spring; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required`

### [inferred-relation] King's Edict

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast of Power; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Blood Money; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Cull the Weak; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- out: Drag Under; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Fox-Fire; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Hidden Blade; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Imperial Decree; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- in: Blast of Power; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`

### [inferred-relation] Kinkou Initiate

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Clockwork Keeper; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Evershade Stalker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Insightful Investigator; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Clockwork Keeper; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Evershade Stalker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Insightful Investigator; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Lecturing Yordle; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Poro Herder; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`

### [inferred-relation] Kinkou Monk

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Fae Dragon; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::requi...`
- in: Fae Dragon; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::requi...`
- in: Overt Operation; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:gets a +1 :rb_might: buff:::required`
- in: Pit Rookie; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::requi...`
- in: Spirit's Refuge; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::requi...`
- out: Overt Operation; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:gets a +1 :rb_might: buff:::required`

### [inferred-relation] Kog'Maw, Caustic

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Kraken Hunter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Black Rose Dignitary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Daring Poro; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Black Rose Dignitary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Daring Poro; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: LeBlanc, Fragmented; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Lucian, Gunslinger; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`

### [inferred-relation] Lady of Luminosity - Starter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Annie, Stubborn; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Fizz, Trickster; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Kai'Sa, Evolutionary; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Annie, Stubborn; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Fizz, Trickster; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Kai'Sa, Evolutionary; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Lux, Illuminated; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:restriction:cost_threshold:card::::costs=energy>=5:...`
- in: Virtuoso; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=spell_played`

### [inferred-relation] Last Breath

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bullet Time; type `similar_effect`; strength 0.72; reason `secondary:damage:variable:unit[controller=opponent;location=battlefield]::required:active`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Dune Drake; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Bullet Time; type `similar_effect`; strength 0.72; reason `secondary:damage:variable:unit[controller=opponent;location=battlefield]::required:active`
- in: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Dune Drake; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Piltover Enforcer; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Pirate's Haven; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit[controller=friendly]:::re...`

### [inferred-relation] Last Rites

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Angle Shot; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`
- out: Boneshiver; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`

### [inferred-relation] Last Stand

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Fiora, Peerless; type `similar_effect`; strength 0.72; reason `secondary:stat_multiplier:might:2:active`
- in: Fiora, Peerless; type `similar_effect`; strength 0.72; reason `secondary:stat_multiplier:might:2:active`
- in: Vi, Hotheaded; type `similar_effect`; strength 0.72; reason `secondary:stat_multiplier:might:2:active`
- in: Vi, Hotheaded; type `similar_effect`; strength 0.72; reason `secondary:stat_multiplier:might:2:this_turn::active`
- out: Vi, Hotheaded; type `similar_effect`; strength 0.72; reason `secondary:stat_multiplier:might:2:active`
- out: Vi, Hotheaded; type `similar_effect`; strength 0.72; reason `secondary:stat_multiplier:might:2:this_turn::active`

### [inferred-relation] Laurent Bladekeeper

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Jhin, Murderous Artist; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Kai'Sa, Evolutionary; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Kayn, Unleashed; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- in: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- in: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`

### [inferred-relation] Laurent Duelist

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_attacker:active`
- out: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Inferna; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Jinx, Demolitionist; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_attacker:active`
- in: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`

### [inferred-relation] LeBlanc, Fragmented

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Lecturing Yordle

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Clockwork Keeper; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Evershade Stalker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Insightful Investigator; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Kinkou Initiate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Clockwork Keeper; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Evershade Stalker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Insightful Investigator; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- in: Kinkou Initiate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`

### [inferred-relation] Lee Sin, Ascetic

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Cithria of Cloudfield; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- out: Enthusiastic Promoter; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- out: Gemhand Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Gustwalker; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Jeweled Colossus; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Cithria of Cloudfield; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`

### [inferred-relation] Lee Sin, Centered

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Soul Shepherd; type `similar_effect`; strength 0.72; reason `secondary:stat_no_location:might_modified:might:positive:unit[controller=friendly]::sta...`
- out: Soul Shepherd; type `similar_effect`; strength 0.72; reason `secondary:stat_no_location:might_modified:might:positive:unit[controller=friendly]::sta...`

### [inferred-relation] Legion Quartermaster

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`

### [inferred-relation] Leona, Determined

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Daisy!; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent;locatio...`
- out: Jeweled Colossus; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Daisy!; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent;locatio...`
- in: Jeweled Colossus; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`

### [inferred-relation] Leona, Zealot

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Ahri, Inquisitive; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Crescent Guardian; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Daisy!; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Direwing; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`

### [inferred-relation] Lillia, Fae Fawn

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bashful Bloom; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created::::required:ob...`
- in: Bashful Bloom; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created::::required:ob...`
- in: Sprite Burst; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created::::required:ob...`
- in: Sprite Call; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created::::required:ob...`
- out: Sprite Burst; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created::::required:ob...`
- out: Sprite Call; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created::::required:ob...`

### [inferred-relation] Lillia, Protector of Dreams

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Back-Alley Bar; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Friendship; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Irelia, Fervent; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Jinx, Rebel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Back-Alley Bar; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Friendship; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`

### [inferred-relation] Lilting Lullaby

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- out: Defy; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- out: Flurry of Feathers; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- out: Hard Bargain; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Abandon; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Defy; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Flurry of Feathers; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Hard Bargain; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`

### [inferred-relation] Lonely Poro

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Long Sword

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:when=self_played`
- out: Cloth Armor; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Cloth Armor; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:when=self_played`
- out: Cloth Armor; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:when=self_played`

### [inferred-relation] Lord Broadmane

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blood Rush; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:assault:unit:this_turn:required:active:require=duration=while,s...`
- out: Blood Rush; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:assault:unit:temporary:required:active:require=durat...`
- out: Cleave; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:assault:unit:this_turn:required:active:require=duration=while,s...`
- out: Cleave; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:assault:unit:temporary:required:active:require=durat...`
- in: Blood Rush; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:assault:unit:this_turn:required:active:require=duration=while,s...`
- in: Blood Rush; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:assault:unit:temporary:required:active:require=durat...`
- in: Cleave; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:assault:unit:this_turn:required:active:require=duration=while,s...`
- in: Cleave; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:assault:unit:temporary:required:active:require=durat...`

### [inferred-relation] Loyal Poro

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Loyal Pup

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:here:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:here:optional:active`
- in: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:here:active`
- in: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:here:optional:active`

### [inferred-relation] Lucian, Gunslinger

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Black Rose Dignitary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Daring Poro; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Kraken Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: LeBlanc, Fragmented; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Black Rose Dignitary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Daring Poro; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Kraken Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: LeBlanc, Fragmented; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`

### [inferred-relation] Lucian, Merciless

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Armed Assailant; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=g...`
- out: Armed Assailant; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:gear_cost_reduced:1:rune:gear[cont...`
- out: Combat Chef; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=g...`
- out: Combat Chef; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:gear_cost_reduced:1:rune:gear[cont...`

### [inferred-relation] Lunar Boon

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Consult the Past; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Detonate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Dunebreaker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Get Excited!; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- out: Gutter Palace; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`

### [inferred-relation] Lux, Crownguard

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Undertitan; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:2:energy::::required`
- out: Undertitan; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:2:energy::::required`

### [inferred-relation] Lux, Illuminated

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Annie, Stubborn; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Fizz, Trickster; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Kai'Sa, Evolutionary; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Annie, Stubborn; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Fizz, Trickster; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Kai'Sa, Evolutionary; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Combat Experience; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:card::this_turn...`
- out: Hwei, Brooding Painter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:card::this_turn...`

### [inferred-relation] Machine Evangel

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Maddened Marauder

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Fight or Flight; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit:base::required`
- out: Janna, Savior; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active:when=self_played`
- out: Janna, Savior; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:required:active:when=self_played`
- out: Janna, Savior; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:base:required:active:when=self_played`
- in: Fight or Flight; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit:base::required`
- in: Janna, Savior; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active:when=self_played`
- in: Janna, Savior; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:required:active:when=self_played`
- in: Janna, Savior; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:base:required:active:when=self_played`

### [inferred-relation] Maduli the Gatekeeper

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Moonfall; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield[controller=opponent]:active`
- in: Zenith Blade; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield[controller=opponent]:active`
- out: Moonfall; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield[controller=opponent]:active`
- out: Zenith Blade; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield[controller=opponent]:active`

### [inferred-relation] Mageseeker Investigator

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- out: Bard, Mercurial; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:required:active`
- out: Bard, Mercurial; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:battlefield:required:active`
- out: Call to Battle; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit:battlefield::required`
- out: Call to Battle; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- out: Call to Battle; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:required:active`
- out: Call to Battle; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:battlefield:required:active`
- in: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`

### [inferred-relation] Mageseeker Warden

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`
- in: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`
- in: Miss Fortune, Buccaneer; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`
- in: Rockfall Path; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`
- out: Miss Fortune, Buccaneer; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`
- out: Rockfall Path; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`

### [inferred-relation] Magma Wurm

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bushwhack; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:entry_state:enter_ready:token_enters_ready:unit[controller=fri...`
- in: Bushwhack; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:entry_state:enter_ready:token_enters_ready:unit[controller=fri...`

### [inferred-relation] Malzahar, Fanatic

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Altar of Memories; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Spectral Centaur; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Vanguard Helm; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Vicious Snapjaws; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- in: Viktor, Leader; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Altar of Memories; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Spectral Centaur; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Vanguard Helm; type `enables`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`

### [inferred-relation] Marai Spire

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Forge of the Fluft; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`
- out: Forgotten Library; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`
- in: Forge of the Fluft; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`
- in: Forgotten Library; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`
- in: Ornn's Forge; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`
- out: Ornn's Forge; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`

### [inferred-relation] Marching Orders

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Carnivorous Snapvine; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- out: Challenge; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- out: Clash of Giants; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- out: Dragon's Rage; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- out: Gentlemen's Duel; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- in: Carnivorous Snapvine; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:mutual_might:each_other:active`
- in: Challenge; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`
- in: Clash of Giants; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to their mights:damage:eac...`

### [inferred-relation] Mask of Foresight

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Back-Alley Bar; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Friendship; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Irelia, Fervent; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Jinx, Rebel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Lillia, Protector of Dreams; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Back-Alley Bar; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- in: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`

### [inferred-relation] Master Bingwen

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Armed Assailant; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=g...`
- out: Armed Assailant; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:gear_cost_reduced:1:rune:gear[cont...`
- out: Combat Chef; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=g...`
- out: Combat Chef; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:gear_cost_reduced:1:rune:gear[cont...`

### [inferred-relation] Master Yi, Tempered

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required:when=self_conqu...`
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:card:ongoing:required:active`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:card:ongoing:required:active`
- out: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Fiora, Victorious; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:deflect:card:ongoing:required:active`
- out: Fiora, Victorious; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:card:ongoing:required:active`

### [inferred-relation] Master Yi, Unstoppable

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Alpha Wildclaw; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:::active`
- out: Alpha Wildclaw; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:active`
- out: Baron Nashor; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:restriction:prevent:card::::prevented=choose`
- out: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:4:energy:card:::...`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:card:active`

### [inferred-relation] Meditation

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Consult the Past; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Detonate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Dunebreaker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Hidden Blade; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Lunar Boon; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Concentrate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Consult the Past; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`

### [inferred-relation] Megatusk

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bounty Hunter; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:unit:temporary:required:active`
- out: Bounty Hunter; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:unit:this_turn:required:active`
- out: Gem Jammer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:unit:temporary:required:active`
- out: Gem Jammer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:unit:this_turn:required:active`
- in: Bounty Hunter; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:unit:temporary:required:active`
- in: Bounty Hunter; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:unit:this_turn:required:active`
- in: Gem Jammer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:unit:temporary:required:active`
- in: Gem Jammer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:unit:this_turn:required:active`

### [inferred-relation] Might of Demacia - Starter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Consult the Past; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Detonate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Dunebreaker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Hidden Blade; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Lunar Boon; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Meditation; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- in: Concentrate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`

### [inferred-relation] Mind Rune

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Body Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- out: Calm Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- out: Chaos Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- out: Fury Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Body Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Calm Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Chaos Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Fury Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`

### [inferred-relation] Mindsplitter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Insightful Investigator; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:card[zone=hand]:::required:when=...`
- in: Insightful Investigator; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:card[zone=hand]:::required:when=...`

### [inferred-relation] Minefield

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Virtuoso; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:card:trash:required:active`
- out: Virtuoso; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:card:trash:required:active`

### [inferred-relation] Minotaur Reckoner

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Determined Sentry; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:restriction:prevent:unit:base:::prevented=move`
- in: Determined Sentry; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:restriction:prevent:unit:base:::prevented=move`
- in: Vilemaw's Lair; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:::active`
- in: Vilemaw's Lair; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:active`
- in: Vilemaw's Lair; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:unit:::active`
- out: Vilemaw's Lair; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:::active`
- out: Vilemaw's Lair; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:active`
- out: Vilemaw's Lair; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:unit:::active`

### [inferred-relation] Mirror Image

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Deceiver; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:copy_effect:copy:card_copied:unit:::`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:temporary:unit:ongoing:required:active`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:temporary:unit:ongoing:required:active`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:temporary_grant:unit:ongoing:required:active`
- out: Dune Drake; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Fading Memories; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:temporary:unit:ongoing:required:active`
- out: Fading Memories; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:temporary:unit:ongoing:required:active`

### [inferred-relation] Mischievous Marai

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Crescent Strike; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=here]::required:active`
- in: Crescent Strike; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=here]::required:active`
- in: Twisted Fate, Gambler; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[controller=opponent;locat...`
- out: Twisted Fate, Gambler; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[controller=opponent;locat...`

### [inferred-relation] Miss Fortune, Buccaneer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit[controller=friendly]:active`
- out: Mageseeker Warden; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`
- in: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- in: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`
- in: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit[controller=friendly]:active`
- in: Mageseeker Warden; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`

### [inferred-relation] Miss Fortune, Captain

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Jhin, Murderous Artist; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Kai'Sa, Evolutionary; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Kayn, Unleashed; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Laurent Bladekeeper; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Master Yi, Tempered; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`

### [inferred-relation] Mister Root

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Corina Veraza; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Corrupt Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Fae Porter; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Grim Resolve; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required`
- out: Herald of Spring; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required`
- out: Irresistible Faefolk; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Kato the Arm; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Kha'Zix, Mutating Horror; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required`

### [inferred-relation] Mistfall

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Adaptatron; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Albus Ferros; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Aphelios, Exalted; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Arena Bar; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Blind Monk; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Buhru Captain; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Call to Glory; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Cithria of Cloudfield; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`

### [inferred-relation] Mobilize

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Find Your Center; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Find Your Center; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Obelisk of Power; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Party Favors; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Qiyana, Victorious; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Retreat; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`

### [inferred-relation] Monastery of Hirana

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- in: Sunken Temple; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::optional:when=battlefield_conq...`
- out: Sunken Temple; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::optional:when=battlefield_conq...`

### [inferred-relation] Monch

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Spoils of War; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction_exact:play_cost_reduced:energy:2:unit:active`
- out: Spoils of War; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction_exact:play_cost_reduced:energy:2:unit:active`

### [inferred-relation] Monster Harpoon

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast Corps Cadet; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Crescent Strike; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:4:damage::required:active`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Incinerate; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Iron Ballista; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- in: Blast Corps Cadet; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`

### [inferred-relation] Moonfall

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Ahri, Inquisitive; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:-2:might:unit[controlle...`
- out: Ahri, Inquisitive; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- out: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:optional:active`
- out: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:battlefield:optional:active`
- out: Call to Battle; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Eclipse; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`

### [inferred-relation] Moonlight Affliction

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Ahri, Inquisitive; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Eclipse; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Eclipse; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:negative:unit:this_turn:required:active`
- out: Forbidding Waste; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Frigid Touch; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Frigid Touch; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:negative:unit:this_turn:required:active`
- out: Icevale Archer; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`

### [inferred-relation] Morbid Return

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Cemetery Attendant; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:return_to_hand:card_returned_to_hand:hand[controller=you...`
- out: Guardian of the Passage; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active`
- out: Guerilla Warfare; type `similar_effect`; strength 0.72; reason `secondary:move:hand[controller=friendly;zone=hand]:hand[controller=friendly]:required:a...`
- out: Guerilla Warfare; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active`
- out: Guerilla Warfare; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:required:active`
- out: Guerilla Warfare; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand[controller=friendly]:required:active`
- in: Cemetery Attendant; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:return_to_hand:card_returned_to_hand:hand[controller=you...`
- in: Guardian of the Passage; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active`

### [inferred-relation] Mosstomper

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required:when=self_conqu...`
- out: Gemhand Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Gustwalker; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required:when=self_conqu...`
- out: Gustwalker; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Master Yi, Tempered; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required:when=self_conqu...`
- in: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required:when=self_conqu...`
- in: Gemhand Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`

### [inferred-relation] Mutated Mouser

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blue Sentinel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_defender:active`
- in: Blue Sentinel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_defender:active`
- in: Shen, Kinkou; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Towering Combatant; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Shen, Kinkou; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Towering Combatant; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`

### [inferred-relation] Mystic Poro

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Divining Shells; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional:w...`
- out: Divining Shells; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- out: Gemcraft Seer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional:w...`
- out: Gemcraft Seer; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- out: Jeweled Colossus; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional:w...`
- out: Jeweled Colossus; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`

### [inferred-relation] Mystic Reversal

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Conscription; type `similar_effect`; strength 0.72; reason `secondary:control_change:gain_control:gain:active`
- out: Hostile Takeover; type `similar_effect`; strength 0.72; reason `secondary:control_change:gain_control:gain:active`
- in: Conscription; type `similar_effect`; strength 0.72; reason `secondary:control_change:gain_control:gain:active`
- in: Hostile Takeover; type `similar_effect`; strength 0.72; reason `secondary:control_change:gain_control:gain:active`
- in: Possession; type `similar_effect`; strength 0.72; reason `secondary:control_change:gain_control:gain:active`
- out: Possession; type `similar_effect`; strength 0.72; reason `secondary:control_change:gain_control:gain:active`

### [inferred-relation] Nami, Headstrong

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent]::this_...`
- out: Existential Dread; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent]::this_...`
- out: Heroic Charge; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent]::this_...`
- out: Hostile Takeover; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::required`
- in: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent]::this_...`
- in: Existential Dread; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent]::this_...`

### [inferred-relation] Navori Fighting Pit

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`

### [inferred-relation] Needlessly Large Yordle

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Drag Under; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Find Your Center; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Herald of Scales; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Jaull-Fish; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Master Yi, Unstoppable; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`

### [inferred-relation] Nidalee, Cat Form

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Corrupt Enforcer; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=combat_won`
- out: Glorious Executioner; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=combat_won`
- in: Corrupt Enforcer; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=combat_won`
- in: Glorious Executioner; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=combat_won`

### [inferred-relation] Nilah, Joyful Ascetic

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Alpha Strike; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Gardens of Becoming; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- out: Jhin, Murderous Artist; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Kai'Sa, Evolutionary; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Kayn, Unleashed; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`

### [inferred-relation] Nocturne, Horrifying

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Jhin, Meticulous Killer; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:play:card:::optional`
- out: Jhin, Murderous Artist; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Kai'Sa, Evolutionary; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Kayn, Unleashed; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`

### [inferred-relation] Not So Fast

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Repulse; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell_or_ability[controlle...`
- out: Repulse; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell_or_ability[controlle...`

### [inferred-relation] Noxian Drummer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Corina Veraza; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Corina Veraza; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:here[location...`
- out: Corrupt Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Fae Porter; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Irresistible Faefolk; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Kato the Arm; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Mister Root; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- in: Corina Veraza; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`

### [inferred-relation] Noxian Guillotine

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast of Power; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Blood Money; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Cull the Weak; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- out: Drag Under; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Fox-Fire; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Hidden Blade; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Imperial Decree; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: King's Edict; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`

### [inferred-relation] Noxus Hopeful

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Drag Under; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Find Your Center; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Herald of Scales; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Jaull-Fish; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Master Yi, Unstoppable; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Needlessly Large Yordle; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`

### [inferred-relation] Obelisk of Power

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Find Your Center; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Mobilize; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Find Your Center; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Mobilize; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Party Favors; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Qiyana, Victorious; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`

### [inferred-relation] On the Hunt

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Dune Drake; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Dune Drake; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Piltover Enforcer; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Shurelya's Requiem; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit[controller=you]:::required`
- out: Piltover Enforcer; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Shurelya's Requiem; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit[controller=you]:::required`

### [inferred-relation] Orb of Regret

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Stupefy; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:-1:might:unit::this_tur...`
- out: Stupefy; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:-1:might:unit::this_tur...`

### [inferred-relation] Order Rune

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Body Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- out: Calm Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- out: Chaos Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- out: Fury Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- out: Mind Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Body Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Calm Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`
- in: Chaos Rune; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::`

### [inferred-relation] Ornn's Forge

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Forge of the Fluft; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`
- out: Forgotten Library; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`
- out: Marai Spire; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`
- in: Forge of the Fluft; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`
- in: Forgotten Library; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`
- in: Marai Spire; type `similar_effect`; strength 0.72; reason `secondary:require_state:you_control_this_battlefield:while:active`

### [inferred-relation] Ornn, Blacksmith

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Fate Weaver; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:4:card::::required:object=card[location=top;zone...`
- out: Ivern, Nurturer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::required:w...`
- in: Fate Weaver; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:4:card::::required:object=card[location=top;zone...`
- in: Ivern, Nurturer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::required:w...`

### [inferred-relation] Ornn, Forge God

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Armed Assailant; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=g...`
- out: Armed Assailant; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:gear_cost_reduced:1:rune:gear[cont...`
- out: Combat Chef; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=g...`
- out: Combat Chef; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:gear_cost_reduced:1:rune:gear[cont...`

### [inferred-relation] Overt Operation

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- out: Arena Bar; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- out: Blade Dancer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- out: Blind Monk; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- out: Fiora, Worthy; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`
- out: Guards!; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::optional`

### [inferred-relation] Overzealous Fan

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:optional:active`
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:base:optional:active`
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move:unit:base:optional:active`
- out: Emperor's Divide; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Fight or Flight; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Flash; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Isolate; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`

### [inferred-relation] Pack of Wonders

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`

### [inferred-relation] Party Favors

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Find Your Center; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Mobilize; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Obelisk of Power; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Find Your Center; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Mobilize; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Obelisk of Power; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`

### [inferred-relation] Peak Guardian

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Fae Dragon; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_played`
- in: Fae Dragon; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_played`
- in: Poro Herder; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_played`
- in: Sea Monkey; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_played`
- in: Trifarian Gloryseeker; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_played`
- out: Poro Herder; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_played`

### [inferred-relation] Perched Grimwyrm

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- in: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- in: Rengar, Pouncing; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:play:card:battlefield::required`
- in: Rengar, Trophy Hunter; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- in: Stalking Wolf; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- in: Stalking Wolf; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:battlefield:play:active`
- out: Rengar, Pouncing; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:play:card:battlefield::required`
- out: Rengar, Trophy Hunter; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`

### [inferred-relation] Petal Pixie

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Dr. Mundo, Expert; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- out: Draven, Showboat; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- out: Ornn, Forge God; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- in: Dr. Mundo, Expert; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- in: Draven, Showboat; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- in: Ornn, Forge God; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- in: Sett, Kingpin; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- out: Sett, Kingpin; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`

### [inferred-relation] Petricite Monument

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Allay, Eager Admirer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:deflect:unit:ongoing:required:active`
- out: Allay, Eager Admirer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:deflect:unit:ongoing:required:active`
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- out: Forge of the Future; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- in: Allay, Eager Admirer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:deflect:unit:ongoing:required:active`
- in: Allay, Eager Admirer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:deflect:unit:ongoing:required:active`
- in: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- in: Forge of the Future; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`

### [inferred-relation] Petty Officer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Black Rose Dignitary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Daring Poro; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Kraken Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: LeBlanc, Fragmented; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Lucian, Gunslinger; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Black Rose Dignitary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Daring Poro; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Kraken Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`

### [inferred-relation] Pickpocket

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Card Sharp; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Disarming Rake; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::optional:when=self_played`
- in: Card Sharp; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Disarming Rake; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::optional:when=self_played`
- in: Trove Golem; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Trove Golem; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`

### [inferred-relation] Piercing Light

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast Corps Cadet; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Incinerate; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Iron Ballista; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Monster Harpoon; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- in: Blast Corps Cadet; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`

### [inferred-relation] Piltover Enforcer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bashful Bloom; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Blood Rose; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Dune Drake; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Last Breath; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Mirror Image; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: On the Hunt; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Bashful Bloom; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`

### [inferred-relation] Pirate's Haven

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Back-Alley Bar; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Dune Drake; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Friendship; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Irelia, Fervent; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Jinx, Rebel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Last Breath; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit[controller=friendly]:::re...`

### [inferred-relation] Pit Rookie

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Fae Dragon; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::requi...`
- out: Kinkou Monk; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::requi...`
- in: Fae Dragon; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::requi...`
- in: Kinkou Monk; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::requi...`
- in: Spirit's Refuge; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::requi...`
- out: Spirit's Refuge; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::requi...`

### [inferred-relation] Plundering Poro

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Yeti Brawler; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Yeti Brawler; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`

### [inferred-relation] Poppy, Defender of the Meek

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Concentrate; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:card:active`
- out: Here to Help; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- out: Here to Help; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:card:active`
- out: Master Yi, Unstoppable; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- out: Master Yi, Unstoppable; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:card:active`
- in: Concentrate; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- in: Concentrate; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:card:active`

### [inferred-relation] Poppy, Paragon

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Darius, Executioner; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`
- out: Dropboarder; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`
- in: Darius, Executioner; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`
- in: Dropboarder; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`
- in: Pyke, Dockside Butcher; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`
- in: Voracious Gromp; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:3:xp::::required`
- out: Pyke, Dockside Butcher; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`
- out: Voracious Gromp; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:3:xp::::required`

### [inferred-relation] Poro Herder

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Clockwork Keeper; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Evershade Stalker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Fae Dragon; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_played`
- out: Insightful Investigator; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Kinkou Initiate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Lecturing Yordle; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`

### [inferred-relation] Poro Snax

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- out: Clockwork Keeper; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Evershade Stalker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Forge of the Future; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- out: Insightful Investigator; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Kinkou Initiate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Lecturing Yordle; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Petricite Monument; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`

### [inferred-relation] Portal Rescue

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arcane Shift; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:unit[controller=friendly]:::required`
- in: Arcane Shift; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:unit[controller=friendly]:::required`
- in: Thrill of the Hunt; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:unit[controller=friendly]:::required`
- out: Thrill of the Hunt; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:unit[controller=friendly]:::required`

### [inferred-relation] Possession

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Conscription; type `similar_effect`; strength 0.72; reason `output:event_produced:control_change:gain_control:control_gained:unit[controller=oppone...`
- out: Conscription; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- out: Highlander; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- out: Hostile Takeover; type `similar_effect`; strength 0.72; reason `output:event_produced:control_change:gain_control:control_gained:unit[controller=oppone...`
- out: Hostile Takeover; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- out: Mystic Reversal; type `similar_effect`; strength 0.72; reason `secondary:control_change:gain_control:gain:active`
- in: Conscription; type `similar_effect`; strength 0.72; reason `output:event_produced:control_change:gain_control:control_gained:unit[controller=oppone...`
- in: Conscription; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`

### [inferred-relation] Power Nexus

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Ahri, Alluring; type `similar_effect`; strength 0.72; reason `secondary:score_amount:1:point:active`
- out: Aspirant's Climb; type `similar_effect`; strength 0.72; reason `secondary:score_amount:1:point:active`
- out: Draven, Audacious; type `similar_effect`; strength 0.72; reason `secondary:score_amount:1:point:active`
- out: Ivern, Friend to All; type `similar_effect`; strength 0.72; reason `secondary:score_amount:1:point:active`
- in: Ahri, Alluring; type `similar_effect`; strength 0.72; reason `secondary:score_amount:1:point:active`
- in: Aspirant's Climb; type `similar_effect`; strength 0.72; reason `secondary:score_amount:1:point:active`
- in: Draven, Audacious; type `similar_effect`; strength 0.72; reason `secondary:score_amount:1:point:active`
- in: Ivern, Friend to All; type `similar_effect`; strength 0.72; reason `secondary:score_amount:1:point:active`

### [inferred-relation] Premonition

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Concentrate; type `similar_effect`; strength 0.72; reason `secondary:draw_cards:multi::required:active`
- out: Consult the Past; type `similar_effect`; strength 0.72; reason `secondary:draw_cards:multi::required:active`
- out: Detonate; type `similar_effect`; strength 0.72; reason `secondary:draw_cards:multi::required:active`
- out: Dunebreaker; type `similar_effect`; strength 0.72; reason `secondary:draw_cards:multi::required:active`
- out: Hidden Blade; type `similar_effect`; strength 0.72; reason `secondary:draw_cards:multi::required:active`
- out: Invert Timelines; type `similar_effect`; strength 0.72; reason `secondary:draw_cards:multi::required:active`
- out: Lunar Boon; type `similar_effect`; strength 0.72; reason `secondary:draw_cards:multi::required:active`
- out: Meditation; type `similar_effect`; strength 0.72; reason `secondary:draw_cards:multi::required:active`

### [inferred-relation] Prepared Neophyte

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Targonian Visionary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:4:might:card:::required`
- in: Yi, Meditative; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:4:might:card:::required`
- out: Targonian Visionary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:4:might:card:::required`
- out: Yi, Meditative; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:4:might:card:::required`

### [inferred-relation] Pridestalker

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Combat Experience; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:unit::this_turn...`
- in: Combat Experience; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:unit::this_turn...`
- in: Primal Strength; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- in: Punch First; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Primal Strength; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Punch First; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`

### [inferred-relation] Primal Strength

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Call to Glory; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Combat Experience; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Defiant Dance; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Discipline; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Divining Shells; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Feral Strength; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Pridestalker; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- in: Call to Glory; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`

### [inferred-relation] Prize of Progress

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Back-Alley Bar; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Friendship; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Irelia, Fervent; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Jinx, Rebel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Lillia, Protector of Dreams; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Mask of Foresight; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Pirate's Haven; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`

### [inferred-relation] Production Surge

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Assembly Rig; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:mech_unit_token_created:your_base[locati...`
- out: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Drag Under; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Ferrous Forerunner; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:mech_unit_token_created:your_base[locati...`
- out: Find Your Center; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Herald of Scales; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Jaull-Fish; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`

### [inferred-relation] Progress Day

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Invert Timelines; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:4:card::::required`
- out: Premonition; type `similar_effect`; strength 0.72; reason `secondary:draw_cards:multi::required:active`
- in: Invert Timelines; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:4:card::::required`
- in: Premonition; type `similar_effect`; strength 0.72; reason `secondary:draw_cards:multi::required:active`

### [inferred-relation] Promising Future

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Baited Hook; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:5:card::::required:object=card[location=top;zone...`
- in: Baited Hook; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:5:card::::required:object=card[location=top;zone...`
- in: Reinforce; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:5:card::::required:object=card[location=top;zone...`
- out: Reinforce; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:5:card::::required:object=card[location=top;zone...`

### [inferred-relation] Punch First

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Call to Glory; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Combat Experience; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Defiant Dance; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Discipline; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Divining Shells; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Feral Strength; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Pridestalker; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`
- out: Primal Strength; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active`

### [inferred-relation] Pyke, Dockside Butcher

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Darius, Executioner; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`
- out: Darius, Trifarian; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- out: Diana, No Longer Human; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`
- out: Dropboarder; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:self_ready:card:::required:when=self_played`
- out: Dune Drake; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::this_turn...`

### [inferred-relation] Pyke, Returned

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Altar of Memories; type `enabled_by`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- in: Spectral Centaur; type `enabled_by`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- in: Vanguard Helm; type `enabled_by`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- in: Vicious Snapjaws; type `enabled_by`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- in: Viktor, Leader; type `enabled_by`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- out: Altar of Memories; type `enables`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- out: Spectral Centaur; type `enables`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- out: Vanguard Helm; type `enables`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`

### [inferred-relation] Qiyana, Victorious

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Find Your Center; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Kai'Sa, Survivor; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_conquers`
- out: Mobilize; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Obelisk of Power; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Party Favors; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- in: Find Your Center; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`

### [inferred-relation] Rabadon's Deathcrown

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Forgefire Cape; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Forgefire Cape; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=any`
- out: Forgefire Cape; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=any`
- in: Forgefire Cape; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`

### [inferred-relation] Radiant Dawn

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Back Off; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Blast Cone; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Bone Skewer; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Daisy!; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Eclipse Herald; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Existential Dread; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Facebreaker; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Heroic Charge; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`

### [inferred-relation] Raging Firebrand

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Concentrate; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- out: Here to Help; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- out: Master Yi, Unstoppable; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- out: Poppy, Defender of the Meek; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- in: Concentrate; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- in: Here to Help; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- in: Master Yi, Unstoppable; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- in: Poppy, Defender of the Meek; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`

### [inferred-relation] Raging Soul

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Jhin, Murderous Artist; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Kai'Sa, Evolutionary; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Kayn, Unleashed; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Laurent Bladekeeper; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Master Yi, Tempered; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`

### [inferred-relation] Rally the Troops

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Cithria of Cloudfield; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- out: Enthusiastic Promoter; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- out: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- in: Cithria of Cloudfield; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- in: Enthusiastic Promoter; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- in: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`

### [inferred-relation] Ravenbloom Conservatory

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Apprentice Smith; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`
- out: Blind Fury; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`
- out: Diana, Lunari; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`
- in: Apprentice Smith; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`
- in: Blind Fury; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`
- in: Diana, Lunari; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:1:card::::required:object=card[location=top;zo...`

### [inferred-relation] Ravenbloom Student

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Annie, Stubborn; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Fizz, Trickster; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Kai'Sa, Evolutionary; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Annie, Stubborn; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Fizz, Trickster; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Kai'Sa, Evolutionary; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Back-Alley Bar; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`

### [inferred-relation] Reaver's Row

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:optional:active`
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:base:optional:active`
- out: Emperor's Divide; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Fight or Flight; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Flash; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Isolate; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Overzealous Fan; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`

### [inferred-relation] Rebuke

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`

### [inferred-relation] Recruit the Vanguard

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Altar to Unity; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- out: Forge of the Future; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- out: Machine Evangel; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- in: Altar to Unity; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- in: Forge of the Future; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- in: Machine Evangel; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- in: Viktor, Innovator; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- in: Viktor, Leader; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`

### [inferred-relation] Recurve Bow

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Forgefire Cape; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[controller=opponent;locat...`
- out: Long Sword; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Long Sword; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=fury`
- out: Long Sword; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=fury`

### [inferred-relation] Reflection

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:copy:card_copied:active`
- out: Mirror Image; type `similar_effect`; strength 0.72; reason `secondary:copy:card_copied:active`
- in: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:copy:card_copied:active`
- in: Mirror Image; type `similar_effect`; strength 0.72; reason `secondary:copy:card_copied:active`

### [inferred-relation] Reinforce

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Baited Hook; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:unit:::optional`
- out: Baited Hook; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:5:card::::required:object=card[location=top;zone...`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:card:active`
- out: Here to Help; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:active`
- out: Here to Help; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction:play_cost_reduced:energy:large:card:active`

### [inferred-relation] Rek'Sai, Breacher

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Black Rose Dignitary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Daring Poro; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Kraken Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: LeBlanc, Fragmented; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Lucian, Gunslinger; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Petty Officer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Black Rose Dignitary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Daring Poro; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`

### [inferred-relation] Rek'Sai, Swarm Queen

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- in: Twisted Fate, Gambler; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::required:w...`
- in: Void Burrower; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:one:::optional`
- in: Void Burrower; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:2:card::::optional:object=card[location=top;zo...`
- in: Void Rush; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:one:::optional`
- out: Twisted Fate, Gambler; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::required:w...`
- out: Void Burrower; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:one:::optional`

### [inferred-relation] Relentless Pursuit

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Altar of Blood; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:card:base:optional:active`
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:optional:active`
- out: Emperor's Divide; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Fight or Flight; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Flash; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Isolate; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Overzealous Fan; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`

### [inferred-relation] Relentless Storm

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Grand Duelist; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::optional:cost=act...`
- in: Grand Duelist; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::optional:cost=act...`

### [inferred-relation] Rell, Magnetic

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::required:object=gear`
- out: Angle Shot; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`
- out: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:card:active`
- out: Boneshiver; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`

### [inferred-relation] Renata Glasc, Mastermind

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Ahri, Alluring; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Aspirant's Climb; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Draven, Audacious; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Ivern, Friend to All; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Power Nexus; type `similar_effect`; strength 0.72; reason `secondary:score_amount:1:point:active`
- in: Ahri, Alluring; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Aspirant's Climb; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Draven, Audacious; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`

### [inferred-relation] Rengar, Pouncing

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_attacker:active`
- out: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Inferna; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Jinx, Demolitionist; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Laurent Duelist; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Perched Grimwyrm; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:play:card:battlefield::required`

### [inferred-relation] Rengar, Trophy Hunter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:battlefield[controller=opponent]:play:active`
- out: Dauntless Vanguard; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Dauntless Vanguard; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:battlefield[controller=opponent]:play:active`
- out: Deadbloom Predator; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Deadbloom Predator; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:battlefield[controller=opponent]:play:active`
- out: Jhin, Meticulous Killer; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Miss Fortune, Buccaneer; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`

### [inferred-relation] Rengar, Unseen

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Chemtech Enforcer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_attacker:active`
- out: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Inferna; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Jhin, Murderous Artist; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`

### [inferred-relation] Repulse

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Not So Fast; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell_or_ability[controlle...`
- in: Not So Fast; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell_or_ability[controlle...`

### [inferred-relation] Retreat

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`

### [inferred-relation] Revna the Lorekeeper

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Annie, Stubborn; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Fizz, Trickster; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Kai'Sa, Evolutionary; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Annie, Stubborn; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Fizz, Trickster; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Kai'Sa, Evolutionary; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`

### [inferred-relation] Rhasa the Sunderer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- out: Bashful Bloom; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- out: Battering Ram; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- out: Eager Apprentice; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- in: Atakhan; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- in: Bashful Bloom; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- in: Battering Ram; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`
- in: Eager Apprentice; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::...`

### [inferred-relation] Ribbon Dancer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bonds of Strength; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:unit[controller...`
- out: Corina Veraza; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Corrupt Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: En Garde; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:unit[controller...`
- out: Fae Porter; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:to a battlefield:::required:when=self_moves`
- out: Grand Strategem; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Heroic Charge; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:unit[controller...`
- out: Inviolus Vox; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`

### [inferred-relation] Ride the Wind

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Hostile Takeover; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::required`
- out: Nami, Headstrong; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::required`
- out: Relentless Pursuit; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=friendly]:::required`
- out: Relentless Pursuit; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:unit[controller=friendly]:active`
- in: Hostile Takeover; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::required`
- in: Nami, Headstrong; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:card:::required`
- in: Relentless Pursuit; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=friendly]:::required`
- in: Relentless Pursuit; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:unit[controller=friendly]:active`

### [inferred-relation] Rift Herald

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Right of Conquest

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Seat of Power; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:per=battlefield you o...`
- out: Seat of Power; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:per=battlefield you o...`

### [inferred-relation] Riposte

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- out: Defy; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- out: Flurry of Feathers; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- out: Hard Bargain; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- out: Lilting Lullaby; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Abandon; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Defy; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Flurry of Feathers; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`

### [inferred-relation] Ripper's Bay

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Startipped Peak; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::optional`
- out: Startipped Peak; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::optional`

### [inferred-relation] Riptide Rex

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arcane Shift; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=battlefield]::required:active`
- out: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:6:damage::required:active`
- out: Firestorm; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=battlefield]::required:active`
- in: Arcane Shift; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=battlefield]::required:active`
- in: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:6:damage::required:active`
- in: Firestorm; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=battlefield]::required:active`
- in: Shakedown; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:6:damage::required:active`
- in: Singularity; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:6:damage::required:active`

### [inferred-relation] Rocket Barrage

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Acceptable Losses; type `similar_effect`; strength 0.72; reason `secondary:removal:gear_dies:gear:required:active`
- out: Crescent Strike; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:4:damage::required:active`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=base]::required:active`
- out: Detonate; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::required`
- out: Monster Harpoon; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:4:damage::required:active`
- in: Acceptable Losses; type `similar_effect`; strength 0.72; reason `secondary:removal:gear_dies:gear:required:active`
- in: Crescent Strike; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:4:damage::required:active`
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=base]::required:active`

### [inferred-relation] Rockfall Path

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`
- out: Mageseeker Warden; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`
- out: Miss Fortune, Buccaneer; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`
- in: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`
- in: Mageseeker Warden; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`
- in: Miss Fortune, Buccaneer; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:unit:active`

### [inferred-relation] Royal Entourage

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Hall of Legends; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:legend:active`
- in: Hall of Legends; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:legend:active`

### [inferred-relation] Royal Guard

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Emperor's Dais; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sand_soldier_unit_token_created:here[loc...`
- in: Emperor's Dais; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sand_soldier_unit_token_created:here[loc...`

### [inferred-relation] Ruin Runner

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Alpha Wildclaw; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:::active`
- out: Alpha Wildclaw; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:active`
- out: Baron Nashor; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:restriction:prevent:card::::prevented=choose`
- out: Master Yi, Unstoppable; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:restriction:prevent:card::::prevented=choose`
- in: Alpha Wildclaw; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:active`
- in: Alpha Wildclaw; type `similar_effect`; strength 0.72; reason `secondary:prevent:choose:::active`
- in: Baron Nashor; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:restriction:prevent:card::::prevented=choose`
- in: Master Yi, Unstoppable; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:restriction:prevent:card::::prevented=choose`

### [inferred-relation] Ruined Rex

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Rumble, Hotheaded

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Death from Below; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`
- out: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`
- in: Death from Below; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`
- in: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`
- in: Undying Legion; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`
- out: Undying Legion; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`

### [inferred-relation] Rumble, Scrapper

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Assembly Rig; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:mech_unit_token_created:your_base[locati...`
- out: Ferrous Forerunner; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:mech_unit_token_created:your_base[locati...`
- out: Production Surge; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:mech_unit_token_created:your_base[locati...`
- in: Assembly Rig; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:mech_unit_token_created:your_base[locati...`
- in: Ferrous Forerunner; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:mech_unit_token_created:your_base[locati...`
- in: Production Surge; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:mech_unit_token_created:your_base[locati...`

### [inferred-relation] Rune Prison

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Back Off; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`
- in: Back Off; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`
- in: Solari Shieldbearer; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`
- in: Thwonk!; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`
- out: Solari Shieldbearer; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`
- out: Thwonk!; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`

### [inferred-relation] Sabotage

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`

### [inferred-relation] Sacred Shears

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Sacrifice

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Consult the Past; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Detonate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Dunebreaker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Find Your Center; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Hidden Blade; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Lunar Boon; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`

### [inferred-relation] Safety Inspector

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit[controller=opponent]:::required`
- out: Cull the Weak; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- in: Atakhan; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit[controller=opponent]:::required`
- in: Cull the Weak; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- in: Shard of Undoing; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit[controller=opponent]:::required`
- out: Shard of Undoing; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit[controller=opponent]:::required`
- in: Altar of Memories; type `enabled_by`; strength 0.7; reason `generic_unit_death_enables_friendly_unit_dies`
- in: Battle Mistress; type `enabled_by`; strength 0.7; reason `generic_unit_death_enables_enemy_unit_dies`

### [inferred-relation] Sai Scout

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Divining Shells; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional:w...`
- out: Divining Shells; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- out: Gemcraft Seer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional:w...`
- out: Gemcraft Seer; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:1:card::::required:object=card[location=top;zone...`
- out: Jeweled Colossus; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional:w...`

### [inferred-relation] Salvage

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Adaptatron; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::optional`
- in: Adaptatron; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::optional`

### [inferred-relation] Sandshifter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Battle Mistress; type `enabled_by`; strength 0.95; reason `enemy_unit_dies_enables_enemy_unit_dies`
- out: Battle Mistress; type `enables`; strength 0.95; reason `enemy_unit_dies_enables_enemy_unit_dies`
- out: Harnessed Dragon; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:enemy_unit_dies:unit[controller=opponent]:::required:...`
- in: Harnessed Dragon; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:enemy_unit_dies:unit[controller=opponent]:::required:...`

### [inferred-relation] Scorchclaw

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required:when=self_conqu...`
- out: Gemhand Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Gustwalker; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required:when=self_conqu...`
- out: Gustwalker; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Master Yi, Tempered; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required:when=self_conqu...`
- out: Mosstomper; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:2:xp::::required:when=self_conqu...`
- out: Mosstomper; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`

### [inferred-relation] Scorn of the Moon

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Dragonsoul Sage; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- out: Energy Conduit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- out: Hand of Noxus; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- out: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Dragonsoul Sage; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Energy Conduit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Hand of Noxus; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`
- in: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:energy::::required:c...`

### [inferred-relation] Scrapyard Champion

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Ezreal, Prodigy; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required:when=self_played`
- out: Jinx, Demolitionist; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:2:card::::required:when=self_played`
- in: Ezreal, Prodigy; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required:when=self_played`
- in: Jinx, Demolitionist; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:2:card::::required:when=self_played`

### [inferred-relation] Scrutinizing Sergeant

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Demacian Diplomat; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_played`
- in: Demacian Diplomat; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_played`
- in: Shepherd's Heirloom; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_played`
- out: Shepherd's Heirloom; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_played`

### [inferred-relation] Scryer's Bloom

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Alpha Strike; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- out: Called Shot; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:2:card::::required:object=card[location=top;zone...`
- out: Dramatic Visionary; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:2:card::::required:object=card[location=top;zone...`
- out: Forge of the Future; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- out: Gardens of Becoming; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`

### [inferred-relation] Scuttle Crab

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Sea Monkey

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Fae Dragon; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_played`
- out: Gemhand Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Gustwalker; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Mosstomper; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Peak Guardian; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_played`

### [inferred-relation] Seal of Discord

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Daughter of the Void; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Fire Below the Mountain; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Daughter of the Void; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Fire Below the Mountain; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Seal of Focus; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Seal of Insight; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`

### [inferred-relation] Seal of Focus

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Daughter of the Void; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Fire Below the Mountain; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Seal of Discord; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Daughter of the Void; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Fire Below the Mountain; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Seal of Discord; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`

### [inferred-relation] Seal of Insight

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Daughter of the Void; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Fire Below the Mountain; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Seal of Discord; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Seal of Focus; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Daughter of the Void; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Fire Below the Mountain; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`

### [inferred-relation] Seal of Rage

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Daughter of the Void; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Fire Below the Mountain; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Seal of Discord; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Seal of Focus; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Seal of Insight; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Daughter of the Void; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Fire Below the Mountain; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`

### [inferred-relation] Seal of Strength

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Daughter of the Void; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Fire Below the Mountain; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Seal of Discord; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Seal of Focus; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Seal of Insight; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Seal of Rage; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- in: Daughter of the Void; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`

### [inferred-relation] Seal of Unity

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Daughter of the Void; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Fire Below the Mountain; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Honeyfruit; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Seal of Discord; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Seal of Focus; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Seal of Insight; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Seal of Rage; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`
- out: Seal of Strength; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:add_resource:resource_added:1:rune::::required:cos...`

### [inferred-relation] Seat of Power

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Right of Conquest; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:per=battlefield you o...`
- in: Right of Conquest; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:per=battlefield you o...`

### [inferred-relation] Sentinel Adept

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Armed Assailant; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=g...`
- out: Armed Assailant; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:gear_cost_reduced:1:rune:gear[cont...`
- out: Combat Chef; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=g...`
- out: Combat Chef; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:gear_cost_reduced:1:rune:gear[cont...`

### [inferred-relation] Serrated Dirk

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Long Sword; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Long Sword; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=fury`
- out: Long Sword; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=fury`
- out: Recurve Bow; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`

### [inferred-relation] Sett, Brawler

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Adaptatron; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_conquers`
- in: Adaptatron; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_conquers`

### [inferred-relation] Sett, Kingpin

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Dr. Mundo, Expert; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- out: Draven, Showboat; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- out: Ornn, Forge God; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- out: Petal Pixie; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- in: Dr. Mundo, Expert; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- in: Draven, Showboat; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- in: Ornn, Forge God; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`
- in: Petal Pixie; type `similar_effect`; strength 0.72; reason `secondary:stat_self_scaling:might_modified:might:scaling:active`

### [inferred-relation] Shadow

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Crescent Guardian; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Daisy!; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Direwing; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`

### [inferred-relation] Shadow Watcher

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Crescent Guardian; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Daisy!; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Direwing; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Dunebreaker; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Eager Drakehound; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`

### [inferred-relation] Shadow's Call

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Consult the Past; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:temporary:unit:ongoing:required:active`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:temporary:unit:ongoing:required:active`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:temporary_grant:unit:ongoing:required:active`
- out: Detonate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Dunebreaker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Fading Memories; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:temporary:unit:ongoing:required:active`

### [inferred-relation] Shakedown

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Consult the Past; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Detonate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Dunebreaker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:6:damage::required:active`
- out: Hidden Blade; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Lunar Boon; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Meditation; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`

### [inferred-relation] Shard of Undoing

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit[controller=opponent]:::required`
- out: Cull the Weak; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- out: Safety Inspector; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit[controller=opponent]:::required`
- in: Atakhan; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit[controller=opponent]:::required`
- in: Cull the Weak; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- in: Safety Inspector; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit[controller=opponent]:::required`
- in: Altar of Memories; type `enabled_by`; strength 0.7; reason `generic_unit_death_enables_friendly_unit_dies`
- in: Battle Mistress; type `enabled_by`; strength 0.7; reason `generic_unit_death_enables_enemy_unit_dies`

### [inferred-relation] Shen, Kinkou

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blue Sentinel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_defender:active`
- out: Mutated Mouser; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Blue Sentinel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_defender:active`
- in: Mutated Mouser; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Towering Combatant; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Towering Combatant; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`

### [inferred-relation] Shepherd's Heirloom

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Angle Shot; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`
- out: Boneshiver; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Boneshiver; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`
- out: Boneshiver; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active`

### [inferred-relation] Show of Strength

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Kadregrin the Infernal; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:per=your [Mighty] units`
- in: Kadregrin the Infernal; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:per=your [Mighty] units`

### [inferred-relation] Showstopper

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- out: Bard, Mercurial; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:required:active`
- out: Call to Battle; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- out: Call to Battle; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:required:active`
- out: Iascylla; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- out: Mageseeker Investigator; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`

### [inferred-relation] Shurelya's Requiem

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Forgefire Cape; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Forgefire Cape; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=any`
- out: Forgefire Cape; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=any`
- out: On the Hunt; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit[controller=you]:::required`

### [inferred-relation] Sigil of the Storm

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Battle Mistress; type `enabled_by`; strength 0.9; reason `rune_recycled_enables_rune_recycled`
- out: Battle Mistress; type `enables`; strength 0.9; reason `rune_recycled_enables_rune_recycled`

### [inferred-relation] Simian Ancestor

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Cithria of Cloudfield; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- out: Enthusiastic Promoter; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- out: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- out: Rally the Troops; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- in: Cithria of Cloudfield; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`
- in: Enthusiastic Promoter; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required`

### [inferred-relation] Singularity

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bellows Breath; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Dancing Grenade; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:6:damage::required:active`
- out: Falling Star; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Final Spark; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Icathian Rain; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Riptide Rex; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:6:damage::required:active`
- out: Shakedown; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:6:damage::required:active`

### [inferred-relation] Sinister Poro

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:optional:active`
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:base:optional:active`
- out: Emperor's Divide; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Fight or Flight; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Flash; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Isolate; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Overzealous Fan; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`

### [inferred-relation] Siphon Power

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Against the Odds; type `similar_effect`; strength 0.72; reason `secondary:stat_no_location:might_modified:might:positive:unit[controller=friendly]:this...`
- in: Against the Odds; type `similar_effect`; strength 0.72; reason `secondary:stat_no_location:might_modified:might:positive:unit[controller=friendly]:this...`
- in: Yuumi, Magical Cat; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly;location=here]:th...`
- in: Yuumi, Magical Cat; type `similar_effect`; strength 0.72; reason `secondary:stat_no_location:might_modified:might:positive:unit[controller=friendly]:this...`
- out: Yuumi, Magical Cat; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly;location=here]:th...`
- out: Yuumi, Magical Cat; type `similar_effect`; strength 0.72; reason `secondary:stat_no_location:might_modified:might:positive:unit[controller=friendly]:this...`

### [inferred-relation] Sivir, Mercenary

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Crimson Pigeons; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card:::required`
- out: Jhin, Murderous Artist; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Kai'Sa, Evolutionary; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Kayn, Unleashed; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Laurent Bladekeeper; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`

### [inferred-relation] Sky Splitter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Disintegrate; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Hextech Ray; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Incinerate; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Iron Ballista; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Monster Harpoon; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`

### [inferred-relation] Skyfall of Areion

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Blighted Battleaxe; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Blighted Battleaxe; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=energy=1,rune=fury`
- out: Blighted Battleaxe; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=energy=1,rune=fury`
- in: Blighted Battleaxe; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`

### [inferred-relation] Skyward Strike

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Blast Cone; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:unit[controller=opponent]:active`
- out: Charm; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:::required`
- out: Dragon's Rage; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:::required`
- out: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent]::this_...`
- out: Existential Dread; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent]::this_...`
- out: Heroic Charge; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent]::this_...`

### [inferred-relation] Smite

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Arcane Shift; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- out: Ashe, Focused; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- out: Blind Fury; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Dazzling Aurora; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- out: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Disintegrate; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:3:damage:unit[location=battlefield]:::r...`

### [inferred-relation] Smoke and Mirrors

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:active`
- out: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:required:active`
- out: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:card:location:required:active`
- out: Forgotten Signpost; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:active`
- out: Forgotten Signpost; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:required:active`
- in: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:active`
- in: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:required:active`
- in: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:card:location:required:active`

### [inferred-relation] Smoke Screen

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Eclipse; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:-4:might:unit::this_tur...`
- out: Forbidding Waste; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Icevale Archer; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Leona, Zealot; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Moonfall; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Moonlight Affliction; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Moonlight Affliction; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:negative:unit:this_turn:required:active`

### [inferred-relation] Sneaky Deckhand

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Miss Fortune, Buccaneer; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:play:card:battlefield[state=open]::optional`
- out: Rengar, Trophy Hunter; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Sai Scout; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:play:card:battlefield[state=open]::optional`
- in: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- in: Miss Fortune, Buccaneer; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:play:card:battlefield[state=open]::optional`
- in: Rengar, Trophy Hunter; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- in: Sai Scout; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:play:card:battlefield[state=open]::optional`

### [inferred-relation] Soaring Scout

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Solari Chief

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Bone Skewer; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:card::this_turn:required`
- in: Bone Skewer; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:card::this_turn:required`
- in: Vex, Apathetic; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:card::this_turn:required`
- out: Vex, Apathetic; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:card::this_turn:required`

### [inferred-relation] Solari Shieldbearer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Back Off; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`
- out: Rune Prison; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`
- in: Back Off; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`
- in: Rune Prison; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`
- in: Thwonk!; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`
- out: Thwonk!; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`

### [inferred-relation] Sona, Harmonious

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- out: Dark Child - Starter; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- out: Ekko, Recurrent; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- out: Ekko, Recurrent; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune[controller=friendly]::required:active`
- out: Gentle Gemdragon; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- out: Hwei, Brooding Painter; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- in: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- in: Dark Child - Starter; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`

### [inferred-relation] Soraka, Wanderer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Conscription; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- out: Highlander; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- out: Highlander; type `similar_effect`; strength 0.72; reason `secondary:replacement:unit_dies:heal_exhaust_recall:active`
- out: Highlander; type `similar_effect`; strength 0.72; reason `secondary:replacement:unit_dies:heal_exhaust_recall:unit:active`
- out: Hostile Takeover; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- out: Possession; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- in: Conscription; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- in: Highlander; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`

### [inferred-relation] Soul Harvest

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast of Power; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Blood Money; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Cull the Weak; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- out: Drag Under; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Fox-Fire; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Hidden Blade; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Imperial Decree; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: King's Edict; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`

### [inferred-relation] Soul Shepherd

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Lee Sin, Centered; type `similar_effect`; strength 0.72; reason `secondary:stat_no_location:might_modified:might:positive:unit[controller=friendly]::sta...`
- in: Lee Sin, Centered; type `similar_effect`; strength 0.72; reason `secondary:stat_no_location:might_modified:might:positive:unit[controller=friendly]::sta...`

### [inferred-relation] Soul Sword

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=calm`
- out: Brutalizer; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Brutalizer; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=calm`
- out: Brutalizer; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=calm`

### [inferred-relation] Soulgorger

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Cemetery Attendant; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active:when=self_played`
- in: Cemetery Attendant; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active:when=self_played`
- in: Spectral Matron; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active:cost=ignored:when=self_played`
- in: Spectral Matron; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active:when=self_played`
- out: Spectral Matron; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active:cost=ignored:when=self_played`
- out: Spectral Matron; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active:when=self_played`

### [inferred-relation] Spectral Centaur

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Baited Hook; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Deathgrip; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`

### [inferred-relation] Spectral Matron

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Fizz, Trickster; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:restriction:cost_cap_constraint:card::::costs=cost<...`
- out: Glasc Mixologist; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:unit_played:unit[zone=trash]:::optional:costs...`
- out: Soulgorger; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active:cost=ignored:when=self_played`
- out: Soulgorger; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active:when=self_played`
- in: Fizz, Trickster; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:restriction:cost_cap_constraint:card::::costs=cost<...`
- in: Glasc Mixologist; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:unit_played:unit[zone=trash]:::optional:costs...`
- in: Soulgorger; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active:cost=ignored:when=self_played`
- in: Soulgorger; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active:when=self_played`

### [inferred-relation] Spinning Axe

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:when=self_played`
- out: Cloth Armor; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Cloth Armor; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:when=self_played`
- out: Cloth Armor; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:when=self_played`

### [inferred-relation] Spirit's Refuge

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Allay, Eager Admirer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:deflect:unit:ongoing:required:active`
- out: Allay, Eager Admirer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:deflect:unit:ongoing:required:active`
- out: Fae Dragon; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::requi...`
- out: Kinkou Monk; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::requi...`
- out: Petricite Monument; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:unit[controller=fri...`
- out: Pit Rookie; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::requi...`

### [inferred-relation] Spoils of War

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Consult the Past; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Detonate; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Dunebreaker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Hidden Blade; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Lunar Boon; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Meditation; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`
- out: Might of Demacia - Starter; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:2:card::::required`

### [inferred-relation] Sprite

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Altar of Memories; type `enabled_by`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- in: Spectral Centaur; type `enabled_by`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- in: Vanguard Helm; type `enabled_by`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- in: Vicious Snapjaws; type `enabled_by`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- in: Viktor, Leader; type `enabled_by`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- out: Altar of Memories; type `enables`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- out: Spectral Centaur; type `enables`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- out: Vanguard Helm; type `enables`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`

### [inferred-relation] Sprite Burst

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bashful Bloom; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created::::required:ob...`
- out: Bashful Bloom; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit[token_state=token]:::requ...`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Dune Drake; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Lillia, Fae Fawn; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created::::required:ob...`
- out: Piltover Enforcer; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- in: Bashful Bloom; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created::::required:ob...`
- in: Bashful Bloom; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit[token_state=token]:::requ...`

### [inferred-relation] Sprite Call

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bashful Bloom; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created::::required:ob...`
- out: Bashful Bloom; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit[token_state=token]:::requ...`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Dune Drake; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Lillia, Fae Fawn; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created::::required:ob...`
- out: Piltover Enforcer; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Sprite Burst; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created::::required:ob...`
- out: Sprite Burst; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit[token_state=token]:::requ...`

### [inferred-relation] Sprite Fountain

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Sprite Mother

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Trevor Snoozebottom; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created:here[location=...`
- in: Trevor Snoozebottom; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit[location=here;token_state...`
- out: Trevor Snoozebottom; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created:here[location=...`
- out: Trevor Snoozebottom; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit[location=here;token_state...`

### [inferred-relation] Sprite Queen

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Sprite Fountain; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created:your_base[loca...`
- out: Sprite Fountain; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit[controller=you;location=b...`
- in: Sprite Fountain; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created:your_base[loca...`
- in: Sprite Fountain; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit[controller=you;location=b...`

### [inferred-relation] Square Up

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Blood Rush; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:unit::this_turn:req...`
- out: Cleave; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:unit::this_turn:req...`
- out: Get Excited!; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- out: Gutter Palace; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- out: Lord Broadmane; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:assault:unit:this_turn:required:active:require=duration=while,s...`
- out: Lord Broadmane; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:assault:unit:temporary:required:active:require=durat...`

### [inferred-relation] Stacked Deck

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Double Trouble; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:3:card::::required:object=card[location=top;zone...`
- out: Ivern, Nurturer; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:3:card::::required:object=card[location=top;zone...`
- out: Rift Herald; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:3:card::::required:object=card[location=top;zone...`
- in: Double Trouble; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:3:card::::required:object=card[location=top;zone...`
- in: Ivern, Nurturer; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:3:card::::required:object=card[location=top;zone...`
- in: Rift Herald; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:3:card::::required:object=card[location=top;zone...`

### [inferred-relation] Stalking Wolf

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arachnoid Horror; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Dauntless Vanguard; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Deadbloom Predator; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Jhin, Meticulous Killer; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Miss Fortune, Buccaneer; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Miss Fortune, Buccaneer; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:battlefield:play:active`
- out: Nocturne, Horrifying; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`
- out: Perched Grimwyrm; type `similar_effect`; strength 0.72; reason `secondary:play_restriction:card:active`

### [inferred-relation] Stalwart Poro

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Jeweled Colossus; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Leona, Determined; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Jeweled Colossus; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Leona, Determined; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Sunlit Guardian; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Taric, Protector; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`

### [inferred-relation] Stand United

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- out: Arena Bar; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- out: Blind Monk; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- out: Karma, Channeler; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- out: Mistfall; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`
- out: Overt Operation; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required`

### [inferred-relation] Star Spring

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:optional:active`
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:base:optional:active`
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move:unit:base:optional:active`
- out: Emperor's Divide; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Fight or Flight; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Flash; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Isolate; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`

### [inferred-relation] Star-Crossed

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active`

### [inferred-relation] Stare Down

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Alpha Strike; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Gardens of Becoming; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- out: Isolate; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:base::required`
- out: Janna, Savior; type `similar_effect`; strength 0.72; reason `secondary:move:unit[controller=opponent]:base:required:active`
- out: Keeper of the Hammer; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- out: Nilah, Joyful Ascetic; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- out: Overzealous Fan; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`

### [inferred-relation] Starhound

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Annie, Stubborn; type `similar_effect`; strength 0.72; reason `secondary:move:hand[controller=friendly;zone=hand]:hand[controller=friendly]:required:a...`
- out: Annie, Stubborn; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active:when=self_...`
- out: Annie, Stubborn; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:required:active:w...`
- out: Annie, Stubborn; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand[controller=friendly]:required:active:when=self_played`
- out: Aspiring Engineer; type `similar_effect`; strength 0.72; reason `secondary:move:hand[controller=friendly;zone=hand]:hand[controller=friendly]:required:a...`
- out: Aspiring Engineer; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:active:when=self_...`
- out: Aspiring Engineer; type `similar_effect`; strength 0.72; reason `secondary:move_output:card_returned_to_hand:hand[controller=friendly]:required:active:w...`
- out: Aspiring Engineer; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand[controller=friendly]:required:active:when=self_played`

### [inferred-relation] Startipped Peak

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Ripper's Bay; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::optional`
- in: Ripper's Bay; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::optional`

### [inferred-relation] Stellacorn Herder

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Hwei, Brooding Painter; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_moves`
- in: Hwei, Brooding Painter; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_moves`
- in: Traveling Merchant; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_moves`
- out: Traveling Merchant; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_moves`

### [inferred-relation] Sterak's Gage

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Akshan, Mischievous; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:when=self_played`
- out: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=calm`
- out: Brutalizer; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Brutalizer; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=calm`

### [inferred-relation] Stormbringer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Last Breath; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_its_might:damage::required:active`
- in: Last Breath; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_its_might:damage::required:active`
- in: Strike Down; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_its_might:damage::required:active`
- out: Strike Down; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_its_might:damage::required:active`

### [inferred-relation] Stormclaw Ursine

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Albus Ferros; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required:when=sel...`
- in: Albus Ferros; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required:when=sel...`

### [inferred-relation] Strike Down

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Angle Shot; type `similar_effect`; strength 0.72; reason `secondary:attachment:detach:gear:active`
- out: Last Breath; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_its_might:damage::required:active`
- out: Last Breath; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:source_might:unit[controller=opponent]:active`
- out: Stormbringer; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_its_might:damage::required:active`
- in: Angle Shot; type `similar_effect`; strength 0.72; reason `secondary:attachment:detach:gear:active`
- in: Last Breath; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_its_might:damage::required:active`
- in: Last Breath; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:source_might:unit[controller=opponent]:active`
- in: Stormbringer; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_its_might:damage::required:active`

### [inferred-relation] Stupefy

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Forbidding Waste; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Icevale Archer; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Leona, Zealot; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Moonfall; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Moonlight Affliction; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active`
- out: Moonlight Affliction; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:negative:unit:this_turn:required:active`
- out: Orb of Regret; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:-1:might:unit::this_tur...`

### [inferred-relation] Sudden Storm

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast Corps Cadet; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Crescent Strike; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:4:damage::required:active`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Incinerate; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Iron Ballista; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Monster Harpoon; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`

### [inferred-relation] Sumpworks Map

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- out: Forge of the Future; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- out: Petricite Monument; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies::::`
- out: Petricite Monument; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- out: Poro Snax; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- out: Scryer's Bloom; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- out: Sprite; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies::::`
- out: Sprite Fountain; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies::::`

### [inferred-relation] Sunken Temple

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Monastery of Hirana; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::optional:when=battlefield_conq...`
- in: Monastery of Hirana; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::optional:when=battlefield_conq...`

### [inferred-relation] Sunlit Guardian

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Jeweled Colossus; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Leona, Determined; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Stalwart Poro; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Jeweled Colossus; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Leona, Determined; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Stalwart Poro; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`

### [inferred-relation] Super Mega Death Rocket!

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Bellows Breath; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::optional`
- out: Dancing Grenade; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::optional`
- out: Falling Star; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Final Spark; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`

### [inferred-relation] Svellsongur

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Angle Shot; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`
- out: Boneshiver; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Boneshiver; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active`
- out: Boneshiver; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active`

### [inferred-relation] Switcheroo

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Convergent Mutation; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:variable:active`
- out: Deathgrip; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:variable:active`
- in: Convergent Mutation; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:variable:active`
- in: Deathgrip; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:variable:active`

### [inferred-relation] Symbol of the Solari

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Altar of Blood; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:base:active`
- out: Conscription; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:base:active`
- out: Conscription; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:base:required:active`
- out: Emperor's Divide; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:base:required:active`
- out: Fight or Flight; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:base:required:active`
- out: Flash; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:base:required:active`
- out: Highlander; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:base:active`
- out: Highlander; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:base:required:active`

### [inferred-relation] Tactical Retreat

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Conscription; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- out: Highlander; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- out: Highlander; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:replacement_effect:prevent:unit::this_turn::prevent...`
- out: Hostile Takeover; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- out: Possession; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- out: Soraka, Wanderer; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- out: Soraka, Wanderer; type `similar_effect`; strength 0.72; reason `secondary:replacement:unit_dies:heal_exhaust_recall:active`
- out: Soraka, Wanderer; type `similar_effect`; strength 0.72; reason `secondary:replacement:unit_dies:heal_exhaust_recall:unit:active`

### [inferred-relation] Targon's Peak

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune::required:active`
- out: Dark Child - Starter; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- out: Dark Child - Starter; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune::required:active`
- out: Ekko, Recurrent; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- out: Gentle Gemdragon; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`
- out: Gentle Gemdragon; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune::required:active`
- out: Hwei, Brooding Painter; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:rune:active`

### [inferred-relation] Targonian Visionary

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Prepared Neophyte; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:4:might:card:::required`
- in: Prepared Neophyte; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:4:might:card:::required`
- in: Yi, Meditative; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:4:might:card:::required`
- out: Yi, Meditative; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:4:might:card:::required`

### [inferred-relation] Taric, Protector

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Black Flame Altar; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:shield:unit:ongoing:required:active:require=duration...`
- out: Black Flame Altar; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:shield:unit:ongoing:required:active:require=duration=while,stat...`
- out: Jeweled Colossus; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Leona, Determined; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Stalwart Poro; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Sunlit Guardian; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- in: Black Flame Altar; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:shield:unit:ongoing:required:active:require=duration...`

### [inferred-relation] Tasty Faefolk

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Teemo, Scout

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Combat Experience; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:card::this_turn...`
- out: Hwei, Brooding Painter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:card::this_turn...`
- out: Lux, Illuminated; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:card::this_turn...`
- in: Combat Experience; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:card::this_turn...`
- in: Hwei, Brooding Painter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:card::this_turn...`
- in: Lux, Illuminated; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:3:might:card::this_turn...`

### [inferred-relation] Teemo, Strategist

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bellows Breath; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:1:damage:unit:::required`
- out: Crackshot Corsair; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- out: Elder Dragon; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- out: Final Spark; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- out: Frozen Fortress; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:1:damage::required:active`
- out: Singularity; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Super Mega Death Rocket!; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`

### [inferred-relation] Temporal Portal

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: The Academy; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:spell[controller=yo...`
- out: The Academy; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:spell[controller=yo...`

### [inferred-relation] Temptation

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bonds of Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Desert's Call; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Double Trouble; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Downstage Dramatics; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Existential Dread; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Feral Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Forgotten Signpost; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:active`
- out: Forgotten Signpost; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:required:active`

### [inferred-relation] The Academy

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Temporal Portal; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:spell[controller=yo...`
- in: Temporal Portal; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:keyword_grant:gain_keyword:keyword_granted:spell[controller=yo...`

### [inferred-relation] The Arena's Greatest

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Ahri, Alluring; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Aspirant's Climb; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Draven, Audacious; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Ivern, Friend to All; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Power Nexus; type `similar_effect`; strength 0.72; reason `secondary:score_amount:1:point:active`
- out: Renata Glasc, Mastermind; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Ahri, Alluring; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Aspirant's Climb; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`

### [inferred-relation] The Boss

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Altar of Blood; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::optional`
- out: Overt Operation; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::optional`
- out: Relentless Pursuit; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:card:base:optional:active`
- out: Symbol of the Solari; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:base:active`
- in: Altar of Blood; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::optional`
- in: Overt Operation; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::optional`

### [inferred-relation] The Candlelit Sanctum

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Called Shot; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:2:card::::required:object=card[location=top;zone...`
- out: Dramatic Visionary; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:2:card::::required:object=card[location=top;zone...`
- out: Scryer's Bloom; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:2:card::::required:object=card[location=top;zone...`
- in: Called Shot; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:2:card::::required:object=card[location=top;zone...`
- in: Dramatic Visionary; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:2:card::::required:object=card[location=top;zone...`
- in: Scryer's Bloom; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:look:2:card::::required:object=card[location=top;zone...`

### [inferred-relation] The Grand Plaza

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Gutter Palace; type `similar_effect`; strength 0.72; reason `output:payoff_output:score_change:score:game_won::::required`
- in: Gutter Palace; type `similar_effect`; strength 0.72; reason `output:payoff_output:score_change:score:game_won::::required`

### [inferred-relation] The Harrowing

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Cemetery Attendant; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:unit_played:unit[zone=trash]:::required`
- out: Heedless Resurrection; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:unit_played:unit[zone=trash]:::required`
- in: Cemetery Attendant; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:unit_played:unit[zone=trash]:::required`
- in: Heedless Resurrection; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:unit_played:unit[zone=trash]:::required`
- in: Undying Loyalty; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active`
- in: Undying Loyalty; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active:cost=ignored`
- out: Undying Loyalty; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active`
- out: Undying Loyalty; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active:cost=ignored`

### [inferred-relation] The List

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Frigid Touch; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:-2:might:unit::this_tur...`
- in: Frigid Touch; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:-2:might:unit::this_tur...`

### [inferred-relation] The Papertree

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Find Your Center; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Mobilize; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Obelisk of Power; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Party Favors; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Qiyana, Victorious; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Retreat; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Sacrifice; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`

### [inferred-relation] The Ruination

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast of Power; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Blood Money; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Cull the Weak; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- out: Drag Under; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Fox-Fire; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Hidden Blade; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Imperial Decree; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: King's Edict; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`

### [inferred-relation] The Syren

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Emperor's Divide; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=friendly;location=battle...`
- out: Overzealous Fan; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Reaver's Row; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Relentless Pursuit; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Sinister Poro; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Star Spring; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Symbol of the Solari; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:base:required:active`

### [inferred-relation] The Zero Drive

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Thermo Beam

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Acceptable Losses; type `similar_effect`; strength 0.72; reason `secondary:removal:gear_dies:gear:required:active`
- out: Detonate; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::required`
- out: Rocket Barrage; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::required`
- in: Acceptable Losses; type `similar_effect`; strength 0.72; reason `secondary:removal:gear_dies:gear:required:active`
- in: Detonate; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::required`
- in: Rocket Barrage; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::required`
- in: Zaun Punk; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::required`
- out: Zaun Punk; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::required`

### [inferred-relation] Thousand-Tailed Watcher

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blastcone Fae; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active:when=self_played`
- out: Frostcoat Cub; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active:when=self_played`
- in: Blastcone Fae; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active:when=self_played`
- in: Frostcoat Cub; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:negative:active:when=self_played`

### [inferred-relation] Thrill of the Hunt

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arcane Shift; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:unit[controller=friendly]:::required`
- out: Portal Rescue; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:unit[controller=friendly]:::required`
- in: Arcane Shift; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:unit[controller=friendly]:::required`
- in: Portal Rescue; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:unit[controller=friendly]:::required`

### [inferred-relation] Thwonk!

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Back Off; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit::this_turn:required`
- out: Bonds of Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Desert's Call; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Double Trouble; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Downstage Dramatics; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Existential Dread; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`

### [inferred-relation] Tianna Crownguard

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Forgotten Monument; type `similar_effect`; strength 0.72; reason `secondary:prevent:score:active`
- in: Forgotten Monument; type `similar_effect`; strength 0.72; reason `secondary:prevent:score:active`

### [inferred-relation] Tibbers

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Disintegrate; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:3:damage:unit[location=battlefield]:::r...`
- out: Hextech Ray; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:3:damage:unit[location=battlefield]:::r...`
- out: Smite; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:3:damage:unit[location=battlefield]:::r...`
- in: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- in: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`

### [inferred-relation] Tideturner

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:card:location::optional`
- out: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:card:location::required`
- out: Forgotten Signpost; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:active`
- out: Forgotten Signpost; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:required:active`
- out: Smoke and Mirrors; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:active`
- out: Smoke and Mirrors; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:required:active`
- out: Smoke and Mirrors; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:card:location:required:active`
- in: Azir, Ascendant; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:card:location::optional`

### [inferred-relation] Time Warp

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arcane Shift; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- out: Ashe, Focused; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- out: Blind Fury; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- out: Dazzling Aurora; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- out: Smite; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- in: Arcane Shift; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- in: Ashe, Focused; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`
- in: Blind Fury; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:card:::required`

### [inferred-relation] Towering Combatant

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blue Sentinel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_defender:active`
- out: Mutated Mouser; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- out: Shen, Kinkou; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Blue Sentinel; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Garen, Rugged; type `similar_effect`; strength 0.72; reason `secondary:combat_might_modifier:might_modified:might:positive:2:self:while_defender:active`
- in: Mutated Mouser; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`
- in: Shen, Kinkou; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card::while:req...`

### [inferred-relation] Towering Pairofant

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Black Rose Dignitary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Crescent Guardian; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Daisy!; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Daring Poro; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Direwing; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`

### [inferred-relation] Trapping Grounds

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Flurry of Feathers; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:bird_unit_token_created::::required:obje...`
- out: Gutter Palace; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:bird_unit_token_created::::required:obje...`
- in: Flurry of Feathers; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:bird_unit_token_created::::required:obje...`
- in: Gutter Palace; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:bird_unit_token_created::::required:obje...`
- in: Walking Roost; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:bird_unit_token_created::::required:obje...`
- out: Walking Roost; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:bird_unit_token_created::::required:obje...`

### [inferred-relation] Traveling Merchant

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Corrupt Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_moves`
- out: Hwei, Brooding Painter; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_moves`
- out: Hwei, Brooding Painter; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_moves`
- out: Stellacorn Herder; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_moves`
- in: Corrupt Enforcer; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_moves`
- in: Hwei, Brooding Painter; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required:when=self_moves`

### [inferred-relation] Treasure Hunter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Black Market Broker; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Blood Money; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Bushwhack; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Draven, Vanquisher; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Eminent Benefactor; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Fae Dragon; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Honest Broker; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`

### [inferred-relation] Treasure Trove

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Aphelios, Exalted; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- out: Find Your Center; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Forge of the Future; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- out: Mobilize; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Obelisk of Power; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Party Favors; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required`
- out: Petricite Monument; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`

### [inferred-relation] Trevor Snoozebottom

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Dune Drake; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Jeweled Colossus; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Leona, Determined; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Piltover Enforcer; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Sprite Mother; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:sprite_unit_token_created:here[location=...`
- out: Sprite Mother; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit[location=here;token_state...`

### [inferred-relation] Tricksy Tentacles

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Forgotten Signpost; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:active`
- out: Forgotten Signpost; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:required:active`
- out: Forgotten Signpost; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:location:required:active`
- out: Smoke and Mirrors; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:active`
- out: Smoke and Mirrors; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:required:active`
- out: Temptation; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:location::requ...`
- in: Forgotten Signpost; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:active`
- in: Forgotten Signpost; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:location:required:active`

### [inferred-relation] Trifarian Gloryseeker

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Fae Dragon; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_played`
- out: Peak Guardian; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_played`
- out: Poro Herder; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_played`
- out: Sea Monkey; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_played`
- in: Fae Dragon; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_played`
- in: Peak Guardian; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::required:when=self_played`

### [inferred-relation] Trifarian War Camp

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Brush; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:might_modified:1:might:unit[locati...`
- in: Brush; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:might_modified:1:might:unit[locati...`
- in: Trusty Ramhound; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:might_modified:1:might:unit[locati...`
- out: Trusty Ramhound; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:might_modified:1:might:unit[locati...`

### [inferred-relation] Trinity Force

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Doran's Blade; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Doran's Blade; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=body`
- out: Doran's Blade; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=body`
- out: Hexdrinker; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`

### [inferred-relation] Trove Golem

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Card Sharp; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Pickpocket; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Card Sharp; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- in: Pickpocket; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`

### [inferred-relation] Trusty Ramhound

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Brush; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:might_modified:1:might:unit[locati...`
- out: Gemhand Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Gustwalker; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Mosstomper; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Scorchclaw; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Sea Monkey; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Trifarian War Camp; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:might_modified:1:might:unit[locati...`

### [inferred-relation] Tryndamere, Barbarian

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Ahri, Alluring; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Aspirant's Climb; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Draven, Audacious; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Ivern, Friend to All; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Power Nexus; type `similar_effect`; strength 0.72; reason `secondary:score_amount:1:point:active`
- out: Renata Glasc, Mastermind; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: The Arena's Greatest; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- in: Ahri, Alluring; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`

### [inferred-relation] Turn to Dust

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Fading Memories; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:temporary:gear:ongoing:required:active`
- out: Fading Memories; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:temporary:gear:ongoing:required:active`
- out: Fading Memories; type `similar_effect`; strength 0.72; reason `secondary:temporary_grant:gear:ongoing:required:active`
- in: Fading Memories; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:temporary:gear:ongoing:required:active`
- in: Fading Memories; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:temporary:gear:ongoing:required:active`
- in: Fading Memories; type `similar_effect`; strength 0.72; reason `secondary:temporary_grant:gear:ongoing:required:active`

### [inferred-relation] Twisted Fate, Gambler

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Crescent Strike; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=here]::required:active`
- out: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent]::this_...`
- out: Existential Dread; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent]::this_...`
- out: Heroic Charge; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent]::this_...`

### [inferred-relation] Udyr, Wildman

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Blast Corps Cadet; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Incinerate; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`
- out: Iron Ballista; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:2:damage:unit[location=battlefield]:::r...`

### [inferred-relation] Unchecked Power

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Disintegrate; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Hextech Ray; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Incinerate; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Iron Ballista; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Monster Harpoon; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`

### [inferred-relation] Undercover Agent

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Undertitan

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Back to Back; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Bonds of Strength; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Dangerous Duo; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:positive:active:when=self_played`
- out: Decisive Strike; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: En Garde; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Frigid Jewel; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Gentlemen's Duel; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`
- out: Grand Strategem; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]:this_turn:requir...`

### [inferred-relation] Undying Legion

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Death from Below; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`
- out: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`
- out: Rumble, Hotheaded; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`
- in: Death from Below; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`
- in: Immortal Phoenix; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`
- in: Rumble, Hotheaded; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:play:card_played:card[zone=trash]:::optional`

### [inferred-relation] Undying Loyalty

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Drag Under; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Find Your Center; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Glasc Mixologist; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active`
- out: Glasc Mixologist; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active:cost=ignored`
- out: Heedless Resurrection; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active`
- out: Heedless Resurrection; type `similar_effect`; strength 0.72; reason `secondary:play_from_zone:unit_played:unit:from=trash:active:cost=ignored`

### [inferred-relation] Unforgiven

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Flash; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=friendly]:base::required`
- out: Overzealous Fan; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Reaver's Row; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Relentless Pursuit; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Sinister Poro; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Star Spring; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Symbol of the Solari; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:unit:base:required:active`

### [inferred-relation] Unlicensed Armory

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Altar of Blood; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::optional`
- out: Get Excited!; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- out: Gutter Palace; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- out: Lunar Boon; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- out: Relentless Pursuit; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:card:base:optional:active`
- out: Square Up; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`

### [inferred-relation] Unsung Hero

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Unyielding Spirit

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Counter Strike; type `similar_effect`; strength 0.72; reason `secondary:prevent:damage_dealt:active`
- out: Kayn, Unleashed; type `similar_effect`; strength 0.72; reason `secondary:prevent:damage_dealt:active`
- in: Counter Strike; type `similar_effect`; strength 0.72; reason `secondary:prevent:damage_dealt:active`
- in: Kayn, Unleashed; type `similar_effect`; strength 0.72; reason `secondary:prevent:damage_dealt:active`

### [inferred-relation] Upstage Comedy

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blood Rose; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit:::required`
- out: Bonds of Strength; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Desert's Call; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Double Trouble; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Downstage Dramatics; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`
- out: Dune Drake; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Existential Dread; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2`

### [inferred-relation] Vanguard Armory

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Herald of the Arcane; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created::::required:o...`
- in: Herald of the Arcane; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created::::required:o...`

### [inferred-relation] Vanguard Attendant

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Crescent Guardian; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Daisy!; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Direwing; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Dunebreaker; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Eager Drakehound; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`

### [inferred-relation] Vanguard Captain

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Faithful Manufactor; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:here[location...`
- in: Faithful Manufactor; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:here[location...`

### [inferred-relation] Vanguard Helm

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Baited Hook; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Deathgrip; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`

### [inferred-relation] Vault Breaker

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blood Rush; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:assault:unit:this_turn:required:active:require=duration=while,s...`
- out: Blood Rush; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:assault:unit:temporary:required:active:require=durat...`
- out: Bounty Hunter; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:unit:temporary:required:active`
- out: Bounty Hunter; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:unit:this_turn:required:active`
- out: Cleave; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:assault:unit:this_turn:required:active:require=duration=while,s...`
- out: Cleave; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:assault:unit:temporary:required:active:require=durat...`
- out: Gem Jammer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:ganking:unit:temporary:required:active`
- out: Gem Jammer; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:ganking:unit:this_turn:required:active`

### [inferred-relation] Vaults of Helia

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Vex, Cheerless; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:increase_cost:play_cost_increased:1:energy:car...`
- out: Vex, Cheerless; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:increase_cost:play_cost_increased:1:energy:car...`

### [inferred-relation] Vayne, Hunter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Crescent Guardian; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Daisy!; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`

### [inferred-relation] Veiled Temple

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Angle Shot; type `similar_effect`; strength 0.72; reason `secondary:attachment:detach:gear:active`
- out: Strike Down; type `similar_effect`; strength 0.72; reason `secondary:attachment:detach:gear:active`
- in: Angle Shot; type `similar_effect`; strength 0.72; reason `secondary:attachment:detach:gear:active`
- in: Strike Down; type `similar_effect`; strength 0.72; reason `secondary:attachment:detach:gear:active`

### [inferred-relation] Vengeance

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast of Power; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Blood Money; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Cull the Weak; type `similar_effect`; strength 0.72; reason `secondary:removal:unit_dies:unit:required:active`
- out: Drag Under; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Fox-Fire; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Hidden Blade; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: Imperial Decree; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`
- out: King's Edict; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:unit_dies:unit:::required`

### [inferred-relation] Veteran Poro

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Armed Assailant; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=g...`
- out: Armed Assailant; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:gear_cost_reduced:1:rune:gear[cont...`
- out: Combat Chef; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=g...`
- out: Combat Chef; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:gear_cost_reduced:1:rune:gear[cont...`

### [inferred-relation] Vex, Apathetic

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Bone Skewer; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:card::this_turn:required`
- out: Solari Chief; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:card::this_turn:required`
- in: Bone Skewer; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:card::this_turn:required`
- in: Solari Chief; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:card::this_turn:required`

### [inferred-relation] Vex, Cheerless

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Irelia, Graceful; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction_exact:play_cost_reduced:energy:1:spell:active`
- out: Vaults of Helia; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:increase_cost:play_cost_increased:1:energy:car...`
- in: Irelia, Graceful; type `similar_effect`; strength 0.72; reason `secondary:cost_reduction_exact:play_cost_reduced:energy:1:spell:active`
- in: Vaults of Helia; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:increase_cost:play_cost_increased:1:energy:car...`

### [inferred-relation] Vex, Mocking

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- out: Azir, Sovereign; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:optional:active`
- out: Call to Battle; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- out: Evelynn, Entrancing; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:optional:active`
- out: Iascylla; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:active`
- out: Iascylla; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield:optional:active`

### [inferred-relation] Vi, Destructive

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Back-Alley Bar; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Eclipse Herald; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`
- out: Friendship; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn...`

### [inferred-relation] Vi, Hotheaded

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Fiora, Peerless; type `similar_effect`; strength 0.72; reason `secondary:stat_multiplier:might:2:active`
- out: Last Stand; type `similar_effect`; strength 0.72; reason `secondary:stat_multiplier:might:2:active`
- out: Last Stand; type `similar_effect`; strength 0.72; reason `secondary:stat_multiplier:might:2:this_turn::active`
- in: Fiora, Peerless; type `similar_effect`; strength 0.72; reason `secondary:stat_multiplier:might:2:active`
- in: Last Stand; type `similar_effect`; strength 0.72; reason `secondary:stat_multiplier:might:2:active`
- in: Last Stand; type `similar_effect`; strength 0.72; reason `secondary:stat_multiplier:might:2:this_turn::active`

### [inferred-relation] Vi, Peacekeeper

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Daisy!; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent;locatio...`
- out: Leona, Determined; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent;locatio...`
- in: Daisy!; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent;locatio...`
- in: Leona, Determined; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent;locatio...`

### [inferred-relation] Vicious Snapjaws

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Baited Hook; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Deathgrip; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`

### [inferred-relation] Viktor, Innovator

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Altar to Unity; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- out: Forge of the Future; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- out: Machine Evangel; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- out: Recruit the Vanguard; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- in: Altar to Unity; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- in: Forge of the Future; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- in: Machine Evangel; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`
- in: Recruit the Vanguard; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:recruit_unit_token_created:your_base[loc...`

### [inferred-relation] Viktor, Leader

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Baited Hook; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Deathgrip; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.92; reason `friendly_unit_dies_enables_friendly_unit_dies`

### [inferred-relation] Vilemaw

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Facebreaker; type `similar_effect`; strength 0.72; reason `secondary:prevent:deal_combat_damage:active`
- out: Facebreaker; type `similar_effect`; strength 0.72; reason `secondary:prevent:deal_combat_damage:::active`
- in: Facebreaker; type `similar_effect`; strength 0.72; reason `secondary:prevent:deal_combat_damage:active`
- in: Facebreaker; type `similar_effect`; strength 0.72; reason `secondary:prevent:deal_combat_damage:::active`

### [inferred-relation] Vilemaw's Lair

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Determined Sentry; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:active`
- out: Determined Sentry; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:::active`
- out: Determined Sentry; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:unit:::active`
- out: Minotaur Reckoner; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:::active`
- out: Minotaur Reckoner; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:active`
- out: Minotaur Reckoner; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:unit:::active`
- in: Determined Sentry; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:::active`
- in: Determined Sentry; type `similar_effect`; strength 0.72; reason `secondary:prevent:move:active`

### [inferred-relation] Virtuoso

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Annie, Stubborn; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Fizz, Trickster; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Kai'Sa, Evolutionary; type `enabled_by`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Annie, Stubborn; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Fizz, Trickster; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- in: Kai'Sa, Evolutionary; type `enables`; strength 0.82; reason `spell_played_enables_spell_played`
- out: Lady of Luminosity - Starter; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=spell_played`
- out: Minefield; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:card:trash:required:active`

### [inferred-relation] Void Assault

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Blast Cone; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:unit[controller=opponent]:active`
- out: Charm; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:::required`
- out: Dragon's Rage; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:::required`
- out: Relentless Pursuit; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=friendly]:::required`
- out: Relentless Pursuit; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:unit[controller=friendly]:active`
- out: Ride the Wind; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=friendly]:::required`
- out: Skyward Strike; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=opponent]:::required`
- in: Blast Cone; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:unit[controller=opponent]:active`

### [inferred-relation] Void Burrower

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Rek'Sai, Swarm Queen; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:one:::optional`
- out: Rek'Sai, Swarm Queen; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:2:card::::optional:object=card[location=top;zo...`
- in: Rek'Sai, Swarm Queen; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:one:::optional`
- in: Rek'Sai, Swarm Queen; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:card_flow:reveal:2:card::::optional:object=card[location=top;zo...`
- in: Void Rush; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:one:::optional`
- out: Void Rush; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:one:::optional`

### [inferred-relation] Void Drone

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Concentrate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Drag Under; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Find Your Center; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Herald of Scales; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Jaull-Fish; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Master Yi, Unstoppable; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Needlessly Large Yordle; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`

### [inferred-relation] Void Gate

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Annie, Fiery; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:bonus_damage_added:1:bonus_damage:...`
- in: Annie, Fiery; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:modify_stat:bonus_damage_added:1:bonus_damage:...`

### [inferred-relation] Void Hatchling

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Karma, Channeler; type `enabled_by`; strength 0.9; reason `card_recycled_enables_card_recycled`
- out: Karma, Channeler; type `enables`; strength 0.9; reason `card_recycled_enables_card_recycled`

### [inferred-relation] Void Rush

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- out: Rek'Sai, Swarm Queen; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:one:::optional`
- out: Void Burrower; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:one:::optional`
- in: Brazen Buccaneer; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::...`
- in: Rek'Sai, Swarm Queen; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:one:::optional`
- in: Void Burrower; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:banish:card_banished:one:::optional`

### [inferred-relation] Void Seeker

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Crescent Strike; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:4:damage::required:active`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Disintegrate; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Falling Comet; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Flurry of Blades; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Hextech Ray; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Incinerate; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`
- out: Iron Ballista; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[location=battlefield]::required:active`

### [inferred-relation] Voidreaver

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Alpha Strike; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- out: Amateur Recital; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Flash; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:move:unit_moved:unit[controller=friendly]:base::required`
- out: Gardens of Becoming; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- out: Keeper of the Hammer; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- out: Nilah, Joyful Ascetic; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required`
- out: Overzealous Fan; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`
- out: Reaver's Row; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:base:active`

### [inferred-relation] Volibear, Furious

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=here]::required:active:when...`
- out: Crackshot Corsair; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=here]::required:active:when...`
- out: Sky Splitter; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:5:damage::required:active`
- out: Super Mega Death Rocket!; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:5:damage::required:active`
- in: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=here]::required:active:when...`
- in: Crackshot Corsair; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit[controller=opponent;location=here]::required:active:when...`
- in: Sky Splitter; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:5:damage::required:active`
- in: Super Mega Death Rocket!; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:5:damage::required:active`

### [inferred-relation] Voracious Gromp

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Poppy, Paragon; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:3:xp::::required`
- in: Poppy, Paragon; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:3:xp::::required`

### [inferred-relation] Wages of Pain

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Black Market Broker; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Blood Money; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Bushwhack; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Disintegrate; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:3:damage:unit[location=battlefield]:::r...`

### [inferred-relation] Walking Roost

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Flurry of Feathers; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:bird_unit_token_created::::required:obje...`
- out: Gutter Palace; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:bird_unit_token_created::::required:obje...`
- out: Trapping Grounds; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:bird_unit_token_created::::required:obje...`
- in: Flurry of Feathers; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:bird_unit_token_created::::required:obje...`
- in: Gutter Palace; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:bird_unit_token_created::::required:obje...`
- in: Trapping Grounds; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:bird_unit_token_created::::required:obje...`

### [inferred-relation] Wallop

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Blood Rose; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit:::required`
- out: Call to Glory; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:as an additional cost:::optional`
- out: Deceiver; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: Dune Drake; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`
- out: First Mate; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:state_modifier:ready:unit_ready:unit:::required`
- out: Piltover Enforcer; type `similar_effect`; strength 0.72; reason `secondary:state_action:ready:unit_ready:unit:active`

### [inferred-relation] Warmog's Armor

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Doran's Blade; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Doran's Blade; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=body`

### [inferred-relation] Warwick, Hunter

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Crescent Guardian; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Daisy!; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Direwing; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Dunebreaker; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Eager Drakehound; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`

### [inferred-relation] Watchful Sentry

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Baited Hook; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Blade of the Ruined King; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Commander Ledros; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Cruel Patron; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Deathgrip; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Heedless Resurrection; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`
- out: Malzahar, Fanatic; type `enabled_by`; strength 0.84; reason `friendly_unit_dies_enables_self_dies`

### [inferred-relation] Whirlwind

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Blitzcrank, Impassive; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Downwell; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Emperor's Dais; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:optional:active`
- out: Emperor's Dais; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active`
- out: Emperor's Dais; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:optional:active`
- out: Emperor's Dais; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:optional:active`

### [inferred-relation] Whiteflame Protector

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Dangerous Duo; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:positive:active:when=self_played`
- out: Dangerous Duo; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active:when=self_p...`
- out: Undertitan; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:positive:active:when=self_played`
- in: Dangerous Duo; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:positive:active:when=self_played`
- in: Dangerous Duo; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit:this_turn:required:active:when=self_p...`
- in: Undertitan; type `similar_effect`; strength 0.72; reason `secondary:stat_family:might_modified:might:positive:active:when=self_played`

### [inferred-relation] Wielder of Water

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Crimson Pigeons; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card:::required`
- out: Sivir, Mercenary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card:::required`
- in: Crimson Pigeons; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card:::required`
- in: Sivir, Mercenary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:2:might:card:::required`

### [inferred-relation] Wildclaw Shaman

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Mistfall; type `enabled_by`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Mistfall; type `enables`; strength 0.86; reason `unit_buffed_enables_unit_buffed`
- out: Buhru Captain; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::optional:when=self_played`
- in: Buhru Captain; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:buff:unit_buffed:card:::optional:when=self_played`

### [inferred-relation] Wily Newtfish

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Gemhand Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Gustwalker; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Jhin, Murderous Artist; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Kai'Sa, Evolutionary; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Kayn, Unleashed; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`

### [inferred-relation] Wind Wall

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Abandon; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- out: Defy; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- out: Flurry of Feathers; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- out: Hard Bargain; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- out: Lilting Lullaby; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- out: Riposte; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Abandon; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`
- in: Defy; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:counter:spell_countered:spell:::required:polarity=...`

### [inferred-relation] Windsinger

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Angler Beast; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`
- out: Beast Below; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`
- out: Grim Apothecary; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:optional:active:when=self_played`
- out: Grim Apothecary; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`
- out: Grim Apothecary; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:optional:active:when=self_played`
- out: Grim Apothecary; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:optional:active:when=self_played`
- in: Angler Beast; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`
- in: Beast Below; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`

### [inferred-relation] Wizened Elder

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `secondary:require_state:while_buffed:while:active`
- out: Gemhand Hunter; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Gustwalker; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Mosstomper; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Scorchclaw; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Sea Monkey; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`
- out: Trusty Ramhound; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card:::required`

### [inferred-relation] World Atlas

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Cloth Armor; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:unit[controller=you]:::r...`
- out: Cloth Armor; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:active:cost=rune=mind`
- out: Cloth Armor; type `similar_effect`; strength 0.72; reason `secondary:attachment:attach:gear:unit[controller=friendly]:active:cost=rune=mind`
- out: Cull; type `similar_effect`; strength 0.72; reason `output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:obje...`

### [inferred-relation] Wuju Apprentice

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Clockwork Keeper; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Crowd Favorite; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- out: Enthralling Protector; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- out: Evershade Stalker; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Gemhand Hunter; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- out: Herald of Spring; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`
- out: Insightful Investigator; type `similar_effect`; strength 0.72; reason `output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played`
- out: Kha'Zix, Evolving Hunter; type `similar_effect`; strength 0.72; reason `output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required:when=self_conqu...`

### [inferred-relation] Wuju Master

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Baron Nashor; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]::static:active`
- out: Confront; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:entry_state:enter_ready:token_enters_ready:unit[controller=you...`
- out: Darius, Executioner; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]::static:active`
- out: Garen, Commander; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]::static:active`
- in: Baron Nashor; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]::static:active`
- in: Confront; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:entry_state:enter_ready:token_enters_ready:unit[controller=you...`
- in: Darius, Executioner; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]::static:active`
- in: Garen, Commander; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly]::static:active`

### [inferred-relation] Xerath, Freed

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Curtain Call; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Deadly Flourish; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`
- out: Falling Star; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:3:damage:unit:::required`
- out: Final Spark; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Singularity; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- out: Super Mega Death Rocket!; type `similar_effect`; strength 0.72; reason `secondary:damage:positive:unit::required:active`
- in: Anivia, Primal; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:3:damage::required:active`

### [inferred-relation] Xin Zhao, Vigilant

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Crescent Guardian; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Daisy!; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Direwing; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Dunebreaker; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Eager Drakehound; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`

### [inferred-relation] Yasuo, Remorseful

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Caitlyn, Patrolling; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_my_might:damage::required:active`
- out: Ezreal, Dashing; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to my might:damage:unit[co...`
- out: Kha'Zix, Evolving Hunter; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:self_might:unit[controller=opponent]:active:when=self_attacks`
- out: Kha'Zix, Evolving Hunter; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:self_might:unit[controller=opponent;location=here]:active:when...`
- out: Lucian, Gunslinger; type `similar_effect`; strength 0.72; reason `secondary:damage:variable:unit[controller=opponent;location=here]::required:active:when...`
- in: Caitlyn, Patrolling; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_my_might:damage::required:active`
- in: Ezreal, Dashing; type `similar_effect`; strength 0.72; reason `event:event_produced:damage:damage:damage_dealt:damage equal to my might:damage:unit[co...`
- in: Kha'Zix, Evolving Hunter; type `similar_effect`; strength 0.72; reason `secondary:damage_scaling:self_might:unit[controller=opponent]:active:when=self_attacks`

### [inferred-relation] Yasuo, Windrider

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Ahri, Alluring; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Aspirant's Climb; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Draven, Audacious; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Ivern, Friend to All; type `similar_effect`; strength 0.72; reason `predicate:payoff_output:score_change:score:1:point::::required`
- out: Jhin, Murderous Artist; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`

### [inferred-relation] Yeti Brawler

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Altar of Memories; type `enabled_by`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- in: Spectral Centaur; type `enabled_by`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- in: Vanguard Helm; type `enabled_by`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- in: Vicious Snapjaws; type `enabled_by`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- in: Viktor, Leader; type `enabled_by`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- out: Altar of Memories; type `enables`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- out: Spectral Centaur; type `enables`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`
- out: Vanguard Helm; type `enables`; strength 0.85; reason `self_unit_dies_enables_friendly_unit_dies`

### [inferred-relation] Yi, Honed

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Arena Kingpin; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Atakhan; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Bandle Soldier; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Bilgewater Bully; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Breakneck Mech; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Commander Ledros; type `similar_effect`; strength 0.72; reason `predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield`
- out: Crescent Guardian; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`
- out: Daisy!; type `similar_effect`; strength 0.72; reason `event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required`

### [inferred-relation] Yi, Meditative

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Prepared Neophyte; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:4:might:card:::required`
- out: Targonian Visionary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:4:might:card:::required`
- in: Prepared Neophyte; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:4:might:card:::required`
- in: Targonian Visionary; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:4:might:card:::required`

### [inferred-relation] Yone, Blademaster

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Aphelios, Exalted; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- in: Jax, Unrelenting; type `enabled_by`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Aphelios, Exalted; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Jax, Unrelenting; type `enables`; strength 0.82; reason `equipment_attached_enables_equipment_attached`
- out: Armed Assailant; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=g...`
- out: Armed Assailant; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:static_modifier:reduce_cost:gear_cost_reduced:1:rune:gear[cont...`
- out: Caitlyn, Patrolling; type `similar_effect`; strength 0.72; reason `secondary:damage_amount:damage_equal_to_my_might:damage::required:active`
- out: Combat Chef; type `similar_effect`; strength 0.72; reason `output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=g...`

### [inferred-relation] Yuumi, Magical Cat

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Against the Odds; type `similar_effect`; strength 0.72; reason `secondary:stat_no_location:might_modified:might:positive:unit[controller=friendly]:this...`
- out: Block; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:tank:unit:temporary:required:active`
- out: Block; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:tank:unit:this_turn:required:active`
- out: Siphon Power; type `similar_effect`; strength 0.72; reason `secondary:stat:might_modified:might:positive:unit[controller=friendly;location=here]:th...`
- out: Siphon Power; type `similar_effect`; strength 0.72; reason `secondary:stat_no_location:might_modified:might:positive:unit[controller=friendly]:this...`
- in: Against the Odds; type `similar_effect`; strength 0.72; reason `secondary:stat_no_location:might_modified:might:positive:unit[controller=friendly]:this...`
- in: Block; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant_by_keyword:tank:unit:temporary:required:active`
- in: Block; type `similar_effect`; strength 0.72; reason `secondary:keyword_grant:tank:unit:this_turn:required:active`

### [inferred-relation] Zaun Punk

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Acceptable Losses; type `similar_effect`; strength 0.72; reason `secondary:removal:gear_dies:gear:required:active`
- out: Detonate; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::required`
- out: Rocket Barrage; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::required`
- out: Thermo Beam; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::required`
- in: Acceptable Losses; type `similar_effect`; strength 0.72; reason `secondary:removal:gear_dies:gear:required:active`
- in: Detonate; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::required`
- in: Rocket Barrage; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::required`
- in: Thermo Beam; type `similar_effect`; strength 0.72; reason `event:event_produced:removal:kill:gear_dies:gear:::required`

### [inferred-relation] Zaun Warrens

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Flame Chompers; type `enabled_by`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Flame Chompers; type `enables`; strength 0.78; reason `card_discarded_enables_self_discarded`
- out: Get Excited!; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- out: Gutter Palace; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- out: Lunar Boon; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- out: Square Up; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- out: Unlicensed Armory; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`
- in: Get Excited!; type `similar_effect`; strength 0.72; reason `output:event_produced:card_flow:discard:card_discarded:1:card::::required`

### [inferred-relation] Zaunite Bouncer

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Angler Beast; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active:when=self_played`
- out: Angler Beast; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`
- out: Angler Beast; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active:when=self_played`
- out: Angler Beast; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active:when=self_played`
- out: Beast Below; type `similar_effect`; strength 0.72; reason `secondary:move:hand[zone=hand]:hand:required:active:when=self_played`
- out: Beast Below; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:active:when=self_played`
- out: Beast Below; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_recalled:hand:required:active:when=self_played`
- out: Beast Below; type `similar_effect`; strength 0.72; reason `secondary:move_to_zone:hand:hand:required:active:when=self_played`

### [inferred-relation] Zenith Blade

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- in: Radiant Dawn; type `enabled_by`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Radiant Dawn; type `enables`; strength 0.88; reason `unit_stunned_enables_unit_stunned`
- out: Maduli the Gatekeeper; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield[controller=opponent]:active`
- out: Moonfall; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield[controller=opponent]:active`
- out: Moonfall; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield[controller=opponent]:optional:active`
- out: Vex, Mocking; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent;locatio...`
- out: Vex, Mocking; type `similar_effect`; strength 0.72; reason `output:event_produced:state_modifier:stun:unit_stunned:unit[controller=opponent;locatio...`
- in: Maduli the Gatekeeper; type `similar_effect`; strength 0.72; reason `secondary:move_output:unit_moved:battlefield[controller=opponent]:active`

### [inferred-relation] Zephyr Sage

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Jeweled Colossus; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Lee Sin, Ascetic; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Leona, Determined; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Stalwart Poro; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Sunlit Guardian; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Taric, Protector; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Trevor Snoozebottom; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`
- out: Vex, Mocking; type `similar_effect`; strength 0.72; reason `output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::while:req...`

### [inferred-relation] Zhonya's Hourglass

- authority_note: pipeline-suggested relations only; never official ruling authority.

Pipeline-suggested related cards:
- out: Bloodharbor Ripper; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- out: Conscription; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- out: Forge of the Future; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- out: Highlander; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- out: Hostile Takeover; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`
- out: Petricite Monument; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- out: Poro Snax; type `similar_effect`; strength 0.72; reason `event:event_produced:produced_event:kill:self_dies:card:::required`
- out: Possession; type `similar_effect`; strength 0.72; reason `output:event_produced:movement:return_to_hand:unit_recalled:card[zone=base]:::required`

## Broad Or Low-Confidence Relations

[quality-warning] Broad relations are omitted from per-card blocks in the default GPT package. They are summarized here for audit context.

- broad_relation_count: 4889
- broad_reasons: spell_card_can_be_countered (3438), cost:rune:any (1451)

## Experimental Deck Synergy

[inferred-relation] `deck_synergy` is experimental and default hidden when the dataset manifest marks it that way.

### [inferred-relation] Adaptatron

- in: Bubble Bot; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- in: Rumble, Hotheaded; type `deck_synergy`; strength 0.66; reason `target_tag:mech`

### [inferred-relation] Akshan, Mischievous

- in: Body Rune; type `deck_synergy`; strength 0.306; reason `cost:rune:body`
- in: Seal of Strength; type `deck_synergy`; strength 0.306; reason `cost:rune:body`

### [inferred-relation] Alpha Strike

- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Alpha Wildclaw

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:cat`

### [inferred-relation] Altar of Blood

- in: Body Rune; type `deck_synergy`; strength 0.275; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.275; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.275; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.275; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.275; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.275; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.275; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.275; reason `cost:rune:calm`

### [inferred-relation] Altar to Unity

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Ancient Henge

- in: Hextech Anomaly; type `deck_synergy`; strength 0.612; reason `cost:energy:variable`

### [inferred-relation] Ancient Warmonger

- in: Chaos Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:chaos`
- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Anivia, Primal

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:bird`

### [inferred-relation] Arachnoid Horror

- out: Crowd Favorite; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Enthralling Protector; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Arise!

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Armed Assailant

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Fury Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:fury`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Assembly Rig

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Azir, Ascendant

- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:bird`

### [inferred-relation] Azir, Sovereign

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Stealthy Pursuer; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`
- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] B.F. Sword

- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Unity; type `deck_synergy`; strength 0.68; reason `cost:rune:order`

### [inferred-relation] Back Off

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Baited Hook

- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Bard, Mercurial

- out: Stealthy Pursuer; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`

### [inferred-relation] Bashful Bloom

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`
- in: Hextech Anomaly; type `deck_synergy`; strength 0.612; reason `cost:energy:partial`
- in: Lux, Crownguard; type `deck_synergy`; strength 0.34; reason `cost:energy:partial`

### [inferred-relation] Battle Mistress

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Bellows Breath

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Mind Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:mind`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Bird

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:bird`

### [inferred-relation] Black Market Broker

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Blade of the Ruined King

- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Unity; type `deck_synergy`; strength 0.68; reason `cost:rune:order`

### [inferred-relation] Blast Cone

- in: Blitzcrank, Impassive; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`
- in: Charm; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`
- in: Dragon's Rage; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`
- in: Evelynn, Entrancing; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`
- in: Iascylla; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`
- in: Imposing Challenger; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`
- in: Irresistible Faefolk; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`
- in: Isolate; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`

### [inferred-relation] Blast Corps Cadet

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Fury Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:fury`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Blastcone Fae

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Blazing Scorcher

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Fury Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:fury`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Blighted Battleaxe

- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Hand of Noxus; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Blind Monk

- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Blitzcrank, Impassive

- out: Blast Cone; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`
- in: Bubble Bot; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- in: Rumble, Hotheaded; type `deck_synergy`; strength 0.66; reason `target_tag:mech`

### [inferred-relation] Block

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Blood Money

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Blood Rose

- in: Poppy, Paragon; type `deck_synergy`; strength 0.68; reason `cost:xp:3`
- in: Voracious Gromp; type `deck_synergy`; strength 0.68; reason `cost:xp:3`
- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Blood Rush

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Bloodharbor Ripper

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Body Rune

- out: Back Off; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- out: Blastcone Fae; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- out: Block; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- out: Bone Skewer; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- out: Boneshiver; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- out: Bullet Time; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- out: Bushwhack; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- out: Consult the Past; type `deck_synergy`; strength 0.68; reason `cost:rune:body`

### [inferred-relation] Bonds of Strength

- in: Lux, Crownguard; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- in: Undertitan; type `deck_synergy`; strength 0.612; reason `cost:energy:2`

### [inferred-relation] Bone Skewer

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Boneshiver

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Boots of Swiftness

- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`

### [inferred-relation] Breakneck Mech

- in: Bubble Bot; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- in: Rumble, Hotheaded; type `deck_synergy`; strength 0.66; reason `target_tag:mech`

### [inferred-relation] Brush

- out: Alpha Wildclaw; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- out: Anivia, Primal; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Azir, Ascendant; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Azir, Sovereign; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Bird; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Cemetery Attendant; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- out: Crimson Pigeons; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:ivern`

### [inferred-relation] Brutalizer

- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Bubble Bot

- out: Adaptatron; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- out: Blitzcrank, Impassive; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- out: Breakneck Mech; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- in: Rumble, Hotheaded; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- out: Carrion Dredger; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- out: Dangerous Duo; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- out: Ferrous Forerunner; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- out: Forecaster; type `deck_synergy`; strength 0.66; reason `target_tag:mech`

### [inferred-relation] Bullet Time

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Bushwhack

- in: Altar to Unity; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Arise!; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Assembly Rig; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Bashful Bloom; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Battle Mistress; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Black Market Broker; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Blood Money; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Bloodharbor Ripper; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Call to Battle

- out: Stealthy Pursuer; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`

### [inferred-relation] Called Shot

- in: Chaos Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:chaos`
- in: Seal of Discord; type `deck_synergy`; strength 0.612; reason `cost:rune:chaos`

### [inferred-relation] Calm Rune

- out: Azir, Ascendant; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- out: Back Off; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- out: Blastcone Fae; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- out: Block; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- out: Bone Skewer; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- out: Brutalizer; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- out: Bullet Time; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- out: Bushwhack; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Card Sharp

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Carrion Dredger

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Bubble Bot; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- in: Rumble, Hotheaded; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Cemetery Attendant

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:dog`

### [inferred-relation] Chaos Rune

- out: Back Off; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- out: Blastcone Fae; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- out: Block; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- out: Bone Skewer; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- out: Boots of Swiftness; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- out: Bullet Time; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- out: Bushwhack; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- out: Consult the Past; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`

### [inferred-relation] Charm

- out: Blast Cone; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`

### [inferred-relation] Chem-Baroness

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Assembly Rig; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Baited Hook; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Blighted Battleaxe; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Chemtech Cask

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Clockwork Keeper

- in: Calm Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:calm`
- in: Seal of Focus; type `deck_synergy`; strength 0.612; reason `cost:rune:calm`

### [inferred-relation] Cloth Armor

- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Seal of Insight; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`

### [inferred-relation] Commander Ledros

- in: Order Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:order`
- in: Seal of Unity; type `deck_synergy`; strength 0.612; reason `cost:rune:order`

### [inferred-relation] Confront

- in: Altar to Unity; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Arise!; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Assembly Rig; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Bashful Bloom; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Battle Mistress; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Black Market Broker; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Blood Money; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Bloodharbor Ripper; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Conscription

- in: Poppy, Paragon; type `deck_synergy`; strength 0.367; reason `cost:xp:partial`
- in: Voracious Gromp; type `deck_synergy`; strength 0.367; reason `cost:xp:partial`
- in: Alpha Strike; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`
- in: Arachnoid Horror; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`
- in: Blood Rose; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`
- in: Crowd Favorite; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`
- in: Demacian Diplomat; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`
- in: Enthralling Protector; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Consult the Past

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Corina Veraza

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`
- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Crescent Guardian

- in: Chaos Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:chaos`
- in: Seal of Discord; type `deck_synergy`; strength 0.612; reason `cost:rune:chaos`

### [inferred-relation] Crimson Pigeons

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:bird`

### [inferred-relation] Crowd Favorite

- in: Arachnoid Horror; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Grim Resolve; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Gustwalker; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Herald of Spring; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Kha'Zix, Mutating Horror; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Master Yi, Tempered; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Mister Root; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Mosstomper; type `deck_synergy`; strength 0.68; reason `cost:xp:2`

### [inferred-relation] Cull

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`

### [inferred-relation] Curtain Call

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Daisy!

- out: Alpha Wildclaw; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- out: Anivia, Primal; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Azir, Ascendant; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Azir, Sovereign; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Bird; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Cemetery Attendant; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- out: Crimson Pigeons; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:ivern`

### [inferred-relation] Danger Zone

- in: Body Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:chaos`
- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Fury Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:fury`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Dangerous Duo

- in: Bubble Bot; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- in: Rumble, Hotheaded; type `deck_synergy`; strength 0.66; reason `target_tag:mech`

### [inferred-relation] Daring Poro

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:poro`

### [inferred-relation] Deadly Flourish

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Deceiver

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Demacian Diplomat

- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Desert's Call

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`
- in: Lux, Crownguard; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- in: Undertitan; type `deck_synergy`; strength 0.612; reason `cost:energy:2`

### [inferred-relation] Doran's Blade

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Seal of Strength; type `deck_synergy`; strength 0.68; reason `cost:rune:body`

### [inferred-relation] Doran's Ring

- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`

### [inferred-relation] Doran's Shield

- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Double Trouble

- in: Lux, Crownguard; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- in: Undertitan; type `deck_synergy`; strength 0.612; reason `cost:energy:2`

### [inferred-relation] Downstage Dramatics

- in: Lux, Crownguard; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- in: Undertitan; type `deck_synergy`; strength 0.612; reason `cost:energy:2`

### [inferred-relation] Dragon's Rage

- out: Blast Cone; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`

### [inferred-relation] Dragonsoul Sage

- out: Assembly Rig; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Baited Hook; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Blighted Battleaxe; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Blind Monk; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Bloodharbor Ripper; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Boneshiver; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Emperor of the Sands; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Ezreal, Prodigy; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Draven, Vanquisher

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Eager Drakehound

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:dog`

### [inferred-relation] Eclipse Herald

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:bird`

### [inferred-relation] Edge of Night

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Ekko, Recurrent

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Mind Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:mind`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Eminent Benefactor

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Emperor of the Sands

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Emperor's Dais

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Emperor's Divide

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Energy Conduit

- out: Assembly Rig; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Baited Hook; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Blighted Battleaxe; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Blind Monk; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Bloodharbor Ripper; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Boneshiver; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Emperor of the Sands; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Ezreal, Prodigy; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Enthralling Protector

- in: Arachnoid Horror; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Grim Resolve; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Gustwalker; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Herald of Spring; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Kha'Zix, Mutating Horror; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Master Yi, Tempered; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Mister Root; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Mosstomper; type `deck_synergy`; strength 0.68; reason `cost:xp:2`

### [inferred-relation] Evelynn, Entrancing

- out: Blast Cone; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`
- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`

### [inferred-relation] Existential Dread

- in: Lux, Crownguard; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- in: Undertitan; type `deck_synergy`; strength 0.612; reason `cost:energy:2`

### [inferred-relation] Experimental Hexplate

- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Seal of Insight; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`

### [inferred-relation] Eye of the Herald

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Unity; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Ezreal, Dashing

- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Seal of Insight; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`

### [inferred-relation] Ezreal, Prodigy

- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Facebreaker

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Fae Dragon

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Fae Porter

- out: Stealthy Pursuer; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`

### [inferred-relation] Faithful Manufactor

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Feral Strength

- in: Lux, Crownguard; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- in: Undertitan; type `deck_synergy`; strength 0.612; reason `cost:energy:2`

### [inferred-relation] Ferrous Forerunner

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Bubble Bot; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- in: Rumble, Hotheaded; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Fight or Flight

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Flash

- out: Stealthy Pursuer; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`

### [inferred-relation] Flurry of Feathers

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Forecaster

- in: Bubble Bot; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- in: Rumble, Hotheaded; type `deck_synergy`; strength 0.66; reason `target_tag:mech`

### [inferred-relation] Forge of the Future

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Forgefire Cape

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Forgotten Signpost

- out: Stealthy Pursuer; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`

### [inferred-relation] Fox-Fire

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Frigid Touch

- in: Lux, Crownguard; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- in: Undertitan; type `deck_synergy`; strength 0.612; reason `cost:energy:2`

### [inferred-relation] Frisky Hunter

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:cat`

### [inferred-relation] Frostcoat Cub

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Mind Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:mind`
- in: Seal of Insight; type `deck_synergy`; strength 0.612; reason `cost:rune:mind`

### [inferred-relation] Fury Rune

- out: Assembly Rig; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- out: Back Off; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- out: Blastcone Fae; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- out: Blighted Battleaxe; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- out: Block; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- out: Bone Skewer; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- out: Bullet Time; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- out: Bushwhack; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`

### [inferred-relation] Garbage Grabber

- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Gardens of Becoming

- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Gearhead

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Mind Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:mind`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Gem Jammer

- in: Bubble Bot; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- in: Rumble, Hotheaded; type `deck_synergy`; strength 0.66; reason `target_tag:mech`

### [inferred-relation] Gemhand Hunter

- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Grandmaster at Arms

- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Green Father

- out: Alpha Wildclaw; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- out: Anivia, Primal; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Azir, Ascendant; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Azir, Sovereign; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Bird; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Cemetery Attendant; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- out: Crimson Pigeons; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:ivern`

### [inferred-relation] Grim Resolve

- out: Crowd Favorite; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Enthralling Protector; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Guardian Angel

- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Guards!

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`

### [inferred-relation] Gustwalker

- out: Crowd Favorite; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Enthralling Protector; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:dog`

### [inferred-relation] Gutter Palace

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Hand of Noxus

- out: Assembly Rig; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Baited Hook; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Blighted Battleaxe; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Blind Monk; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Bloodharbor Ripper; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Boneshiver; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Emperor of the Sands; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Ezreal, Prodigy; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Hard Bargain

- in: Lux, Crownguard; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- in: Undertitan; type `deck_synergy`; strength 0.612; reason `cost:energy:2`

### [inferred-relation] Herald of Spring

- out: Crowd Favorite; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Enthralling Protector; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Herald of the Arcane

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Here to Help

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Hexdrinker

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Seal of Strength; type `deck_synergy`; strength 0.68; reason `cost:rune:body`

### [inferred-relation] Hextech Anomaly

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Hextech Gauntlets

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Hidden Blade

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Honest Broker

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Honeyfruit

- out: Assembly Rig; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Baited Hook; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Blighted Battleaxe; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Blind Monk; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Bloodharbor Ripper; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Boneshiver; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Emperor of the Sands; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Ezreal, Prodigy; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Hostile Takeover

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Hunter's Machete

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Seal of Strength; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Iascylla

- out: Blast Cone; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`

### [inferred-relation] Imposing Challenger

- out: Blast Cone; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`

### [inferred-relation] Irresistible Faefolk

- out: Blast Cone; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`

### [inferred-relation] Isolate

- out: Blast Cone; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`

### [inferred-relation] Ivern, Friend to All

- out: Alpha Wildclaw; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- out: Anivia, Primal; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Azir, Ascendant; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Azir, Sovereign; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Bird; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Cemetery Attendant; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- out: Crimson Pigeons; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Daring Poro; type `deck_synergy`; strength 0.66; reason `target_tag:poro`

### [inferred-relation] Ivern, Nurturer

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:ivern`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:ivern`

### [inferred-relation] Janna, Savior

- out: Blast Cone; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`

### [inferred-relation] Jaull-Fish

- in: Body Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:body`
- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Jhin, Murderous Artist

- out: Assembly Rig; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Baited Hook; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Blighted Battleaxe; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Blind Monk; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Bloodharbor Ripper; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Boneshiver; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Emperor of the Sands; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Ezreal, Prodigy; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Jinx, Demolitionist

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Fury Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:fury`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Kai'Sa, Survivor

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Fury Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:fury`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Keeper of Masks

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`

### [inferred-relation] Keeper of the Hammer

- in: Poppy, Paragon; type `deck_synergy`; strength 0.68; reason `cost:xp:3`
- in: Voracious Gromp; type `deck_synergy`; strength 0.68; reason `cost:xp:3`
- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Kha'Zix, Evolving Hunter

- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Kha'Zix, Mutating Horror

- out: Crowd Favorite; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Enthralling Protector; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Kraken Hunter

- in: Body Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:body`
- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Last Rites

- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`

### [inferred-relation] Lee Sin, Centered

- in: Body Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:body`
- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Legion Rearguard

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Fury Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:fury`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Lillia, Fae Fawn

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`
- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Lonely Poro

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:poro`

### [inferred-relation] Long Sword

- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Seal of Rage; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`

### [inferred-relation] Lotus Trap

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Loyal Poro

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:poro`

### [inferred-relation] Loyal Pup

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:dog`

### [inferred-relation] Lux, Crownguard

- out: Unforgiven; type `deck_synergy`; strength 0.68; reason `cost:energy:2`
- out: Vi, Hotheaded; type `deck_synergy`; strength 0.68; reason `cost:energy:2`
- out: Bonds of Strength; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- out: Desert's Call; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- out: Double Trouble; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- out: Downstage Dramatics; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- out: Existential Dread; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- out: Feral Strength; type `deck_synergy`; strength 0.612; reason `cost:energy:2`

### [inferred-relation] Machine Evangel

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Maduli the Gatekeeper

- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`

### [inferred-relation] Magma Wurm

- in: Altar to Unity; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Arise!; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Assembly Rig; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Bashful Bloom; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Battle Mistress; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Black Market Broker; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Blood Money; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Bloodharbor Ripper; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Marching Orders

- in: Hextech Anomaly; type `deck_synergy`; strength 0.551; reason `cost:energy:partial`
- in: Lux, Crownguard; type `deck_synergy`; strength 0.408; reason `cost:energy:partial`
- in: Undertitan; type `deck_synergy`; strength 0.408; reason `cost:energy:partial`
- in: Chem-Baroness; type `deck_synergy`; strength 0.275; reason `cost:energy:partial`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.275; reason `cost:energy:partial`
- in: Energy Conduit; type `deck_synergy`; strength 0.275; reason `cost:energy:partial`
- in: Hand of Noxus; type `deck_synergy`; strength 0.275; reason `cost:energy:partial`
- in: Honeyfruit; type `deck_synergy`; strength 0.275; reason `cost:energy:partial`

### [inferred-relation] Master Yi, Tempered

- out: Crowd Favorite; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Enthralling Protector; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Mega-Mech

- in: Bubble Bot; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- in: Rumble, Hotheaded; type `deck_synergy`; strength 0.66; reason `target_tag:mech`

### [inferred-relation] Megatusk

- in: Poppy, Paragon; type `deck_synergy`; strength 0.68; reason `cost:xp:3`
- in: Voracious Gromp; type `deck_synergy`; strength 0.68; reason `cost:xp:3`

### [inferred-relation] Mind Rune

- out: Back Off; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- out: Blastcone Fae; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- out: Block; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- out: Bone Skewer; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- out: Bullet Time; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- out: Bushwhack; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- out: Cloth Armor; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- out: Consult the Past; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`

### [inferred-relation] Mirror Image

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Mischievous Marai

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Miss Fortune, Captain

- in: Body Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:body`
- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Mister Root

- out: Crowd Favorite; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Enthralling Protector; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Chaos Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:chaos`
- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Moonfall

- out: Blast Cone; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`

### [inferred-relation] Mosstomper

- out: Crowd Favorite; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Enthralling Protector; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:dog`

### [inferred-relation] Mutated Mouser

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:cat`

### [inferred-relation] Mystic Poro

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:poro`

### [inferred-relation] Nami, Headstrong

- in: Calm Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:calm`
- in: Seal of Focus; type `deck_synergy`; strength 0.612; reason `cost:rune:calm`

### [inferred-relation] Nidalee, Cat Form

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:cat`

### [inferred-relation] Nilah, Joyful Ascetic

- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- in: Body Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:body`
- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Noxian Drummer

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Order Rune

- out: B.F. Sword; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- out: Back Off; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- out: Baited Hook; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- out: Blade of the Ruined King; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- out: Blastcone Fae; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- out: Block; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- out: Bone Skewer; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- out: Bullet Time; type `deck_synergy`; strength 0.68; reason `cost:rune:order`

### [inferred-relation] Pakaa Cub

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Pickpocket

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Piercing Light

- in: Fury Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:fury`
- in: Lux, Crownguard; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- in: Seal of Rage; type `deck_synergy`; strength 0.612; reason `cost:rune:fury`
- in: Undertitan; type `deck_synergy`; strength 0.612; reason `cost:energy:2`

### [inferred-relation] Plundering Poro

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:poro`

### [inferred-relation] Poppy, Defender of the Meek

- in: Poppy, Paragon; type `deck_synergy`; strength 0.612; reason `cost:xp:3`
- in: Voracious Gromp; type `deck_synergy`; strength 0.612; reason `cost:xp:3`

### [inferred-relation] Poppy, Paragon

- out: Blood Rose; type `deck_synergy`; strength 0.68; reason `cost:xp:3`
- out: Keeper of the Hammer; type `deck_synergy`; strength 0.68; reason `cost:xp:3`
- out: Megatusk; type `deck_synergy`; strength 0.68; reason `cost:xp:3`
- out: Poppy, Defender of the Meek; type `deck_synergy`; strength 0.612; reason `cost:xp:3`
- out: Safety Inspector; type `deck_synergy`; strength 0.612; reason `cost:xp:3`
- out: Conscription; type `deck_synergy`; strength 0.367; reason `cost:xp:partial`

### [inferred-relation] Poro Snax

- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Pouty Poro

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:poro`

### [inferred-relation] Power Nexus

- in: Body Rune; type `deck_synergy`; strength 0.275; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.275; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.275; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.275; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.275; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.275; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.275; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.275; reason `cost:rune:calm`

### [inferred-relation] Prize of Progress

- in: Bubble Bot; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- in: Rumble, Hotheaded; type `deck_synergy`; strength 0.66; reason `target_tag:mech`

### [inferred-relation] Production Surge

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Pyke, Dockside Butcher

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Pyke, Returned

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`

### [inferred-relation] Rabadon's Deathcrown

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Reaver's Row

- out: Stealthy Pursuer; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`

### [inferred-relation] Recruit the Vanguard

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Recurve Bow

- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Seal of Rage; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`

### [inferred-relation] Red Brambleback

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Fury Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:fury`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Rek'Sai, Breacher

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Fury Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:fury`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Relentless Pursuit

- out: Stealthy Pursuer; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`

### [inferred-relation] Renata Glasc, Industrialist

- in: Altar to Unity; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Arise!; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Assembly Rig; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Bashful Bloom; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Battle Mistress; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Black Market Broker; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Blood Money; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Bloodharbor Ripper; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Renata Glasc, Mastermind

- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Rengar, Pouncing

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:cat`

### [inferred-relation] Rengar, Trophy Hunter

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:cat`

### [inferred-relation] Rengar, Unseen

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Ride the Wind

- out: Stealthy Pursuer; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`

### [inferred-relation] Rocket Barrage

- in: Mind Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:mind`
- in: Seal of Insight; type `deck_synergy`; strength 0.612; reason `cost:rune:mind`
- in: Hextech Anomaly; type `deck_synergy`; strength 0.551; reason `cost:energy:partial`
- in: Lux, Crownguard; type `deck_synergy`; strength 0.306; reason `cost:energy:partial`
- in: Undertitan; type `deck_synergy`; strength 0.306; reason `cost:energy:partial`
- in: Chem-Baroness; type `deck_synergy`; strength 0.275; reason `cost:energy:partial`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.275; reason `cost:energy:partial`
- in: Energy Conduit; type `deck_synergy`; strength 0.275; reason `cost:energy:partial`

### [inferred-relation] Royal Guard

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Rumble, Hotheaded

- out: Adaptatron; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- out: Blitzcrank, Impassive; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- out: Breakneck Mech; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- out: Bubble Bot; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- out: Carrion Dredger; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- out: Dangerous Duo; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- out: Ferrous Forerunner; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- out: Forecaster; type `deck_synergy`; strength 0.66; reason `target_tag:mech`

### [inferred-relation] Rumble, Scrapper

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Bubble Bot; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- in: Rumble, Hotheaded; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Sacred Shears

- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Unity; type `deck_synergy`; strength 0.68; reason `cost:rune:order`

### [inferred-relation] Safety Inspector

- in: Poppy, Paragon; type `deck_synergy`; strength 0.612; reason `cost:xp:3`
- in: Voracious Gromp; type `deck_synergy`; strength 0.612; reason `cost:xp:3`

### [inferred-relation] Scorchclaw

- out: Crowd Favorite; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Enthralling Protector; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:dog`

### [inferred-relation] Scorn of the Moon

- out: Assembly Rig; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Baited Hook; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Blighted Battleaxe; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Blind Monk; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Bloodharbor Ripper; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Boneshiver; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Emperor of the Sands; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Ezreal, Prodigy; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Scrapyard Champion

- in: Bubble Bot; type `deck_synergy`; strength 0.66; reason `target_tag:mech`
- in: Rumble, Hotheaded; type `deck_synergy`; strength 0.66; reason `target_tag:mech`

### [inferred-relation] Scrutinizing Sergeant

- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Scryer's Bloom

- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`

### [inferred-relation] Scuttle Crab

- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Sea Monkey

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Seal of Discord

- out: Back Off; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- out: Blastcone Fae; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- out: Block; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- out: Bone Skewer; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- out: Boots of Swiftness; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- out: Bullet Time; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- out: Bushwhack; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- out: Consult the Past; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`

### [inferred-relation] Seal of Focus

- out: Azir, Ascendant; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- out: Back Off; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- out: Blastcone Fae; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- out: Block; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- out: Bone Skewer; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- out: Brutalizer; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- out: Bullet Time; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- out: Bushwhack; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Seal of Insight

- out: Back Off; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- out: Blastcone Fae; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- out: Block; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- out: Bone Skewer; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- out: Bullet Time; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- out: Bushwhack; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- out: Cloth Armor; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- out: Consult the Past; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`

### [inferred-relation] Seal of Rage

- out: Assembly Rig; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- out: Back Off; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- out: Blastcone Fae; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- out: Blighted Battleaxe; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- out: Block; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- out: Bone Skewer; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- out: Bullet Time; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- out: Bushwhack; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`

### [inferred-relation] Seal of Strength

- out: Back Off; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- out: Blastcone Fae; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- out: Block; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- out: Bone Skewer; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- out: Boneshiver; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- out: Bullet Time; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- out: Bushwhack; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- out: Consult the Past; type `deck_synergy`; strength 0.68; reason `cost:rune:body`

### [inferred-relation] Seal of Unity

- out: B.F. Sword; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- out: Back Off; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- out: Baited Hook; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- out: Blade of the Ruined King; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- out: Blastcone Fae; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- out: Block; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- out: Bone Skewer; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- out: Bullet Time; type `deck_synergy`; strength 0.68; reason `cost:rune:order`

### [inferred-relation] Serrated Dirk

- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Seal of Rage; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`

### [inferred-relation] Shadow

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Hand of Noxus; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Sharkling

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Fury Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:fury`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Shepherd's Heirloom

- in: Alpha Strike; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- in: Blood Rose; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- in: Crowd Favorite; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- in: Demacian Diplomat; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- in: Enthralling Protector; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- in: Gardens of Becoming; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- in: Gemhand Hunter; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- in: Herald of Spring; type `deck_synergy`; strength 0.68; reason `cost:xp:1`

### [inferred-relation] Shurelya's Requiem

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Sinister Poro

- out: Blast Cone; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`
- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:poro`

### [inferred-relation] Sivir, Mercenary

- in: Chaos Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:chaos`
- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Skyfall of Areion

- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Hand of Noxus; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Skyward Strike

- out: Blast Cone; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`

### [inferred-relation] Smoke and Mirrors

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Soaring Scout

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:bird`

### [inferred-relation] Soul Sword

- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Spinning Axe

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Sprite Burst

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Sprite Call

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`

### [inferred-relation] Sprite Fountain

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Sprite Mother

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Sprite Queen

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Stalking Wolf

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:dog`

### [inferred-relation] Stalwart Poro

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:poro`

### [inferred-relation] Stand United

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Stare Down

- out: Blast Cone; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`
- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Starhound

- out: Alpha Wildclaw; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- out: Anivia, Primal; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Azir, Ascendant; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Azir, Sovereign; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Bird; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Cemetery Attendant; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- out: Crimson Pigeons; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- out: Daring Poro; type `deck_synergy`; strength 0.66; reason `target_tag:poro`

### [inferred-relation] Stealthy Pursuer

- in: Azir, Sovereign; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`
- in: Bard, Mercurial; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`
- in: Call to Battle; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`
- in: Emperor's Divide; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`
- in: Fae Porter; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`
- in: Flash; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`
- in: Forgotten Signpost; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`
- in: Reaver's Row; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`

### [inferred-relation] Sterak's Gage

- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Stormbringer

- out: Stealthy Pursuer; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`

### [inferred-relation] Sudden Storm

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Svellsongur

- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Swift Scout

- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Switcheroo

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Tasty Faefolk

- in: Calm Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:calm`
- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Teemo, Scout

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Teemo, Strategist

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Temporal Portal

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Temptation

- out: Blast Cone; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`
- in: Lux, Crownguard; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- in: Undertitan; type `deck_synergy`; strength 0.612; reason `cost:energy:2`

### [inferred-relation] The Syren

- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- out: Stealthy Pursuer; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`

### [inferred-relation] The Zero Drive

- in: Chem-Baroness; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.68; reason `cost:energy:1`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.68; reason `cost:energy:1`

### [inferred-relation] Thousand-Tailed Watcher

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Mind Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:mind`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Thwonk!

- in: Lux, Crownguard; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- in: Undertitan; type `deck_synergy`; strength 0.612; reason `cost:energy:2`

### [inferred-relation] Tideturner

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Trapping Grounds

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Treasure Hoard

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Treasure Hunter

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Treasure Trove

- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`

### [inferred-relation] Trevor Snoozebottom

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Tricksy Tentacles

- out: Blast Cone; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`

### [inferred-relation] Trinity Force

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Seal of Strength; type `deck_synergy`; strength 0.68; reason `cost:rune:body`

### [inferred-relation] Trove Golem

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Trusty Ramhound

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:dog`

### [inferred-relation] Twisted Fate, Gambler

- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Insight; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Seal of Rage; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Seal of Unity; type `deck_synergy`; strength 0.68; reason `cost:rune:order`

### [inferred-relation] Ultrasoft Poro

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:poro`

### [inferred-relation] Undertitan

- out: Unforgiven; type `deck_synergy`; strength 0.68; reason `cost:energy:2`
- out: Vi, Hotheaded; type `deck_synergy`; strength 0.68; reason `cost:energy:2`
- out: Bonds of Strength; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- out: Desert's Call; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- out: Double Trouble; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- out: Downstage Dramatics; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- out: Existential Dread; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- out: Feral Strength; type `deck_synergy`; strength 0.612; reason `cost:energy:2`

### [inferred-relation] Unforgiven

- in: Lux, Crownguard; type `deck_synergy`; strength 0.68; reason `cost:energy:2`
- in: Undertitan; type `deck_synergy`; strength 0.68; reason `cost:energy:2`
- out: Stealthy Pursuer; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`

### [inferred-relation] Unlicensed Armory

- in: Fury Rune; type `deck_synergy`; strength 0.612; reason `cost:rune:fury`
- in: Seal of Rage; type `deck_synergy`; strength 0.612; reason `cost:rune:fury`

### [inferred-relation] Upstage Comedy

- in: Lux, Crownguard; type `deck_synergy`; strength 0.612; reason `cost:energy:2`
- in: Undertitan; type `deck_synergy`; strength 0.612; reason `cost:energy:2`

### [inferred-relation] Valley of Idols

- in: Chem-Baroness; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Dragonsoul Sage; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Energy Conduit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Hand of Noxus; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Honeyfruit; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Jhin, Murderous Artist; type `deck_synergy`; strength 0.612; reason `cost:energy:1`
- in: Scorn of the Moon; type `deck_synergy`; strength 0.612; reason `cost:energy:1`

### [inferred-relation] Vanguard Armory

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Vanguard Captain

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Veteran Poro

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:poro`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:poro`

### [inferred-relation] Vi, Hotheaded

- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Lux, Crownguard; type `deck_synergy`; strength 0.68; reason `cost:energy:2`
- in: Seal of Rage; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Undertitan; type `deck_synergy`; strength 0.68; reason `cost:energy:2`

### [inferred-relation] Vicious Snapjaws

- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Viktor, Innovator

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Viktor, Leader

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Void Assault

- out: Blast Cone; type `deck_synergy`; strength 0.68; reason `enemy_unit_moved_supports_enemy_unit_move_trigger`
- out: Stealthy Pursuer; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`

### [inferred-relation] Voidreaver

- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- in: Alpha Strike; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- in: Arachnoid Horror; type `deck_synergy`; strength 0.68; reason `cost:xp:2`
- in: Blood Rose; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- in: Crowd Favorite; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- in: Demacian Diplomat; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- in: Enthralling Protector; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- in: Gardens of Becoming; type `deck_synergy`; strength 0.68; reason `cost:xp:1`

### [inferred-relation] Voracious Gromp

- out: Blood Rose; type `deck_synergy`; strength 0.68; reason `cost:xp:3`
- out: Keeper of the Hammer; type `deck_synergy`; strength 0.68; reason `cost:xp:3`
- out: Megatusk; type `deck_synergy`; strength 0.68; reason `cost:xp:3`
- out: Poppy, Defender of the Meek; type `deck_synergy`; strength 0.612; reason `cost:xp:3`
- out: Safety Inspector; type `deck_synergy`; strength 0.612; reason `cost:xp:3`
- out: Conscription; type `deck_synergy`; strength 0.367; reason `cost:xp:partial`

### [inferred-relation] Wages of Pain

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`

### [inferred-relation] Walking Roost

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Zilean, Time Mage; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`

### [inferred-relation] Warmog's Armor

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Seal of Strength; type `deck_synergy`; strength 0.68; reason `cost:rune:body`

### [inferred-relation] Warwick, Hunter

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:dog`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:dog`

### [inferred-relation] Windsinger

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] World Atlas

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Seal of Insight; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`

### [inferred-relation] Wuju Apprentice

- out: Shepherd's Heirloom; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Voidreaver; type `deck_synergy`; strength 0.68; reason `cost:xp:1`
- out: Conscription; type `deck_synergy`; strength 0.275; reason `cost:xp:partial`

### [inferred-relation] Wuju Master

- in: Altar to Unity; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Arise!; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Assembly Rig; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Bashful Bloom; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Battle Mistress; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Black Market Broker; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Blood Money; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- in: Bloodharbor Ripper; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Xerath, Freed

- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Seal of Rage; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`

### [inferred-relation] Yeti Brawler

- out: Bushwhack; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Confront; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Magma Wurm; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Renata Glasc, Industrialist; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`
- out: Wuju Master; type `deck_synergy`; strength 0.82; reason `token_created_to_token_entry_modifier`

### [inferred-relation] Yuumi, Magical Cat

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:cat`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:cat`

### [inferred-relation] Zenith Blade

- out: Stealthy Pursuer; type `deck_synergy`; strength 0.66; reason `friendly_unit_moved_supports_move_with_unit_permission`

### [inferred-relation] Zephyr Sage

- in: Brush; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Daisy!; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Green Father; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Ivern, Friend to All; type `deck_synergy`; strength 0.66; reason `target_tag:bird`
- in: Starhound; type `deck_synergy`; strength 0.66; reason `target_tag:bird`

### [inferred-relation] Zhonya's Hourglass

- in: Body Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:body`
- in: Calm Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`
- in: Chaos Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Fury Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:fury`
- in: Mind Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:mind`
- in: Order Rune; type `deck_synergy`; strength 0.68; reason `cost:rune:order`
- in: Seal of Discord; type `deck_synergy`; strength 0.68; reason `cost:rune:chaos`
- in: Seal of Focus; type `deck_synergy`; strength 0.68; reason `cost:rune:calm`

### [inferred-relation] Zilean, Time Mage

- in: Altar to Unity; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`
- in: Arise!; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`
- in: Assembly Rig; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`
- in: Bashful Bloom; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`
- in: Carrion Dredger; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`
- in: Corina Veraza; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`
- in: Deceiver; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`
- in: Desert's Call; type `deck_synergy`; strength 0.66; reason `token_unit_created_supports_token_copy_replacement`
