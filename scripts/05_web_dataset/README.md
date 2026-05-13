# Web Dataset

Esta etapa monta um contrato simples para o frontend consumir os artefatos semanticos atuais sem precisar juntar varios JSONL em runtime.

## Fluxo

```txt
data/processed/cards/normalized/cards_normalized.json
data/processed/cards/semantic/cards_semantic_facts.jsonl
data/processed/cards/relations/cards_card_relations.jsonl
  -> build_card_explorer_dataset.py
  -> data/processed/web/card_explorer_index.json
  -> data/processed/web/relations/*.json
  -> data/processed/web/facts/*.json
  -> data/processed/web/card_explorer_dataset_report.json/md
  -> audit_card_explorer_dataset.py
  -> data/processed/web/card_explorer_quality_report.json/md
```

O dataset inclui:

- cartas normalizadas com texto, custos, stats, dominios, tipos, tags e imagens;
- facts compactos separados em shards para detalhe/debug futuro;
- indice de cartas com filtros, contadores e caminho do shard de relacoes;
- relacoes compactas em shards por carta para `enables`, `enabled_by`, `similar_effect` e `deck_synergy`;
- manifest de `relation_types`, labels, visibilidade padrao, politica broad e campos obrigatorios;
- contadores separados de relacoes totais, high-signal, broad e `broad_only`;
- aviso persistente para cartas com `rule_variants`, indicando que os fatos usam o texto primario normalizado;
- opcoes de filtro com contagens;
- indice de busca textual basico;
- relatorio de tamanho dos artefatos, cobertura e distribuicao.

## Auditoria de Qualidade

Depois de gerar o dataset, rode:

```powershell
python scripts/05_web_dataset/audit_card_explorer_dataset.py
```

A auditoria parte do contrato final do front e gera um baseline de confianca das relacoes:

- distribuicao de grau do grafo por carta e por tipo de relacao;
- hubs e razoes amplas que dominam o grafo;
- cartas sem relacao, cartas com apenas relacoes amplas e linhas relacionais sem fatos;
- matriz de fatos candidatos nao usados por relacao, classificada como `needs_relation_rule`, `needs_extraction_fix`, `intentional_ignored` ou `weak_fact`;
- subconjunto acionavel dessa matriz, excluindo triggers contextuais marcados como `intentional_ignored`;
- amostras priorizadas para revisao humana;
- backtrace por carta amostrada, ligando texto original, fatos extraidos e relacoes geradas.

## Estado Atual

Ultima rodada regenerada:

- `767` cartas no dataset final;
- `6311` fatos semanticos;
- `14590` relacoes;
- `9701` relacoes de alto sinal;
- `4889` relacoes broad;
- `42` cartas sem relacao;
- `0` cartas apenas com relacoes broad;
- `44` cartas com variantes de texto sinalizadas;
- `0` cartas com linhas relacionais descobertas pelo auditor sem fato.
- `501` fatos candidatos sem relacao, dos quais `232` seguem acionaveis apos separar `269` skips amplos/contextuais como `intentional_ignored`;
- `220` fatos acionaveis classificados como `needs_relation_rule`, alem de `1` `needs_extraction_fix` e `11` `weak_fact`.

O snapshot publicado e `2026-05-13`. O manifest do dataset declara `relation_types`, politica broad, campos obrigatorios por tipo, thresholds e fontes usadas para gerar o artefato.

Os broad reasons atuais sao `spell_card_can_be_countered` e `cost:rune:any`. Eles sao uteis para auditoria e descoberta secundaria, mas nao entram na lane high-signal padrao do front.

Quando o relatorio mostrar cartas isoladas com fatos bons, o proximo passo e revisar `semantic_relation_rules.json` ou as chaves programaticas de similaridade. Quando mostrar linhas sem fatos ou fatos fracos, volte para `semantic_extraction_rules.json`, `semantic_ontology.json`, `semantic_facts_schema.json` e exemplos dourados.
