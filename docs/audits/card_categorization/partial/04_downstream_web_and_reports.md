# Auditoria parcial 04 - relacoes, dataset web e reports

## Escopo analisado

Esta rodada revisou como os fatos extraidos viram relacoes e como essas relacoes chegam ao dataset e ao frontend.

O foco foi a categoria exibida para usuario final: relacoes broad, tipos de relacao ignorados, filtros expostos pelo dataset mas nao usados pelo app, e divergencia entre reports gerados.

## Artefatos relidos

- `data/processed/cards/semantic/cards_semantic_facts.jsonl`
- `data/processed/cards/relations/cards_card_relations.jsonl`
- `data/processed/cards/relations/cards_card_relations_report.md`
- `data/processed/web/card_explorer_dataset.json`
- `data/processed/web/card_explorer_dataset_report.md`
- `data/processed/web/card_explorer_quality_report.md`
- `scripts/04_cards_feature_extraction/build_card_relations.py`
- `scripts/04_cards_feature_extraction/contracts/semantic_relation_rules.json`
- `scripts/04_cards_feature_extraction/contracts/semantic_quality_policy.json`
- `scripts/05_web_dataset/build_card_explorer_dataset.py`
- `scripts/05_web_dataset/audit_card_explorer_dataset.py`
- `web/app/app.js`
- `web/app/README.md`
- `web/ideias.md`

## Cartas confrontadas

- `Acceptable Losses`
- `Angle Shot`
- `Block`
- `Dancing Grenade`
- `Fading Memories`
- `Mageseeker Warden`
- `Vaults of Helia`
- `Curtain Call`
- `Rockfall Path`

## Regras de relacao confrontadas

- `spell_card_can_be_countered`
- `token_created_to_token_entry_modifier`
- `generic_unit_death_enables_friendly_unit_dies`
- `unit_buffed_enables_unit_buffed`
- `resource_synergy`
- `derived_synergy`
- `similarity`

## Comandos executados e resultado

- `Get-Content card_explorer_dataset_report.md`: `767` cartas, `5428` fatos, `9884` relacoes, `100` cartas sem relacoes, `22` broad-only, `2` cartas com linhas relacionais sem cobertura.
- `Get-Content card_explorer_quality_report.md`: `9884` relacoes, `3438` broad, `0.3478` share broad, `22` broad-only, mas `cards_with_uncovered_relational_lines: 0`.
- `Get-Content cards_card_relations_report.md`: `similar_effect: 4746`, `enabled_by: 2041`, `enables: 2041`, `deck_synergy: 1056`; `spell_card_can_be_countered: 3438`.
- PowerShell em `cards_card_relations.jsonl`: confirmou `Vaults of Helia` conectado por similaridade a cartas de reducao de custo por causa do fato falso `play_cost_reduced`.
- `rg -n "deck_synergy|RELATION_TYPES|match.broad|relation.match|filters|produced_events|outputs|power"`: confirmou que o builder e auditor web conhecem `deck_synergy`, mas o frontend so lista tres tipos de relacao.
- `rg -n "Curtain Call|Rockfall Path|cards_with_uncovered_relational_lines|uncovered"`: confirmou divergencia de report entre dataset e quality audit.

## Achados

### 1. `deck_synergy` e gerado e empacotado, mas o frontend nao mostra

- categoria do achado: divergencia dataset x UI
- severidade: media
- confianca: alta
- evidencia: `cards_card_relations_report.md` mostra `deck_synergy: 1056`. `scripts/05_web_dataset/build_card_explorer_dataset.py:23` inclui `deck_synergy` em `RELATION_TYPES`. `scripts/05_web_dataset/audit_card_explorer_dataset.py:24` tambem inclui o tipo. No frontend, `web/app/app.js:2` define `RELATION_TYPES = ["enabled_by", "enables", "similar_effect"]`.
- impacto: 1056 relacoes calculadas nao tem superficie principal no app, apesar de entrarem nas contagens de qualidade e no dataset.
- recomendacao: decidir se `deck_synergy` e produto ou artefato experimental. Se for produto, adicionar aba/filtro/ordenacao; se nao for, remover das metricas principais para evitar falsa expectativa.
- teste faltante: teste de paridade entre `dataset.relation_type_counts` e tipos exibidos pelo frontend.

### 2. Relacoes broad nao sao filtradas nem rebaixadas por padrao no app

- categoria do achado: risco de experiencia e interpretacao
- severidade: alta
- confianca: alta
- evidencia: `spell_card_can_be_countered` responde por `3438` relacoes, `34.78%` do grafo. `card_explorer_quality_report.md` lista `22` cartas broad-only e exemplos como `Acceptable Losses`, `Angle Shot`, `Block` e `Dancing Grenade`. `web/app/app.js:91-99` agrupa relacoes por tipo sem verificar `relation.match.broad`; `web/app/app.js:212` exibe a razao/strength, mas nao rebaixa broad na selecao principal.
- impacto: relacoes de baixo sinal podem dominar a experiencia e esconder relacoes realmente explicativas.
- recomendacao: filtrar broad por padrao, ou ordenar depois de high-signal com controle visual explicito. O dataset ja tem `match.broad`; o frontend precisa respeitar esse campo.
- teste faltante: fixture de carta broad-only garantindo que broad nao aparece no estado default, ou aparece em uma secao separada.

### 3. Filtros do dataset nao tem paridade com filtros do frontend

- categoria do achado: divergencia de contrato web
- severidade: media
- confianca: alta
- evidencia: `card_explorer_dataset_report.md` mostra filtros para `tags`, `produced_events`, `outputs` e `power`, alem dos filtros usados. `scripts/05_web_dataset/build_card_explorer_dataset.py:195-206` cria esses counters; `web/app/app.js:80-86` filtra apenas domains, types, triggers, keywords, energy, might e predicates. O app mostra `power` como stat em cards (`web/app/app.js:172`, `:233`), mas nao filtra por ele.
- impacto: o dataset carrega dimensoes sem UI, e demandas ja registradas em `web/ideias.md` podem ficar desconectadas do contrato real.
- recomendacao: publicar um contrato explicito de filtros suportados pela UI. Se um filtro entra no dataset mas nao no app, marcar `experimental` ou `hidden`.
- teste faltante: snapshot de filtros do dataset contra filtros renderizados por `renderFilters`.

### 4. Reports discordam sobre linhas relacionais descobertas

- categoria do achado: divergencia de auditoria
- severidade: media
- confianca: alta
- evidencia: `card_explorer_dataset_report.md:37` reporta `cards_with_uncovered_relational_lines: 2`; `card_explorer_quality_report.md:12` reporta `cards_with_uncovered_relational_lines: 0`. A busca por `Curtain Call` e `Rockfall Path` aparece no contexto do dataset report, mas nao no resumo do quality report.
- impacto: revisores podem concluir que nao ha lacunas relacionais enquanto outro report afirma que existem.
- recomendacao: centralizar a funcao que identifica linha relacional descoberta e usar o mesmo criterio no builder e no auditor.
- teste faltante: unidade compartilhada para `is_uncovered_relational_line`, com fixture para `Curtain Call` e `Rockfall Path`.

### 5. Erros de fatos sobem diretamente para relacoes e produto

- categoria do achado: propagacao de erro
- severidade: alta
- confianca: alta
- evidencia: `Vaults of Helia` recebeu `play_cost_reduced` por uma linha que aumenta custo. O grafo entao conecta a carta a varias cartas de desconto por `similar_effect` com reason `output:state_or_modifier:static_modifier:reduce_cost:play_cost_reduced:1:energy:card:::required`.
- impacto: mesmo que o relation builder funcione como projetado, ele amplifica erro upstream. O problema aparece como categorizacao de produto, nao apenas como bug de extracao.
- recomendacao: adicionar validacoes de sanidade relacional por polaridade, especialmente para custo, dano, might, heal/kill, ready/exhaust e prevent/produce.
- teste faltante: audit relation que detecte pares improvaveis quando a evidencia contem `more` mas o output diz `reduced`.

### 6. Documentacao de estado atual esta desatualizada

- categoria do achado: manutencao
- severidade: baixa
- confianca: alta
- evidencia: `README.md` e README da etapa 04 ainda citam contagens antigas, como `5382` fatos e `9047` relacoes em `scripts/04_cards_feature_extraction/README.md:430`. Reports atuais indicam `5428` fatos e `9884` relacoes.
- impacto: confunde revisao de progresso e comparacao de regressao.
- recomendacao: manter contagens apenas em reports gerados ou datar claramente cada snapshot de README.
- teste faltante: check opcional que detecte contagens estaticas desatualizadas em documentacao.

## Testes faltando

- Teste de paridade `RELATION_TYPES` entre builder, auditor e frontend.
- Teste de comportamento default para `match.broad`.
- Teste de filtros renderizados contra filtros publicados no dataset.
- Teste compartilhado para uncovered relational lines.
- Teste de sanidade relacional por polaridade.

## Conclusao parcial

O downstream assume que fatos upstream sao semanticamente corretos e que todos os tipos/filtros publicados sao intencionais para a UI. Hoje esses contratos nao estao alinhados: `deck_synergy` some no frontend, broad relations entram no fluxo principal, filtros existem sem UI, e dois reports discordam sobre lacunas.
