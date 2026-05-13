# Execucao estendida - indice de resultados

## Contexto

Esta execucao continua a auditoria nao mutante solicitada em `goal.md`. O objetivo desta fase e repetir a analise em varias ondas com agentes novos e contexto limpo, salvando os resultados brutos/parciais para consolidacao posterior.

## Restricoes mantidas

- Nao alterar codigo, configs, dados raw ou outputs processados.
- Nao implementar correcoes.
- Nao fazer commits.
- Escrever somente relatorios Markdown em `docs/audits/card_categorization/`.
- Em cada ciclo, confrontar cartas normalizadas e regras de categorizacao com o comportamento do pipeline.

## Ondas planejadas

| Onda | Status | Escopos |
| --- | --- | --- |
| 1 | completa | extracao semantica por riscos, pre-pipeline, relacoes/web, goldens/auditoria, corpus de textos normalizados, contratos entre etapas |
| 2 | completa | mergulhos estreitos em custo/recurso, replacement/prevent, modais, attachment/reminder, similaridade e invariantes de contrato |
| 3 | completa | regras oficiais x fatos, amostragem de cartas, payload/schema, cartas isoladas, runas/recursos e produto frontend |
| 4 | completa | keywords oficiais, falsos positivos de relacoes, falsos negativos por texto rico e suite independente de invariantes |

## Arquivos desta fase

Os resultados brutos dos agentes serao salvos como:

- `11_wave1_agent_*.md`
- `21_wave2_agent_*.md`
- `31_wave3_agent_*.md`
- `32_wave3_agent_*.md`
- `33_wave3_agent_*.md`
- `34_wave3_agent_*.md`
- `35_wave3_agent_*.md`
- `36_wave3_agent_*.md`
- `41_wave4_agent_*.md`
- `42_wave4_agent_*.md`
- `43_wave4_agent_*.md`
- `44_wave4_agent_*.md`
- `19_wave1_local_crosscheck.md`

Relatorios locais de checagem cruzada entre ondas serao salvos como:

- `19_wave1_local_crosscheck.md`
- `29_wave2_local_crosscheck.md`
- `39_wave3_local_crosscheck.md`
- `49_wave4_local_crosscheck.md`

## Resultados locais salvos

- `19_wave1_local_crosscheck.md`: varredura local encontrou novos riscos em `generic_cost_reduction`, `Determined Sentry`, `Buhru Captain` e `effect_lines`.
- `11_wave1_agent_kant_contracts_goldens.md`: goldens minimos, auditoria sem warnings apesar de linhas descobertas, duplicidades, schema incompleto.
- `12_wave1_agent_hegel_pre_pipeline_normalization.md`: variantes semanticas, richest printing, reminder text, modal bullets e effect_lines attached-only.
- `13_wave1_agent_lagrange_corpus_patterns.md`: padroes `would/instead`, negacao, choose one, copy/becomes, up to, additional cost, more/less e swap.
- `14_wave1_agent_faraday_relations_web.md`: broad hubs, deck_synergy invisivel, resource synergy falso, similaridade larga, filtros divergentes.
- `15_wave1_agent_hooke_clause_modality_negation.md`: modalidade por linha, governadores opcionais, must, negacao, replacement/prevent, activation_split e clause_group.
- `16_wave1_agent_meitner_stage_contracts.md`: reminder como fato, activation_cost em triggers, XP em custo ausente, runas basicas e contratos 01-05.
- `29_wave2_local_crosscheck.md`: confirmou `activation_cost` em linhas `When/If/While`, custos XP ausentes e baixa modelagem de replacement/prevention.
- `39_wave3_local_crosscheck.md`: analisou cartas sem relacao, broad-only e hubs, mostrando fatos uteis sem familia relacional e broad dominando top hubs.
- `21_wave2_agent_carver_cost_resource.md`: custos XP, activation split, thresholds, more/less, additional/ignore cost e resource synergy.
- `22_wave2_agent_sartre_replacement_negation.md`: replacement/prevent ausentes, negacao invertida e restricoes sem fato.
- `23_wave2_agent_pascal_modals_choices.md`: grupos modais, bullets, Repeat, inline `or`, memoria de escolha e choice kind.
- `24_wave2_agent_leibniz_attachment_reminder.md`: Equip/reminder duplicando custos, effect_lines attached-only, attach explicito e recall.
- `25_wave2_agent_lovelace_relations_similarity.md`: similaridade larga, broad hubs, resource synergy, dedup e isolamento.
- `26_wave2_agent_boole_test_invariants.md`: invariantes de regressao, suite de cartas e lacunas de contrato.
- `31_wave3_agent_ramanujan_core_rules.md`: regras centrais contra fatos, incluindo reminder/effect text, recall, modes, additional costs, replacement, Basic Runes e keywords.
- `32_wave3_agent_dalton_sampling.md`: amostragem estratificada de 61 cartas, custos, texto citado/concedido, copy/modals, recall, broad-only e `rule_variants`.
- `33_wave3_agent_kepler_payload_schema.md`: payload schema, ontologia, `source_ref`, `web_uses` e shapes negativos/duplicados.
- `34_wave3_agent_franklin_relations_isolation.md`: cartas sem relacao, broad-only, hubs, lacunas de relacao e fan-out generico.
- `35_wave3_agent_harvey_runes_resources.md`: Basic Runes, Add multi-symbol, XP/rainbow/any, truncamento de custos e channel.
- `36_wave3_agent_hilbert_frontend_product.md`: riscos de produto no explorador web: `deck_synergy` invisivel, broad, isoladas, filtros e evidencia.
- `41_wave4_agent_noether_keywords_official_terms.md`: keywords oficiais, Accelerate sem `enter_ready`, marker falso positivo, Add como acao e conquer.
- `42_wave4_agent_newton_relation_false_positives.md`: broad de counter, similaridade generica, `resource_synergy` com custo/limite e duplicacao de `derived_synergy`.
- `43_wave4_agent_goodall_false_negatives.md`: falsos negativos por texto rico em attachment/equipment, Temporary, replacement/prevent, control, zone movement e score.
- `44_wave4_agent_erdos_test_invariants.md`: suite independente de goldens/invariantes para fatos, relacoes, broad-only e dataset web.
- `49_wave4_local_crosscheck.md`: checagem local de cobertura de termos oficiais, blind spots ricos, broad hubs e familias sem relacao util.

## Observacao

Os relatorios `00` a `04` e `99` foram produzidos antes da clarificacao de que a execucao deveria continuar por mais tempo. Eles permanecem como uma primeira consolidacao, mas esta fase salva resultados adicionais para uma consolidacao posterior.
