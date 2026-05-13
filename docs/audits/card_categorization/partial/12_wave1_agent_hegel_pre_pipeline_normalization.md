# Onda 1 - agente Hegel - pre-pipeline e normalizacao

## Escopo

Auditoria nao mutante sobre pre-pipeline e normalizacao, com foco em `cards_normalized.json`, `rule_variants`, `rules_lines`, `effect_lines`, `html_to_lines`, `richest_printing`, `play_id` e relacao com regras oficiais.

O agente informou que nao editou arquivos. A worktree ja estava suja antes da auditoria: `goal.md` modificado e `docs/` nao rastreado.

## Inventario

- `cards_normalized.json`: 767 cartas jogaveis, 949 impressoes, 140 grupos com multiplas impressoes.
- `rule_variants`: 44 cartas; 8 continuam semanticamente diferentes mesmo removendo parenteses/lembretes.
- `effect_lines`: 27 cartas, todas `gear` com tag `Equipment`.
- Headers modais com lista: 6 casos concretos.
- Linhas `[Equip]` com texto de lembrete parentetico embutido: 36.

## Achados

### Achado 1 - Variantes semanticas colapsadas no mesmo `play_id`

- categoria do achado: parsing/normalizacao
- severidade: alta
- confianca: alta
- evidencia: `gameplay_signature` exclui `rules_text` e `effect_text`; o `play_id` e gerado dessa assinatura em `normalize_cards.py:298` e `normalize_cards.py:342`. A etapa 04 itera apenas `rules_lines` e `effect_lines` em `extract_semantic_facts.py:26` e `extract_semantic_facts.py:2170`.
- cartas concretas: `Gold`, `The Boss`, `Emperor of the Sands`, `Void Burrower`, `Yone, Blademaster`, `Lonely Poro`, `Teemo, Strategist`, `Karma, Channeler`.
- regra relacionada: lembretes nao alteram funcao de jogo segundo `core-rules.md:684`; variantes devem ser classificadas entre lembrete e texto funcional.
- impacto provavel no produto final: fatos semanticos passam a representar uma variante textual escolhida, mas o `play_id` representa todas as impressoes. Isso mistura errata/rewording funcional com reprint cosmetico.
- recomendacao: introduzir `text_variant_id` ou `oracle_variant_id`, marcar variante atual/canonica explicitamente, e fazer a etapa 04 emitir fatos por variante ou por oracle declarado, nao apenas pelo texto top-level.
- teste que deveria existir: validar que as 8 cartas acima geram variantes funcionais distintas ou uma decisao explicita de oracle; falhar se uma variante funcional ficar apenas em `rule_variants` sem fatos.

### Achado 2 - `richest_printing` nao e oracle

- categoria do achado: parsing/normalizacao
- severidade: alta
- confianca: alta
- evidencia: `richest_printing` ordena por maior comprimento de texto em `normalize_cards.py:252`. Em `Emperor of the Sands`, `canonical_printing_id` e `sfd-197-221`, mas o texto top-level vem de `SFD-247/221`: `Your Sand Soldiers have [Weaponmaster]` vs `Sand Soldiers you play have [Weaponmaster]`.
- regra relacionada: a regra oficial distingue texto funcional de lembrete; comprimento nao e criterio de funcao ou atualidade.
- impacto provavel no produto final: a carta pode carregar no topo um texto nao canonico, e a etapa 04 vai extrair apenas esse texto.
- recomendacao: separar "texto mais completo para leitura" de "texto oracle para semantica". Se nao houver oracle oficial, exigir prioridade de set/data ou decisao manual auditavel.
- teste que deveria existir: quando `canonical_printing_id` nao pertence a variante top-level, exigir campo `oracle_source` ou falhar.

### Achado 3 - Lembretes estao misturados ao texto funcional

- categoria do achado: parsing/normalizacao
- severidade: alta
- confianca: alta
- evidencia: `html_to_lines` usa `BeautifulSoup.get_text("\n")` e nao marca parenteses como lembrete em `normalize_cards.py:120`. Exemplos: `Warmog's Armor` e `Hexdrinker` normalizam `[Equip] :rb_rune_body: (:rb_rune_body:: Attach this...)`.
- regra relacionada: `core-rules.md:672` e `core-rules.md:684` dizem que lembretes podem existir e nao alteram a funcao de jogo.
- impacto provavel no produto final: a etapa 04 pode extrair custo/acao duplicados a partir do lembrete. Nos fatos existentes, `Warmog's Armor` e `Hexdrinker` carregam custo de Equip duplicado porque a linha contem custo funcional e custo repetido no parenteses.
- recomendacao: normalizar em segmentos: `functional_text`, `reminder_text`, `is_reminder`, `line_role`. A etapa 04 deve ignorar lembretes para efeitos mecanicos, usando-os apenas como ajuda/glossario.
- teste que deveria existir: para `Warmog's Armor` e `Hexdrinker`, Equip deve produzir um unico custo `:rb_rune_body:` e um unico attach funcional.

### Achado 4 - Hierarquia modal/bullets e perdida

- categoria do achado: parsing/normalizacao
- severidade: alta
- confianca: alta
- evidencia: `<ul><li>` vira linhas planas. `Curtain Call` fica como header `Choose one you haven't already chosen` seguido de quatro linhas independentes; `Rocket Barrage`, `Disposal Order`, `Flurry of Feathers`, `Udyr, Wildman` e `Aphelios, Exalted` tem o mesmo padrao. A taxonomia conhece `choice_modal` e `modal_option` em `feature_relation_taxonomy.json:135`, mas a extracao usa fontes planas.
- regra relacionada: modos sao escolhidos como parte de jogar spells/abilities em `core-rules.md:2245` e `core-rules.md:3063`; Repeat permite escolhas diferentes em `core-rules.md:5912`.
- impacto provavel no produto final: opcoes modais viram efeitos independentes sem exclusividade, sem `option_index`, sem `not already chosen`, e sem relacao correta com Repeat.
- recomendacao: preservar blocos HTML/listas como `rules_blocks` com `modal_group_id`, `option_index`, `selection_count`, `selection_constraint`.
- teste que deveria existir: `Curtain Call` deve gerar 1 grupo modal com 4 opcoes e restricao `not_already_chosen`; `Rocket Barrage` deve vincular Repeat ao grupo modal.

### Achado 5 - `effect_lines` de equipamentos nao carregam contexto de anexo

- categoria do achado: divergencia entre regras, cartas normalizadas e implementacao
- severidade: alta
- confianca: alta
- evidencia: todas as 27 cartas com `effect_lines` sao `gear` + `Equipment`. A etapa 04 trata `effect_lines` como fonte igual a `rules_lines`. Nos fatos existentes, `Warmog's Armor` produz `self_conquers` e `buff me` no `play_id` do Gear; `Hexdrinker` produz `has_keyword Deflect` no Gear.
- regra relacionada: Effect Text fica inativo salvo quando anexado em `core-rules.md:752`, e e anexado ao Rules Text do Top-Most Card em `core-rules.md:755` e `core-rules.md:5096`.
- impacto provavel no produto final: relacoes web podem dizer que o equipamento conquista, recebe buff ou tem Deflect, quando o sujeito efetivo e a unidade equipada.
- recomendacao: adicionar metadados `effect_active_when: attached`, `effective_subject: attached_top_most_card`, mantendo `source_play_id` do equipamento.
- teste que deveria existir: `Warmog's Armor` deve produzir efeito concedido ao host anexado; `Hexdrinker` deve modelar Deflect como keyword concedida ao card equipado enquanto anexado.

## Comandos executados

Todos foram somente leitura. Principais comandos:

```powershell
git status --short
Get-ChildItem -LiteralPath <arquivos obrigatorios> | Select-Object FullName,Length,LastWriteTime
Get-Content -LiteralPath scripts\03_cards_formatter\normalize_cards.py
Get-Content -LiteralPath scripts\03_cards_formatter\README.md
rg -n "rule_variants|effect_lines|rules_lines|html_to_lines|richest_printing|play_id|modal|modes" ...
rg -n "default_source_fields|rules_lines|effect_lines|choice_modal|modal_option" ...
rg -n "<regras oficiais relevantes>" data\processed\rules\core-rules.md
python -  # leituras JSON para contagens, variantes, modais, effect_lines e exemplos concretos
rg -n "play:<ids auditados>" data\processed\cards\normalized\cards_normalized.json
rg -n "play:warmog-s-armor|play:hexdrinker" data\processed\cards\semantic\cards_semantic_facts.jsonl
Get-Content -LiteralPath data\processed\cards\semantic\cards_semantic_audit_report.md | Select-Object -First 180
```

Houve um `rg` com erro de quoting por causa de `Warmog's Armor`; ele nao alterou estado e foi reexecutado com padrao seguro.
