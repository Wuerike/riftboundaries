# Cards Formatter

Normaliza o JSON bruto oficial das cartas de Riftbound para um formato mais simples de consumir por codigo.

Esta etapa nao extrai acoes, zonas, mecanicas, estrategias ou relacoes entre cartas. Ela apenas limpa, agrupa e achata os dados oficiais.

## Uso

```bash
python scripts/03_cards_formatter/normalize_cards.py
```

Por padrao, o script le:

```txt
data/raw/cards.json
```

E gera:

```txt
data/processed/cards/normalized/cards_normalized.json
```

## O que e normalizado

- campos camelCase viram snake_case;
- impressoes sao agrupadas por uma assinatura jogavel, nao apenas por nome;
- a assinatura usa `name`, `domain_ids`, `card_type_ids`, `supertype_ids`, `energy`, `might`, `power` e `might_bonus`;
- o corpo da carta usa a descricao mais rica disponivel entre as impressoes;
- variantes, reprints, promo cards e artes alternativas ficam em `printings`;
- o identificador da carta jogavel fica em `play_id`;
- a assinatura usada para gerar o `play_id` fica em `signature`;
- ids, numeros de colecao e codigos publicos das impressoes ficam em `printing_ids`, `collector_numbers` e `public_codes`;
- cada impressao usa `printing_id`, evitando ambiguidade com `play_id`;
- entidades com `id`/`label` viram `{ "id": ..., "name": ... }`;
- arrays como `domains`, `card_types`, `supertypes` e `illustrators` continuam como arrays;
- HTML de regras e efeitos mais ricos e preservado em `rules_html`/`effect_html`;
- texto limpo e gerado em `rules_text`, `rules_lines`, `effect_text` e `effect_lines`;
- imagens ficam dentro de cada item de `printings`;
- cada impressao mantem `raw_refs` com origem e indice no arquivo bruto;
- quando existem textos de regra diferentes entre impressoes, eles ficam preservados em `rule_variants`;
- `printings` guarda apenas metadados de impressao: ids, codigo publico, set, raridade, orientacao, imagem, ilustradores e `raw_refs`.
