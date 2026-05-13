# Onda 1 - agente Meitner - contratos entre etapas 01-05 e produto final

## Escopo

Auditoria nao mutante sobre contratos de entrada/saida entre etapas 01-05 e produto final.

O agente informou que nao editou arquivos. `git status --short` ja estava sujo antes da auditoria: `M goal.md` e `?? docs/`.

## Achados

### 1. Reminder text esta virando fato semantico executavel

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `normalize_cards.py` achata HTML em texto puro sem preservar/filtrar italico/parentheses de reminder text (`normalize_cards.py:120`). Pelas regras, reminder text nao tem efeito na funcao de jogo (`core-rules.md:678`, `core-rules.md:681`, `core-rules.md:684`). Exemplo concreto: `The Boss` tem `spend its buff to heal...` em `cards_normalized.json:23251`, mas gerou `unit_buffed` com evidencia `buff to heal it` em `cards_semantic_facts.jsonl:4612`. A regra `buff_unit` e ampla demais (`semantic_extraction_rules.json:1603`).
- regra relacionada: regras oficiais de reminder text; `buff_unit`.
- impacto provavel no produto final: texto explicativo ou parte de expressao idiomatica pode virar evento real de buff, gerando filtros e relacoes falsas.
- recomendacao: criar teste de fronteira `normalized -> semantic_facts` que falhe se evidencia de fato vier de reminder text; segmentar texto funcional e lembrete.
- teste que deveria existir: golden negativo para `The Boss` proibindo `unit_buffed` a partir de `buff to heal it`.

### 2. `activation_cost` classifica linhas de trigger como custo ativado

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: a regra declarativa roda em qualquer linha (`pattern: ".+"`) em `semantic_extraction_rules.json:341`, e `activation_split()` divide pelo ultimo `": "` da linha, inclusive simbolos como `:rb_might:` em texto comum (`extract_semantic_facts.py:1289`). Exemplos: `Karma, Channeler` gera custo ativado a partir de `When you recycle...` (`cards_semantic_facts.jsonl:2442`); `Lux, Illuminated` gera custo `energy 5` e `reduce_cost` a partir de `spell that costs 5 or more` (`cards_semantic_facts.jsonl:2780`; `semantic_extraction_rules.json:1873`). O agente encontrou 13 fatos de custo cuja evidencia comeca com `When`.
- regra relacionada: `activation_cost`; `generic_cost_reduction`.
- impacto provavel no produto final: triggers condicionais sao classificados como custos ativados, contaminando filtros de custo e sinergias de recurso.
- recomendacao: contrato para `activation_cost`: so aceitar custo antes de `:` quando a linha comecar com custo real ou keyword permissiva seguida de custo, nao quando comecar com `When/If/While`.
- teste que deveria existir: goldens negativos para `Karma, Channeler` e `Lux, Illuminated`.

### 3. Custos ativados com XP perdem componente XP

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `parse_non_symbol_costs()` reconhece simbolos, kill, discard e recycle, mas nao `Spend N XP` (`extract_semantic_facts.py:1274`). Exemplo: `Blood Rose` tem `Spend 3 XP, :rb_exhaust:: Ready a unit.` (`cards_normalized.json:7748`), mas o fato de custo contem so `exhaust`, sem XP (`cards_semantic_facts.jsonl:520`). O mesmo padrao aparece em `Voidreaver` e `Keeper of the Hammer`.
- regra relacionada: `activation_cost`; custos de XP.
- impacto provavel no produto final: custos por XP ficam subcontados, afetando filtros e sinergias de recurso/custo.
- recomendacao: validar `Spend N XP` em custos ativados e adicionais como `{"resource":"xp","amount":N}`.
- teste que deveria existir: goldens para `Blood Rose`, `Voidreaver` e `Keeper of the Hammer` exigindo custo XP.

### 4. `rule_variants` preserva divergencias, mas a extracao ignora todas exceto a richest printing

- categoria do achado: parsing/normalizacao
- severidade: media
- confianca: alta
- evidencia: a assinatura jogavel exclui texto de regras (`normalize_cards.py:298`); o agrupamento escolhe o texto mais longo como `rules_lines` (`normalize_cards.py:252`, `normalize_cards.py:320`); o extrator so percorre `rules_lines`/`effect_lines` do card agrupado (`extract_semantic_facts.py:2170`). Ha 44 cartas com `rule_variants`. Em cartas como `The Boss`, `Void Burrower` e `Karma, Channeler`, isso pode mudar triggers, custos e outputs sem criar novo `play_id`.
- regra relacionada: contrato de normalizacao e identidade jogavel.
- impacto provavel no produto final: fatos representam um texto escolhido por heuristica, nao necessariamente a variante funcional correta.
- recomendacao: definir contrato explicito para `rule_variants`: extrair fatos por variante ou escolher variante canonica por set/data/errata, nunca por texto mais longo sem teste.
- teste que deveria existir: teste para cartas com variantes funcionais exigindo decisao explicita de oracle.

### 5. Regras oficiais de runas ainda nao entram no contrato semantico

- categoria do achado: divergencia entre regras, cartas normalizadas e implementacao
- severidade: media
- confianca: media
- evidencia: as regras dizem que Basic Runes sempre tem duas habilidades, incluindo Add e Recycle (`core-rules.md:1146`, `core-rules.md:1152`). Mas `Body Rune` esta sem `rules_lines` (`cards_normalized.json:29588`) e so gera fatos estruturais de tipo/dominio (`cards_semantic_facts.jsonl:551`). Isso deixa runas fora de sinergias de recurso.
- regra relacionada: regras oficiais de Basic Runes.
- impacto provavel no produto final: runas basicas podem ficar invisiveis para categorias de recurso e sinergia.
- recomendacao: decidir se habilidades basicas de rune devem ser materializadas por fatos estruturais derivados das regras oficiais.
- teste que deveria existir: golden/fixture para `Body Rune` e demais runas basicas com Add/Recycle esperados ou justificativa explicita de exclusao.

### 6. O dataset final inclui `deck_synergy`, mas o frontend nao renderiza essa categoria

- categoria do achado: integracao entre etapas
- severidade: media
- confianca: alta
- evidencia: o builder do dataset inclui quatro tipos, inclusive `deck_synergy` (`build_card_explorer_dataset.py:23`, `build_card_explorer_dataset.py:290`). O app so conhece `enabled_by`, `enables` e `similar_effect` (`app.js:1`) e so itera relacoes outgoing desses tipos (`app.js:90`). Resultado atual: 1056 relacoes `deck_synergy` existem no dataset, mas nao aparecem no produto final.
- regra relacionada: contrato do dataset web e frontend.
- impacto provavel no produto final: uma categoria gerada e validada nao chega ao usuario.
- recomendacao: adicionar teste do dataset final contra o frontend: todo `relation_type` presente no dataset deve ser renderizado, filtrado ou explicitamente marcado como oculto por contrato.
- teste que deveria existir: snapshot de `relation_type` do dataset contra `RELATION_TYPES` do frontend.

## Observacoes de contrato

- Os artefatos atuais tem 767 cartas, 5428 fatos e 9884 relacoes.
- Isso diverge dos READMEs, que ainda citam 5382 fatos e 9047 relacoes (`README.md:165`, `scripts/05_web_dataset/README.md:47`).
- Os relatorios processados concordam com os arquivos atuais.
- `python scripts\04_cards_feature_extraction\validate_semantic_contracts.py` passou, mas ele valida contratos JSON e vazamento de termos; nao pega falsos positivos em fatos gerados.

## Recomendacoes de testes/contratos

- Criar teste de fronteira `normalized -> semantic_facts` que falhe se evidencia de fato vier de reminder text, especialmente `buff if...`, `buff to heal`, textos entre parenteses e exemplos com keywords.
- Criar contrato para `activation_cost`: so aceitar custo antes de `:` quando a linha comecar com custo real ou keyword permissiva seguida de custo, nao quando comecar com `When/If/While`.
- Adicionar golden examples negativos para `The Boss`, `Karma, Channeler`, `Lux, Illuminated`, `Blood Rose`, `Voidreaver` e `Keeper of the Hammer`.
- Validar `Spend N XP` em custos ativados e adicionais como `{"resource":"xp","amount":N}`.
- Definir contrato explicito para `rule_variants`: extrair fatos por variante, ou escolher variante canonica por set/data/errata, nunca por texto mais longo sem teste.
- Adicionar teste do dataset final contra o frontend: todo `relation_type` presente no dataset deve ser renderizado, filtrado ou explicitamente marcado como oculto por contrato.

## Comandos executados

- `Get-ChildItem -Name`, `rg --files`, `git status --short`
- `Get-Content`/`rg -n` nos READMEs obrigatorios, `core-rules.md`, scripts 03-05, contratos semanticos e `web/app/app.js`
- Scripts Python somente leitura para contar cartas/fatos/relacoes, validar referencias e amostrar cartas concretas
- `Select-String` para linhas de `cards_normalized.json`, `cards_semantic_facts.jsonl` e dataset web
- `python scripts\04_cards_feature_extraction\validate_semantic_contracts.py`
