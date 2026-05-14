# Card Explorer Dataset Report

Report for the sharded card explorer dataset rooted at `data/processed/web/card_explorer_index.json`.

## Summary

- card_count: 767
- fact_count: 6311
- relation_count: 14590
- high_signal_relation_count: 9701
- broad_relation_count: 4889
- cards_with_rule_variants: 44

## Snapshot

- date: 2026-05-13
- broad_relation_count_threshold: 500
- similarity: {'max_similar_facts_per_key': 35, 'broad_similar_facts_per_key': 12, 'always_skip_keys': ['output:payoff_output:card_flow:draw:card_drawn:1:card::::required', 'output:payoff_output:card_flow:draw:card_drawn:1:card::::optional', 'predicate:payoff_output:payoff:repeat_effect::::optional', 'output:state_or_modifier:state_modifier:ready:self_ready:card:::required', 'output:state_or_modifier:state_modifier:ready:self_ready:card:::optional', 'output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::required', 'output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional'], 'broad_key_markers': ['repeat_effect', 'card_drawn:1:card', 'card_recycled', 'self_ready', 'secondary:require_state', 'secondary:stat_family']}
- legacy_rule_count_max: 650

## Filter Option Counts

- domains: 7
- card_types: 6
- tags: 113
- keywords: 24
- triggers: 22
- produced_events: 23
- outputs: 46
- predicates: 47
- energy: 12
- might: 12
- power: 4

## Web Artifacts

- shard_count: 32
- max_artifact_bytes: 52428800
- index_bytes: 1810051
- largest_relation_shard: 28.json (831989 bytes)
- largest_fact_shard: 00.json (226211 bytes)

## Relation Types

- similar_effect: 6634
- deck_synergy: 3306
- enabled_by: 2325
- enables: 2325

## Coverage

- cards_missing_facts: 0
- cards_without_relations: 42
- cards_with_only_broad_relations: 0
- cards_with_uncovered_relational_lines: 0

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

## Cards Without Relations By Bucket

- other: 7
- vanilla/no_text: 7
- card_flow: 6
- movement/location: 5
- cost/resource: 5
- stat/buff/damage_modifier: 5
- kill/heal/replacement: 3
- permission/restriction: 2
- stun: 1
- damage: 1

## Broad Relation Reasons

- spell_card_can_be_countered: 3438
- cost:rune:any: 1451
