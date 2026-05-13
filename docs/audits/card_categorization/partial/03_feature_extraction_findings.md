# Auditoria parcial 03 - extracao semantica de cartas

## Escopo analisado

Esta rodada focou em `scripts/04_cards_feature_extraction/extract_semantic_facts.py`, nos contratos de extracao e nos fatos gerados em `cards_semantic_facts.jsonl`.

O objetivo foi comparar comportamento real contra cartas normalizadas concretas e regras de categorizacao, especialmente onde a auditoria atual declara `0` erros e `0` warnings.

## Artefatos relidos

- `data/processed/cards/normalized/cards_normalized.json`
- `data/processed/cards/semantic/cards_semantic_facts.jsonl`
- `data/processed/cards/semantic/cards_semantic_audit_report.md`
- `data/processed/cards/semantic/cards_semantic_golden_report.json`
- `scripts/04_cards_feature_extraction/extract_semantic_facts.py`
- `scripts/04_cards_feature_extraction/audit_semantic_facts.py`
- `scripts/04_cards_feature_extraction/validate_semantic_golden_examples.py`
- `scripts/04_cards_feature_extraction/contracts/semantic_extraction_rules.json`
- `scripts/04_cards_feature_extraction/contracts/semantic_golden_examples.json`
- `scripts/04_cards_feature_extraction/contracts/semantic_quality_policy.json`
- `scripts/04_cards_feature_extraction/contracts/feature_relation_taxonomy.json`

## Cartas confrontadas

- `Vaults of Helia`
- `Janna, Savior`
- `Arachnoid Horror`
- `The Academy`
- `Dancing Grenade`
- `Safety Inspector`
- `Mageseeker Warden`
- `Disposal Order`
- `Rabadon's Deathcrown`
- `Bashful Bloom`
- `Mirror Image`
- `Sprite Burst`
- `Sprite Call`
- `Sprite Fountain`
- `Sprite Mother`
- `Sprite Queen`
- `Trevor Snoozebottom`

## Regras de extracao confrontadas

- `generic_cost_reduction`
- `move_unit`
- `trigger_self_conquers_or_holds`
- `trigger_self_conquers`
- `grant_keyword_to_target`
- `deal_damage`
- `kill_generic_unit`
- `prevent_ready_enemy_units_gear`
- `ready_unit`
- `play_token`
- `draw_cards`
- `recycle_card`

## Comandos executados e resultado

- `rg -n -F "line_has_optional_governor"`: confirmou aplicacao de modalidade opcional por linha em `extract_semantic_facts.py:217`, `:225`, `:981`, `:1715`.
- `rg -n -F "generic_cost_reduction"`: confirmou regra contratual em `semantic_extraction_rules.json:1873` e builder em `extract_semantic_facts.py:2054`.
- `rg -n -F "trigger_self_conquers"`: confirmou regras sobrepostas em `semantic_extraction_rules.json:67` e `:77`.
- `rg -n -F "Move (?P<target>"`: confirmou regex legado de movimento em `extract_semantic_facts.py:1991`.
- PowerShell sobre `cards_semantic_facts.jsonl`: confirmou `3011` fatos estruturais, `1759` por contrato e `658` por regra legada.
- PowerShell sobre cartas especificas: confirmou fatos falsos ou incompletos em `Vaults of Helia`, `Janna, Savior`, `The Academy`, `Disposal Order` e `Rabadon's Deathcrown`.
- Leitura de `cards_semantic_audit_report.md`: `5428` fatos, `27` linhas sem fatos, `0` erros, `0` warnings, `golden_pass: True`, `legacy_rule_count: 658`.
- Leitura de `cards_semantic_golden_report.json`: `40` exemplos, `73` fatos esperados, `73` encontrados, `pass: true`.

## Achados

### 1. Modificador de custo inverte direcao de aumento para reducao

- categoria do achado: bug de categorizacao critica
- severidade: critica
- confianca: alta
- evidencia: `generic_cost_reduction` casa `costs?` e o builder sempre emite `predicate: reduce_cost` e output `play_cost_reduced`. `Vaults of Helia` tem a linha normalizada `When you hold here, your non-token units cost :rb_energy_1: more to play this turn.` O fato gerado e `static_modifier / reduce_cost`, com evidencia `cost :rb_energy_1: more to play this turn` e output `play_cost_reduced`.
- consequencia observada: relacoes `similar_effect` ligam `Vaults of Helia` a cartas de desconto como `Battering Ram`, `Eager Apprentice`, `Ezreal, Prodigy`, `Irelia, Graceful`, `Marai Spire` e `Ornn's Forge`.
- regra afetada: `generic_cost_reduction`.
- recomendacao: separar custo aumentado de custo reduzido. `costs more` deve virar `increase_cost` ou `cost_increased`, com polaridade explicita.
- teste faltante: golden para `Vaults of Helia` rejeitando `reduce_cost` e exigindo output de aumento de custo.

### 2. Extracao por contrato e legado duplica fatos contraditorios

- categoria do achado: bug de implementacao
- severidade: alta
- confianca: alta
- evidencia: `facts_for_line` existe em `extract_semantic_facts.py:2119` e a auditoria reporta `658` fatos `legacy_rule`. O regex legado de movimento em `extract_semantic_facts.py:1991` ainda roda apos as regras contratuais. `Janna, Savior` gera dois fatos `move` para a mesma instrucao: um contratual correto com target `up to one enemy unit from here`, destination `its base`; outro legado com target bruto `up` e destination `one enemy unit from here to its base`.
- impacto: uma linha vira dois eventos, um deles com alvo semanticamente quebrado. Isso contamina similaridade e relacoes.
- recomendacao: quando uma regra contratual cobre uma evidencia, bloquear regras legadas equivalentes ou exigir deduplicacao por `source_ref.unit_index`, predicado e span de evidencia.
- teste faltante: golden negativo para `Janna, Savior` exigindo ausencia de target `raw: up`.

### 3. Triggers sobrepostos geram eventos duplicados

- categoria do achado: bug de regra contratual
- severidade: alta
- confianca: alta
- evidencia: `semantic_extraction_rules.json:67` define `trigger_self_conquers_or_holds`; `semantic_extraction_rules.json:77` define `trigger_self_conquers`. `Arachnoid Horror` com texto de Hunt `When I conquer or hold` gera `self_conquers`, `self_holds` e outro `self_conquers` duplicado.
- impacto: uma carta pode parecer observar mais triggers que observa, enviesando filtros e relacoes por trigger.
- recomendacao: adicionar guard de exclusao para `trigger_self_conquers` quando a evidencia contiver `or hold`, ou gerar um unico fato composto com dois eventos.
- teste faltante: golden para uma carta com Hunt exigindo exatamente dois eventos observados, sem duplicata.

### 4. Modalidade opcional e propagada para a linha inteira

- categoria do achado: bug de escopo
- severidade: alta
- confianca: alta
- evidencia: `line_has_optional_governor` marca a linha como opcional se encontra termos como `you may`; `payload_with_line_modality` aplica a modalidade ao fato. Em `The Academy`, a acao obrigatoria `give your next spell this turn [Repeat] equal to its base cost` vira `modality: optional` porque o reminder parentetico diz `You may pay the additional cost...`. Em `Dancing Grenade`, `Deal 2 to a unit` tambem vira opcional porque outra clausula da mesma linha diz que o controlador pode jogar o spell novamente.
- impacto: efeitos requeridos viram opcionais, alterando filtros, relacoes e interpretacao de payoff.
- recomendacao: escopar modalidade por clausula/evidencia, ignorar reminder text quando ele explica keyword ou custo e preservar `If they do` como condicao separada.
- teste faltante: golden para `The Academy` e `Dancing Grenade` exigindo a modalidade correta por clausula.

### 5. Negacao gera fatos positivos de acao

- categoria do achado: bug de negacao
- severidade: alta
- confianca: alta
- evidencia: `Safety Inspector` contem `If you paid my additional cost, you don't kill a unit this way`. A regra `kill_generic_unit` casa `kill a unit` dentro da negacao e emite fato positivo, alem da restricao correta. `Mageseeker Warden` contem `spells and abilities can't ready enemy units and gear`; a extracao gera a restricao `prevent`, mas tambem um fato positivo `ready`.
- impacto: cartas de prevencao/restricao podem aparecer como cartas que produzem o evento prevenido.
- recomendacao: criar negative guards comuns para `can't`, `cannot`, `don't`, `doesn't`, `prevent`, `instead`, `not`; aplicar antes de builders de acao positiva.
- teste faltante: goldens negativos para `Safety Inspector` e `Mageseeker Warden`.

### 6. Adjetivo de estado em token vira acao `ready`

- categoria do achado: bug de parsing local
- severidade: media
- confianca: alta
- evidencia: textos como `Play a ready ... token` geram fatos `ready` alem de `play_token`. A consulta local encontrou o padrao em `Bashful Bloom`, `Mirror Image`, `Sprite Burst`, `Sprite Call`, `Sprite Fountain`, `Sprite Mother`, `Sprite Queen`, `Trevor Snoozebottom` e `Deceiver`.
- impacto: criacao de token pronto se mistura com acao de ready sobre unidade existente.
- recomendacao: no contexto `Play a ready <...> token`, registrar `entry_state: ready` dentro do token criado e nao emitir `predicate: ready` separado.
- teste faltante: golden para `Sprite Burst` exigindo token state `ready` e ausencia de output `unit_ready`.

### 7. Modal choices sao emitidos como se todas as opcoes resolvessem

- categoria do achado: bug de estrutura semantica
- severidade: alta
- confianca: alta
- evidencia: `Disposal Order` tem `Choose one -`, depois opcao de reciclar ate 3 cartas e opcao `Draw 1.`. A extracao gera dois fatos `recycle` e um `draw`, todos com `modality: required`, sem grupo modal.
- impacto: filtros e relacoes podem tratar a carta como draw e recycle simultaneos.
- recomendacao: representar opcoes exclusivas com `choice_group_id` e `choice_mode`, mantendo outputs dentro de cada opcao.
- teste faltante: golden de exclusividade para `Disposal Order`.

### 8. Fatos de `effect_lines` ignoram contexto active/inactive

- categoria do achado: bug de contrato semantico
- severidade: alta
- confianca: alta
- evidencia: `Rabadon's Deathcrown` gera `static_modifier / modify_stat` a partir de `source_field: effect_lines` com `payload.modality: static`; a evidencia e `Your spells and abilities deal 3 Bonus Damage`, e a linha completa contem `(while this is attached)`.
- impacto: facts web e relacoes nao conseguem diferenciar modificador ativo no objeto attached de texto inativo na carta solta.
- recomendacao: toda extracao de `effect_lines` deve carregar `activation_context` e `applies_to`; o default nao deve ser static incondicional.
- teste faltante: golden especifico para gear com effect text.

### 9. Auditoria atual nao sinaliza linhas de alta prioridade sem cobertura suficiente

- categoria do achado: lacuna de auditoria
- severidade: alta
- confianca: alta
- evidencia: `cards_semantic_audit_report.md` declara `0` erros, `0` warnings e `27` linhas sem fatos. Subauditoria independente revisou linhas como `Rockfall Path`, `Blue Sentinel`, `Red Brambleback`, `Mystic Reversal`, `Svellsongur`, `Switcheroo`, `Rumble`, `Scrapper Mech`, `Maduli` e encontrou familias de alta prioridade ainda sem modelagem adequada. O proprio report atual mostra `legacy_rule_count: 658`, o que deveria ser um sinal de maturidade parcial.
- impacto: o status "sem issues" e otimista demais para decisao de produto.
- recomendacao: ranquear linhas sem cobertura por familia e prioridade do inventario; reportar uso de regra legada como warning quando o contrato declara que aquela familia ja deveria estar modelada.
- teste faltante: auditoria que combine `cards_taxonomy_alignment.json` com linhas sem fatos e `source_kind: legacy_rule`.

### 10. Contratos existem, mas Python ainda concentra semantica concreta

- categoria do achado: fragilidade arquitetural
- severidade: media
- confianca: alta
- evidencia: a etapa 04 README diz que `semantic_extraction_rules.json` deve conter regras deterministicas de extracao (`scripts/04_cards_feature_extraction/README.md:160-162`), mas o report atual ainda tem `658` fatos `legacy_rule`, e regras hard-coded de Python continuam emitindo semantica. A propria funcao de movimento legada e um exemplo concreto.
- impacto: revisores podem ajustar JSON esperando cobrir comportamento real, enquanto parte relevante ainda vive em regex Python sem schema contratual equivalente.
- recomendacao: reduzir legado por familia, documentar allowlist temporaria por regra e criar uma meta de queda do `legacy_rule_count`.
- teste faltante: check de regressao que falhe se uma familia ja migrada voltar a depender de `legacy_rule`.

## Testes faltando

- Goldens negativos de ausencia, nao apenas presenca minima.
- Testes de polaridade para aumento/reducao de custo.
- Testes de deduplicacao contrato x legado.
- Testes de trigger composto sem duplicata.
- Testes de modalidade por clausula e sem reminder text.
- Testes de negacao/prevent.
- Testes de choices exclusivos.
- Testes de `effect_lines` attached-only.

## Conclusao parcial

O maior risco da etapa 04 nao e falta de cobertura numerica. O maior risco e cobertura falsa: os fatos existem, a auditoria passa, mas alguns representam polaridade invertida, negacao ignorada, duplicacao ou escopo errado. Esses casos afetam diretamente categorias, filtros e relacoes.
