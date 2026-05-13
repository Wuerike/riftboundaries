# Onda 3 - agente Hilbert - produto final frontend e UX de categorizacao

## Escopo

Auditoria nao mutante da onda 3 sobre produto final frontend e UX de categorizacao.

## Achados

### 1. `deck_synergy` fica invisivel no produto final

- categoria do achado: integracao entre etapas
- severidade: alta
- confianca: alta
- evidencia: o dataset publica `deck_synergy` em `build_card_explorer_dataset.py:23`, mas a UI so renderiza `enabled_by`, `enables` e `similar_effect` em `app.js:2`. Resultado: 1056 relacoes somem. Exemplos concretos: `Vanguard Armory` tem 5 `deck_synergy` outgoing e aparece como sem relacoes; `Renata Glasc, Industrialist` tem 64 `deck_synergy` incoming e tambem nao mostra esse valor ao focar a carta.
- regra relacionada: contrato dataset/frontend.
- impacto provavel no produto final: uma familia de relacao gerada nao e exploravel pelo usuario.
- recomendacao: adicionar lane/contador de `deck_synergy` ou declarar exclusao explicita no contrato.
- teste que deveria existir: frontend fixture focando `Vanguard Armory` deve mostrar lane/contador de `deck_synergy` ou uma exclusao explicita.

### 2. Relacoes broad aparecem como recomendacoes reais

- categoria do achado: integracao entre etapas
- severidade: alta
- confianca: alta
- evidencia: a UI renderiza so tipo, razao e forca em `app.js:202`, sem `match.broad` nem evidencia. O relatorio aponta 3438 broad relations por `spell_card_can_be_countered`. `Acceptable Losses` e `Angle Shot` sao broad-only: no app parecem `Enabled Cards` para contra-magicas como `Abandon`, mesmo a evidencia real sendo so `source=spell`.
- regra relacionada: `spell_card_can_be_countered`; `match.broad`.
- impacto provavel no produto final: relacoes de baixo sinal aparecem como recomendacoes estrategicas.
- recomendacao: marcar broad/low-signal no app, demover por padrao ou esconder atras de toggle.
- teste que deveria existir: frontend fixture focando `Acceptable Losses` deve marcar `spell_card_can_be_countered` como broad/low-signal.

### 3. Vazio por filtro e vazio por cobertura sao indistinguiveis

- categoria do achado: integracao entre etapas
- severidade: alta
- confianca: alta
- evidencia: `Ahri, Inquisitive`, `Ravenborn Tome` e `Vilemaw` tem fatos semanticos, mas 0 relacoes. A UI mostra a mesma mensagem `No related cards match these filters` usada quando um filtro remove resultados. Isso oculta 100 cartas sem relacoes, incluindo 56 `missing_relation_rule` e 8 `weak_fact`.
- regra relacionada: contrato de diagnostico web.
- impacto provavel no produto final: usuario nao diferencia ausencia real de relacao de filtro ativo.
- recomendacao: distinguir estados `no relations in dataset`, `only broad hidden`, `filters removed results` e `relation rules missing`.
- teste que deveria existir: frontend fixture focando `Ahri, Inquisitive` deve diferenciar `sem relacoes no dataset` de `filtros removeram resultados`.

### 4. Filtros sao globais e aplicados ao card relacionado, nao a relacao

- categoria do achado: integracao entre etapas
- severidade: media
- confianca: alta
- evidencia: `cardMatchesRelationFilters` filtra propriedades do card alvo em `app.js:78`, e `relationsByType` aplica isso igualmente em todas as lanes. Nao ha filtro por `match.reason`, broad/high-signal, forca, evidencia, output da relacao ou direcao. Em `Wind Wall`, nao ha como remover as 191 relacoes broad de `spell can be countered` sem filtrar indiretamente os cards.
- regra relacionada: filtros do dataset e relation match.
- impacto provavel no produto final: usuario pensa filtrar relacoes, mas filtra atributos globais da carta relacionada.
- recomendacao: adicionar filtros de relacao por `match.reason`, `match.broad`, `strength`, `evidence`, `source_fact_id/target_fact_id`.
- teste que deveria existir: filtro broad/high-signal deve operar em relacoes, nao em atributos globais da carta.

### 5. Facetas publicadas pelo dataset nao existem na sidebar

- categoria do achado: integracao entre etapas
- severidade: media
- confianca: alta
- evidencia: o builder gera `tags`, `produced_events`, `outputs` e `power` em `build_card_explorer_dataset.py:195`, mas a UI so renderiza dominio, tipo, trigger, keyword, energy, might e predicate em `app.js:320`. Foram confirmadas 113 tags, 22 produced events, 43 outputs e 4 power facets ausentes. Exemplo: `Ravenborn Tome` tem `bonus_damage_added`, mas nao ha filtro de output.
- regra relacionada: contrato dataset/frontend.
- impacto provavel no produto final: categorias extraidas ficam inacessiveis ao usuario.
- recomendacao: renderizar facetas ou declarar como experimentais/ocultas.
- teste que deveria existir: snapshot de filtros publicados vs filtros renderizados.

### 6. Evidencia e ordenacao escondem a causa da categorizacao

- categoria do achado: manutencao
- severidade: media
- confianca: alta
- evidencia: o dataset preserva `relation.evidence` em `build_card_explorer_dataset.py:65`, mas o app nao a mostra. Alem disso, cada lane corta em 40 itens em `app.js:289` sem indicar `mostrando 40 de N`. `Abandon` tem 191 `enabled_by` outgoing, mas o usuario ve so os primeiros 40 e nao consegue auditar por evidencia.
- regra relacionada: contrato de evidencia de relacao.
- impacto provavel no produto final: usuarios e revisores nao conseguem explicar por que a categoria/relacao apareceu.
- recomendacao: exibir evidencia resumida e contagem total/corte por lane.
- teste que deveria existir: fixture com `Abandon` verifica contagem total e evidencia visivel.

### 7. Relatorios discordam sobre linhas relacionais descobertas

- categoria do achado: manutencao
- severidade: media
- confianca: alta
- evidencia: o agente recalculou em memoria: builder reporta 2 `cards_with_uncovered_relational_lines`, enquanto quality audit reporta 0. Os casos do builder sao `Curtain Call` e `Rockfall Path`; `Rockfall Path` tem `Units can't be played here` mas so fatos oficiais.
- regra relacionada: detection de uncovered relational lines.
- impacto provavel no produto final: reduz confianca no diagnostico exibido/consumido pela auditoria.
- recomendacao: centralizar criterio e alinhar reports.
- teste que deveria existir: dataset regression para paridade entre dataset report e quality report para `cards_with_uncovered_relational_lines`.

## Comandos/testes executados pelo agente

- `node --check web\app\app.js`: passou.
- Auditoria de dataset em memoria via `audit_card_explorer_dataset.py`: 767 cards, 5428 facts, 9884 relations, 100 sem relacoes, 22 broad-only.
- Builder em memoria via `build_card_explorer_dataset.py`: reproduziu 9884 relations e 1056 `deck_synergy`.
- Tentativa de escrever saidas em `C:\tmp` falhou por `PermissionError`; nenhum arquivo do repositorio foi alterado.

## Testes recomendados

- Frontend fixture: focar `Vanguard Armory` deve mostrar lane/contador de `deck_synergy` ou uma exclusao explicita.
- Frontend fixture: focar `Acceptable Losses` deve marcar `spell_card_can_be_countered` como broad/low-signal.
- Frontend fixture: focar `Ahri, Inquisitive` deve diferenciar `sem relacoes no dataset` de `filtros removeram resultados`.
- Dataset regression: assert de paridade entre dataset report e quality report para `cards_with_uncovered_relational_lines`.
