# Onda 4 - falsos positivos de relacoes

Auditoria somente leitura. O agente leu os artefatos solicitados e amostrou relacoes diretamente de `cards_card_relations.jsonl`, cruzando com fatos semanticos e cards normalizados. Nao editou arquivos.

## Achados priorizados

### P0 - `spell_card_can_be_countered` domina o grafo e deve ser filtrado como broad

- regra: `scripts/04_cards_feature_extraction/contracts/semantic_relation_rules.json:89`
- geracao: `scripts/04_cards_feature_extraction/build_card_relations.py:245`
- severidade: alta
- confianca: alta

O relatorio mostra `spell_card_can_be_countered: 3438`, sendo o unico broad reason registrado. Isso representa `34.8%` das `9884` relacoes.

| Relacao | Evidencia | Problema |
|---|---|---|
| `Abandon -> Defy`, `enables` | fonte: `spell`; alvo: `Counter a spell that costs...` | A evidencia so diz que Abandon e spell. Isso e vulnerabilidade/interacao ampla, nao sinergia util. |
| `Abandon -> Flurry of Feathers`, `enables` | fonte: `spell`; alvo: `Counter a spell` | Justifica "pode ser alvo", mas nao "habilita" no sentido de deckbuilding. |
| `Abandon -> Acceptable Losses`, `enabled_by` | fonte: `Counter a spell`; alvo: `spell` | A direcao fica semanticamente confusa no explorer: o counter aparece como enabled by qualquer spell. |

Impacto no explorer web: `web/app/app.js` exibe `enabled_by`, `enables` e `similar_effect` sem filtrar broad. Assim, spells e counterspells viram hubs artificiais. O relatorio web ja acusa `cards_with_only_broad_relations: 22` e broad reason `spell_card_can_be_countered: 3438`.

Recomendacao: excluir broad relations por padrao do explorer, ou mover para uma categoria separada como "can interact with / can be countered", nao `enables`.

### P1 - `similar_effect` ainda cria falsos positivos por chaves genericas

- regra: `scripts/04_cards_feature_extraction/build_card_relations.py:624`, `scripts/04_cards_feature_extraction/build_card_relations.py:690`
- severidade: alta
- confianca: alta

| Relacao | Reason | Avaliacao |
|---|---|---|
| `Abandon -> Downwell` | `output:...return_to_hand:unit_recalled...required` | Fraco. Abandon retorna "it" apos counter; Downwell retorna todas unidades e gear. Mesmo verbo, contexto e alvo diferentes. |
| `Abandon -> Factory Recall` | mesma chave `return_to_hand` | Fraco. Spell counter bounce vs retorno de gear. |
| `Bellows Breath -> Final Spark` | `secondary:damage:positive:unit::required` | Broad demais. Agrupa dano 1 multi-alvo com dano 8 a uma unidade. |
| `Falling Star -> Icathian Rain` | mesma chave damage | Aparece ate 12 vezes para o mesmo par+reason por multiplos fatos. |
| `Bloodharbor Ripper -> Seal of Focus` | `resource_added:1:rune` | Conflui rune rainbow e rune especifica como similar effect. |

Impacto: hubs de similaridade ficam bons para "mesma familia verbal", mas ruins para recomendacoes finas. O explorer ordena por strength e mostra ate 40 por lane; esses falsos positivos competem com relacoes melhores.

Recomendacao: incluir alvo, escopo e amount em chaves secundarias de damage; diferenciar `rainbow` de runas especificas; deduplicar por `(source_card, target_card, relation_type, reason)` para visualizacao.

### P1 - `resource_synergy` mistura custo real, custo opcional e restricao `cost no more than`

- regra: `scripts/04_cards_feature_extraction/build_card_relations.py:426`
- severidade: alta
- confianca: alta

| Relacao | Evidencia | Problema |
|---|---|---|
| `Dragonsoul Sage -> Ancient Warmonger` | `[Add] :rb_energy_1:` -> `[Accelerate] You may pay :rb_energy_1...` | Parcialmente valido, mas e custo opcional, nao custo base. |
| `Lux, Crownguard -> Rell, Magnetic` | `[Add] :rb_energy_2:` -> `play an Equipment with Energy cost no more than :rb_energy_2:` | Falso positivo provavel: `:rb_energy_2:` e limite de custo do alvo, nao pagamento. |
| `Lux, Crownguard -> Undying Loyalty` | `[Add] :rb_energy_2:` -> `Play a unit with cost no more than :rb_energy_2...` | Mesmo problema: restricao de selecao, nao custo pago. |
| `Seal of Strength -> Akshan, Mischievous` | `[Add] :rb_rune_body:` -> `pay :rb_rune_body::rb_rune_body:` | A saida de 1 rune casa com custo de 2 runes sem modelar insuficiencia parcial. |

Impacto: quando `deck_synergy` for exposto, geradores de recurso virarao hubs muito fortes. Hoje `deck_synergy` existe no dataset, mas nao e mostrado em `RELATION_TYPES` no app, entao o risco esta latente.

Recomendacao: separar `cost_payment`, `additional_cost`, `optional_cost`, `cost_cap_constraint` e `cost_reduction`. `resource_synergy` deveria casar apenas com pagamentos reais, com pontuacao menor para pagamento parcial.

### P2 - `derived_synergy` duplica `enables` sem nova evidencia

- regra: `scripts/04_cards_feature_extraction/build_card_relations.py:395`
- severidade: media-alta
- confianca: alta

| Relacao derivada | Evidencia | Observacao |
|---|---|---|
| `Abandon -> Karma, Channeler` | `You may recycle it` -> `When you recycle...` | E a mesma justificativa da relacao `enables`; `deck_synergy` so replica com strength menor. |
| `Adaptatron -> Mistfall` | `buff me` -> `When you buff a friendly unit` | Valida como enables; duplicada como synergy. |
| `Annie, Stubborn -> Lux, Illuminated` | `play me, return a spell...` -> `When you play a spell` | O parser parece capturar `play me` como `spell_played`, gerando sinergia suspeita. |

Tambem ha duplicatas por multiplos fatos: `Peak Guardian -> Mistfall` aparece 4 vezes como `enables` e 4 vezes como `deck_synergy`.

Impacto: se o explorer passar a mostrar `deck_synergy`, ele vai repetir recomendacoes ja presentes em `enables`, inflando contagens e rankings.

## Testes recomendados

1. Teste que `spell_card_can_be_countered` fica marcado `broad=true` e nao entra nas lanes padrao do explorer.
2. Golden tests para direcao de `enables/enabled_by` em counterspell: spell nao deve parecer sinergizar com todo counter.
3. Teste de `resource_synergy` distinguindo pagamento real de `cost no more than`.
4. Teste de custo parcial: gerar 1 rune nao deve ter a mesma forca contra custo de 2+ runes.
5. Teste de similaridade damage incluindo amount e target cardinality.
6. Teste de dedupe por par de cartas no payload web, preservando multiplas evidencias apenas como detalhes.

## Comandos usados

```powershell
Get-ChildItem -Force
rg --files
git status --short
Get-Content data\processed\cards\relations\cards_card_relations_report.md -TotalCount 240
Get-Content scripts\04_cards_feature_extraction\build_card_relations.py -TotalCount 260
Get-Content scripts\04_cards_feature_extraction\contracts\semantic_relation_rules.json -TotalCount 260
Get-Content scripts\04_cards_feature_extraction\contracts\feature_relation_taxonomy.json -TotalCount 260
Get-Content data\processed\cards\relations\cards_card_relations.jsonl -TotalCount 5
Get-Content data\processed\cards\semantic\cards_semantic_facts.jsonl -TotalCount 5
Get-Content data\processed\cards\normalized\cards_normalized.json -TotalCount 80
rg -n "def build_identity_event_relations|def build_resource_synergy_relations|def build_enables_synergy_relations|def build_similar_effect_relations|def similar_key|def secondary_similar_keys|spell_card_can_be_countered|broad_relation_count_threshold|max_similar_facts_per_key|broad_key_markers" scripts\04_cards_feature_extraction data\processed\cards\relations\cards_card_relations_report.md data\processed\web\card_explorer_dataset_report.md
```

Tambem foram usados scripts Python somente leitura via stdin para agregar contagens e amostrar pares dos JSON/JSONL.
