# Auditoria parcial 01 - visao geral e riscos centrais

## Escopo analisado

Analise nao mutante do pipeline de categorizacao de cartas, com foco inicial em:

- entrada global e artefatos processados;
- contrato entre normalizacao, inventario, extracao semantica, relacoes e dataset web;
- comportamento de `scripts/04_cards_feature_extraction/extract_semantic_facts.py` contra cartas normalizadas concretas;
- relatorios gerados em `data/processed/cards/*` e `data/processed/web/*`.

## Arquivos principais lidos

- `README.md`
- `data/raw/README.md`
- `scripts/01_cards_extraction/README.md`
- `scripts/02_rules_formatter/README.md`
- `scripts/03_cards_formatter/README.md`
- `scripts/03_cards_formatter/normalize_cards.py`
- `scripts/04_cards_feature_extraction/README.md`
- `scripts/04_cards_feature_extraction/extract_semantic_facts.py`
- `scripts/04_cards_feature_extraction/build_card_relations.py`
- `scripts/04_cards_feature_extraction/audit_semantic_facts.py`
- `scripts/04_cards_feature_extraction/validate_semantic_golden_examples.py`
- `scripts/04_cards_feature_extraction/contracts/semantic_extraction_rules.json`
- `scripts/04_cards_feature_extraction/contracts/semantic_relation_rules.json`
- `scripts/04_cards_feature_extraction/contracts/semantic_quality_policy.json`
- `scripts/04_cards_feature_extraction/contracts/feature_relation_taxonomy.json`
- `data/processed/cards/semantic/cards_semantic_audit_report.md`
- `data/processed/cards/relations/cards_card_relations_report.md`
- `data/processed/web/card_explorer_dataset_report.md`
- `data/processed/web/card_explorer_quality_report.md`
- `web/app/app.js`

## Cartas normalizadas consultadas

- `Dancing Grenade`
- `Safety Inspector`
- `Mageseeker Warden`
- `Meditation`
- `Wallop`
- `Draven, Vanquisher`
- `Emperor's Dais`
- `Green Father`
- `Vilemaw`
- `Gold`
- `The Boss`
- `Master Yi, Unstoppable`
- cartas com token pronto: `Bashful Bloom`, `Mirror Image`, `Sprite Burst`, `Sprite Call`, `Sprite Fountain`, `Sprite Mother`, `Sprite Queen`, `Trevor Snoozebottom`

## Regras de categorizacao consultadas

- `semantic_extraction_rules.json`: `deal_damage`, `draw_cards`, `ready_unit`, `kill_each_player_unit`, `kill_opponent_unit`, `kill_generic_unit`, `prevent_ready_enemy_units_gear`, `optional_exhaust_self`, `play_token`.
- `semantic_relation_rules.json`: `spell_card_can_be_countered`, `generic_unit_death_enables_friendly_unit_dies`, `unit_buffed_enables_unit_buffed`, `token_created_to_token_entry_modifier`, similaridade.
- `semantic_quality_policy.json`: `optional_governors`, limiar de relacao ampla, buckets de blind spot.
- `feature_relation_taxonomy.json`: familias de alta prioridade como `stat_modifier`, `damage_effect`, `movement_modifier`, `ready_exhaust_effect`, `token_creation`, `play_permission`, `restriction_or_permission`.

## Entendimento da entrada e saida

Entrada inicial do sistema:

- cartas oficiais em `data/raw/cards.json`, extraidas da galeria oficial via `scripts/01_cards_extraction/fetch_cards.py`;
- regras oficiais em PDF, principalmente `data/raw/core-rules-20260330.pdf`, processadas para `data/processed/rules/core-rules.md/json/jsonl`;
- o README declara que `core-rules.json` ainda nao esta ligado aos fatos das cartas (`README.md:103`, `README.md:157`, `README.md:169`).

Cartas normalizadas:

- `data/processed/cards/normalized/cards_normalized.json`;
- a normalizacao gera `rules_text`, `rules_lines`, `effect_text`, `effect_lines` e preserva `rule_variants` quando impressoes divergem (`scripts/03_cards_formatter/README.md:39`, `scripts/03_cards_formatter/README.md:42`);
- o `play_id` e gerado por assinatura jogavel baseada em nome, dominios, tipos, energia, Might, Power e bonus de Might, nao pelo texto de regras (`scripts/03_cards_formatter/README.md:29`).

Saida esperada:

- fatos em `data/processed/cards/semantic/cards_semantic_facts.jsonl`;
- relacoes em `data/processed/cards/relations/cards_card_relations.jsonl`;
- dataset final em `data/processed/web/card_explorer_dataset.json`;
- frontend estatico em `web/app/` consumindo esse dataset.

## Como a etapa 04 contribui para a categorizacao

`extract_semantic_facts.py` le apenas `rules_lines` e `effect_lines` como fontes textuais (`scripts/04_cards_feature_extraction/extract_semantic_facts.py:26`, `scripts/04_cards_feature_extraction/extract_semantic_facts.py:2172`). Ele gera fatos com `semantic_role`, `fact_type`, `predicate`, `payload`, `source_ref`, `evidence` e `web_uses`. Esses fatos alimentam:

- filtros e detalhes do frontend;
- relacoes `enables`, `enabled_by`, `similar_effect` e `deck_synergy`;
- auditorias de cobertura, isolamento, relacoes amplas e lacunas.

## Comandos executados e resultado

- `git status --short`: mostrou `M goal.md` preexistente; nenhum arquivo de codigo ou dados foi alterado por esta auditoria.
- `rg --files`: mapeou artefatos do pipeline.
- `Get-Content -Raw -Encoding UTF8 README.md` e READMEs das etapas 01-05: confirmou fluxo e contratos.
- `rg -n ...`: usado para localizar linhas relevantes em scripts, contratos e relatorios.
- Consultas PowerShell somente leitura com `ConvertFrom-Json`: contaram e amostraram cartas com `rule_variants`, fatos de cartas especificas e modalidades.

## Achados

### 1. Modalidade opcional e aplicada no nivel da linha inteira

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `line_has_optional_governor` marca uma linha como opcional se contem `you may`, `may pay`, `may exhaust`, etc. (`scripts/04_cards_feature_extraction/extract_semantic_facts.py:217`); `payload_with_line_modality` aplica isso a qualquer fato da linha (`scripts/04_cards_feature_extraction/extract_semantic_facts.py:221`). Em `Dancing Grenade`, o fato `Deal 2 to a unit` sai com `modality: optional`, porque a mesma linha depois diz que o controlador pode jogar o spell de novo. A linha normalizada e: `Deal 2 to a unit. Its controller may play this spell again for :rb_rune_rainbow:. If they do, this deals 1 additional Bonus Damage...`.
- regra relacionada: `deal_damage` em `semantic_extraction_rules.json` / builder `deal_damage`; `optional_governors` em `semantic_quality_policy.json`.
- impacto provavel no produto final: uma acao obrigatoria vira opcional, mudando chaves de similaridade e relacoes; cartas de dano podem ficar menos comparaveis ou agrupadas com efeitos opcionais.
- recomendacao: calcular modalidade por evidencia ou clausula, nao pela linha inteira; preservar condicoes `If they do`/`Otherwise` explicitamente.
- teste que deveria existir: golden/negativo para `Dancing Grenade` exigindo que `Deal 2 to a unit` seja `required` enquanto o replay e o bonus condicionado sejam separados.

### 2. Texto negativo gera fatos positivos de acao

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `kill_generic_unit` casa `kill a unit` sem guarda contra negacao (`scripts/04_cards_feature_extraction/contracts/semantic_extraction_rules.json:1046`). `Safety Inspector` gera tres fatos de kill na mesma linha: `each player must kill one of their units`, `kill one of their units` e `kill a unit`; o ultimo vem de `If you paid my additional cost, you don't kill a unit this way`, que deveria ser somente restricao/prevent. O proprio golden de `Safety Inspector` exige o fato `must` e a restricao, mas nao rejeita o fato extra incorreto (`scripts/04_cards_feature_extraction/contracts/semantic_golden_examples.json:723`, `scripts/04_cards_feature_extraction/contracts/semantic_golden_examples.json:803`, `scripts/04_cards_feature_extraction/contracts/semantic_golden_examples.json:825`).
- regra relacionada: `kill_each_player_unit`, `kill_opponent_unit`, `kill_generic_unit`, `restriction_additional_cost_prevents_self_kill`.
- impacto provavel no produto final: fatos falsos de `unit_dies` podem criar enables/similaridade indevidos para cartas que nao produzem aquele kill em todos os cenarios.
- recomendacao: adicionar guardas de negacao e sobreposicao; tratar `don't kill a unit` como restricao, nunca como `event_produced`.
- teste que deveria existir: golden negativo para `Safety Inspector` garantindo ausencia de fato `kill_generic_unit` com evidencia `kill a unit` dentro de `don't kill`.

### 3. Restricao "can't ready" tambem gera um fato positivo `ready`

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Mageseeker Warden` tem a linha `spells and abilities can't ready enemy units and gear`. O extractor cria corretamente uma restricao `prevent`, mas tambem cria `state_or_modifier / ready / unit_ready` com evidencia `ready enemy units and gear`. O report web mostra essa combinacao no backtrace (`data/processed/web/card_explorer_quality_report.md:232`, `data/processed/web/card_explorer_quality_report.md:241`).
- regra relacionada: `prevent_ready_enemy_units_gear` e `ready_unit`.
- impacto provavel no produto final: uma carta que impede ready pode ser categorizada como carta que ready unidades, contaminando filtros, similaridade e futuras relacoes.
- recomendacao: `ready_unit` deve ignorar contextos de negacao/prevent ou exigir inicio de acao/imperativo sem `can't/cannot/don't`.
- teste que deveria existir: exemplo dourado para `Mageseeker Warden` que espera `prevent` e rejeita `unit_ready`.

### 4. "Play a ready token" e interpretado como acao de ready

- categoria do achado: categorizacao incorreta
- severidade: media
- confianca: alta
- evidencia: 9 fatos `ready` foram encontrados em textos do tipo `Play a ready ... token`. Exemplos: `Sprite Burst` e `Sprite Call` geram `outputs: unit_ready` em vez de apenas estado de entrada/token creation. O inventario mostra a linguagem real `play a ready {number} :rb_might: sprite unit token with [temporary]` como familia `ready_exhaust_effect, token_creation` (`data/processed/cards/inventory/cards_taxonomy_alignment.md:347`).
- regra relacionada: `ready_unit`, `play_token`, familia `token_creation`.
- impacto provavel no produto final: cartas que criam tokens prontos podem aparecer como alternativas de cartas que ready unidades existentes.
- recomendacao: distinguir adjetivo de estado (`ready token`) de acao (`Ready a unit`); enriquecer `token_creation.object.state` e evitar `unit_ready` separado para o adjetivo.
- teste que deveria existir: golden para `Sprite Burst` exigindo token state `ready` e ausencia de `predicate: ready`.

### 5. `rule_variants` sao preservadas, mas nao entram na extracao

- categoria do achado: perda de informacao
- severidade: media
- confianca: alta
- evidencia: 44 cartas normalizadas possuem `rule_variants`. O normalizador preserva variantes (`scripts/03_cards_formatter/normalize_cards.py:260`, `scripts/03_cards_formatter/normalize_cards.py:370`), mas `extract_semantic_facts.py` processa apenas `rules_lines` e `effect_lines` (`scripts/04_cards_feature_extraction/extract_semantic_facts.py:26`, `scripts/04_cards_feature_extraction/extract_semantic_facts.py:2172`). Exemplos com variantes: `Gold`, `Green Father`, `Vilemaw`, `The Boss`, `Master Yi, Unstoppable`.
- regra relacionada: contrato de entrada de `cards_normalized.json`; regras de extracao que dependem de texto de carta.
- impacto provavel no produto final: diferencas entre impressoes podem ficar invisiveis para fatos e relacoes; se a variante mais rica nao for semanticamente correta, a categorizacao fica enviesada.
- recomendacao: auditar `rule_variants` como fonte de divergencia, com sinal explicito no report; decidir se variantes devem produzir fatos alternativos, warnings ou revisao manual.
- teste que deveria existir: auditoria que falhe ou avise quando uma carta com `rule_variants` tem variantes semanticamente diferentes nao modeladas.

### 6. Relacoes broad chegam ao frontend sem filtro padrao

- categoria do achado: integracao entre etapas
- severidade: media
- confianca: alta
- evidencia: o README diz que `spell_card_can_be_countered` deve ser broad e filtrado/rebaixado por padrao (`README.md:167`). A auditoria web mostra `3438` relacoes broad, `34.78%` do grafo, e `22` cartas apenas com relacoes broad (`data/processed/web/card_explorer_quality_report.md:11`, `data/processed/web/card_explorer_quality_report.md:13`, `data/processed/web/card_explorer_quality_report.md:15`). O frontend agrupa `enabled_by`, `enables` e `similar_effect` sem checar `relation.match.broad` (`web/app/app.js:2`, `web/app/app.js:90`, `web/app/app.js:93`, `web/app/app.js:99`).
- regra relacionada: `spell_card_can_be_countered` em `semantic_relation_rules.json`; `semantic_quality_policy.json` broad relation policy.
- impacto provavel no produto final: cartas de spell/counter dominam a experiencia e mascaram relacoes de alto sinal.
- recomendacao: filtrar broad por padrao, ou ordenar depois de high-signal com controle visual claro.
- teste que deveria existir: teste de dataset/frontend garantindo que relacoes `match.broad == true` nao aparecem no conjunto padrao ou ficam abaixo das high-signal.

### 7. Documentacao de estado atual esta defasada em relacao aos artefatos gerados

- categoria do achado: manutencao
- severidade: baixa
- confianca: alta
- evidencia: `README.md` declara `5382` fatos, `9047` relacoes, `144` cartas sem relacao e `45` broad-only (`README.md:165`, `README.md:166`). Os reports gerados indicam `5428` fatos, `9884` relacoes, `100` cartas sem relacao e `22` broad-only (`data/processed/web/card_explorer_dataset_report.md:8`, `data/processed/web/card_explorer_dataset_report.md:9`, `data/processed/web/card_explorer_dataset_report.md:35`, `data/processed/web/card_explorer_dataset_report.md:36`).
- regra relacionada: contratos operacionais do pipeline e criterio de confianca de reports.
- impacto provavel no produto final: revisores podem priorizar problemas ja mudados ou deixar de notar regressao real.
- recomendacao: mover contagens de estado atual para reports gerados ou datar explicitamente a rodada.
- teste que deveria existir: check simples que compara contagens documentadas com reports, ou remove contagens estaticas do README.

## Testes faltando

- Testes negativos de ausencia de fatos extras, nao apenas `minimum_expected_facts`.
- Testes de modalidade por clausula/evidencia.
- Testes de negacao para `can't`, `cannot`, `don't`, `doesn't`.
- Testes de adjetivo de estado em token (`play a ready token`) contra acao `Ready`.
- Testes de contrato entre `rule_variants` e extracao.
- Testes de frontend/dataset para relacoes broad filtradas/rebaixadas por padrao.

## Oportunidades de melhoria

- Separar parsing por clausula com escopo de modalidade, condicao e negacao.
- Adicionar uma camada de "negative guards" reutilizavel para builders de acao.
- Transformar mais regras hard-coded de Python em contratos JSON ou marcar explicitamente excecoes programaticas.
- Incluir `rule_variants` nos reports de cobertura.
- Criar golden examples que validem tanto presenca quanto ausencia.

## Duvidas e hipoteses ainda nao confirmadas

- Se `rule_variants` representam erratas/prints antigos ou textos oficialmente equivalentes.
- Se o frontend deve mostrar `deck_synergy` agora ou apenas depois de uma revisao de UX.
- Se os fatos de `ready token` foram intencionais para viabilizar `token_created_to_token_entry_modifier` ou se deveriam migrar para `entry_state`.
