# Onda 4 - suite independente de invariantes

Auditoria feita somente leitura. O agente nao editou arquivos. O pipeline atual ja valida contratos, goldens minimos, auditoria semantica, relacoes e dataset web, mas falta uma camada de testes independentes que congele invariantes de regressao por bug real, especialmente onde o corpus ainda mostra lacunas: relacoes ausentes para modificadores/permissao/restricao, broad-only, payloads frageis e dataset frontend.

Arquivos lidos: `semantic_facts_schema.json`, `semantic_quality_policy.json`, `semantic_extraction_rules.json`, `semantic_relation_rules.json`, scripts em `scripts/04_cards_feature_extraction`, reports e exemplos em `data/processed/cards/semantic`, `data/processed/cards/relations`, `data/processed/web`.

## Testes propostos

### 1. Golden de papel semantico: trigger nao e efeito

Fixture:

- `Harnessed Dragon`, `play:harnessed-dragon:c4bb02f1`
- linha: `When you play me, kill an enemy unit.`

Expected facts:

- `trigger_observed/event_trigger/observe_event` com `payload.event.id = self_played`.
- `event_produced/removal/kill` com `payload.event.id = enemy_unit_dies`.
- Ambos com mesmo `clause_group_id`, mas facts separados.
- `kill` nunca pode aparecer como `trigger_observed`.

Bug que pega: regressao de categorizacao trigger/effect. Severidade: alta.

Onde rodar: apos `extract_semantic_facts.py`, como golden independente de facts; tambem em `audit_semantic_facts.py` como invariant estrutural.

### 2. Golden de modalidade opcional com custo e payoffs

Fixture:

- `Altar of Memories`, `play:altar-of-memories:2de88f83`
- linha: `When a friendly unit dies, you may exhaust me to draw 1, then put a card from your hand on the top or bottom of your Main Deck.`

Expected facts:

- Trigger `friendly_unit_dies`.
- Cost `activated_ability_cost/exhaust`, `payload.modality = optional`.
- Payoff `draw` com `card_drawn`, amount `1 card`.
- Payoff `move` com `deck_card_put_top_or_bottom`.
- Todos os fatos textuais apontam para `rules_lines:0`.

Bug que pega: perda de `you may` em custo/payoff e colapso de multiplos efeitos em um unico fact. Severidade: alta.

Onde rodar: golden facts e auditoria de `optional_governors` em `semantic_quality_policy.json`.

### 3. Schema payload completo para activation cost

Fixture:

- `Poro Snax`, `play:poro-snax:089d7772`
- linha: `:rb_energy_1::rb_rune_calm:, :rb_exhaust:, Kill this: Draw 1.`

Expected facts:

- Um `cost_or_requirement` com custos separados:
  - energy `1`;
  - rune `calm`;
  - exhaust self;
  - kill self ou event/cost explicito conforme contrato.
- Payoff `draw 1`.
- `source_ref.source_field = rules_lines`, `line_index = 1`, `evidence` substring exata.
- Nenhum custo deve ficar apenas em `evidence` sem payload estruturado.

Bug que pega: payload sem `costs` e resource cost invisivel para relacoes `resource_synergy`. Severidade: alta.

Onde rodar: pos-extracao, antes de relacoes. Novo teste de schema payload em `tests/semantic/test_fact_payload_invariants.py` ou equivalente.

### 4. Source ref e evidence nao negociaveis

Fixtures:

- amostra estratificada de todos os facts textuais do corpus;
- `Spinning Axe`, `play:spinning-axe:54c823a0`;
- `Ahri, Inquisitive`, `play:ahri-inquisitive:d6396fae`;
- `Keeper's Verdict`, `play:keeper-s-verdict:9e4e390e`.

Expected:

- Para todo fact nao-`official_field`:
  - `source_ref.source_field` em `rules_lines|effect_lines`;
  - `line_index` inteiro;
  - `line_text` igual ao texto normalizado da carta;
  - `evidence` contida em `line_text`;
  - `unit_text`, `normalized_unit`, `parameterized_unit` preenchidos ou explicitamente `null` so quando inventario nao cobre.
- Para `official_field`, `line_index = null`.

Bug que pega: facts orfaos, evidence inventada, quebra do frontend/debug/reports. Severidade: critica.

Onde rodar: pos-extracao e no build web dataset.

### 5. Negacao/restricao nao pode virar evento produzido

Fixtures:

- `Rockfall Path`, `play:rockfall-path:f690a406`: `Units can't be played here.`
- `Mageseeker Warden`, `play:mageseeker-warden:f27157dd`: `spells and abilities can't ready enemy units and gear.`

Expected facts:

- `restriction_or_permission/restriction` ou `prevent`.
- `payload.polarity` ou campo equivalente de prevencao/restricao.
- Nao gerar `event_produced` para `unit_played` ou `unit_ready`.

Bug que pega: falso positivo grave de enablement e relacoes incorretas do tipo "esta carta produz ready/play". Severidade: critica.

Onde rodar: pos-extracao e em relacoes, garantindo que facts de restricao nao alimentem `produced_event_facts`.

### 6. Replacement effect com `would/instead`

Fixture:

- `Zilean, Time Mage`, `play:zilean-time-mage:8fb4d0e9`
- linha: `Once each turn, if you would play a token unit while I'm at a battlefield, you may play that token and an additional copy of it instead.`

Expected facts:

- `state_or_modifier/replacement_effect/copy`.
- `payload.target.kind = token`, `card_types = unit`.
- `payload.outputs` contem `token_copied`.
- `payload.modality = optional`.
- Nao emitir `event_produced` generico de `card_played` so por conter `play`.

Bug que pega: confundir replacement com producao direta e relacoes amplas falsas com token/play. Severidade: alta.

Onde rodar: golden facts e invariant de modalidade/polaridade.

### 7. Modificador de Might deve gerar similaridade de alto sinal

Fixtures:

- `Ahri, Inquisitive`, `play:ahri-inquisitive:d6396fae`: `give an enemy unit here -2 :rb_might: this turn`.
- `Fiora, Peerless`, `play:fiora-peerless:f8a59eeb`: `double my Might this combat`.

Expected facts:

- Ahri:
  - `state_or_modifier/stat_change/modify_stat`;
  - output `might_modified`;
  - amount `-2 might`;
  - target `unit`, `controller = opponent`, `location = here`;
  - trigger context `self_attacks,self_defends`.
- Fiora:
  - `state_or_modifier/stat_change/modify_stat`;
  - output `might_modified`;
  - multiplier `2`;
  - duration `this_combat`.
- Expected relations:
  - nao necessariamente entre Ahri e Fiora, mas cada uma deve ter pelo menos uma `similar_effect` ou relation de alto sinal baseada em stat modifier quando existirem pares compativeis;
  - nao podem ficar `relation_count = 0` se facts ja sao relacionais.

Bug que pega: lacuna real atual, em que ambos aparecem como `missing_relation_rule` e zero relacoes no quality report. Severidade: media-alta.

Onde rodar: pos-`build_card_relations.py` e pos-`audit_card_explorer_dataset.py`.

### 8. Keyword grant nao pode ficar so como marker

Fixtures:

- `Fortified Position`, `play:fortified-position:31bb26b4`: `It gains [Shield 2] this combat.`
- `The Academy`, `play:the-academy:f9fe7741`: `give your next spell this turn [Repeat] equal to its base cost`.
- `Purifier`, `play:purifier:3e9bbd4c`: `Your Equipment each give [Assault].`

Expected facts:

- Sempre deve haver `state_or_modifier/keyword_grant/gain_keyword`.
- `identity_or_descriptor/keyword_marker` pode existir, mas nao basta.
- Payload precisa ter `keywords`, `target`, `duration` quando textual.

Bug que pega: falso negativo de efeito relacional e frontend mostrando keyword mas perdendo sinergia/filtro de concessao. Severidade: alta.

Onde rodar: pos-extracao. Dataset web: `semantic.keywords` e `semantic.outputs` devem conter `keyword_granted`.

### 9. Attach/detach deve preservar direcao

Fixtures:

- `Angle Shot`, `play:angle-shot:f8a4b638`: `Attach that Equipment to that unit or detach that Equipment from that unit. Draw 1.`
- `Spinning Axe`, `play:spinning-axe:54c823a0`: `Attach this to a unit you control.`

Expected facts:

- Angle Shot:
  - `event_produced/attach` com `equipment_attached`;
  - `event_produced/detach` com `equipment_detached`;
  - `payoff_output/draw`.
- Spinning Axe:
  - `event_produced/attach`, nao `detach`;
  - `target.kind = unit`, `controller = you`.
- Expected relations:
  - attach-related similarity can be broad-skipped if too large, mas attach e detach nao podem colapsar em um reason.

Bug que pega: direcao invertida ou perdida e relacao de attachment/copy incorreta. Severidade: alta.

Onde rodar: golden facts e relation invariants sobre `match.reason` e `output_id`.

### 10. Broad relation deve ser marcada e rebaixada no frontend

Fixture:

- broad reason atual: `spell_card_can_be_countered`;
- cartas afetadas: `Abandon`, `Not So Fast`, muitas spells alvo;
- report atual: `3438` relacoes broad, share `0.3478`.

Expected relations:

- Toda relacao com reason `spell_card_can_be_countered` deve ter `match.broad = true`.
- `strength <= 0.48`.
- Nao deve contar como high-signal no quality report.
- Cards com apenas esse tipo entram em `broad_only`, nao em `ok`.
- Frontend dataset deve preservar `match.broad`, `match.reason`, `strength`.

Bug que pega: hub artificial e frontend ranking poluido por relacao generica. Severidade: alta.

Onde rodar: pos-relacoes, pos-`build_card_explorer_dataset.py`, pos-auditoria web.

### 11. Broad-only nao deve mascarar lacuna real

Fixtures atuais:

- `Acceptable Losses`, `play:acceptable-losses:23e05503`;
- `Keeper's Verdict`, `play:keeper-s-verdict:9e4e390e`;
- `Angle Shot`, `play:angle-shot:f8a4b638`.

Expected:

- Se uma carta tem `relation_count > 0` mas `high_signal_relation_count = 0`, classificar `broad_only`.
- Nao permitir `diagnostic = ok`.
- Para `Acceptable Losses`, expected fact `gear_dies` deve existir, mas relation suite deve indicar ausencia de regra especifica para gear death se so broad/spell-like existir.

Bug que pega: metrica de cobertura enganosa e regressao de auditoria frontend. Severidade: media-alta.

Onde rodar: `audit_card_explorer_dataset.py`.

### 12. Dataset frontend deve ser lossless para semantica usavel

Fixtures:

- `Confront`, `play:confront:dca66872`: `Units you play this turn enter ready. Draw 1.`
- `Altar of Memories`, `play:altar-of-memories:2de88f83`.

Expected dataset:

- Card contem `semantic.facts` compactos com `fact_id`, role, type, predicate, payload, evidence, source, web_uses, extractor, confidence.
- `semantic.outputs` inclui `token_enters_ready` e `card_drawn` para Confront.
- `relations.incoming/outgoing_counts` soma igual ao numero de relacoes compactadas.
- `filters.outputs` contem ids presentes em cards.
- `search_text` inclui evidences dos facts.

Bug que pega: frontend dataset descartando payload/reason/source e filtros inconsistentes com cards. Severidade: alta.

Onde rodar: pos-`build_card_explorer_dataset.py`.

### 13. Linha relacional descoberta nao pode ficar sem fact

Fixtures de lacuna/limite:

- `Rockfall Path`: `Units can't be played here.`
- `Keeper's Verdict`: `Its owner places it on the top or bottom of their Main Deck.`
- `Mystic Reversal`: `Gain control of a spell. You may make new choices for it.`
- `Blue Sentinel`: `Your hold effects for holding here trigger an additional time.`

Expected:

- Toda linha contendo tokens de `relational_keywords` deve ter pelo menos um fact nao-identity, salvo allowlist explicita.
- Severidade varia:
  - `can't`, `cannot`, `only`, `prevent`: alta;
  - `choose one` headings: baixa/allowlist;
  - `copy`, `gain control`, `trigger additional time`: media-alta.

Bug que pega: regressao de cobertura real, nao apenas contagem de facts. Severidade: alta para restricao/permissao.

Onde rodar: auditoria semantica independente, usando `semantic_quality_policy.json`.

### 14. Eventos produzidos sem observadores devem ser classificados

Dados atuais:

- Produced sem observers no report: `spell_countered`, `gear_dies`, `unit_moved`, `token_created`, `equipment_detached`, `damage_dealt`, `card_banished`, `unit_dies`, `card_discarded`, `card_moved`.
- Observed sem producers: `self_discarded`.

Expected:

- Cada evento sem par precisa estar em uma de tres categorias:
  - intentional ignored, via `relation_event_ignore`;
  - missing relation rule;
  - missing extraction producer/observer.
- `gear_dies` com `Acceptable Losses` deve cair em missing relation rule se nao houver target observer.
- `self_discarded` com `Flame Chompers` deve ser explicitamente acompanhado por producer play-self ou marcado como trigger-only sem enablement.

Bug que pega: eventos semanticamente bons mas inuteis para relacoes. Severidade: media-alta.

Onde rodar: pos-auditoria semantica e pos-relacoes.

## Ordem recomendada da suite

1. `contract_static_tests`: schema, ontology, extraction rules, relation rules, domain leakage.
2. `fact_golden_tests`: fixtures reais com expected facts de alto nivel.
3. `fact_invariant_tests`: source_ref, evidence, modality, role/predicate/payload.
4. `relation_golden_tests`: enables/enabled_by/similar/deck_synergy em fixtures pequenas.
5. `relation_quality_tests`: broadness, broad-only, skipped similarity, unlinked relation candidates.
6. `web_dataset_tests`: compactacao lossless, filtros, counts, broad flags e diagnostics.

## Comandos usados

```powershell
Get-Location
rg --files
git status --short
Get-Content -Raw scripts\04_cards_feature_extraction\contracts\semantic_facts_schema.json
Get-Content -Raw scripts\04_cards_feature_extraction\contracts\semantic_quality_policy.json
Get-Content -Raw scripts\04_cards_feature_extraction\contracts\semantic_extraction_rules.json
Get-Content -Raw scripts\04_cards_feature_extraction\contracts\semantic_relation_rules.json
Get-Content -Raw scripts\04_cards_feature_extraction\README.md
Get-Content -Raw scripts\04_cards_feature_extraction\semantic_contracts.py
Get-Content -Raw scripts\04_cards_feature_extraction\validate_semantic_contracts.py
Get-Content -Raw scripts\04_cards_feature_extraction\validate_semantic_golden_examples.py
Get-Content -Raw scripts\04_cards_feature_extraction\extract_semantic_facts.py
Get-Content -Raw scripts\04_cards_feature_extraction\build_card_relations.py
Get-Content -Raw scripts\04_cards_feature_extraction\audit_semantic_facts.py
Get-Content -Raw scripts\05_web_dataset\build_card_explorer_dataset.py
Get-Content -Raw scripts\05_web_dataset\audit_card_explorer_dataset.py
Get-Content -Raw scripts\04_cards_feature_extraction\contracts\semantic_golden_examples.json
Get-Content -Raw data\processed\cards\semantic\cards_semantic_audit_report.md
Get-Content -Raw data\processed\cards\relations\cards_card_relations_report.md
Get-Content -Raw data\processed\web\card_explorer_quality_report.md
Select-String -Path data\processed\cards\semantic\cards_semantic_facts.jsonl -Pattern 'play:ahri-inquisitive|play:fiora-peerless|play:fortified-position|play:ravenborn-tome|play:mageseeker-warden|play:vilemaw|play:acceptable-losses|play:spinning-axe|play:rockfall-path|play:keeper-s-verdict'
Select-String -Path data\processed\cards\relations\cards_card_relations.jsonl -Pattern 'spell_card_can_be_countered|play:acceptable-losses|play:ahri-inquisitive|play:fiora-peerless|play:ravenborn-tome|play:mageseeker-warden'
Get-Content -Raw data\processed\cards\normalized\cards_normalized.json | ConvertFrom-Json
Get-Content -Raw data\processed\web\card_explorer_dataset.json | ConvertFrom-Json
```

Observacao: um comando PowerShell de formatacao falhou por sintaxe de pipeline vazio durante a exploracao; o agente reexecutou a versao equivalente apenas leitura com variavel intermediaria.
