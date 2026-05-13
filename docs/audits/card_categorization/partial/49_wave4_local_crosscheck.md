# Onda 4 - checagem local independente

Auditoria local somente leitura. Nao rodei builders nem alterei dados processados; usei agregacoes em memoria sobre `cards_normalized.json`, `cards_semantic_facts.jsonl` e `cards_card_relations.jsonl`.

## Resumo numerico

- Cartas normalizadas: `767`
- Fatos semanticos: `5428`
- Relacoes: `9884`
- Cartas sem relacao: `100`
- Cartas broad-only: `22`
- Cartas sem relacao util e com texto rico: `104`
- Relacoes broad detectadas: `3438`, todas por `spell_card_can_be_countered`

Top hubs por grau total:

| carta | grau total | grau non-broad | grau broad |
|---|---:|---:|---:|
| Abandon | 471 | 73 | 398 |
| Flurry of Feathers | 421 | 23 | 398 |
| Defy | 414 | 16 | 398 |
| Hard Bargain | 410 | 12 | 398 |
| Lilting Lullaby | 410 | 12 | 398 |
| Riposte | 410 | 12 | 398 |
| Wind Wall | 410 | 12 | 398 |
| Not So Fast | 400 | 2 | 398 |
| Repulse | 400 | 2 | 398 |
| Karma, Channeler | 173 | 173 | 0 |
| Mistfall | 163 | 163 | 0 |
| Bushwhack | 119 | 101 | 18 |

## Cobertura de termos oficiais

Contagem de cartas cujo texto contem o termo, fatos cuja evidencia contem o termo, e cartas sem fato funcional direto para o termo:

| termo | cartas | fatos por evidencia | fatos funcionais | cartas sem fato funcional |
|---|---:|---:|---:|---:|
| Assault | 29 | 40 | 10 | 19 |
| Tank | 22 | 26 | 4 | 19 |
| Deflect | 35 | 53 | 16 | 20 |
| Ganking | 31 | 41 | 11 | 20 |
| Hidden | 38 | 41 | 3 | 35 |
| Deathknell | 24 | 25 | 1 | 23 |
| Equip | 46 | 99 | 53 | 2 |
| Repeat | 25 | 52 | 28 | 2 |
| Accelerate | 24 | 50 | 25 | 0 |
| Channel | 19 | 20 | 20 | 0 |
| Recycle | 48 | 54 | 54 | 4 |
| Buff | 43 | 78 | 70 | 1 |
| Recall | 12 | 12 | 12 | 0 |
| Add | 27 | 52 | 25 | 3 |
| Score | 14 | 10 | 10 | 5 |
| Conquer | 62 | 80 | 80 | 14 |
| Reaction | 96 | 107 | 10 | 87 |
| Temporary | 23 | 43 | 19 | 13 |
| Shield | 23 | 30 | 6 | 17 |

## Achados

### A1 - Keywords defensivas e de permissao quase nao viram fatos funcionais

- categoria: regra ausente / submodelagem de keyword
- severidade: alta
- confianca: alta
- evidencia: `Hidden` aparece em `38` cartas, mas so `3` fatos funcionais usam essa evidencia; `Deathknell` aparece em `24`, mas so `1`; `Reaction` aparece em `96`, mas so `10`. `Tank`, `Deflect`, `Ganking`, `Assault` e `Shield` tambem ficam majoritariamente como marcadores.
- exemplos: `Pakaa Cub`, `Bird`, `Garen, Rugged`, `Mutated Mouser`, `Kog'Maw, Caustic`, `Fiora, Victorious`.
- impacto: filtros por funcao real nao distinguem protecao, permissao de timing, emboscada/hidden, morte e restricoes de combate.
- teste recomendado: cada keyword oficial deve ter pelo menos um fato funcional normativo ou uma classificacao explicita `keyword_marker_only_allowed`.

### A2 - Texto rico ainda fica sem relacao util

- categoria: lacuna downstream
- severidade: alta
- confianca: alta
- evidencia: `104` cartas com texto rico estao sem relacao ou broad-only. Familias mais frequentes nesses blind spots: `zone_movement=40`, `cost_resource=30`, `replacement_prevent_negation=14`, `attachment_gear=12`, `temporary=5`.
- exemplos: `Keeper's Verdict`, `Turn to Dust`, `Forgotten Monument`, `LeBlanc, Everywhere at Once`, `Ava Achiever`, `Ravenborn Tome`, `Kog'Maw, Caustic`, `The Candlelit Sanctum`.
- impacto: o explorador pode parecer correto numericamente, mas omite cartas com mecanicas reais porque elas nao entram em familia relacional.
- teste recomendado: carta com texto relacional e fato candidato forte nao pode ficar `degree=0` ou `broad_only` sem justificativa allowlisted.

### A3 - Broad domina a visao de counter spells

- categoria: falso positivo de relacao / sinal fraco
- severidade: alta
- confianca: alta
- evidencia: `spell_card_can_be_countered` responde por `3438` relacoes; os top 9 hubs de counter tem `398` relacoes broad cada. `Not So Fast` e `Repulse` tem so `2` relacoes non-broad contra `398` broad.
- impacto: rankings e lanes de relacao ficam dominados por "ser spell" em vez de sinergia acionavel.
- teste recomendado: `spell_card_can_be_countered` nao deve contar para grau high-signal nem aparecer por padrao como `enabled_by/enables`.

### A4 - Blind spots mostram que fatos existem, mas a taxonomia relacional nao os consome

- categoria: integracao entre fatos e relacoes
- severidade: media-alta
- confianca: alta
- evidencia: `Ahri, Inquisitive` tem `modify_stat` e dois `observe_event`, mas grau `0`; `Ravenborn Tome` tem `pay` e `modify_stat`, mas grau `0`; `Carnivorous Snapvine` tem `damage` e `observe_event`, mas grau `0`.
- impacto: melhorar extracao sozinha nao resolve; e preciso mapear familias intermediarias para relacoes de similaridade e sinergia.
- teste recomendado: fixtures com fatos funcionais devem gerar pelo menos relacoes de familia quando houver outra carta semanticamente equivalente.

### A5 - Cartas broad-only com efeitos especificos seguem invisiveis como efeitos

- categoria: regra ausente
- severidade: alta
- confianca: alta
- evidencia: `Keeper's Verdict` tem texto de colocar unidade no topo/fundo do Main Deck, mas so fatos estruturais/keyword; `Turn to Dust` tem `Give a gear [Temporary]`, mas sem familia especifica; `Acceptable Losses` tem `kill gear`, mas aparece broad-only.
- impacto: cartas de remocao, Temporary e Gear ficam classificadas basicamente como spells counteraveis.
- teste recomendado: goldens especificos para `Keeper's Verdict`, `Turn to Dust`, `Acceptable Losses`, `Mystic Reversal`, `Switcheroo`.

## Familias de blind spot

| familia | cartas ricas sem relacao util | exemplos |
|---|---:|---|
| zone_movement | 40 | Mushroom Pouch, Keeper's Verdict, Ava Achiever, Stealthy Pursuer, Baron Pit |
| cost_resource | 30 | Bandle Tree, Raging Firebrand, Dancing Grenade, Ava Achiever, Royal Entourage |
| replacement_prevent_negation | 14 | Baron Pit, Forgotten Monument, Alpha Wildclaw, Brynhir Thundersong, Counter Strike |
| attachment_gear | 12 | Turn to Dust, Acceptable Losses, Heimerdinger, Inventor, Fading Memories, Mageseeker Warden |
| temporary | 5 | Turn to Dust, LeBlanc, Everywhere at Once, Fading Memories, Smoke and Mirrors, Petal Pixie |
| token_create | 3 | Baron Pit, Green Father, Zilean, Time Mage |
| copy | 2 | Reflection, Zilean, Time Mage |
| swap | 2 | Green Father, Switcheroo |
| score_win | 2 | Green Father, Forgotten Monument |
| control | 1 | Mystic Reversal |

## Comando local

Usei um script Python inline somente leitura para agregar:

- termos oficiais em `rules_lines` e `effect_lines`;
- fatos por `play_id`, `predicate` e evidencia;
- grau total, non-broad e broad por carta;
- familias regex de texto rico em cartas `degree=0` ou `broad_only`.
