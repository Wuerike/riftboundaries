# Etapa 4: Extracao Semantica de Cartas

Esta etapa transforma o texto normalizado das cartas em fatos semanticos e relacoes entre cartas. Tudo aqui ainda esta em desenvolvimento; nao existe divisao entre versoes antigas e novas dentro do fluxo atual.

Fonte base:

```text
data/processed/cards/normalized/cards_normalized.json
```

## Fluxo Atual

```text
cards_normalized.json
  -> inventory_text_patterns.py
  -> cards_text_inventory.json/md
  -> feature_relation_taxonomy.json
  -> align_inventory_taxonomy.py
  -> cards_taxonomy_alignment.json/md
  -> semantic_ontology.json
  -> semantic_extraction_rules.json
  -> semantic_relation_rules.json
  -> semantic_quality_policy.json
  -> semantic_facts_schema.json + semantic_golden_examples.json
  -> validate_semantic_contracts.py
  -> extract_semantic_facts.py
  -> cards_semantic_facts.jsonl + cards_semantic_facts_report.json
  -> validate_semantic_golden_examples.py
  -> cards_semantic_golden_report.json
  -> audit_semantic_facts.py
  -> cards_semantic_audit_report.json/md
  -> build_card_relations.py
  -> cards_card_relations.jsonl + cards_card_relations_report.json/md
  -> scripts/05_web_dataset/build_card_explorer_dataset.py
  -> scripts/05_web_dataset/audit_card_explorer_dataset.py
```

Cada recurso existe para alimentar o proximo. O inventario descobre a linguagem real das cartas; a taxonomia define o contrato semantico desejado; o alinhamento mostra onde ha maior valor de modelagem; o extractor gera fatos; os auditores validam qualidade; as relacoes e o dataset web tornam esses fatos navegaveis.

## 1. Inventario de Texto

Script:

```text
scripts/04_cards_feature_extraction/inventory_text_patterns.py
```

Inputs:

```text
data/processed/cards/normalized/cards_normalized.json
```

Outputs:

```text
data/processed/cards/inventory/cards_text_inventory.json
data/processed/cards/inventory/cards_text_inventory.md
```

Responde: "Que linguagem existe nas cartas?"

O inventario levanta linhas e unidades de texto com normalizacao, frequencia, cartas exemplo, campos de origem, flags superficiais e familias candidatas heuristicas. Ele nao gera fatos finais; ele aponta onde a linguagem recorrente merece modelagem deterministica.

Comando:

```powershell
python scripts/04_cards_feature_extraction/inventory_text_patterns.py
```

## 2. Taxonomia Semantica

Arquivo:

```text
scripts/04_cards_feature_extraction/contracts/feature_relation_taxonomy.json
```

Responde: "Quais papeis, eixos e usos web precisamos representar?"

A taxonomia e um contrato semantico revisado. Ela agrupa familias do inventario em papeis como `event_produced`, `trigger_observed`, `payoff_output`, `cost_or_requirement`, `restriction_or_permission`, `state_or_modifier`, `targeting_or_scope` e `identity_or_descriptor`.

Ela tambem indica:

- `semantic_axes`: dimensoes como action, object, event, cost, target, location, stat, keyword e duration.
- `semantic_targets`: areas de linguagem que devem virar regras de extracao verificaveis.
- `family_mappings`: como cada familia candidata do inventario conversa com papeis, eixos, alvos semanticos e usos web.

Este arquivo pode ser revisado manualmente ou com ajuda de LLM, mas deve continuar pequeno, explicito e orientado ao contrato. Ele nao deve virar uma lista grande de aliases ou regexes.

## 3. Alinhamento Inventario -> Taxonomia

Script:

```text
scripts/04_cards_feature_extraction/align_inventory_taxonomy.py
```

Inputs:

```text
data/processed/cards/inventory/cards_text_inventory.json
scripts/04_cards_feature_extraction/contracts/feature_relation_taxonomy.json
```

Outputs:

```text
data/processed/cards/inventory/cards_taxonomy_alignment.json
data/processed/cards/inventory/cards_taxonomy_alignment.md
```

Responde: "Onde a linguagem real das cartas encosta na taxonomia, e o que devemos modelar primeiro?"

Como analisar:

- `summary`: cobertura geral de familias e unidades mapeadas.
- `family_alignment`: familias ordenadas por prioridade, frequencia e papeis.
- `semantic_target_summary`: areas de linguagem com maior pressao de modelagem.
- `semantic_target_seed_groups`: frases parametrizadas que podem virar regras de extracao.
- `top_high_priority_units`: unidades que combinam frequencia e impacto para a plataforma.
- `web_readiness`: leitura rapida de cobertura para enablement, similaridade e deck synergy.

Comando:

```powershell
python scripts/04_cards_feature_extraction/align_inventory_taxonomy.py
```

## 4. Schema de Fatos Semanticos

Arquivo:

```text
scripts/04_cards_feature_extraction/contracts/semantic_facts_schema.json
```

Responde: "Qual e o formato dos fatos que o frontend e as relacoes podem consumir?"

O schema define o contrato de `cards_semantic_facts.jsonl`: campos obrigatorios, papeis semanticos, tipos de fato, eventos canonicos, outputs canonicos, acoes canonicas e regras minimas de qualidade.

Um fato semantico deve representar uma unidade de significado rastreavel: um trigger, evento produzido, payoff, custo, restricao, modificador, alvo/escopo ou identidade.

## 4.1 Contratos JSON de Runtime

Arquivos:

```text
scripts/04_cards_feature_extraction/contracts/semantic_ontology.json
scripts/04_cards_feature_extraction/contracts/semantic_extraction_rules.json
scripts/04_cards_feature_extraction/contracts/semantic_relation_rules.json
scripts/04_cards_feature_extraction/contracts/semantic_quality_policy.json
scripts/04_cards_feature_extraction/contracts/semantic_contracts_schema.json
```

Responde: "Onde o conhecimento semantico que cresce com o jogo deve morar?"

Esses contratos concentram o conhecimento de dominio que antes crescia dentro dos scripts:

- `semantic_ontology.json`: IDs canonicos de roles, fact types, actions, events, outputs, entidades, recursos, stats, zonas, relation types e web uses.
- `semantic_extraction_rules.json`: regras deterministicas de extracao por regex, guard e template de fatos.
- `semantic_relation_rules.json`: regras deterministicas para enables, enabled_by, similar_effect e deck_synergy.
- `semantic_quality_policy.json`: politica de auditoria, keywords relacionais, buckets de blind spot, thresholds de broad relation e allowlist temporaria de vazamento legado.
- `semantic_contracts_schema.json`: descricao do formato esperado desses contratos.

Scripts devem funcionar como parsers/motores desses contratos. Ao modelar conhecimento novo do jogo, prefira atualizar os JSONs e os golden examples antes de alterar Python.

Altere Python quando a mudanca for uma capacidade programatica reaproveitavel, por exemplo um builder novo que interpreta uma familia de regras, uma chave de similaridade mais precisa ou uma melhoria de auditoria. Nesses casos, mantenha a semantica concreta nos contratos e use exemplos dourados para fixar comportamento.

Validador:

```powershell
python scripts/04_cards_feature_extraction/validate_semantic_contracts.py
```

## 5. Exemplos Dourados

Arquivo:

```text
scripts/04_cards_feature_extraction/contracts/semantic_golden_examples.json
scripts/04_cards_feature_extraction/contracts/semantic_regression_invariants.json
```

Responde: "Quais fatos minimos precisamos extrair em cartas reais representativas?"

Os exemplos dourados nao sao parses completos das cartas. Eles sao checkpoints minimos para impedir regressao em padroes importantes.

`semantic_regression_invariants.json` complementa os exemplos positivos com fatos proibidos, invariantes de broad/dedupe e paridade do manifest do dataset web. Falhas nesse arquivo indicam regressao mesmo quando os fatos minimos continuam presentes.

Validador:

```text
scripts/04_cards_feature_extraction/validate_semantic_golden_examples.py
```

Comando:

```powershell
python scripts/04_cards_feature_extraction/validate_semantic_golden_examples.py
```

Output:

```text
data/processed/cards/semantic/cards_semantic_golden_report.json
```

## 6. Extrator de Fatos Semanticos

Script:

```text
scripts/04_cards_feature_extraction/extract_semantic_facts.py
```

Inputs:

```text
data/processed/cards/normalized/cards_normalized.json
data/processed/cards/inventory/cards_text_inventory.json
scripts/04_cards_feature_extraction/contracts/feature_relation_taxonomy.json
data/processed/cards/inventory/cards_taxonomy_alignment.json
scripts/04_cards_feature_extraction/contracts/semantic_ontology.json
scripts/04_cards_feature_extraction/contracts/semantic_extraction_rules.json
scripts/04_cards_feature_extraction/contracts/semantic_facts_schema.json
```

Outputs:

```text
data/processed/cards/semantic/cards_semantic_facts.jsonl
data/processed/cards/semantic/cards_semantic_facts_report.json
```

Responde: "Quais fatos semanticos extraimos das cartas?"

O extractor e deterministico. Ele deve continuar trabalhando a partir do texto normalizado, inventario, taxonomia, alinhamento, ontologia, regras de extracao e schema. Ao adicionar uma regra nova, prefira:

1. confirmar que a linguagem aparece no inventario;
2. conferir o papel dela na taxonomia;
3. adicionar ou ajustar exemplo dourado quando o risco for alto;
4. implementar uma regra pequena e rastreavel;
5. regenerar fatos, validar exemplos e rodar auditoria.

Comando:

```powershell
python scripts/04_cards_feature_extraction/extract_semantic_facts.py
```

## 7. Auditoria Semantica

Script:

```text
scripts/04_cards_feature_extraction/audit_semantic_facts.py
```

Inputs:

```text
data/processed/cards/normalized/cards_normalized.json
data/processed/cards/semantic/cards_semantic_facts.jsonl
data/processed/cards/semantic/cards_semantic_facts_report.json
scripts/04_cards_feature_extraction/contracts/semantic_facts_schema.json
scripts/04_cards_feature_extraction/contracts/semantic_golden_examples.json
scripts/04_cards_feature_extraction/contracts/semantic_ontology.json
scripts/04_cards_feature_extraction/contracts/semantic_quality_policy.json
data/processed/cards/inventory/cards_taxonomy_alignment.json
```

Outputs:

```text
data/processed/cards/semantic/cards_semantic_audit_report.json
data/processed/cards/semantic/cards_semantic_audit_report.md
```

Responde: "A extracao semantica esta boa o suficiente para alimentar relacoes?"

O auditor mede cobertura, evidencias, fatos ambiguos, eventos sem par e lacunas de linguagem prioritaria. Se ele mostrar erro estrutural, corrija o extractor antes de gerar relacoes.

Comando:

```powershell
python scripts/04_cards_feature_extraction/audit_semantic_facts.py
```

## 8. Relacoes Entre Cartas

Script:

```text
scripts/04_cards_feature_extraction/build_card_relations.py
```

Inputs:

```text
data/processed/cards/semantic/cards_semantic_facts.jsonl
scripts/04_cards_feature_extraction/contracts/semantic_facts_schema.json
scripts/04_cards_feature_extraction/contracts/semantic_ontology.json
scripts/04_cards_feature_extraction/contracts/semantic_relation_rules.json
scripts/04_cards_feature_extraction/contracts/semantic_quality_policy.json
```

Outputs:

```text
data/processed/cards/relations/cards_card_relations.jsonl
data/processed/cards/relations/cards_card_relations_report.json
data/processed/cards/relations/cards_card_relations_report.md
```

Responde: "Quais cartas se habilitam, sao habilitadas ou parecem cumprir papeis parecidos?"

As relacoes sao derivadas dos fatos semanticos. Elas devem evitar inferencias soltas: cada relacao precisa carregar evidencia, score, razao e chaves semanticas usadas.

O builder tambem separa relacoes amplas de relacoes de alto sinal. Chaves de similaridade devem incluir contexto quando ele muda a leitura da carta, como trigger da clausula, alvo, destino, zona, keyword concedida, escala por recurso, custos e requisitos de estado. Se uma carta continua isolada mesmo com fatos bons, a decisao correta costuma ser criar uma familia de relacao precisa, nao forcar uma relacao generica.

Comando:

```powershell
python scripts/04_cards_feature_extraction/build_card_relations.py
```

## 9. Feedback Loop

Use os reports nessa ordem:

1. `cards_text_inventory.md`: descobrir linguagem recorrente ainda nao modelada.
2. `cards_taxonomy_alignment.md`: decidir quais familias e alvos semanticos priorizar.
3. `cards_semantic_golden_report.json`: bloquear regressao nos exemplos dourados.
4. `cards_semantic_audit_report.md`: encontrar lacunas, ambiguidade e eventos sem par.
5. `cards_card_relations_report.md`: avaliar se as relacoes ficaram uteis para a plataforma.
6. `card_explorer_dataset_report.md`: garantir que o frontend recebeu o contrato esperado.
7. `card_explorer_quality_report.md`: auditar isolamento, broad-only, hubs artificiais e fatos que nao viraram relacao.

## Prompt Para Revisar a Taxonomia Com LLM

Use quando quiser atualizar `feature_relation_taxonomy.json` a partir dos dados atuais.

```text
Quero revisar a taxonomia semantica de cartas de Riftbound.

Objetivo final:
- gerar fatos semanticos deterministas;
- derivar relacoes enables, enabled_by, similar_effect e deck_synergy;
- alimentar filtros por dominio, trigger, custo, stats, keywords, acoes, eventos e modificadores.

Arquivos de contexto:
- data/processed/cards/inventory/cards_text_inventory.json
- data/processed/cards/inventory/cards_text_inventory.md
- data/processed/cards/inventory/cards_taxonomy_alignment.json
- data/processed/cards/inventory/cards_taxonomy_alignment.md
- scripts/04_cards_feature_extraction/contracts/feature_relation_taxonomy.json
- scripts/04_cards_feature_extraction/contracts/semantic_facts_schema.json
- scripts/04_cards_feature_extraction/contracts/semantic_golden_examples.json

Tarefa:
1. Analise as familias candidatas e unidades mais frequentes do inventario.
2. Compare com os papeis, eixos, semantic_targets e web_uses da taxonomia.
3. Aponte familias mal mapeadas, duplicadas ou vagas.
4. Sugira ajustes pequenos e justificaveis no JSON.
5. Nao transforme a taxonomia em lista de regexes.
6. Nao afirme semantica que a evidencia das cartas nao sustenta.

Schema esperado:
{
  "version": "YYYY-MM-DD",
  "purpose": "string",
  "web_goals": ["string"],
  "relation_roles": {
    "role_id": "description"
  },
  "semantic_axes": {
    "axis_id": "description"
  },
  "semantic_targets": {
    "target_id": "description"
  },
  "family_mappings": {
    "inventory_family_id": {
      "roles": ["role_id"],
      "axes": ["axis_id"],
      "semantic_targets": ["target_id"],
      "web_uses": ["filters|similarity|enables|deck_synergy"],
      "priority": "high|medium|low",
      "notes": "string"
    }
  },
  "open_questions": ["string"]
}
```

## Prompt Para Revisar o Schema Com LLM

```text
Quero revisar o contrato de fatos semanticos de Riftbound.

Objetivo:
- fatos deterministas, rastreaveis por evidencia;
- boa base para relacoes entre cartas;
- util para filtros, similaridade e analise de deck.

Arquivos:
- scripts/04_cards_feature_extraction/contracts/semantic_facts_schema.json
- scripts/04_cards_feature_extraction/contracts/semantic_ontology.json
- scripts/04_cards_feature_extraction/contracts/semantic_extraction_rules.json
- scripts/04_cards_feature_extraction/contracts/semantic_relation_rules.json
- scripts/04_cards_feature_extraction/contracts/semantic_quality_policy.json
- scripts/04_cards_feature_extraction/contracts/semantic_golden_examples.json
- data/processed/cards/semantic/cards_semantic_facts_report.json
- data/processed/cards/semantic/cards_semantic_audit_report.md
- data/processed/cards/relations/cards_card_relations_report.md
- data/processed/web/card_explorer_quality_report.md
- data/processed/cards/inventory/cards_taxonomy_alignment.md
- data/processed/cards/inventory/cards_text_inventory.md

Tarefa:
1. Identifique campos ausentes para representar triggers, custos, recursos, eventos produzidos, payoffs e modificadores.
2. Avalie se os eventos e outputs canonicos cobrem a linguagem recorrente.
3. Sugira mudancas pequenas no schema, com impacto esperado no extractor e nas relacoes.
4. Preserve rastreabilidade: todo fato precisa de evidencia e source_ref.
5. Evite campos que dependam de julgamento subjetivo sem evidencia textual.
```

## Estado Atual e Proximos Ganhos

- Estado atual da rodada: `6311` fatos, `14590` relacoes, `73/73` exemplos dourados, `90` fixtures de regressao, `119` fatos esperados, `51` fatos proibidos, `46` expectativas de relacao, `16` invariantes de relacao, `6` invariantes de dataset, regressions/invariantes verdes, `0` erros e `179` warnings na auditoria semantica.
- A auditoria final do frontend esta em `data/processed/web/card_explorer_quality_report.md`.
- Relacoes high-signal: `9701`; relacoes broad: `4889`; cartas broad-only: `0`; cartas sem relacao: `42`.
- Broad reasons atuais: `spell_card_can_be_countered` e `cost:rune:any`; ambos devem ficar fora da ordenacao principal do frontend.
- O dataset web publica contadores separados de `relation_count`, `high_signal_relation_count`, `broad_relation_count`, `broad_only`, `cards_with_rule_variants` e snapshot datado com thresholds.
- A auditoria web separa `501` fatos candidatos sem relacao em `220` `needs_relation_rule`, `1` `needs_extraction_fix`, `269` `intentional_ignored` e `11` `weak_fact`; os casos restantes priorizam regras precisas para keyword references, custos/zonas, stats, ready, replacement e card flow. A rodada tambem cobre recursos `[Add]`, skips auditaveis de similaridade generica, familias de prevent/replacement/swap/score, separacao de keyword intrinseca/grant/referencia, triggers de conquista/hold do jogador, evidencia de relacoes no dataset e manifest explicito para o frontend.
- As cartas restantes sem relacao estao concentradas em `missing_relation_rule`, `weak_fact` e texto pouco relacional. Priorize novas familias precisas para custo/zonas, card flow, score/replacement e efeitos que ainda aparecem como fatos bons sem relacao.
- Nao use o objetivo "zerar isolamento" como criterio isolado. Uma relacao nova precisa ser mais informativa do que compartilhar um verbo generico.
- Aumentar exemplos dourados em cartas-chave para triggers, custos, keywords concedidas, zonas e efeitos de substituicao.
- Ligar fatos semanticos a regras oficiais em `data/processed/rules/core-rules.json`.
- Melhorar o frontend conforme novos fatos e relacoes ficarem mais expressivos.
