# Riftbound Card Explorer

Frontend estatico para explorar o dataset semantico atual.

## Rodar localmente

Na raiz do repo:

```bash
python -m http.server 4173 --bind 127.0.0.1
```

Abra:

```txt
http://127.0.0.1:4173/web/app/
```

O app carrega:

```txt
data/processed/web/card_explorer_index.json
data/processed/web/relations/*.json sob demanda
```

## Recursos atuais

- busca da carta foco na lateral, sem listagem fixa de cartas;
- estado inicial sem carta foco, com resumo do dataset;
- filtros por dominio, tipo, trigger, keyword, energy, might e modificador/predicado aplicados nas cartas relacionadas;
- detalhe da carta foco com texto e contadores de relacao high-signal e broad;
- marcador de variantes quando textos oficiais diferem entre impressoes;
- secoes de relacao high-signal controladas pelo manifest do dataset;
- cada relacao mostra reason/evidence compactos publicados nos shards;
- lane secundaria para broad matches, sem entrar na contagem principal;
- `deck_synergy` fica oculto por padrao quando o manifest marcar como experimental;
- modal de carta relacionada com acao explicita para ver suas relacoes;
- secoes minimizaveis quando o layout empilha em telas menores;
- `Clear` limpa filtros, busca, modal e volta ao estado inicial;
- layout responsivo com gaveta de filtros em telas pequenas.

Esta primeira versao nao depende de Node/NPM.
