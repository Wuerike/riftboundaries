# Onda 3 - agente Kepler - payload, schema e ontology

## Escopo

Auditoria nao mutante da onda 3 sobre payload/schema/ontology shape e compatibilidade downstream.

O agente informou que nao editou arquivos nem rodou builders/auditores que escrevem outputs. Usou leitura direta e scripts in-memory. `git status --short` ao final: `M goal.md`, `?? docs/`.

## Contagens principais

- Fatos: 5428; cartas com fatos: 767; relacoes atuais: 9884.
- Relacoes: `similar_effect 4746`, `enabled_by 2041`, `enables 2041`, `deck_synergy 1056`.
- `source_ref.source_field`: `official_field 3011`, `rules_lines 2363`, `effect_lines 54`.
- Campos obrigatorios de topo: 0 ausentes.
- `evidence`: 0 vazio.
- Referencias de linha contra `cards_normalized.json`: 0 invalidas.
- Payload keys reais: `object 2453`, `amounts 1902`, `modality 1655`, `stat 1399`, `outputs 933`, `event 929`, `target 904`, `costs 209`, `duration 181`, `destination 81`, `location 73`, `conditions 71`, `modifiers 64`, `keywords 35`, `source 28`, `resource 25`, `polarity 13`.
- Payload keys fora do schema: `alternative_cost`, `cost_constraints`, `damage_kind`, `destination`, `distribution`, `keywords`, `limit`, `multiplier`, `prevented_action`, `prevented_event`, `replacement`, `resource`, `restriction`, `scaling`, `source`, `stat`, `threshold`, `win_condition`.
- Payload key do schema nunca vista: `subject`.

## Shapes reais mais frequentes

| count | fact_type / predicate | payload keys |
| ---: | --- | --- |
| 1395 | `stat_change / has_stat` | `amounts`, `stat` |
| 849 | `identity_reference / has_domain` | `object` |
| 767 | `identity_reference / has_card_type` | `object` |
| 651 | `keyword_marker / has_keyword` | `object` |
| 339 | `event_trigger / observe_event` | `event`, `modality` |
| 169 | `activated_ability_cost / pay` | `costs`, `modality` |
| 101 | `card_flow / draw` | `amounts`, `modality`, `outputs` |
| 84 | `stat_change / modify_stat` | `amounts`, `duration`, `modality`, `outputs`, `target` |
| 74 | `damage / damage` | `amounts`, `event`, `modality`, `target` |
| 63 | `state_modifier / ready` | `modality`, `outputs`, `target` |
| 55 | `produced_event / attach` | `event`, `modality`, `object`, `outputs`, `target` |
| 44 | `movement / move` | `destination`, `event`, `location`, `modality`, `outputs`, `target` |

## Relacoes que assumem shape

- `semantic_relation_rules.json:90-98` assume selector por `payload.object.id == spell` para relacao ampla de counter.
- `build_card_relations.py:61-80` coleta qualquer chave recursiva chamada `event`; `84-89` so reconhece `payload.outputs[*].id`.
- `build_card_relations.py:120-172` assume `payload.costs[*].resource/amount/domain`, `payload.outputs[*]`, `payload.amounts[*]` e `payload.resource`.
- `build_card_relations.py:549-658` assume `target`, `destination`, `keywords`, `scaling`, `prevented_action`, `cost_constraints`, `amounts[0]`, `duration`, `modality`.
- `build_card_explorer_dataset.py:45-59` copia `web_uses`, mas nao o usa como gate; `219-233` gera filtros por eventos/outputs/predicados diretamente do payload.

## Achados

### Achado 1 - Schema de payload nao cobre o contrato real

- categoria do achado: arquitetura
- severidade: alta
- confianca: alta
- evidencia: `semantic_facts_schema.json:306-316` documenta payload generico, mas o corpus tem 18 chaves nao documentadas; exemplos: `Fizz` usa `cost_constraints` (`cards_semantic_facts.jsonl:1644`), `Zilean` usa `replacement` (`:5428`), `Volibear` usa `distribution` (`:5143`), `Elder Dragon` usa `threshold` (`:1376`).
- regra relacionada: `semantic_facts_schema.json`; `semantic_extraction_rules.json`.
- impacto provavel no produto final: novas regras podem gerar payloads que passam na auditoria estrutural, mas quebram ou somem em relacoes/filtros por falta de contrato por `fact_type/predicate`.
- recomendacao: formalizar shape por par `fact_type/predicate`, incluindo chaves extras hoje usadas.
- teste que deveria existir: validacao de payload por `fact_type/predicate`, falhando em chave desconhecida ou chave obrigatoria ausente.

### Achado 2 - Ontologia nao cobre enums aninhados usados nos fatos

- categoria do achado: integracao entre etapas
- severidade: media
- confianca: alta
- evidencia: top-level enums estao validos, mas payload aninhado tem `kind: tag` em `Ivern` e `The List` (`cards_semantic_facts.jsonl:2286`, `:4634`), enquanto `semantic_ontology.json:167` nao lista `tag`; `Lotus Trap` usa `stat: damage` (`:2729`), mas `semantic_ontology.json:188` nao lista `damage` como stat; locations livres como `anywhere`, `its base`, `top`, `your_base` nao estao em `zones` (`semantic_ontology.json:196`).
- regra relacionada: `semantic_ontology.json`.
- impacto provavel no produto final: filtros e chaves de similaridade podem fragmentar valores equivalentes ou aceitar texto bruto como enum.
- recomendacao: separar enums fechados de campos `raw/location_text`; adicionar `tag` ou modelar tag como entidade propria.
- teste que deveria existir: varredura recursiva de payload validando `kind`, `stat`, `zone/location` contra ontologia ou allowlist explicita de campos livres.

### Achado 3 - `source_ref` existe, mas a evidencia nem sempre ancora no `unit_text`

- categoria do achado: parsing/normalizacao
- severidade: media
- confianca: alta
- evidencia: 0 evidencias vazias e 0 refs de linha invalidas, mas 170 fatos de texto tem `evidence` que nao aparece no `source_ref.unit_text`; exemplos: `Ancient Henge` (`cards_semantic_facts.jsonl:108`), `Angle Shot` (`:126`), `Volibear` (`:5141`). `build_card_explorer_dataset.py:45-59` ainda remove `line_text/unit_text` do fato compacto.
- regra relacionada: `semantic_facts_schema.json:291-322`.
- impacto provavel no produto final: debugging no frontend e auditorias downstream perdem o atomo textual correto; fatos podem parecer ligados ao unit errado.
- recomendacao: exigir que `evidence` esteja em `unit_text`, ou declarar quando o fato usa a linha inteira/reminder text.
- teste que deveria existir: `for text facts: evidence in unit_text OR source_ref.scope == line_text/reminder`.

### Achado 4 - `web_uses` e decorativo e inconsistente com builders

- categoria do achado: integracao entre etapas
- severidade: media
- confianca: alta
- evidencia: todos os 5428 fatos possuem `web_uses`; combos: `3766 filters+similarity`, `656 deck_synergy+enables+filters+similarity`, `472 deck_synergy+enables+similarity`, `339 deck_synergy+enabled_by+filters+similarity`, `195 deck_synergy+filters+similarity`. Mas `build_card_relations.py` nao le `web_uses`; `build_card_explorer_dataset.py:59` apenas copia. Alem disso, 3662 fatos `identity_or_descriptor` dizem `similarity`, enquanto `semantic_relation_rules.json:143-158` e `build_card_relations.py:626-633` excluem esses fatos da similaridade.
- regra relacionada: `semantic_facts_schema.json:321`; `semantic_relation_rules.json`.
- impacto provavel no produto final: a UI pode exibir usos prometidos que os builders nao respeitam; mudancas em `web_uses` nao alteram relacoes.
- recomendacao: decidir se `web_uses` e contrato executavel ou metadado; se for contrato, usar como gate nos builders.
- teste que deveria existir: paridade entre `web_uses` e elegibilidade real em relations/dataset.

### Achado 5 - Shapes negativos e duplicados vazam como efeitos positivos downstream

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Mageseeker Warden` gera `restriction/prevent` para `can't ready` (`cards_semantic_facts.jsonl:2817`) e tambem `state_modifier/ready` positivo para a mesma frase (`:2818`). `Flash` e `Janna` geram dois movimentos para a mesma instrucao, incluindo alvo bruto `up` e `location` livre (`:1657-1658`, `:2316-2317`). `build_card_relations.py:549-675` transforma esses payloads em chaves de similaridade/filtros.
- regra relacionada: `semantic_extraction_rules.json:1769-1783`, `:1830-1845`; `semantic_relation_rules.json`.
- impacto provavel no produto final: cartas podem aparecer como sinergias/filtros de `ready` ou `move` quando o texto nega ou quando o segundo fato e parse residual.
- recomendacao: tornar `prevented_action` mutuamente exclusivo com output positivo do mesmo verbo; deduplicar fatos por `(play_id, source_ref, predicate, payload normalizado)`.
- teste que deveria existir: golden negativo para `Mageseeker Warden` e golden de dedupe para `Flash`/`Janna`.

## Invariantes/testes recomendados

1. Todo payload deve validar contra schema especifico de `(fact_type, predicate)`.
2. Chaves de payload fora do schema devem falhar, salvo `extensions` explicitamente versionado.
3. `web_uses` deve bater com elegibilidade real nos builders, ou ser removido do contrato executavel.
4. `identity_or_descriptor` nao deve declarar `similarity` se `semantic_relation_rules` o ignora.
5. `evidence` de fato textual deve estar em `source_ref.unit_text`, ou o fato deve declarar escopo de evidencia em linha inteira.
6. Valores recursivos `kind`, `stat`, `zone`, `location`, `resource`, `event.id`, `outputs.id` devem ser validados contra ontologia ou marcados como `raw`.
7. Fato com `prevented_action: X` nao pode coexistir no mesmo `source_ref` com output positivo `action/id` de `X`, salvo regra explicita de replacement.
8. `movement/move` deve exigir `target.kind` e destino normalizado; `target.raw == "up"` deve falhar.
9. Relacoes devem rejeitar fatos com `event_id/output_id` nulos quando o tipo de relacao depende deles.
10. Auditoria deve contar `broad` por motivo: hoje `spell_card_can_be_countered` sozinho gera 3438 relacoes broad.

