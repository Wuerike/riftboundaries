# Auditoria final - categorizacao de cartas

## Resumo executivo

A auditoria nao mutante encontrou riscos reais na categorizacao de cartas. A cobertura numerica parece alta (`5428` fatos, `9884` relacoes, `0` warnings na auditoria semantica), mas ha casos concretos onde a categoria esta errada: aumento de custo vira reducao, negacao vira acao positiva, choices exclusivos viram efeitos simultaneos, e effect text attached-only vira modificador estatico.

Nenhum codigo, config, dado de entrada ou artefato processado foi alterado. Os unicos arquivos criados por esta auditoria estao em `docs/audits/card_categorization/`.

## Relatorios produzidos

- `01_overview_and_core_risks.md`: visao geral e riscos centrais.
- `02_pre_pipeline_normalization_and_rules.md`: entrada, normalizacao, variantes e regras oficiais.
- `03_feature_extraction_findings.md`: bugs e fragilidades da extracao semantica.
- `04_downstream_web_and_reports.md`: relacoes, dataset web, frontend e reports.
- `00_final_prioritized_report.md`: consolidacao final priorizada.
- `99_completion_audit.md`: checklist final contra o objetivo.

## Metodo

Foram usadas leituras locais, consultas `rg`, parsing somente leitura com PowerShell/`ConvertFrom-Json` e tres subagentes independentes:

- Peirce: entrada, normalizacao, variantes e regras oficiais.
- Godel: etapa 04, contratos, fatos e exemplos dourados.
- Hubble: relacoes, dataset web, frontend e reports.

Em cada rodada, a auditoria relia cartas normalizadas e contratos de categorizacao, e confrontava comportamento de codigo com cartas concretas.

## Escopo factual verificado

- `data/raw/cards.json`: `950` printings.
- `cards_normalized.json`: `767` cartas normalizadas.
- Cartas com `rule_variants`: `44`.
- `cards_semantic_facts.jsonl`: `5428` fatos.
- Proveiencia: `3011` structural field, `1759` contract rule, `658` legacy rule.
- Golden report: `40` exemplos, `73/73` fatos esperados encontrados, `pass: true`.
- Relacoes: `9884`, incluindo `3438` broad e `1056` `deck_synergy`.
- Broad share: `0.3478`.
- Cartas sem relacao: `100`.
- Cartas broad-only: `22`.

## 1. Riscos criticos de categorizacao

### C1. Aumento de custo categorizado como reducao de custo

- severidade: critica
- exemplo: `Vaults of Helia`
- evidencia: texto normalizado diz `your non-token units cost :rb_energy_1: more to play this turn`; fato gerado e `predicate: reduce_cost`, output `play_cost_reduced`, regra `generic_cost_reduction`.
- impacto: a carta se relaciona por similaridade com cartas de desconto como `Battering Ram`, `Eager Apprentice`, `Ezreal, Prodigy`, `Irelia, Graceful`, `Marai Spire` e `Ornn's Forge`.
- correcao recomendada: separar `increase_cost` e `reduce_cost`; tratar `more` como polaridade positiva de custo, nao desconto.

### C2. Negacao e prevent geram fatos positivos

- severidade: alta
- exemplos: `Safety Inspector`, `Mageseeker Warden`
- evidencia: `don't kill a unit` gera fato positivo de kill; `can't ready enemy units and gear` gera restricao correta e tambem fato positivo `ready`.
- impacto: cartas que impedem ou removem a acao podem ser classificadas como produtoras daquela acao.
- correcao recomendada: negative guards compartilhados para `can't`, `cannot`, `don't`, `doesn't`, `not`, `prevent`, `instead`.

### C3. Modalidade opcional aplicada na linha inteira

- severidade: alta
- exemplos: `Dancing Grenade`, `The Academy`
- evidencia: `line_has_optional_governor` marca qualquer fato da linha como opcional se a linha contem `you may`. O dano obrigatorio de `Dancing Grenade` e o grant obrigatorio de `[Repeat]` em `The Academy` viram opcionais por causa de outra clausula ou reminder.
- impacto: filtros e relacoes distinguem mal required/optional.
- correcao recomendada: modalidade por clausula/evidencia, com tratamento especial para reminder text.

### C4. Choices exclusivos viram efeitos simultaneos

- severidade: alta
- exemplo: `Disposal Order`
- evidencia: `Choose one -` e achatado; recycle e draw saem como fatos requeridos separados.
- impacto: cartas modais aparecem em categorias de todas as opcoes ao mesmo tempo.
- correcao recomendada: `choice_group_id`, `choice_mode: choose_one`, `option_index` e exclusividade no payload.

### C5. Effect text attached-only vira modificador estatico

- severidade: alta
- exemplo: `Rabadon's Deathcrown`
- evidencia: core rules dizem que Effect Text e inativo salvo quando attached; fato gerado usa `source_field: effect_lines` e `modality: static` sem `activation_context`.
- impacto: relacoes e filtros nao diferenciam texto ativo da carta top-most de texto inativo na carta solta.
- correcao recomendada: modelar `activation_context: attached`, `applies_to: top_most_card`, `inactive_until_attached`.

## 2. Bugs provaveis em `scripts/04_cards_feature_extraction`

- `generic_cost_reduction` aceita `costs?` e sempre emite reducao, mesmo com `cost more`.
- Regex legado de movimento continua rodando junto com regra contratual: `Janna, Savior` gera um fato correto e outro com target `raw: up`.
- Regras `trigger_self_conquers_or_holds` e `trigger_self_conquers` se sobrepoem: `Arachnoid Horror` duplica `self_conquers`.
- `line_has_optional_governor` e `payload_with_line_modality` aplicam optionalidade em escopo amplo demais.
- `ready_unit` casa adjetivo em `Play a ready token`, criando acao `ready` onde deveria haver estado de entrada do token.
- A etapa ainda emite `658` fatos `legacy_rule`, embora os contratos sejam apresentados como fonte principal de semantica revisavel.

## 3. Divergencias entre regras, cartas e implementacao

- Regras oficiais de Effect Text (`core-rules.md:752`, `:755`, `:3846`, `:5140`) nao sao refletidas na extracao de `effect_lines`.
- `rule_variants` preserva divergencias oficiais entre printings, mas a etapa 04 extrai apenas `rules_lines` e `effect_lines` principais.
- `core-rules.json` existe e o README declara ligacao futura com fatos; hoje ele nao valida as categorias geradas.
- `feature_relation_taxonomy` reconhece familias como `choice_modal`, mas a estrutura de fatos nao preserva grupos modais.
- O inventario pode indicar familia relacional de alta prioridade, enquanto o audit semantico ainda retorna `0` warnings.

## 4. Lacunas de teste

- Goldens negativos de ausencia de fatos extras.
- Testes de polaridade: cost more vs cost less/reduced.
- Testes de negacao/prevent.
- Testes de deduplicacao contrato x legado.
- Testes de trigger composto sem duplicata.
- Testes de modalidade por clausula.
- Testes de choices exclusivos.
- Testes de `effect_lines` attached-only.
- Testes de `rule_variants` semanticas.
- Testes de paridade entre builder web, auditor web e frontend.
- Testes de broad relations no estado default da UI.

## 5. Fragilidade de arquitetura e contratos

- O contrato semantico esta dividido entre JSON e Python legado; revisores podem alterar contratos sem afetar todo comportamento real.
- O normalizador perde estrutura de lista/modal ao achatar HTML em linhas.
- O `play_id` agrupa por assinatura jogavel que nao inclui texto de regras, deixando variantes como informacao lateral.
- O relation builder amplifica erros upstream, porque assume que fatos ja representam polaridade, negacao e modalidade corretamente.
- Reports web usam criterios divergentes para `cards_with_uncovered_relational_lines`.
- O frontend ignora parte do contrato do dataset: `deck_synergy`, `tags`, `produced_events`, `outputs` e filtro de `power`.

## 6. Melhorias de manutencao recomendadas

1. Corrigir primeiro polaridade de custo, negacao/prevent, modalidade por clausula, choices e effect text attached-only.
2. Adicionar goldens negativos para os exemplos concretos desta auditoria.
3. Criar uma camada comum de guards: negacao, prevent, reminder, modal option, attached context.
4. Migrar ou isolar regras legadas por familia, com limite esperado para `legacy_rule_count`.
5. Reportar `rule_variants` como risco semantico ate existir extracao por variante.
6. Centralizar criterios de broad relation e uncovered relational lines.
7. Alinhar `RELATION_TYPES` e filtros entre dataset, auditor e frontend.
8. Remover contagens estaticas desatualizadas dos READMEs ou data-las como snapshot.

## Priorizacao sugerida

### P0

- `Vaults of Helia`: `cost more` nao pode virar `reduce_cost`.
- Negative guards para `Safety Inspector` e `Mageseeker Warden`.
- Choices exclusivos para `Disposal Order`.
- `effect_lines` com contexto attached-only.

### P1

- Deduplicacao contrato x legado usando `Janna, Savior`.
- Trigger composto sem duplicata usando `Arachnoid Horror`.
- Modalidade por clausula usando `Dancing Grenade` e `The Academy`.
- Broad relations filtradas/rebaixadas no frontend.

### P2

- Auditoria de `rule_variants`.
- Paridade de `deck_synergy` e filtros web.
- Centralizacao de uncovered relational lines.
- Atualizacao de documentacao de contagens.

## Arquivos principais envolvidos em futuras correcoes

- `scripts/04_cards_feature_extraction/extract_semantic_facts.py`
- `scripts/04_cards_feature_extraction/contracts/semantic_extraction_rules.json`
- `scripts/04_cards_feature_extraction/contracts/semantic_golden_examples.json`
- `scripts/04_cards_feature_extraction/audit_semantic_facts.py`
- `scripts/04_cards_feature_extraction/build_card_relations.py`
- `scripts/05_web_dataset/build_card_explorer_dataset.py`
- `scripts/05_web_dataset/audit_card_explorer_dataset.py`
- `web/app/app.js`

## Comandos e verificacoes principais

- `git status --short`
- `rg --files`
- `rg -n` sobre READMEs, scripts da etapa 03, scripts da etapa 04, contratos, reports web e frontend.
- PowerShell `ConvertFrom-Json` sobre `cards.json`, `cards_normalized.json`, `cards_semantic_facts.jsonl`, `cards_card_relations.jsonl`.
- Leitura de `cards_semantic_audit_report.md`, `cards_semantic_golden_report.json`, `cards_card_relations_report.md`, `card_explorer_dataset_report.md` e `card_explorer_quality_report.md`.

## Limites da auditoria

- Nao foram executados comandos mutantes do pipeline.
- Nao foram alterados contratos, scripts, dados raw ou dados processados.
- Nao houve tentativa de corrigir o pipeline nesta rodada, por restricao explicita do objetivo.
- As recomendacoes sao baseadas em evidencias locais atuais e nos reports gerados ja existentes.

## Conclusao

O pipeline ja tem boa rastreabilidade e muitos artefatos uteis, mas a categorizacao ainda nao esta pronta para ser tratada como fonte confiavel de produto sem revisao dos casos acima. A prioridade deve ser corrigir falsa semantica antes de aumentar cobertura: fatos errados com alta cobertura geram relacoes erradas com alta confianca aparente.
