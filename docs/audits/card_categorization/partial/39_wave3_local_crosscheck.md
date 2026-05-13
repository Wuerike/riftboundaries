# Onda 3 - checagem local cruzada

## Escopo analisado

Checagem local, nao mutante, focada em cartas sem relacao, broad-only e hubs de alto grau no dataset web.

## Arquivos principais lidos

- `data/processed/web/card_explorer_dataset.json`
- `data/processed/cards/semantic/cards_semantic_facts.jsonl`

## Comandos executados e resultado

- PowerShell com `ConvertFrom-Json` sobre `card_explorer_dataset.json`.
- PowerShell com `ConvertFrom-Json` sobre `cards_semantic_facts.jsonl`.

Resultados:

- cartas no dataset: 767.
- cartas sem relacoes: 100.
- cartas broad-only: 22.
- top hubs por grau total: `Abandon` 471, `Flurry of Feathers` 421, `Defy` 414, `Wind Wall` 410, `Riposte` 410, `Lilting Lullaby` 410, `Hard Bargain` 410, `Not So Fast` 400, `Repulse` 400.
- essas cartas top hubs sao dominadas por broad de counter: por exemplo, `Abandon` tem 398 broad de 471; `Wind Wall` tem 398 broad de 410.

## Cartas consultadas

Sem relacao, amostra:

- `Ahri, Inquisitive`
- `Alpha Wildclaw`
- `Ancient Henge`
- `Ava Achiever`
- `Bandle Tree`
- `Baron Pit`
- `Bird`
- `Body Rune`
- `Brynhir Thundersong`
- `Bubble Bot`
- `Calm Rune`
- `Carnivorous Snapvine`
- `Chakram Dancer`
- `Chaos Rune`
- `Daring Poro`
- `Draven, Showboat`
- `Elder Dragon`
- `Fiora, Peerless`
- `Forbidding Waste`
- `Forge of the Fluft`

Broad-only, amostra:

- `Right of Conquest`
- `Show of Strength`
- `Relentless Pursuit`
- `Premonition`
- `Progress Day`
- `Smoke and Mirrors`
- `Unyielding Spirit`
- `Temptation`
- `Strike Down`
- `Switcheroo`
- `Convergent Mutation`
- `Counter Strike`
- `Block`
- `Acceptable Losses`
- `Angle Shot`
- `Dancing Grenade`
- `Lotus Trap`
- `Mystic Reversal`
- `Keeper's Verdict`
- `Downstage Dramatics`
- `Fading Memories`

## Regras de categorizacao consultadas

- familias de relacao consumidas pelo dataset: `enabled_by`, `enables`, `similar_effect`, `deck_synergy`;
- fatos por `extractor.rule_id` das cartas sem relacao;
- broad relation `spell_card_can_be_countered`.

## Achados

### 1. Cartas sem relacao frequentemente tem fatos uteis, mas sem familia relacional consumidora

- categoria do achado: regra ausente
- severidade: alta
- confianca: alta
- evidencia: `Ahri, Inquisitive` tem 8 fatos, incluindo `trigger_self_attacks_or_defends` e `give_might`; `Alpha Wildclaw` tem `prevent_chosen_by_enemy_spells`; `Ancient Henge` tem `add_resource` e `activation_cost`; `Baron Pit` tem `units_move_here_from_anywhere_permission`; `Elder Dragon` tem damage/triggers; mesmo assim todas tem grau 0.
- regra relacionada: `semantic_relation_rules.json`, familias de relation builder.
- impacto provavel no produto final: cartas com categorias semanticas reais ficam invisiveis em navegacao por relacoes.
- recomendacao: criar relacoes para modificadores condicionais, permissoes/restricoes, recursos ativados e battlefield permissions, ou reportar explicitamente como familias ainda nao exploraveis.
- teste que deveria existir: cartas com fatos de alta prioridade nao podem ficar grau 0 sem justificativa de allowlist.

### 2. Runas basicas ficam sem relacao por ausencia de fatos funcionais derivados das regras

- categoria do achado: divergencia entre regras, cartas normalizadas e implementacao
- severidade: media
- confianca: alta
- evidencia: `Body Rune`, `Calm Rune`, `Chaos Rune` aparecem sem relacao e tem so fatos estruturais de tipo/dominio. Isso confirma o risco de que habilidades basicas de runas oficiais nao entram como fatos ou sinergias.
- regra relacionada: regras oficiais de Basic Runes; categorias de recurso.
- impacto provavel no produto final: runas basicas nao aparecem como recursos jogaveis nem conectam com custos.
- recomendacao: decidir se runas basicas devem receber fatos derivados de regra oficial ou se devem ser explicitamente excluidas do explorer.
- teste que deveria existir: fixture para cada rune basica: ou tem fatos de Add/Recycle derivados, ou esta em allowlist de exclusao.

### 3. Broad-only transforma spells com efeitos concretos em apenas counterability

- categoria do achado: integracao entre etapas
- severidade: alta
- confianca: alta
- evidencia: `Counter Strike` tem `draw` e deveria ter prevent; `Dancing Grenade` tem damage; `Block` tem keyword grant; `Angle Shot` tem attach/detach/draw; `Switcheroo` deveria ter stat swap. Mesmo assim aparecem broad-only com 18 relacoes, todas por broad.
- regra relacionada: `spell_card_can_be_countered`; familias de similaridade/enables faltantes ou contaminadas.
- impacto provavel no produto final: a UI sugere que a unica relacao dessas cartas e serem counteraveis, ocultando sua funcao real.
- recomendacao: broad-only deve ser tratado como diagnostico de lacuna, nao como estado aceitavel; high-signal facts dessas cartas devem ter relacoes especificas ou ser reportados como cobertura faltante.
- teste que deveria existir: `Counter Strike`, `Dancing Grenade`, `Block`, `Angle Shot` nao devem ser broad-only.

### 4. Hubs de counter dominam o topo e mascaram relacoes high-signal

- categoria do achado: integracao entre etapas
- severidade: alta
- confianca: alta
- evidencia: `Abandon`, `Flurry of Feathers`, `Defy`, `Wind Wall`, `Riposte`, `Lilting Lullaby`, `Hard Bargain`, `Not So Fast` e `Repulse` tem 398 broad cada ou quase isso; high-signal varia de 2 a 73.
- regra relacionada: `spell_card_can_be_countered`.
- impacto provavel no produto final: ordenacao e contadores de relacao sao dominados por uma relacao generica.
- recomendacao: separar broad do grau total default; ordenar por high-signal primeiro e exibir broad como diagnostico/toggle.
- teste que deveria existir: top hubs por grau default nao deve ser dominado por `spell_card_can_be_countered`.

## Testes faltando

- Fatos high-priority sem relacao devem gerar warning.
- Broad-only com fatos high-signal deve gerar warning.
- Runas basicas devem ter contrato explicito.
- Top hub report deve separar broad e high-signal.
