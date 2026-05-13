# Cards Card Relations Report

Report for `data/processed/cards/relations/cards_card_relations.jsonl`.

## Summary

- fact_count: 6311
- relation_count: 14590
- cards_with_outgoing_relations: 709
- cards_with_incoming_relations: 724
- duplicate_relation_candidates: 1365
- collapsed_relations: 1365

## By Relation Type

- similar_effect: 6634
- deck_synergy: 3306
- enabled_by: 2325
- enables: 2325

## Top Match Reasons

- spell_card_can_be_countered: 3438
- cost:rune:any: 1451
- friendly_unit_dies_enables_self_dies: 384
- predicate:restriction_or_permission:permission:move:card:battlefield:::source=battlefield: 380
- cost:energy:1: 357
- token_created_to_token_entry_modifier: 314
- event:state_or_modifier:entry_state:enter_ready:self_enters:card:::required: 272
- secondary:move_output:unit_recalled:hand:active: 208
- equipment_attached_enables_equipment_attached: 202
- generic_unit_death_enables_friendly_unit_dies: 180
- cost:rune:fury: 132
- output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:2:energy:card:::required: 132
- output:payoff_output:card_flow:draw:card_drawn:2:card::::required: 132
- secondary:move:hand[zone=hand]:hand:required:active: 130
- secondary:move_output:unit_recalled:hand:required:active: 130
- secondary:move_to_zone:hand:hand:required:active: 130
- secondary:damage:positive:unit[location=battlefield]::required:active: 130
- secondary:move_output:unit_moved:base:active: 126
- cost:rune:mind: 118
- cost:rune:body: 114
- cost:rune:calm: 112
- cost:rune:chaos: 112
- output:state_or_modifier:stat_change:modify_stat:might_modified:1:might:card::this_turn:required: 110
- event:event_produced:removal:kill:unit_dies:unit:::required: 110
- predicate:payoff_output:payoff:repeat_effect::::optional:cost=energy=2: 110
- cost:rune:order: 108
- secondary:stat_family:might_modified:might:negative:active: 90
- output:payoff_output:resource_change:channel:rune_channeled:1:rune::::required: 90
- output:payoff_output:token_creation:play_token:gold_gear_token_created::::required:object=token: 90
- event:event_produced:produced_event:kill:self_dies:card:::required: 90
- card_recycled_enables_card_recycled: 84
- friendly_unit_dies_enables_friendly_unit_dies: 80
- unit_buffed_enables_unit_buffed: 72
- output:payoff_output:resource_change:gain_xp:xp_gained:1:xp::::required: 72
- secondary:attachment:attach:gear:active: 72
- output:event_produced:state_modifier:buff:unit_buffed:unit[controller=friendly]:::required: 72
- output:event_produced:produced_event:attach:equipment_attached:card:::optional:object=gear[controller=you]:when=self_played: 72
- output:state_or_modifier:static_modifier:reduce_cost:gear_cost_reduced:1:rune:gear[controller=you]:::optional:when=self_played: 72
- secondary:state_action:ready:unit_ready:unit:active: 72
- output:payoff_output:card_flow:draw:card_drawn:1:card::::required:when=self_played: 72

## Top Contract Rules

- similarity: 6634
- spell_card_can_be_countered: 3438
- resource_synergy: 2698
- friendly_unit_dies_enables_self_dies: 384
- token_created_to_token_entry_modifier: 314
- tag_target_synergy: 222
- equipment_attached_enables_equipment_attached: 202
- generic_unit_death_enables_friendly_unit_dies: 180
- card_recycled_enables_card_recycled: 84
- friendly_unit_dies_enables_friendly_unit_dies: 80
- unit_buffed_enables_unit_buffed: 72
- spell_played_enables_spell_played: 54
- unit_stunned_enables_unit_stunned: 44
- token_unit_created_supports_token_copy_replacement: 40
- card_discarded_enables_self_discarded: 40
- generic_unit_death_enables_enemy_unit_dies: 36
- self_unit_dies_enables_friendly_unit_dies: 30
- enemy_unit_moved_supports_enemy_unit_move_trigger: 16
- friendly_unit_moved_supports_move_with_unit_permission_friendly: 10
- friendly_unit_moved_supports_move_with_unit_permission_you: 6
- enemy_unit_dies_enables_enemy_unit_dies: 4
- rune_recycled_enables_rune_recycled: 2

## Skipped Similarity Keys

- output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::optional: 7
- output:event_produced:card_flow:recycle:card_recycled:card[zone=main_deck]:::required: 17
- output:payoff_output:card_flow:draw:card_drawn:1:card::::optional: 6
- output:payoff_output:card_flow:draw:card_drawn:1:card::::required: 44
- output:state_or_modifier:state_modifier:ready:self_ready:card:::optional: 2
- output:state_or_modifier:state_modifier:ready:self_ready:card:::required: 12
- predicate:payoff_output:payoff:repeat_effect::::optional: 7
- predicate:restriction_or_permission:restriction:require:::while:: 47
- secondary:require_state:while_attacker:while:active: 24
- secondary:require_state:while_defender:while:active: 17
- secondary:stat_family:might_modified:might:positive:active: 34

## Broad Match Reasons

- cost:rune:any: 1451
- spell_card_can_be_countered: 3438
