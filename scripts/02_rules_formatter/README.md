# Rules Formatter

Converte o PDF bruto das regras de Riftbound em formatos melhores para processamento por código e por LLMs.

## Uso

```bash
python scripts/02_rules_formatter/format_core_rules.py
```

Por padrão, o script lê:

```txt
data/raw/core-rules-20260330.pdf
```

E gera:

```txt
data/processed/rules/core-rules.md
data/processed/rules/core-rules.json
data/processed/rules/core-rules.chunks.jsonl
```

## Formatos

- `core-rules.md`: versão legível e versionável das regras.
- `core-rules.json`: lista estruturada de regras, com `id`, texto, páginas, regra pai e seção.
- `core-rules.chunks.jsonl`: blocos menores para busca semântica, embeddings e uso com LLMs.

## Opções

```bash
python scripts/02_rules_formatter/format_core_rules.py \
  --input data/raw/core-rules-20260330.pdf \
  --output-dir data/processed/rules \
  --max-chunk-chars 2400
```
