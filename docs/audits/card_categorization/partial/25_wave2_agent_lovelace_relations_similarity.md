# Onda 2 - agente Lovelace - relation builder, similarity keys e broad/dedup

## Escopo

Auditoria nao mutante da onda 2 sobre relation builder, similarity keys, broad, dedup e resource synergy.

O agente informou que nao editou arquivos. O `git status --short` final continua com mudancas pre-existentes: `M goal.md` e `?? docs/`.

## Achados

### F1 - `similar_effect` usa chaves largas demais

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `build_card_relations.py:624` cria a chave sem carregar condicao, cardinalidade e escopo forte. Pares confirmados:
  - `Arena Kingpin <-> Breakneck Mech`: 2 `similar_effect` por `event:...enter_ready...required`; `Breakneck Mech` perde o `if you control another Mech`.
  - `Bellows Breath <-> Final Spark`: 2 `similar_effect` por `secondary:damage:positive:unit::required`; ignora `1 em ate tres unidades no mesmo local` vs `8 em uma unidade`.
  - `Abandon <-> Downwell`: 2 `similar_effect` por `return_to_hand:unit_recalled`; ignora `it`/spell countered vs `all units and gear`.
- regra relacionada: `similarity` em `semantic_relation_rules.json:139`.
- impacto provavel no produto final: a lane `similar effects` mistura cartas operacionalmente diferentes.
- recomendacao: incluir condicao (`if`, level, trigger), quantidade, alvo bruto/kinds, controlador e escopo na chave; rebaixar chaves secundarias que so preservam sinal/tipo.
- teste que deveria existir: goldens negativos para os tres pares acima.

### F2 - Broad de counter ainda domina graus e broad-only

- categoria do achado: integracao entre etapas
- severidade: alta
- confianca: alta
- evidencia: `spell_card_can_be_countered` esta marcado `broad: true`, mas ainda gera `enables`/`enabled_by` em `build_card_relations.py:245`. Relatorio: 3438 relacoes broad, 34,78% do grafo. `Acceptable Losses` tem 18 relacoes, todas broad, 0 high-signal. `Wind Wall` tem grau 410, sendo 398 broad e 12 high-signal.
- regra relacionada: `semantic_relation_rules.json:89`.
- impacto provavel no produto final: cartas sem sinergia real aparecem conectadas por counterabilidade generica.
- recomendacao: mover para tipo separado (`rules_interaction`/`counterability`) ou excluir de grau/ranking default.
- teste que deveria existir: broad-only cards nao devem contar como conectadas no ranking high-signal.

### F3 - `resource_synergy` confunde custo pagavel com reducao/citacao de custo

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `build_resource_synergy_relations` em `build_card_relations.py:426` liga qualquer produtor `cost:*` a `cost_or_requirement`. `Dragonsoul Sage -> Atakhan` sai como `deck_synergy cost:energy:1`, mas a evidencia alvo e `I cost 1 less...`, ou seja, reducao de custo, nao custo pagavel. `resource_synergy` totaliza 415 relacoes; `cost:energy:1` sozinho gera 348.
- regra relacionada: `semantic_relation_rules.json:125`.
- impacto provavel no produto final: geradores de recurso viram sinergia com reducers e textos que so mencionam custo.
- recomendacao: separar `pay_cost`, `additional_cost`, `activated_cost` e `cost_reduction`; resource synergy deve mirar so custos consumiveis.
- teste que deveria existir: `Dragonsoul Sage` nao deve ligar a `Atakhan`/`Vex, Cheerless` por `cost:energy:1`.

### F4 - `derived_synergy` duplica regras especificas e genericas

- categoria do achado: integracao entre etapas
- severidade: media-alta
- confianca: alta
- evidencia: `build_enables_synergy_relations` em `build_card_relations.py:395` transforma todo `enables` em `deck_synergy`; `dedupe_relations` em `build_card_relations.py:792` deduplica so por `relation_id`. `Atakhan <-> Altar of Memories` tem 6 relacoes: `friendly_unit_dies` e `generic_unit_death` aparecem tanto como `enables/enabled_by` quanto como `deck_synergy`. A generica usa o fato de Atakhan `kill one of their units` com `controller: opponent` contra o trigger `friendly unit dies`.
- regra relacionada: `derived_synergy` em `semantic_relation_rules.json:132`.
- impacto provavel no produto final: o mesmo par recebe peso artificial e, em alguns casos, controller leakage.
- recomendacao: dedupe por par + familia semantica + trigger alvo, preferindo regra especifica; nao derivar synergy de regra generica quando ja ha regra especifica compativel.
- teste que deveria existir: `Atakhan -> Altar of Memories` deve manter so a interacao especifica de friendly death.

### F5 - Fatos bons ainda ficam isolados por falta de familia de relacao

- categoria do achado: regra ausente
- severidade: media
- confianca: alta
- evidencia: `Ahri, Inquisitive` tem 3 fatos relacionais bons (`modify_stat -2 might`, triggers `self_attacks` e `self_defends`) e grau 0. O quality report mostra 100 cartas sem relacao e 736 candidate facts nao ligados.
- regra relacionada: lacuna entre `similarity` e `event_enables`.
- impacto provavel no produto final: cartas com modificadores condicionais uteis somem do grafo.
- recomendacao: adicionar familia para modificadores acionados por ataque/defesa, com sinal, controlador, localizacao e duracao.
- teste que deveria existir: `Ahri, Inquisitive` deve gerar pelo menos similaridade/deck relation high-signal com debuffs condicionais equivalentes.

## Comandos e validacoes

- `git status --short`
- `Get-ChildItem -Recurse` para localizar scripts, contratos, JSON/JSONL e relatorios web.
- `Get-Content` nos contratos, builder e reports.
- `rg -n` para linhas de funcoes/regras.
- Consulta Python somente leitura sobre `cards_normalized.json`, `cards_semantic_facts.jsonl`, `cards_card_relations.jsonl` e reports.

O agente nao rodou builders/auditors que escrevem saida. Validacoes read-only conferiram: 767 cartas, 5428 fatos, 9884 relacoes; tipos `similar_effect=4746`, `enabled_by=2041`, `enables=2041`, `deck_synergy=1056`; pares concretos acima extraidos diretamente do JSONL.
