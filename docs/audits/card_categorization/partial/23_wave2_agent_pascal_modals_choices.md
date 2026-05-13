# Onda 2 - agente Pascal - modais e escolhas

## Escopo

Auditoria nao mutante da onda 2 sobre modais e escolhas.

O agente informou que nao editou arquivos. `git status --short` ao final: `M goal.md`, `?? docs/`.

## Resumo

O problema central e que o pipeline preserva linhas, mas nao preserva blocos modais. `normalize_cards.py` transforma bullets em `rules_lines` independentes, e `extract_semantic_facts.py` cria `clause_group_id` por linha. Resultado: `Choose one`, opcoes exclusivas, restricoes de `not already chosen`, `Repeat` com modos, e escolhas de alvo ficam desconectadas ou desaparecem.

## Achados

### A1 - `Choose one` nao vira fato modal

- categoria do achado: regra ausente
- severidade: alta
- confianca: alta
- evidencia: o agente encontrou 7 linhas com `choose one`; os headers de `Disposal Order`, `Flurry of Feathers`, `Curtain Call` e `Rocket Barrage` tem 0 fatos. `Udyr` e `Aphelios` so emitem custo/trigger na linha do header, sem fato de escolha.
- regra relacionada: `feature_relation_taxonomy.json` tem `choice_modal` e `modal_option`, mas `semantic_extraction_rules.json` so cobre `choose_named_tag` e `choose_tag_from_list`.
- impacto provavel no produto final: as opcoes aparecem como efeitos independentes obrigatorios, nao como modos exclusivos.
- recomendacao: emitir `targeting_or_scope/choice` ou `restriction_or_permission/choice_modal` com `choice_group_id`, `choice_kind: mode`, `choose_count: 1`, `exclusive: true`, `option_count`.
- teste que deveria existir: golden para `Disposal Order`, `Curtain Call` e `Rocket Barrage` com grupo modal.

### A2 - Flattening de bullets quebra vinculo entre header, custo/trigger e opcoes

- categoria do achado: parsing/normalizacao
- severidade: alta
- confianca: alta
- evidencia: `normalize_cards.py:120` usa `soup.get_text("\n")` e depois `splitlines`; bullets perdem hierarquia. `extract_semantic_facts.py:213` cria `clause:{play_id}:{source_field}:{line_index}:ability`.
- exemplos: `Aphelios` linha 0 tem trigger; linhas 1-3 sao opcoes sem o trigger. `Udyr` linha 0 tem custo; linhas 1-4 sao opcoes sem custo. `Curtain Call` linhas 2-5 sao opcoes sem o header `Choose one you haven't already chosen`.
- regra relacionada: normalizacao de HTML e `clause_group_id`.
- impacto provavel no produto final: downstream nao consegue saber quais fatos pertencem ao mesmo modal.
- recomendacao: preservar blocos/listas ou reconstruir blocos modais no extrator; opcoes devem compartilhar `choice_group_id` e herdar contexto do header.
- teste que deveria existir: teste de estrutura de blocos para `Aphelios`, `Udyr` e `Curtain Call`.

### A3 - `Repeat` e modos estao semanticamente errados

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Rocket Barrage` deveria ter custo Repeat `:rb_energy_4::rb_rune_mind:`, mas o fato `activated_ability_cost` so contem `:rb_energy_4:`. `Curtain Call` tem quatro simbolos no texto, mas o custo emitido perde o ultimo `:rb_rune_rainbow:` e mistura instancias alternativas.
- regra relacionada: `activation_split` divide no ultimo `": "` e corta o `:` final de simbolos `:rb_*:`; `repeat_effect` so captura `repeat this ... effect`, sem modelar Repeat como custo adicional.
- regra oficial: `core-rules.md` 820.1 define Repeat como custo adicional opcional; 820.2.a diz que em Repeat as escolhas adicionais podem usar o mesmo modo/alvo ou modos/alvos diferentes.
- impacto provavel no produto final: `Rocket Barrage` nao representa `mesmo modo ou modo diferente`; `Curtain Call` nao representa varias instancias de Repeat nem o bloqueio de modo ja escolhido.
- recomendacao: criar fato `additional_cost/repeat` com custos completos e ligar `repeat_execution` ao `choice_group_id`.
- teste que deveria existir: golden para `Rocket Barrage` e `Curtain Call`.

### A4 - Inline `or` nao diferencia modo, destino e texto de reminder

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Buhru Captain` (`you may draw 1 or buff me`) emite `draw` e `buff` como dois fatos opcionais independentes, sem exclusividade. A reminder text tambem gera fatos extras `buff a unit`, `buff if it doesn't already have one` e `give it a +1`.
- regra relacionada: choice modal inline; reminder text.
- impacto provavel no produto final: a carta parece produzir todos os efeitos, nao escolher exatamente um.
- recomendacao: classificar `or` por contexto: `modal_inline_or` para efeitos alternativos, `destination_choice` para `top or bottom`, `target_constraint_or` para requisitos de alvo, e ignorar reminder quando apenas explica keyword/termo.
- teste que deveria existir: golden para `Buhru Captain` com opcoes exclusivas e fatos proibidos de reminder.

### A5 - `not already chosen` / memoria de escolha nao existe

- categoria do achado: regra ausente
- severidade: alta
- confianca: alta
- evidencia: `Curtain Call` header tem 0 fatos; `Udyr` so tem `Spend my buff`; `Aphelios` so tem trigger; `King's Edict` so emite `Kill those units`.
- regra relacionada: selection constraints.
- impacto provavel no produto final: nao ha como validar `modo nao escolhido`, `nao escolhido este turno` ou `nao escolhido para este spell`.
- recomendacao: adicionar `selection_constraint` estruturado: `not_already_chosen`, com `scope: this_turn | this_spell | this_resolution` e `subject: mode | target`.
- teste que deveria existir: goldens para `Curtain Call`, `Udyr`, `Aphelios` e `King's Edict`.

### A6 - Escolha de alvo e escolha de modo estao misturadas ou ausentes

- categoria do achado: regra ausente
- severidade: media-alta
- confianca: alta
- evidencia: `Blind Fury` revela/banish/recycle, mas nao emite fato para `Choose one` dos cards revelados. `King's Edict` nao emite o fato de cada outro player escolher uma unidade valida. `Disposal Order` nao estrutura `Choose up to 3 cards from opponents' trashes`.
- regra oficial: `core-rules.md` 355.3 cobre modos; 355.5 cobre escolha de objetos; 355.10.e diferencia objetos escolhidos por outros jogadores de targets normais.
- impacto provavel no produto final: escolha de modo, escolha de alvo e escolha feita por outro jogador ficam indistintas ou ausentes.
- recomendacao: usar `choice_kind: mode | target | target_set | actor_choice`, com `targeting: true/false/unknown`, `chooser`, cardinalidade e restricoes.
- teste que deveria existir: goldens para `Blind Fury`, `King's Edict` e `Disposal Order`.

## Goldens recomendados pelo agente

```json
[
  {
    "name": "Rocket Barrage",
    "expected": [
      "choice modal: choose_count=1, option_count=2, exclusive=true",
      "repeat additional_cost costs include energy 4 and rune mind",
      "repeat_allows_different_choices=true",
      "option 0 damage target unit location base",
      "option 1 kill target gear"
    ]
  },
  {
    "name": "Curtain Call",
    "expected": [
      "choice modal: choose_count=1, option_count=4, exclusive=true",
      "selection_constraint: not_already_chosen, subject=mode",
      "repeat costs represented as separate payable instances",
      "all option facts share choice_group_id"
    ]
  },
  {
    "name": "Buhru Captain",
    "expected": [
      "inline modal: choose_count=1, exclusive=true, options=[draw_1,buff_self]",
      "forbidden: reminder-only buff/stat facts as independent card effects"
    ]
  },
  {
    "name": "Aphelios, Exalted",
    "expected": [
      "trigger equipment_attached linked to modal group",
      "selection_constraint: not_already_chosen, scope=this_turn",
      "options ready_runes, channel_rune_exhausted, buff_friendly_unit share choice_group_id"
    ]
  },
  {
    "name": "King's Edict",
    "expected": [
      "actor_choice for each other player, order starts next player",
      "target restriction: unit you don't control, not chosen for this spell",
      "kill references chosen_units"
    ]
  }
]
```

## Comandos

```powershell
rg --files
Get-Content -Raw scripts\03_cards_formatter\normalize_cards.py
Get-Content -Raw scripts\04_cards_feature_extraction\extract_semantic_facts.py
Get-Content -Raw scripts\04_cards_feature_extraction\contracts\semantic_extraction_rules.json
Get-Content -Raw scripts\04_cards_feature_extraction\contracts\feature_relation_taxonomy.json
Get-Content -Raw scripts\04_cards_feature_extraction\contracts\semantic_golden_examples.json
rg -n "Choose|choose|or\b|Repeat|already chosen|mode|modes|option" data\processed\rules\core-rules.md
```

O agente tambem usou scripts Python inline somente leitura para cruzar `cards_normalized.json` com `cards_semantic_facts.jsonl` e contar os casos: 7 linhas `choose one`, 4 linhas `not/already chosen`, 25 linhas com `Repeat`.
