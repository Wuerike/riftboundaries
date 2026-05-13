# Onda 1 - checagem local cruzada

## Escopo analisado

Checagem local, nao mutante, executada enquanto os agentes da onda 1 auditavam escopos independentes. O foco foi procurar padroes de risco no corpus normalizado e confrontar fatos gerados contra regras de categorizacao.

## Arquivos principais lidos

- `data/processed/cards/normalized/cards_normalized.json`
- `data/processed/cards/semantic/cards_semantic_facts.jsonl`
- `scripts/04_cards_feature_extraction/contracts/semantic_extraction_rules.json`
- `scripts/04_cards_feature_extraction/contracts/feature_relation_taxonomy.json`

## Cartas normalizadas consultadas

- `Vaults of Helia`
- `Vex, Cheerless`
- `Defy`
- `Fate Weaver`
- `Fizz, Trickster`
- `Glasc Mixologist`
- `Jayce, Man of Progress`
- `Lady of Luminosity - Starter`
- `Lux, Illuminated`
- `Pickpocket`
- `Rell, Magnetic`
- `Undying Loyalty`
- `Determined Sentry`
- `Buhru Captain`
- `Maduli, The Gatekeeper`
- `Rabadon's Deathcrown`

## Regras de categorizacao consultadas

- `generic_cost_reduction`
- `move_unit`
- `draw_cards`
- `buff_unit`
- `give_might`
- regras de `effect_lines` via fatos por `source_field`
- familias da taxonomia: `cost_modifier`, `movement_modifier`, `choice_modal`, `restriction_or_permission`, `state_modifier`

## Comandos executados e resultado

- PowerShell sobre `cards_normalized.json`: contou cartas contendo padroes textuais de risco.
- PowerShell sobre `cards_semantic_facts.jsonl`: listou fatos `reduce_cost` cujo texto contem `more`, `no more than` ou `or more`.
- PowerShell sobre `cards_semantic_facts.jsonl`: listou fatos positivos em linhas com `can't`, `cannot`, `don't`, `doesn't` ou `not`.
- PowerShell sobre `cards_semantic_facts.jsonl`: agrupou fatos extraidos de `effect_lines` por predicado.

Resultados principais:

- `instead`: 22 cartas.
- `can't`: 39 cartas.
- `don't`: 23 cartas.
- `choose one`: 7 cartas.
- `up to`: 20 cartas.
- `additional cost`: 72 cartas.
- ` more `: 27 cartas.
- ` less`: 49 cartas.
- `copy`: 5 cartas.
- `swap`: 2 cartas.
- `becomes`: 4 cartas.
- `while this is attached`: 1 carta.
- `would`: 13 cartas.
- fatos `reduce_cost`: 37 parecem desconto/ignorar custo, 7 vem de `no more than`, 3 de `or more`, 2 de aumento de custo, 6 outros.
- fatos de `effect_lines`: predicados mais comuns foram `observe_event` (20), `has_keyword` (10), `modify_stat` (4), `draw` (3), `play_token` (3), `damage` (3).

## Entendimento da entrada e saida

A entrada da checagem e o texto normalizado das cartas. A saida avaliada e o conjunto de fatos semanticos ja gerado. A etapa 04 contribui para a categorizacao transformando linhas textuais em predicados, eventos, outputs e papeis semanticos usados por filtros, similaridade e relacoes.

## Achados

### 1. `generic_cost_reduction` tambem captura limites e condicoes de custo

- categoria do achado: categorizacao incorreta
- severidade: critica
- confianca: alta
- evidencia: fatos `reduce_cost` aparecem em textos que nao reduzem custo:
  - `Defy`: `Counter a spell that costs no more than :rb_energy_4:...` gera `reduce_cost`.
  - `Fate Weaver`: `You may reveal a spell with Energy cost :rb_energy_4: or more...` gera `reduce_cost`.
  - `Lady of Luminosity - Starter`: `When you play a spell that costs :rb_energy_5: or more, draw 1.` gera `reduce_cost`.
  - `Lux, Illuminated`: `When you play a spell that costs :rb_energy_5: or more, give me +3...` gera `reduce_cost`.
  - `Vaults of Helia`: `cost :rb_energy_1: more to play this turn` gera `reduce_cost`.
  - `Vex, Cheerless`: texto mistura `friendly spells cost ... less` e `enemy spells cost ... more`, mas o fato unico `reduce_cost` carrega raw que inclui os dois lados.
- regra relacionada: `generic_cost_reduction`.
- impacto provavel no produto final: cartas de counter com limite, triggers condicionais por custo alto e taxes de custo entram em filtros/relacoes de desconto.
- recomendacao: dividir a familia em pelo menos quatro categorias: reducao real, ignorar custo, limite de alvo por custo, condicao de trigger por custo, aumento/tax de custo.
- teste que deveria existir: goldens negativos para `Defy`, `Lady of Luminosity - Starter`, `Lux, Illuminated` e `Vaults of Helia`, proibindo `predicate: reduce_cost`.

### 2. Restricao `I can't move to base` vira evento produzido de movimento

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Determined Sentry` tem a linha `I can't move to base.` e gera fato `semantic_role: event_produced`, `fact_type: movement`, `predicate: move`, regra `move_unit`, output `unit_moved`.
- regra relacionada: `move_unit`; familia `restriction_or_permission` / `movement_modifier`.
- impacto provavel no produto final: uma carta que restringe movimento pode aparecer como carta que move unidade.
- recomendacao: aplicar guard de negacao antes de `move_unit` e criar fato separado de restricao `cannot_move_to_base`.
- teste que deveria existir: golden para `Determined Sentry` exigindo restricao e ausencia de evento produzido `unit_moved`.

### 3. Modal inline com `or` gera opcoes simultaneas e fatos de reminder

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Buhru Captain` tem `When you play me, you may draw 1 or buff me. (To buff a unit, give it a +1 :rb_might: buff if it doesn't already have one.)`. Os fatos gerados incluem:
  - `draw` opcional;
  - `buff` opcional para `me`;
  - outro `buff` opcional para `a unit` vindo do reminder;
  - outro `buff` opcional com target bruto `if it doesn't already have one`;
  - `modify_stat` com target bruto `it a`.
- regra relacionada: `draw_cards`, `buff_unit`, `give_might`, familia `choice_modal`.
- impacto provavel no produto final: uma escolha `draw or buff` vira multiplos fatos independentes e duplica a categoria de buff.
- recomendacao: reconhecer `A or B` como grupo modal quando os dois lados sao outputs alternativos; ignorar reminder text para fatos principais ou marcar como definicao de keyword/termo.
- teste que deveria existir: golden para `Buhru Captain` exigindo um grupo modal opcional com duas opcoes e ausencia de fatos derivados do reminder como output independente.

### 4. `effect_lines` geram muitos predicados sem contrato de contexto

- categoria do achado: divergencia entre regras, cartas normalizadas e implementacao
- severidade: media
- confianca: alta
- evidencia: fatos com `source_field: effect_lines` aparecem em varios predicados: `observe_event` (20), `has_keyword` (10), `modify_stat` (4), `draw` (3), `play_token` (3), `damage` (3), alem de outros. `Rabadon's Deathcrown` e o caso explicitamente marcado como `while this is attached`, mas a mesma ausencia de contexto pode afetar outras gears com effect text.
- regra relacionada: regras oficiais de Effect Text e Attachment; contratos de `source_ref.source_field`.
- impacto provavel no produto final: efeitos attached-only podem ser exibidos como fatos ativos da carta original.
- recomendacao: auditar todos os fatos de `effect_lines` e exigir `activation_context` antes de usa-los em relacoes high-signal.
- teste que deveria existir: check que falhe quando `source_field: effect_lines` nao traz campo de contexto active/inactive/attached.

### 5. Corpus contem ampla superficie para goldens negativos

- categoria do achado: teste faltante
- severidade: media
- confianca: alta
- evidencia: a varredura encontrou 39 cartas com `can't`, 23 com `don't`, 22 com `instead`, 27 com `more`, 49 com `less`, 7 com `choose one`, 5 com `copy`, 2 com `swap`, 13 com `would`.
- regra relacionada: `semantic_golden_examples.json`; familias `restriction_or_permission`, `choice_modal`, `replacement_effect`, `cost_modifier`, `copy_effect`, `stat_modifier`.
- impacto provavel no produto final: os goldens atuais podem passar mesmo com falsas categorias em padroes recorrentes.
- recomendacao: criar um pool de goldens negativos por padrao, priorizando as cartas listadas neste relatorio.
- teste que deveria existir: suite de ausencia por padrao textual, nao apenas presenca minima de fatos esperados.

## Testes faltando

- Testes de limite de alvo por custo: `Defy`, `Pickpocket`.
- Testes de trigger condicionado por custo: `Lady of Luminosity - Starter`, `Lux, Illuminated`.
- Testes de aumento/tax de custo: `Vaults of Helia`, `Vex, Cheerless`.
- Testes de negacao de movimento: `Determined Sentry`.
- Testes de modal inline: `Buhru Captain`.
- Testes de `effect_lines` com contexto.

## Oportunidades de melhoria

- Introduzir uma taxonomia de contexto de custo: `cost_threshold`, `cost_condition`, `cost_discount`, `cost_ignored`, `cost_increase`.
- Preprocessar ou anotar reminder text antes de rodar builders de fatos.
- Adicionar `choice_group_id` para `or` inline, nao apenas para `Choose one`.
- Tratar `can't`/`don't` como guard global antes de qualquer builder de evento produzido.

## Duvidas ou hipoteses ainda nao confirmadas

- Se `ignoring its cost` deve compartilhar parcialmente chaves de similaridade com reducao de custo ou ficar como permissao/cost override separada.
- Se facts de `effect_lines` devem aparecer no frontend por padrao ou apenas em contexto de attachment.
- Se textos de reminder devem ser completamente ignorados para fatos ou mantidos em uma camada explicativa separada.
