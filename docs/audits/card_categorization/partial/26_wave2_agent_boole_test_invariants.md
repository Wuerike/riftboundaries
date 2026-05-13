# Onda 2 - agente Boole - invariantes e contratos de regressao

## Escopo

Auditoria nao mutante da onda 2 sobre invariantes e contratos de regressao para a etapa 04 e web.

O agente informou que nao editou arquivos e nao executou builders/auditors com defaults porque eles escrevem relatorios; usou leitura direta dos JSON/JSONL, contratos, scripts e reports atuais.

## Base verificada

- Cartas normalizadas: 767.
- Fatos semanticos: 5428.
- Linhas textuais: 1248, com 1221 cobertas.
- Relacoes: 9884.
- Broad relations: 3438, todas dominadas por `spell_card_can_be_countered`.
- Cartas sem relacoes: 100.
- Cartas broad-only: 22.
- Goldens atuais: 40 exemplos, 73/73 fatos minimos encontrados.
- Proveniencia dos fatos: 3011 structural, 1759 contract_rule, 658 legacy_rule.

## Invariantes que deveriam virar testes

1. `semantic_ontology.json` e `semantic_facts_schema.json` devem ter os mesmos enums para roles, fact types, actions, events, outputs e relation types.
2. Todo `fact_id` e `relation_id` deve ser unico.
3. Todo fato textual deve ter `evidence` contida exatamente na linha normalizada referenciada.
4. `trigger_observed` exige `payload.event`; `event_produced` exige evento produzido ou output equivalente.
5. Nao pode haver dois fatos no mesmo `play_id/source_field/line_index` com mesmo evento, role, predicate e payload, salvo quando a regra declarar multi-evento.
6. Regras compostas como `When I conquer or hold` devem gerar `self_conquers` e `self_holds` uma vez cada.
7. Modalidade deve ser por clausula/evidencia, nao por linha inteira.
8. Goldens devem ter modo minimo e modo exato: `forbidden_facts`, `max_fact_count_by_source_line` e `exact_expected_facts`.
9. Regras legadas devem ter orcamento explicito. Hoje `legacy_rule_count=658`; qualquer legado nao allowlisted deve falhar.
10. Relacoes `enables` devem ter par reverso `enabled_by`; `similar_effect` deve ser simetrica.
11. Nenhuma relacao deve ligar a carta a ela mesma.
12. Broad relations devem ser marcadas, contadas separadamente e excluidas do ranking default ou rebaixadas.
13. O dataset web deve preservar todos os fatos e relacoes: soma de outgoing e incoming deve bater com `relation_count`.
14. Filtros publicados em `dataset.filters` devem ser renderizados pelo frontend ou marcados como ignorados/experimentais.
15. Builder web e auditor web devem usar a mesma funcao para detectar linha relacional descoberta.

## Cartas para suite de regressao

| Carta | Contrato esperado |
| --- | --- |
| `Harnessed Dragon` | `When you play me` como trigger; `kill an enemy unit` como `event_produced/removal/kill/enemy_unit_dies`. |
| `Altar of Memories` | Trigger `friendly_unit_dies`; custo opcional `exhaust`; `draw 1` e mover carta ao topo/fundo preservados. |
| `Arachnoid Horror` | Hunt gera exatamente dois triggers: `self_conquers`, `self_holds`; sem duplicar `self_conquers`. |
| `Baited Hook` | `Kill a friendly unit` e `Look at top 5` nao devem virar opcionais por causa de `You may banish`. |
| `Sprite Fountain` | `[Temporary]` nao deve gerar dois eventos equivalentes `self_dies` na mesma linha. |
| `Ornn's Forge` | Custo de gear reduzido deve ser especifico; nao deve emitir tambem `play_cost_reduced` generico. |
| `Rockfall Path` | `Units can't be played here` deve virar restricao de play/location, nao ficar so com fatos oficiais. |
| `Curtain Call` | `already` nao pode disparar keyword `ready`; linha de cabecalho modal nao deve virar falso uncovered relacional. |
| `Keeper's Verdict` | `places it on the top or bottom of their Main Deck` deve virar movimento/card-flow, nao so relacao broad por ser spell. |
| `Not So Fast`/`Abandon` | `spell_card_can_be_countered` deve ser broad e nao dominar ranking default. |

## Achados

### 1. Goldens minimos deixam fatos indevidos passarem

- categoria do achado: teste faltante
- severidade: alta
- confianca: alta
- evidencia: `validate_semantic_golden_examples.py` so itera `minimum_expected_facts` e o golden atual passa 73/73, mas `Sprite Fountain`, `Ornn's Forge` e `Arachnoid Horror` tem fatos extras/duplicados.
- regra relacionada: goldens minimos.
- impacto provavel no produto final: regressoes por fatos indevidos passam.
- recomendacao: adicionar `forbidden_facts` e modo exato.
- teste que deveria existir: fixture que falha se `Sprite Fountain` emitir dois `self_dies`.

### 2. Duplicacao semantica em trigger composto

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: o agente encontrou 15 grupos duplicando `self_conquers` em linhas `When I conquer or hold`; exemplo `Arachnoid Horror`.
- regra relacionada: `trigger_self_conquers_or_holds` + `trigger_self_conquers`.
- impacto provavel no produto final: filtros/triggers inflados.
- recomendacao: precedencia ou negative lookahead.
- teste que deveria existir: uma linha Hunt deve produzir exatamente `{self_conquers,self_holds}`.

### 3. Escopo de modalidade por linha

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `payload_with_line_modality` marca a linha inteira como optional quando ha `you may`; `Baited Hook` marca `Kill a friendly unit`, `Look at the top 5` e `recycle the rest` como opcionais.
- regra relacionada: `line_has_optional_governor`.
- impacto provavel no produto final: relacoes e filtros confundem custo/efeito obrigatorio.
- recomendacao: modalidade por clausula.
- teste que deveria existir: `Baited Hook` exige kill/look `required` e banish/play `optional`.

### 4. Sobreposicao de regras especificas e genericas

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Ornn's Forge` gera `gear_cost_reduced` especifico e `play_cost_reduced` generico para a mesma reducao; `Safety Inspector` gera multiplos `kill` na mesma clausula.
- regra relacionada: templates especificos + genericos.
- impacto provavel no produto final: similaridade falsa.
- recomendacao: bloquear regra generica quando a especifica cobre o span.
- teste que deveria existir: uma evidencia coberta por regra especifica nao pode emitir fallback generico equivalente.

### 5. Auditoria web usa matchers divergentes

- categoria do achado: manutencao
- severidade: media-alta
- confianca: alta
- evidencia: `card_explorer_dataset_report.json` reporta `cards_with_uncovered_relational_lines=2`, mas `card_explorer_quality_report.json` reporta 0; a deteccao por substring pega `ready` dentro de `already`, enquanto a regex nao pega `played` como forma de `play`.
- regra relacionada: `relational_keywords`.
- impacto provavel no produto final: reports contraditorios.
- recomendacao: centralizar matcher com limites e variantes morfologicas.
- teste que deveria existir: `Curtain Call` falso, `Rockfall Path` verdadeiro.

### 6. Broad de counter domina grafo

- categoria do achado: integracao entre etapas
- severidade: alta
- confianca: alta
- evidencia: `spell_card_can_be_countered` gera 3438 relacoes, 34.78% do grafo; `Abandon` tem 398 broad de 471.
- regra relacionada: `identity_event_relations`.
- impacto provavel no produto final: hubs artificiais dominam produto.
- recomendacao: separar broad de high-signal no contrato web.
- teste que deveria existir: broad nao entra em ranking default e tem contador proprio.

### 7. Paridade web incompleta

- categoria do achado: integracao entre etapas
- severidade: media
- confianca: alta
- evidencia: dataset inclui `deck_synergy=1056` e filtros `tags`, `outputs`, `produced_events`, `power`; `web/app/app.js` renderiza so `enabled_by`, `enables`, `similar_effect` e filtros parciais.
- regra relacionada: contrato dataset/frontend.
- impacto provavel no produto final: artefatos publicados nao sao exploraveis.
- recomendacao: renderizar ou declarar `ignored`.
- teste que deveria existir: snapshot de relation types/filtros do dataset contra UI.

### 8. Maturidade de contratos parcial

- categoria do achado: arquitetura
- severidade: media
- confianca: alta
- evidencia: `semantic_extraction_rules.json` tem 133 regras, 59 sem `facts`; `semantic_contracts.py` valida `rule.get("facts", [])`, entao regra sem template passa.
- regra relacionada: validacao de contratos.
- impacto provavel no produto final: JSON parece fonte de verdade, mas Python/legacy ainda carrega semantica real.
- recomendacao: exigir `builder`/allowlist explicita e orcamento de legado.
- teste que deveria existir: falhar se regra vazia nao estiver documentada ou se `legacy_rule_count` sair do orcamento.
