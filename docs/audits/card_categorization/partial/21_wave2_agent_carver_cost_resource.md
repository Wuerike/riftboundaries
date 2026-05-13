# Onda 2 - agente Carver - custo, recurso e activation parsing

## Escopo

Auditoria somente leitura da onda 2 sobre custo/recurso/activation parsing.

O agente informou que nao editou arquivos. `git status --short` continuou mostrando apenas mudancas pre-existentes: `M goal.md` e `?? docs/`.

## Achados

### 1. `activation_cost` perde custo `Spend XP`

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Blood Rose`, `Voidreaver` e `Keeper of the Hammer` tem facts `activated_ability_cost` so com `:rb_exhaust:`; o custo `Spend N XP` sumiu. `Crowd Favorite`, `Megatusk` e `Enthralling Protector` tem `Spend N XP:` e nem geram fact de custo.
- regra relacionada: `parse_non_symbol_costs()` so parseia simbolos, Kill, Discard e Recycle; nao parseia `Spend N XP`. Core rules 729-730 tratam XP como recurso ganho/gasto.
- impacto provavel no produto final: filtros e relacoes de custo XP ficam falsamente ausentes; cartas que ganham XP nao conectam com cartas que gastam XP.
- recomendacao: adicionar parsing explicito de `Spend (?P<amount>\d+) XP` em activation costs e emitir `{resource:"xp", amount:N}` junto dos demais custos.
- teste que deveria existir: `Blood Rose` deve ter custos `xp=3` e `exhaust`; `Voidreaver` deve ter `xp=1/exhaust` e `xp=2/exhaust`; `Megatusk` deve gerar `activated_ability_cost` com `xp=3`.

### 2. `activation_split` amplo demais e truncamento de simbolo

- categoria do achado: parsing/normalizacao
- severidade: alta
- confianca: alta
- evidencia: `Altar of Blood` tem 3 runas no texto, mas o fact captura 2; `Power Nexus` tem 4, mas captura 3. `Karma, Channeler` e `Lux, Illuminated` geram `activated_ability_cost` em linhas que sao triggers/thresholds, nao abilities ativadas.
- regra relacionada: `activation_cost` no contrato usa pattern `.+`; `activation_split()` divide no ultimo `":\s+"`, confundindo o `:` final de simbolos com delimitador de ability.
- impacto provavel no produto final: cria custos falsos e perde o ultimo simbolo quando o custo termina em `:rb_*:` antes de `to`.
- recomendacao: reconhecer apenas delimitador real de activated ability, por exemplo `::` apos simbolo/custo ou `Spend N XP:`; separar `may pay ... to ...` como custo condicional de trigger/replacement, nao `activated_ability_cost`.
- teste que deveria existir: `Altar of Blood` deve preservar 3 runas; `Power Nexus` 4; `Karma`/`Lux`/`Vex` nao devem gerar `activated_ability_cost`.

### 3. Thresholds de custo (`or more`, `no more than`) viram reducao

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Lux, Illuminated` e `Lady of Luminosity` viram `reduce_cost` para `costs :rb_energy_5: or more`; `Defy` vira `reduce_cost` para `costs no more than :rb_energy_4:`.
- regra relacionada: `generic_cost_reduction` casa qualquer `cost(s)` com simbolo de energia. Core rule 131.4 diz que checagens de custo usam custo impresso, mesmo se alterado/ignorado.
- impacto provavel no produto final: thresholds sao classificados como modificadores de custo, poluindo similaridade e outputs `play_cost_reduced`.
- recomendacao: criar facts de `cost_threshold`/`cost_constraint` estruturados (`>=5 energy`, `<=4 energy`, `<=1 any rune`) e bloquear `generic_cost_reduction` para `or more` e `no more than`.
- teste que deveria existir: `Defy` deve ter counter com constraints, sem `reduce_cost`; `Lux`/`Lady` devem ter trigger `spell_played` com threshold `energy >= 5`, sem custo nem desconto.

### 4. `cost more/less` e modificadores compostos

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Vaults of Helia` diz `cost :rb_energy_1: more`, mas sai como `reduce_cost`. `Vex, Cheerless` mistura friendly `less`, minimo e enemy `more`; o parser emite um unico `reduce_cost`, target `enemy`, so energia, e ainda cria cost fact falso.
- regra relacionada: `generic_cost_reduction` nao diferencia sinal, alvo, minimo, runa nem clausulas separadas.
- impacto provavel no produto final: aumentos viram descontos; `Vex` gera relacoes/filtros errados e perde a parte de runa/minimum.
- recomendacao: dividir clausulas por alvo, emitir `increase_cost` e `reduce_cost` distintos, com amounts de energia e rune-any, target/controller e minimum.
- teste que deveria existir: `Vaults` deve ser `increase_cost +1 energy`; `Vex` deve gerar `friendly spells reduce energy/rune any` com minimo e `enemy spells increase energy/rune any`.

### 5. `additional_cost` e `ignore cost`

- categoria do achado: regra ausente
- severidade: media-alta
- confianca: alta
- evidencia: 48 cartas tem `as an additional cost`; so 14 geram `additional_cost`. `Wallop`/`Call to Glory` (`spend a buff as an additional cost; ignore this spell's cost`), `Meditation`, `Heedless Resurrection` e varias Accelerate/mandatory costs ficam sem fact apropriado.
- regra relacionada: `additional_cost_to_play_self` cobre basicamente `You may <verb> ... as an additional cost to play me/this`; nao cobre `As an additional cost...`, `As you play...`, Accelerate/Repeat/mandatory forms. Core rules 356.1-356.6 distinguem ignore cost, additional costs, increases e discounts.
- impacto provavel no produto final: custos mandatorios/opcionais e base-cost ignore ficam invisiveis; efeitos condicionados a `paid additional cost` ficam parcialmente orfaos.
- recomendacao: adicionar gramaticas para mandatory/optional additional costs em ambas as ordens, incluindo `spend buff`, `exhaust`, `kill`, Accelerate/Repeat, e fact separado de `ignore_cost`.
- teste que deveria existir: `Wallop` e `Call to Glory` devem ter `additional_cost spend_buff` e `ignore_cost self_spell`; `Meditation` deve ter optional exhaust; `Cruel Patron`/`Legion Quartermaster` devem ter mandatory additional cost.

### 6. Resource synergy downstream truncada e com falsos positivos

- categoria do achado: integracao entre etapas
- severidade: alta
- confianca: alta
- evidencia: havia 31 producers de XP e so 3 XP costs nos facts; `cost:xp` nao aparece nas relacoes. Resource synergy envolvendo cartas-alvo so conectou producers de energia a `Emperor's Dais` e `Vex`; `Vex` e falso positivo. `Power Nexus`/`Altar` nao conectam a producers de `:rb_rune_rainbow:`. `Jhin`/`Honeyfruit` com `[Add] :rb_energy_1::rb_rune_rainbow:` so geram o primeiro recurso.
- regra relacionada: `cost_keys_from_fact()`/`output_keys_from_fact()` so indexam energy/rune, ignoram XP; `resource_from_symbol()` normaliza rainbow para `any`, mas `symbol_costs()` mantem `rainbow`; `add_resource` captura so um simbolo apos `[Add]`.
- impacto provavel no produto final: sinergias XP e rune-any somem; sinergias falsas aparecem a partir de custos falsos; multiplos recursos adicionados sao truncados.
- recomendacao: normalizar `rainbow`/`any` nos dois lados, indexar XP ou criar eixo `xp_progression`, capturar todos os simbolos em `[Add]`, e so gerar resource synergy para facts de custo reais.
- teste que deveria existir: `Gold`/`Honeyfruit`/`Jhin` devem conectar a custos rune-any; XP gainers devem conectar a XP spenders; `Vex` nao deve receber resource synergy como consumidor.

## Comandos principais

- `rg --files`
- `git status --short`
- `rg -n "activation_cost|additional_cost|Spend XP|no more than|or more|costs? more|ignore.*cost|resource" ...`
- consultas Python somente leitura em `cards_normalized.json`, `cards_semantic_facts.jsonl` e `cards_card_relations.jsonl`
- `Get-Content ... core-rules.md | Select-Object ...`
- `Select-String -Path cards_normalized.json ...`
- `Select-String -Path cards_semantic_facts.jsonl ...`

## Goldens positivos

- `Blood Rose`: `Spend 3 XP, :rb_exhaust::` => cost `{xp:3}` + exhaust.
- `Voidreaver`: duas activations, `{xp:1}+exhaust` e `{xp:2}+exhaust`.
- `Keeper of the Hammer`: `{xp:3}+exhaust`.
- `Altar of Blood`: optional pay-to replacement com 3 rune-any, sem truncamento.
- `Power Nexus`: optional pay-to score com 4 rune-any.
- `Defy`: `counter spell` com constraints `energy <= 4` e `rune-any <= 1`.
- `Lux`/`Lady`: trigger de spell played com threshold `printed energy >= 5`.
- `Vaults of Helia`: `increase_cost` de unidades non-token em +1 energy.
- `Vex, Cheerless`: dois modifiers separados, friendly less e enemy more.
- `Honeyfruit`/`Jhin`/`Malzahar`: `[Add]` com multiplos simbolos deve gerar todos os recursos.

## Goldens negativos

- Nao gerar `activated_ability_cost` para `Karma, Channeler` trigger de recycle.
- Nao gerar `activated_ability_cost` para `Lux`/`Lady` cost threshold.
- Nao gerar `reduce_cost` para `Defy` `no more than`.
- Nao gerar `reduce_cost` para `Vaults` `more`.
- Nao gerar `resource_synergy` energy producer -> `Vex` por custo falso.
- Nao truncar o ultimo simbolo antes de `to`.
- Nao tratar `ignore cost` como `reduce_cost`.
