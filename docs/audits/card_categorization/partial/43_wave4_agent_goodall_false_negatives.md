# Onda 4 - falsos negativos e texto rico

Auditoria somente leitura. O agente nao editou arquivos; rodou apenas leitura/analise local. O `git status --short` ja mostrava worktree suja (`goal.md`, `docs/`), mas sem alteracoes do agente.

Criterio usado para "alto risco": carta com sinal textual da familia, sem predicado especifico esperado, e com poucos fatos uteis (`<=2`), nenhuma relacao, ou so relacoes broad (`spell_card_can_be_countered`/similarity). Fatos estruturais/identidade foram excluidos da contagem util.

## Contagens

| Familia | Cartas com sinal | Alto risco | Sem relacao | So broad | Zero fatos uteis | Poucos fatos |
|---|---:|---:|---:|---:|---:|---:|
| attachment/equipment | 113 | 45 | 6 | 24 | 3 | 37 |
| temporary/granted keyword | 84 | 29 | 4 | 17 | 4 | 19 |
| replacement/prevent | 28 | 21 | 2 | 15 | 0 | 18 |
| control | 24 | 19 | 0 | 14 | 3 | 16 |
| zone movement | 212 | 16 | 2 | 12 | 0 | 13 |
| score/win | 25 | 12 | 5 | 6 | 1 | 8 |
| play restriction | 23 | 5 | 2 | 3 | 0 | 4 |
| token creation | 55 | 5 | 2 | 3 | 0 | 4 |
| copy | 6 | 3 | 0 | 0 | 0 | 3 |
| swap | 2 | 2 | 1 | 1 | 1 | 2 |

## Prioridades

### P0 - regras faltantes com impacto direto em busca/relacao

#### `temporary/granted keyword`

- exemplos: `Fading Memories`, `Turn to Dust`, `Last Stand`, `Shadow's Call`, `Fiora, Victorious`, `Syndra, Transcendent`.
- lacuna: concessao de `[Temporary]`, multiplos keywords estaticos/condicionais e keyword grant em objetos nao unidade.
- regra faltante: `grant_keyword_static_or_temporary`, com payload `keyword`, `target`, `duration`, `polarity`, `kill_at_beginning_phase` quando `[Temporary]`.
- golden: `Fading Memories` deve emitir `gain_keyword temporary` para `unit_or_gear`; `Fiora, Victorious` deve emitir grants condicionais `[Deflect]`, `[Ganking]`, `[Shield]`.

#### `replacement/prevent`

- exemplos: `Counter Strike`, `Highlander`, `Tactical Retreat`, `Altar of Blood`, `Soraka, Wanderer`, `Zilean, Time Mage`.
- lacuna: `would ... instead`, `next time ... would`, prevencao de dano, substituicao de morte por heal/exhaust/recall.
- regra faltante: `replacement_would_instead` e `prevent_next_damage`.
- golden: `Counter Strike` deve emitir `prevent damage_dealt` com duracao `next_time_this_turn`; `Highlander` deve emitir replacement `would_die -> heal/exhaust/recall`.

#### `attachment/equipment`

- exemplos: `Heimerdinger, Inventor`, `Forge of the Fluft`, `Veiled Temple`, `Gearhead`, `Svellsongur`.
- lacuna: habilidade concedida por Equipment/gear, copia de effect text enquanto attached, detach condicional, "attached to me doubles bonus".
- regra faltante: `equipment_attached_modifier`, `grant_activated_ability`, `copy_attached_unit_text`, `detach_equipment`.
- golden: `Svellsongur` deve emitir `copy_text` condicionado a `attached`; `Veiled Temple` deve emitir `detach equipment`.

#### `control`

- exemplos: `Mystic Reversal`, `Possession`, `Dancing Grenade`, `Detonate`.
- lacuna: `Gain control of a spell`, `Take control of it`, efeitos baseados em controller.
- regra faltante: `gain_control_target`, `controller_action_permission`.
- golden: `Mystic Reversal` deve emitir `control_change` de spell e `new_choices_permission`; `Possession` deve emitir `gain_control enemy_unit` + `recall`.

### P1 - lacunas relevantes mas mais localizadas

#### `swap`

- exemplos: `Switcheroo`, `Green Father`.
- regra faltante: `swap_stat_values`, `replace_battlefield_with_token`.
- golden: `Switcheroo` deve emitir `swap might` entre duas unidades no mesmo battlefield.

#### `score/win`

- exemplos: `Tianna Crownguard`, `Forgotten Monument`, `Glorious Executioner`, `Nidalee, Cat Form`, `Draven, Showboat`.
- regra faltante: `prevent_points_gain`, `score_restriction`, `combat_win_trigger`, `points_scaled_stat`.
- golden: `Tianna Crownguard` deve emitir restricao `opponents cannot gain points`; `Glorious Executioner` deve emitir trigger `combat_won`.

#### `zone movement`

- exemplos: `Minefield`, `The Candlelit Sanctum`, `Flame Chompers`, `Stellacorn Herder`.
- regra faltante: `mill_top_deck_to_trash`, `put_back_top_deck_order`, `self_discarded_play_permission`, `move_trigger_observer`.
- golden: `Minefield` deve emitir movimento de 2 cartas do Main Deck para trash.

### P2 - ja parcialmente modelado, mas com fatos pouco especificos

#### `copy`

- exemplos: `Mirror Image`, `Keeper of Masks`, `Svellsongur`.
- regra faltante: `token_becomes_copy`, `copy_effect_text`.
- golden: `Mirror Image` deve emitir `play_token Reflection` + `copy target unit` + `Temporary`.

#### `token creation`

- exemplos: `Zilean, Time Mage`, `Baron Nashor`, `Green Father`.
- regra faltante: `additional_token_copy_replacement`, `add_battlefield_token_to_board`.
- golden: `Zilean` deve emitir replacement `play token unit -> play token plus copy`.

#### `play restriction`

- exemplos: `Brynhir Thundersong`, `Lilting Lullaby`, `Rockfall Path`.
- regra faltante: `cannot_play_cards_duration`, `cannot_play_spells_duration`, `cannot_play_units_here`.
- golden: `Brynhir Thundersong` deve emitir restricao `opponents cannot play cards this_turn`.

## Comandos usados

```powershell
Get-ChildItem -Force
rg --files
Get-ChildItem -Recurse -Filter reports -Directory
Get-Content -Path data\processed\cards\normalized\cards_normalized.json -TotalCount 40
Get-Content -Path data\processed\cards\semantic\cards_semantic_facts.jsonl -TotalCount 5
Get-Content -Path data\processed\cards\relations\cards_card_relations.jsonl -TotalCount 5
Get-Content -Path scripts\04_cards_feature_extraction\contracts\feature_relation_taxonomy.json -TotalCount 80
Get-Content -Path scripts\04_cards_feature_extraction\contracts\semantic_extraction_rules.json -TotalCount 80
python -  # scripts inline somente leitura para cruzar cards/fatos/relacoes
rg -n "Temporary|replacement|prevent|copy|control|score|Equipment|gear|token|false negative|blind" docs\audits data\processed\cards\semantic data\processed\cards\relations scripts\tmp
Get-Content -Path data\processed\cards\relations\cards_card_relations_report.md -TotalCount 160
Get-Content -Path data\processed\cards\semantic\cards_semantic_audit_report.md -TotalCount 160
Get-Content -Path scripts\tmp\card_relation_blind_spots.md -TotalCount 200
git status --short
```
