# Onda 3 - agente Ramanujan - regras oficiais contra fatos semanticos

## Escopo

Auditoria nao mutante da onda 3 cruzando `core-rules.md` contra `cards_normalized.json`, `cards_semantic_facts.jsonl`, `semantic_extraction_rules.json`, `feature_relation_taxonomy.json` e `extract_semantic_facts.py`.

Base analisada: 767 cartas, 5428 fatos semanticos.

## Achados

### 1. Reminder text extraido como funcao

- categoria do achado: parsing/normalizacao
- severidade: alta
- confianca: alta
- evidencia: ha 343 fatos vindos de trechos entre parenteses; exemplos: `Abandon` gera `look/recycle` a partir de reminder de `[Predict]`; Equip gera `attach` a partir de `(:cost: Attach...)`.
- regra relacionada: `core-rules.md:678-684`, especialmente 135.2.d.3: reminder text nao afeta funcao de jogo.
- impacto provavel no produto final: cartas sao categorizadas por texto explicativo instavel, duplicando ou falsificando efeitos reais.
- recomendacao: extrair funcao de keywords por expansao normativa, nao pelo parentese impresso.
- teste que deveria existir: fatos funcionais nao podem usar evidencia dentro de reminder text, exceto quando classificados explicitamente como `keyword_reminder` sem impacto funcional.

### 2. Effect Text de Gear tratado como sempre ativo

- categoria do achado: divergencia entre regras, cartas normalizadas e implementacao
- severidade: critica
- confianca: alta
- evidencia: 54 fatos de `effect_lines` em 25 cartas; todos sem condicao `attached`. `Warmog's Armor` gera `When I conquer/buff me`; `Guardian Angel` gera `recall me`; `Doran's Shield` gera `[Tank]`.
- regra relacionada: `core-rules.md:752`, `core-rules.md:5060-5063`, `core-rules.md:5122-5125`: Effect Text e inativo ate anexar e e anexado ao Top-Most Card.
- impacto provavel no produto final: o explorer pode tratar Gear como se tivesse gatilhos/keywords ativos na base, mao ou solto; pronomes `I/me` tambem deveriam apontar para o Top-Most Card quando anexado.
- recomendacao: todos os fatos de `effect_lines` devem carregar `active_condition: attached` e `applies_to: top_most_card`.
- teste que deveria existir: `effect_lines` nao pode produzir fato funcional sem condicao de anexacao.

### 3. Recall modelado como move/return_to_hand

- categoria do achado: categorizacao incorreta
- severidade: critica
- confianca: alta
- evidencia: `Altar of Blood`, `Conscription`, `Soraka`, `Zhonya's Hourglass` geram `predicate: return_to_hand`, `event.id: unit_moved`, `target.zone: base`.
- regra relacionada: `core-rules.md:4193-4205`: Recall vai para Base e nao e Move.
- impacto provavel no produto final: sinergias de movimento disparam indevidamente; bounce para mao e recall para base ficam misturados.
- recomendacao: criar `predicate: recall`, `event.id: unit_recalled/location_changed`, `target.zone: base`, e nunca `unit_moved`.
- teste que deveria existir: fatos com evidencia `recall` nao podem ter `predicate=return_to_hand` nem `event.id=unit_moved`.

### 4. Modes/choices viram efeitos obrigatorios independentes

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Rocket Barrage` tem `Choose one -`, mas os fatos dizem que `Deal 4` e `Kill a gear` sao ambos `required`; `Curtain Call` marca todas as opcoes como required; `Aphelios` idem para tres opcoes.
- regra relacionada: `core-rules.md:2245`, `core-rules.md:5909-5912`: modos sao escolhidos; Repeat faz escolhas separadas por execucao.
- impacto provavel no produto final: filtros e similaridade superestimam outputs; cartas modais parecem fazer tudo.
- recomendacao: gerar `choice_group/modal_option`, com cardinalidade e exclusividade; opcoes nao devem ser `required` global.
- teste que deveria existir: cartas com `Choose one -` devem ter grupo modal e nenhum option fact como required fora do grupo.

### 5. Additional costs e ignore costs estao inconsistentes

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: 6 linhas `As an additional cost...` nao viram `additional_cost` (`Meditation`, `Heedless Resurrection`, `Sacrifice`, `Cruel Patron`, etc.); `Wallop` e `Call to Glory` nao geram fato para `ignore this spell's cost`; `Atakhan` tambem gera evento `kill` separado do custo.
- regra relacionada: `core-rules.md:2311-2314`, `core-rules.md:5267-5273`, `core-rules.md:517`.
- impacto provavel no produto final: custos aparecem como efeitos/payoffs, distorcendo death synergy e custo real/impresso.
- recomendacao: separar custo de efeito; cobrir formas `As an additional cost...`; representar `ignore_self_play_cost` preservando custo impresso.
- teste que deveria existir: custo adicional com `kill/spend/exhaust/return` nao pode gerar `event_produced` fora de `cost_or_requirement`.

### 6. Replacement/prevent subextraido

- categoria do achado: regra ausente
- severidade: alta
- confianca: alta
- evidencia: 27 linhas com `would/instead/prevent`; so poucas viram `replacement_effect`. `Zhonya's Hourglass` vira `kill this` + `recall it` required, sem `replaced_event: friendly_unit_would_die`.
- regra relacionada: `core-rules.md:2666-2678` e `core-rules.md:2311`.
- impacto provavel no produto final: acoes condicionais de replacement parecem efeitos normais; death prevention e recall prevention ficam errados.
- recomendacao: detectar `would...instead` como replacement, com evento substituido e outputs condicionais.
- teste que deveria existir: linhas com `would` + `instead` devem gerar `fact_type=replacement_effect`.

### 7. Basic Runes sem habilidades obrigatorias

- categoria do achado: regra ausente
- severidade: alta
- confianca: alta
- evidencia: `Body/Calm/Chaos/Fury/Mind/Order Rune` tem so `has_card_type` e `has_domain`.
- regra relacionada: `core-rules.md:1143-1155`: toda Basic Rune tem `[E]: [Reaction] - Add [1]` e `Recycle this: [Reaction] - Add [C]`.
- impacto provavel no produto final: geracao de recurso, filtros por Add/Recycle e sinergias com Rune ficam invisiveis.
- recomendacao: injetar fatos normativos para Basic Runes a partir do tipo/dominio.
- teste que deveria existir: cada Basic Rune deve ter fatos `add_energy`, `add_power(domain=self)` e custo/acao `recycle this`.

### 8. Equip/Repeat/Accelerate com tipo de custo errado

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: Equip: 41 `attach` como produced_event e 35 `activated_ability_cost`; Repeat: `Rocket Barrage` perde o rune cost e vira activated cost; Accelerate: 24 activated costs vindos do reminder e sem Power matching.
- regra relacionada: `core-rules.md:5327-5354`, `core-rules.md:5803-5827`, `core-rules.md:5882-5918`.
- impacto provavel no produto final: Equip parece anexar imediatamente; Repeat/Accelerate nao sao modelados como optional additional costs; custos multicomponentes ficam truncados/duplicados.
- recomendacao: criar builders dedicados para keywords, usando regras oficiais, nao `activation_split` sobre parenteses.
- teste que deveria existir: `[Repeat]` e `[Accelerate]` nunca devem gerar `activated_ability_cost`; `[Equip]` deve gerar activated ability, nao attach imediato.

### 9. Tank/Deflect submodelados

- categoria do achado: regra ausente
- severidade: media-alta
- confianca: alta
- evidencia: `Tank` aparece quase so como `keyword_marker`; `Deflect 2` em `Ornn` mantem label, mas nao normaliza `deflect_value=2` e ainda gera custo parcial do reminder.
- regra relacionada: `core-rules.md:5503-5515`, `core-rules.md:5728-5743`.
- impacto provavel no produto final: filtros por protecao/custo adicional obrigatorio e logica de combate perdem funcao real das keywords.
- recomendacao: expandir `Tank` para restricao de atribuicao de dano e `Deflect` para mandatory additional cost com valor.
- teste que deveria existir: `[Deflect 2]` deve gerar valor 2 e custo universal por escolha; `[Tank]` deve gerar combat assignment restriction.

## Comandos principais usados

```powershell
rg --files
rg -n "reminder|Effect Text|Recall|Choose one|additional cost|replacement|Basic Runes|Equip|Repeat|Accelerate|Tank|Deflect" data\processed\rules\core-rules.md
Select-String -Path scripts\04_cards_feature_extraction\extract_semantic_facts.py -Pattern "TEXT_SOURCE_FIELDS|reminder_rules|keyword_marker|recall|additional_cost|Repeat|Equip|Accelerate"
Select-String -Path scripts\04_cards_feature_extraction\contracts\semantic_extraction_rules.json -Pattern "additional_cost|recall_unit|replacement|prevent|reminder_rules"
@' ... agregacao somente-leitura de cards_normalized.json e cards_semantic_facts.jsonl ... '@ | python -
```
