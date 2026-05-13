# Onda 3 - agente Dalton - amostragem sistematica de cartas

## Escopo

Auditoria somente leitura da onda 3 por amostragem sistematica de cartas normalizadas.

O agente leu os arquivos pedidos e usou `cards_card_relations.jsonl/report.md` para classificar buckets de relacao. Comparou `rules_lines`, `effect_lines` e `rule_variants` contra fatos nao estruturais, ignorando `has_card_type`, `has_domain`, `has_stat` e `has_keyword` salvo quando relevante.

## Metodologia

Amostra: 61 cartas unicas, escolhidas por bucket computavel: sem relacao, broad-only, alto grau, `effect_lines`, `rule_variants`, modais, custo, movimento, score, copy e vanilla.

## Cartas amostradas

- sem relacao: `Bandle Tree`, `Baron Pit`, `Forge of the Fluft`, `Forgotten Monument`, `Hall of Legends`, `Reaver's Row`, `Rockfall Path`, `The Candlelit Sanctum`.
- broad-only: `Counter Strike`, `Keeper's Verdict`, `Mystic Reversal`, `Switcheroo`, `Fading Memories`, `Angle Shot`, `Dancing Grenade`, `Lotus Trap`.
- high degree: `Abandon`, `Flurry of Feathers`, `Defy`, `Riposte`, `Lilting Lullaby`, `Karma, Channeler`, `Mistfall`, `Bloodharbor Ripper`.
- effect_lines/equip: `Warmog's Armor`, `Hexdrinker`, `Boneshiver`, `Hunter's Machete`, `Trinity Force`, `Guardian Angel`, `Rabadon's Deathcrown`, `Boots of Swiftness`.
- rule_variants: `Gold`, `Wuju Master`, `The Boss`, `Emperor of the Sands`, `Green Father`, `Scorn of the Moon`, `Void Burrower`, `Master Yi, Unstoppable`.
- modais/custo/movement/score/copy: `Curtain Call`, `Rocket Barrage`, `Buhru Captain`, `King's Edict`, `Altar of Blood`, `Power Nexus`, `The Grand Plaza`, `Aspirant's Climb`, `Gutter Palace`, `Chem-Baroness`, `Find Your Center`, `Needlessly Large Yordle`, `Svellsongur`, `Deceiver`, `Mirror Image`.
- vanilla/controle negativo: `Body Rune`, `Calm Rune`, `Mountain Drake`, `Playful Phantom`, `Mega-Mech`, `Vanguard Sergeant`.

## Achados

### A1 - Custos com simbolos sao contados errado

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: 32 fatos `[Equip]` duplicam simbolos por ler custo e reminder text. `Boneshiver` vira `energy, energy, body, body`; `Svellsongur` idem. No outro sentido, `Power Nexus` tem 4 runas rainbow no texto e payload com 3; `Altar of Blood` tem 3 e payload com 2. Houve 43 candidatos de subcontagem em linhas `pay`/`Repeat`/`Accelerate`.
- regra relacionada: `activation_cost`, `generic_cost_reduction`, familia `cost_modifier`.
- impacto provavel no produto final: filtros e relacoes por custo ficam falsos, especialmente Equip/Repeat/Accelerate e custos repetidos.
- recomendacao: parser de custo deve operar sobre segmento sem reminder e preservar vetor exato de simbolos.
- teste que deveria existir: goldens de cardinalidade exata para `Boneshiver`, `Svellsongur`, `Power Nexus`, `Altar of Blood`, `Rocket Barrage`.

### A2 - Reminder text e texto entre aspas vazam como efeito da carta fonte

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Bloodharbor Ripper` cria fatos `kill_self` e `add_resource` a partir de `It has "[Reaction][>] Kill this..."`, como se a lenda tivesse a habilidade do token Gold; isso ajuda a explicar grau 115. `Buhru Captain` gera buffs extras e `modify_stat` a partir do reminder `To buff a unit...`. `Forge of the Fluft` e `Gardens of Becoming` achatam habilidades concedidas como custos/outputs da fonte.
- regra relacionada: `activation_cost`, `add_resource`, `buff_unit`; falta modelagem `granted_ability`.
- impacto provavel no produto final: relacoes de recurso, morte, buff e custo apontam para cartas erradas.
- recomendacao: separar reminder, texto citado e habilidade concedida com bearer/recipient explicito.
- teste que deveria existir: negativos para `Bloodharbor Ripper` e `Buhru Captain`; positivos de granted ability para `Forge of the Fluft` e `Gardens of Becoming`.

### A3 - Copy esta quase todo ausente

- categoria do achado: regra ausente
- severidade: alta
- confianca: alta
- evidencia: 5 cartas amostradas/contadas tem `copy` ou `effect text`; so `Reflection` e `Zilean, Time Mage` emitem `predicate: copy`. `Svellsongur`, `Deceiver` e `Mirror Image` nao tem fato de copia.
- regra relacionada: `copy_effect`; regras existentes so cobrem `self_becomes_copy_when_played` e `token_play_copy_replacement`.
- impacto provavel no produto final: busca/sinergia por copy perde a maioria dos casos reais.
- recomendacao: adicionar padroes para `becomes a copy`, `copy that unit's text` e copia de token criada por outra carta.
- teste que deveria existir: goldens para `Svellsongur`, `Deceiver`, `Mirror Image`.

### A4 - Modais e escolhas continuam achatados

- categoria do achado: parsing/normalizacao
- severidade: alta
- confianca: alta
- evidencia: `Curtain Call` e `Rocket Barrage` tem `Choose one` sem fato de grupo modal; as opcoes saem como efeitos obrigatorios independentes. `Buhru Captain` emite `draw` e `buff` opcionais sem exclusividade. `King's Edict` so mantem `Kill those units`, sem o chooser `each other player` nem a restricao `hasn't been chosen`.
- regra relacionada: familias `choice_modal` e `modal_option`; regras atuais nao criam `choice_group_id`.
- impacto provavel no produto final: downstream le alternativas como efeitos cumulativos.
- recomendacao: criar fatos de escolha com `choice_group_id`, cardinalidade, exclusividade, chooser e heranca de custo/trigger.
- teste que deveria existir: `Curtain Call`, `Rocket Barrage`, `Buhru Captain`, `King's Edict`.

### A5 - Score, Victory Score e win condition perdem condicoes

- categoria do achado: regra ausente
- severidade: media-alta
- confianca: alta
- evidencia: 7 cartas tem texto de Victory Score/win. `Chem-Baroness` segunda linha nao gera fato. `Poppy, Paragon`, `Find Your Center` e `Leona, Zealot` emitem outputs como se fossem incondicionais. `Aspirant's Climb` e `score` generico, embora altere o limiar de vitoria. `The Grand Plaza` e `Gutter Palace` marcam `win_condition`, mas sem as condicoes numericas no payload.
- regra relacionada: `score_points`, `win_game_condition`, familia `score_modifier`.
- impacto provavel no produto final: filtros de score confundem pontuar, mudar limiar e vencer o jogo.
- recomendacao: separar `score_points`, `victory_score_modifier`, `win_condition` e `score_threshold_condition`.
- teste que deveria existir: goldens para as 7 cartas citadas.

### A6 - Recall e modelado como move mesmo quando o texto diz que nao e move

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Altar of Blood`, `Guardian Angel`, `Zhonya's Hourglass`, `The Boss`, `Highlander`, `Possession` e outros emitem `fact_type: movement`, `event.id: unit_moved` para `recall`. Varios textos dizem literalmente `This isn't a move.`
- regra relacionada: `recall_unit`, `return_to_owner_hand`, familia `movement_modifier`.
- impacto provavel no produto final: sinergias de `when move` podem casar com recall indevidamente.
- recomendacao: usar evento proprio `unit_recalled`/`returned_to_base`, com flag `is_move: false`.
- teste que deveria existir: negativos de move-trigger para `The Boss`, `Zhonya's Hourglass`, `Possession`.

### A7 - Broad-only e sem relacao escondem cartas com texto rico

- categoria do achado: integracao entre etapas
- severidade: alta
- confianca: alta
- evidencia: ha 100 cartas sem relacao, 86 com texto. Ha 22 broad-only; exemplos com 0 fatos nao estruturais: `Keeper's Verdict`, `Mystic Reversal`, `Switcheroo`, `Fading Memories`, `Turn to Dust`. A unica relacao desses casos e `spell_card_can_be_countered`.
- regra relacionada: `semantic_quality_policy` broadness; lacunas em regras de efeito.
- impacto provavel no produto final: explorador web mostra cartas complexas como se so fossem `counterable spells` ou sem sinergia.
- recomendacao: criar alerta de qualidade para broad-only com texto relacional e para cartas textuais sem fatos nao estruturais.
- teste que deveria existir: invariant `broad-only spell with relational text must have at least one specific fact or blind-spot bucket`.

### A8 - `rule_variants` nao entram como fonte semantica variant-aware

- categoria do achado: parsing/normalizacao
- severidade: media
- confianca: media-alta
- evidencia: 44 cartas tem `rule_variants`; os fatos usam apenas `play_id` e `source_ref` canonico, sem `printing_id`/variant ref. `Bloodharbor Ripper` tem variante com e sem reminder de Gold, mas os fatos aplicam a leitura canonica ao `play_id` inteiro. `The Boss` tem duas redacoes com diferencas de custo/recall.
- regra relacionada: `default_source_fields: rules_lines/effect_lines`; ausencia de fonte variante.
- impacto provavel no produto final: uma impressao pode herdar fatos de texto que nao esta naquela impressao.
- recomendacao: normalizar uma fonte canonica limpa ou emitir fatos por variante/printing quando o texto divergir semanticamente.
- teste que deveria existir: snapshot de variantes para `Bloodharbor Ripper`, `The Boss`, `Master Yi, Unstoppable`.

## Testes faltando

- Cardinalidade exata de simbolos em custos, incluindo custo repetido, Equip reminder, Repeat e Accelerate.
- Negativos para reminder text e texto entre aspas que descreve token/keyword, nao a carta fonte.
- Goldens de `granted_ability` com bearer/recipient.
- Goldens de copy para `Svellsongur`, `Deceiver`, `Mirror Image`.
- Goldens de modal com `choice_group_id`.
- Invariant de recall nao produzir `unit_moved`.
- Invariant para broad-only/sem relacao com texto relacional.
- Cobertura variant-aware para cartas com `rule_variants`.

## Comandos

```powershell
rg --files
Get-ChildItem -Force
Get-Item data\processed\cards\normalized\cards_normalized.json, data\processed\cards\semantic\cards_semantic_facts.jsonl, scripts\04_cards_feature_extraction\contracts\semantic_extraction_rules.json, scripts\04_cards_feature_extraction\contracts\semantic_quality_policy.json, scripts\04_cards_feature_extraction\contracts\feature_relation_taxonomy.json
Get-Content ... -TotalCount ...
rg -n "Broad Match Reasons|Broad|broad|Skipped" data\processed\cards\relations\cards_card_relations_report.md scripts\04_cards_feature_extraction\contracts\*.json
@' ... '@ | python -
git status --short
```

O agente informou que nao editou arquivos. O `git status --short` terminou com alteracoes ja presentes: `M goal.md` e `?? docs/`.
