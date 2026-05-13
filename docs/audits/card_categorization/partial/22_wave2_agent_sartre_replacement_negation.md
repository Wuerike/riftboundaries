# Onda 2 - agente Sartre - replacement, prevent e negacao

## Escopo

Auditoria somente leitura da onda 2 sobre replacement, prevent e negacao.

O agente informou que nao editou arquivos. `git status --short` permaneceu com alteracoes preexistentes: `M goal.md` e `?? docs/`.

## Resumo

O problema central e que `would/instead/prevent/can't/don't/not` ainda nao tem tratamento semantico centralizado. A extracao cobre alguns casos pontuais, mas muitos replacements viram apenas `move/recall/kill`, alguns `can't` viram evento positivo, e outros ficam sem fato semantico algum.

Medidas da checagem:

- `would`: 13 cartas; `instead`: 22 cartas; `prevent`: 2 cartas.
- `can't`: 39 cartas; `don't`: 23; `doesn't`: 37; `not`: 3.
- Fatos `predicate=prevent`: 13.
- Fatos `fact_type=replacement_effect`: apenas 2 (`Brush`, `Zilean, Time Mage`).
- Fatos com evidencia contendo `would`: 4; contendo `instead`: 13.
- 15 fatos positivos carregam evidencia com negacao; nem todos sao bugs, mas incluem inversoes reais.

## Confronto carta a carta

| Carta | Texto esperado | Saida observada |
| --- | --- | --- |
| `Counter Strike` | delayed prevent: proxima vez que unidade receberia dano, prevenir; depois comprar 1 | so `Draw 1`; `prevent it` e `would be dealt damage` ausentes |
| `Guardian Angel` | replacement de morte: matar Guardian Angel em vez da unidade, curar/exaurir/recall | so `recall me` em `effect_lines`; sem `replacement_effect`, sem kill da gear, heal, exhaust |
| `Zhonya's Hourglass` | replacement de morte de unidade friendly | `kill this` positivo + `recall it`; sem evento substituido, heal/exhaust e alvo correto |
| `Highlander` | delayed replacement de morte da unidade escolhida | so `recall it instead` como movimento |
| `Altar of Blood` | replacement opcional com custo `AAA`, heal/exhaust/recall | `activation_cost` com so 2 runas + `recall`; sem replacement/heal/exhaust |
| `Soraka, Wanderer` | replacement condicional para outra unidade menor; tambem `must be assigned combat damage last` | so `recall it`; linha de `must` sem fato |
| `Void Hatchling` | replacement/ordem: antes de revelar, olhar topo, opcional reciclar, entao revelar | so `You may recycle it`; sem look/reveal/replacement |
| `Vilemaw's Lair` | restricao: unidades nao podem mover daqui para base | emite `event_produced/move` positivo |
| `Determined Sentry` | restricao: self nao pode mover para base | emite `event_produced/move` positivo |
| `Rockfall Path` | restricao: unidades nao podem ser jogadas aqui | nenhum fato nao estrutural |
| `Maduli the Gatekeeper` | restricao: nao pode ser readied; ativacao de movimento condicional | linha `can't be readied` sem fato |
| `Tianna Crownguard` | enquanto em battlefield, oponentes nao ganham pontos | so `[Deflect]`; restricao ausente |
| `Brynhir Thundersong` | trigger ao jogar + oponentes nao podem jogar cartas neste turno | so trigger `When you play me`; restricao ausente |

## Achados

### 1. Replacement `would/instead` e modelado como efeitos soltos

- categoria do achado: regra ausente
- severidade: alta
- confianca: alta
- evidencia: `Counter Strike` tem texto em `cards_normalized.json:30863`, mas o unico fato relevante e `Draw 1` em `cards_semantic_facts.jsonl:894`. `Highlander`, `Altar of Blood`, `Guardian Angel`, `Zhonya's Hourglass` e `Soraka, Wanderer` viram basicamente `return_to_hand`.
- regra relacionada: core rules dizem que replacement costuma ser identificado por `would` ou `instead` em `core-rules.md:2666`; a regra `recall_unit` so emite movement em `semantic_extraction_rules.json:1851`.
- impacto provavel no produto final: cartas de protecao/replacement entram como cartas de movimento/remocao simples, perdendo sinergia de morte evitada, dano prevenido e duracao.
- recomendacao: criar builder generico de replacement com `replaced_event`, `replacement_outputs`, `duration`, `conditions`, `polarity=replacement/prevention`.
- teste que deveria existir: goldens para `Counter Strike`, `Highlander`, `Altar of Blood`, `Guardian Angel`, `Zhonya's Hourglass`, `Soraka, Wanderer`.

### 2. `prevent it` nao e extraido como delayed replacement

- categoria do achado: regra ausente
- severidade: alta
- confianca: alta
- evidencia: `Counter Strike` contem `prevent it`, mas so gera draw. A unica regra direta de prevent textual cobre `Prevent all spell and ability damage this turn` em `semantic_extraction_rules.json:1917`.
- regra relacionada: core rules definem prevent como delayed replacement em `core-rules.md:3966` e `core-rules.md:4014`.
- impacto provavel no produto final: prevencao de dano nao aparece em filtros, similaridade ou deck synergy.
- recomendacao: regra para `The next time <target> would be dealt/take damage this turn, prevent it`, com `prevented_event=damage_dealt`, alvo vinculado ao `Choose`.
- teste que deveria existir: `Counter Strike` deve emitir `restriction_or_permission/replacement_effect/prevent` e continuar emitindo `draw`.

### 3. Negacao `can't` pode virar evento positivo

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Determined Sentry` (`I can't move to base`) gera `event_produced/move` em `cards_semantic_facts.jsonl:1122`. `Vilemaw's Lair` (`Units can't move from here to base`) gera `event_produced/move` em `cards_semantic_facts.jsonl:5067`.
- regra relacionada: `move_unit` tem guarda fragil `(?<!can )`, que nao bloqueia `can't move`, em `semantic_extraction_rules.json:1828`.
- impacto provavel no produto final: proibicoes de movimento habilitam relacoes como se a carta produzisse movimento.
- recomendacao: detectar spans negados antes dos builders positivos; `can't/cannot/don't/doesn't/not` devem bloquear efeitos positivos dentro do span e emitir restricao apropriada.
- teste que deveria existir: `Determined Sentry`, `Vilemaw's Lair`, `Minotaur Reckoner`, `Vex, Apathetic` sem fato positivo de `move`.

### 4. Negacoes de play/score/ready ficam sem fato

- categoria do achado: regra ausente
- severidade: alta
- confianca: alta
- evidencia: `Rockfall Path` nao emite restricao para `Units can't be played here`; `Brynhir Thundersong` so emite trigger para `When you play me`; `Tianna Crownguard` so emite `[Deflect]`; `Maduli the Gatekeeper` nao emite nada para `I can't be readied`.
- regra relacionada: existem regras pontuais para `prevent_score_here`, `prevent_ready_enemy_units_gear`, `prevent_chosen_by_enemy_spells`, mas nao um parser generico de restricao.
- impacto provavel no produto final: filtros por restricao/permissao nao encontram cartas importantes; algumas cartas ficam classificadas apenas por identidade/trigger.
- recomendacao: adicionar familia generica `can't <action>` com action normalizada (`play`, `gain_points`, `ready`, `move`) e escopo/alvo.
- teste que deveria existir: presenca de `restriction_or_permission/prevent` para `Rockfall Path`, `Brynhir Thundersong`, `Tianna Crownguard`, `Maduli the Gatekeeper`.

### 5. Custos dentro de replacement podem ser parseados como activated ability

- categoria do achado: parsing/normalizacao
- severidade: media-alta
- confianca: alta
- evidencia: `Altar of Blood` tem custo opcional de replacement com 3 runas, mas gera `activated_ability_cost` com 2 runas em `cards_semantic_facts.jsonl:87`.
- regra relacionada: `activation_split` divide em `":\s+"` e confunde simbolos/custos em `extract_semantic_facts.py:1289`.
- impacto provavel no produto final: custo de replacement vira ativacao independente e ainda subconta recurso.
- recomendacao: separar custo condicional `may pay X to <replacement outputs>` de custo ativado `<cost>: <effect>`.
- teste que deveria existir: `Altar of Blood` deve contar 3 runas e classificar o custo como condicao/custo do replacement, nao activated ability.

## Comandos executados

```powershell
rg --files
git status --short
Get-Content -Raw scripts\04_cards_feature_extraction\extract_semantic_facts.py
Get-Content -Raw scripts\04_cards_feature_extraction\contracts\semantic_extraction_rules.json
Get-Content -Raw scripts\04_cards_feature_extraction\contracts\semantic_quality_policy.json
Get-Content -Raw scripts\04_cards_feature_extraction\contracts\feature_relation_taxonomy.json
rg -n "would|instead|prevent|can't|cannot|don't|doesn't|not|replacement|negat" data\processed\rules\core-rules.md scripts\04_cards_feature_extraction
Select-String -Path data\processed\cards\normalized\cards_normalized.json -Pattern "Counter Strike|Guardian Angel|Zhonya's Hourglass|Highlander|Altar of Blood|Soraka|Void Hatchling|Vilemaw's Lair|Determined Sentry|Rockfall Path|Maduli|Tianna|Brynhir"
```

O agente tambem usou consultas PowerShell com `ConvertFrom-Json` sobre `cards_normalized.json` e `cards_semantic_facts.jsonl` para agrupar os textos e fatos dos cards do escopo.

## Testes recomendados

- Adicionar goldens positivos para os 13 cards confrontados.
- Adicionar testes negativos de ausencia: `can't move` nao pode gerar `event_produced/move`; `can't ready` nao pode gerar `ready`.
- Estender o validador ou criar teste separado para `forbidden_facts`, porque o golden atual valida fatos minimos e nao reprova fatos extras ruins.
- Rodar validacao em saida temporaria, sem sobrescrever artefatos:

```powershell
python scripts/04_cards_feature_extraction/validate_semantic_contracts.py
python scripts/04_cards_feature_extraction/extract_semantic_facts.py --output C:\tmp\wave2_cards_semantic_facts.jsonl --report C:\tmp\wave2_cards_semantic_facts_report.json
python scripts/04_cards_feature_extraction/validate_semantic_golden_examples.py --facts C:\tmp\wave2_cards_semantic_facts.jsonl --report C:\tmp\wave2_cards_semantic_golden_report.json
python scripts/04_cards_feature_extraction/audit_semantic_facts.py --facts C:\tmp\wave2_cards_semantic_facts.jsonl --output C:\tmp\wave2_cards_semantic_audit_report.json --markdown C:\tmp\wave2_cards_semantic_audit_report.md
```
