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

`/web/` redireciona para `/web/app/`.

O app carrega:

```txt
data/processed/web/card_explorer_index.json
data/processed/web/relations/*.json sob demanda
```

## Recursos atuais

- tabela densa como experiencia oficial, ordenada por codigo da carta no set;
- busca com sugestoes alfabeticas e abertura direta da carta foco;
- filtros por set, dominio, keyword, trigger, modifier, energy e might;
- renderizacao incremental da listagem inicial para reduzir custo de carregamento;
- carta foco clicavel para abrir o modal de detalhes;
- modal com imagem centralizada, atributos, tags, texto rico e botao `View Relations`;
- historico de navegacao para voltar entre home, filtros, modais e listas de relacoes;
- icones oficiais da Riot para energy, might, exhaust, rune rainbow, tipos, dominios e raridades quando disponiveis;
- keywords renderizadas com cores alinhadas as cartas oficiais, incluindo o padrao `[Keyword][>]`;
- `Clear` limpa filtros, busca, modal e volta ao estado inicial.

O frontend nao depende de Node/NPM.
