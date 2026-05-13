# Onda 2 - checagem local cruzada

## Escopo analisado

Checagem local, nao mutante, focada em dois riscos ja recorrentes: parsing de custo/ativacao e replacement/prevention. A checagem foi feita enquanto os agentes da onda 2 analisavam escopos estreitos.

## Arquivos principais lidos

- `data/processed/cards/normalized/cards_normalized.json`
- `data/processed/cards/semantic/cards_semantic_facts.jsonl`
- `scripts/04_cards_feature_extraction/contracts/semantic_extraction_rules.json`

## Cartas consultadas

- `Altar of Blood`
- `Blood Rose`
- `Draven, Vanquisher`
- `Emperor's Dais`
- `Forge of the Fluft`
- `Icevale Archer`
- `Immortal Phoenix`
- `Ivern, Nurturer`
- `Karma, Channeler`
- `Keeper of the Hammer`
- `Lux, Illuminated`
- `Power Nexus`
- `Rell, Magnetic`
- `Sivir, Mercenary`
- `Spectral Matron`
- `Valley of Idols`
- `Vex, Cheerless`
- `Voidreaver`
- `Yeti Brawler`
- `Yordle Explorer`
- `Counter Strike`
- `Guardian Angel`
- `Zhonya's Hourglass`
- `Highlander`
- `Unlicensed Armory`
- `Soraka, Wanderer`
- `Void Hatchling`
- `Zilean, Time Mage`

## Regras de categorizacao consultadas

- `activation_cost`
- `generic_cost_reduction`
- `recall_unit`
- `kill_self`
- `token_play_copy_replacement`
- regras de `prevent`
- familias `replacement_effect`, `cost_modifier`, `cost_or_requirement`

## Comandos executados e resultado

- PowerShell sobre `cards_semantic_facts.jsonl` agrupando `activation_cost`.
- PowerShell sobre `cards_normalized.json` buscando cartas com `would`, `instead` ou `prevent`.
- PowerShell sobre `cards_semantic_facts.jsonl` listando fatos de linhas com `would`, `instead` ou `prevent`.
- PowerShell agrupando `extractor.rule_id` para contexto de volume.

Resultados:

- `activation_cost_count`: 169.
- `activation_cost` cuja linha comeca com `When`: 13.
- `activation_cost` cuja linha comeca com `If`: 2.
- `activation_cost` cuja linha comeca com `While`: 2.
- `activation_cost` contendo `Spend N XP`: 4.
- cartas com `would`/`instead`/`prevent`: 26.
- fatos aparentemente de replacement/prevented: 11.
- fatos com `predicate: prevent`: 13.

## Achados

### 1. `activation_cost` captura linhas que parecem trigger/condicao, nao habilidade ativada

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: 17 fatos `activation_cost` vem de linhas que comecam com `When`, `If` ou `While`. Exemplos:
  - `Karma, Channeler`: `When you recycle one or more cards...` vira custo ativado.
  - `Lux, Illuminated`: `When you play a spell that costs :rb_energy_5: or more...` vira custo ativado.
  - `Sivir, Mercenary`: `If you've spent at least ... this turn...` vira custo ativado.
  - `Vex, Cheerless`: `While I'm in combat, friendly spells cost ...` vira custo ativado.
- regra relacionada: `activation_cost`.
- impacto provavel no produto final: filtros e relacoes de custo passam a incluir triggers condicionais, thresholds e modificadores estaticos.
- recomendacao: restringir `activation_cost` a linhas com forma de custo ativado real antes do delimitador, evitando linhas iniciadas por `When`, `If` e `While` salvo excecao explicita.
- teste que deveria existir: goldens negativos para `Karma, Channeler`, `Lux, Illuminated`, `Sivir, Mercenary` e `Vex, Cheerless`.

### 2. Custos `Spend N XP` aparecem em linhas de activation, mas payload perde XP

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: 4 fatos `activation_cost` tem linha com `Spend N XP`: `Blood Rose`, `Keeper of the Hammer`, `Voidreaver` em duas habilidades. Em amostra anterior, o payload capturava `exhaust`, mas nao o custo XP.
- regra relacionada: `activation_cost`; parser de custos nao simbolicos.
- impacto provavel no produto final: cartas que consomem XP nao entram corretamente em filtros/sinergias de custo.
- recomendacao: adicionar parsing estruturado para `Spend N XP` como custo, com `resource: xp`.
- teste que deveria existir: `Blood Rose`, `Keeper of the Hammer`, `Voidreaver`.

### 3. Replacement/prevention aparece em 26 cartas, mas poucos fatos carregam semantica de replacement

- categoria do achado: regra ausente
- severidade: alta
- confianca: alta
- evidencia: 26 cartas contem `would`, `instead` ou `prevent`, mas so 11 fatos parecem usar campos/regras de replacement/prevented e 13 fatos tem `predicate: prevent`. Varias linhas com `instead` geram apenas efeitos finais, como `kill`/`recall`/`return_to_hand`, sem o evento substituido.
- regra relacionada: `replacement_effect`; regras de `prevent`.
- impacto provavel no produto final: efeitos de protecao ou substituicao sao categorizados como eventos normais, perdendo a relacao entre evento prevenido e output substituto.
- recomendacao: modelar `prevented_event`, `replacement_outputs`, `condition`, `duration` e `optional_cost` no mesmo grupo de clausula.
- teste que deveria existir: goldens para `Counter Strike`, `Guardian Angel`, `Zhonya's Hourglass`, `Highlander`, `Altar of Blood`, `Soraka, Wanderer`, `Void Hatchling`.

### 4. `would/instead/prevent` mistura custos opcionais, substituicao e output em uma linha

- categoria do achado: arquitetura
- severidade: media
- confianca: alta
- evidencia: `Altar of Blood` contem `would die`, controlador pode pagar tres runas, e outputs `heal`, `exhaust`, `recall` em vez do death. O fato atual inclui `activation_cost` e `recall_unit`, mas nao uma unidade semantica que vincule custo opcional, evento prevenido e replacement.
- regra relacionada: `clause_group_id`; replacement/prevention.
- impacto provavel no produto final: downstream nao consegue diferenciar recall normal de recall como salvamento/substituicao.
- recomendacao: criar objeto de fato composto ou links entre fatos por `condition_id`/`replacement_id`.
- teste que deveria existir: `Altar of Blood` com estrutura que conecta custo opcional a replacement de morte.

## Testes faltando

- Negative tests para `activation_cost` em linhas `When/If/While`.
- Parsing positivo de `Spend N XP`.
- Replacement/prevention com evento prevenido e outputs substitutos.
- Diferenciar `return_to_hand` normal de `return_to_hand` como replacement.
- Checagem de payload de custo por contagem exata de simbolos/recursos.

## Oportunidades de melhoria

- Separar custos em `activation_cost`, `optional_payment`, `threshold_condition`, `static_cost_modifier` e `additional_cost`.
- Introduzir `replacement_id` para vincular evento prevenido, custo, condicao e outputs.
- Adicionar metrica de auditoria: linhas com `would/instead/prevent` sem `replacement_effect` ou `prevented_event`.
