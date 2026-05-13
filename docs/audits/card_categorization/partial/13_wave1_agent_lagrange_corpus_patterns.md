# Onda 1 - agente Lagrange - novos padroes de risco no corpus

## Escopo

Auditoria nao mutante de padroes textuais recorrentes no corpus normalizado. O agente leu:

- `data/processed/cards/normalized/cards_normalized.json`
- `data/processed/cards/semantic/cards_semantic_facts.jsonl`
- `scripts/04_cards_feature_extraction/contracts/semantic_extraction_rules.json`
- `scripts/04_cards_feature_extraction/contracts/feature_relation_taxonomy.json`

O agente informou que nao editou arquivos.

## Inventario do corpus

- 767 cartas.
- 1248 linhas de texto.
- 5428 fatos semanticos.
- Regras atuais: 23 trigger, 5 condition, 4 cost, 100 effect, 1 reminder.

## Resumo por padrao

| Padrao | Linhas | Sinal principal |
| --- | ---: | --- |
| `instead` | 23 | efeitos aparecem como `return_to_hand`/`damage`/`draw`, mas quase nunca como replacement |
| `would` | 13 | so Zilean emite `replacement_effect`; 12 perdem prevencao/substituicao |
| `can't/cannot/don't` | 62 | restricoes ausentes ou invertidas em evento positivo |
| `choose one` | 7 | nenhum padrao em regras; headers modais ficam sem semantica |
| `up to` | 20 | ha fatos, mas cardinalidade/escopo frequentemente ficam no `raw` ou duplicam parse |
| `additional cost` | 83 | so 14 linhas emitem `additional_cost`; muitas variantes ficam como custo generico ou sem vinculo |
| `more/less` | 86 | `cost ... more` vira `reduce_cost`; thresholds viram reducao falsa |
| `copy` / `becomes` | 6 / 6 | token-copy e attached-copy incompletos |
| `swap` | 1 | sem fato |
| `while attached` | 1 exato | coberto no caso exato, mas familia `attached` ainda tem lacunas |
| `ready token` | 10 | bem coberto; risco residual em interacao com copy/temporary |

## Achados

### A-01 - `would` + `instead` nao modela replacement/prevention

- categoria do achado: regra ausente
- severidade: alta
- confianca: alta
- evidencia: a taxonomia tem `replacement_effect`, `polarity: replacement/prevention`, mas as regras so cobrem casos estreitos como Zilean. Exemplos com fato de efeito, mas sem fato de substituicao: `Altar of Blood`, `Guardian Angel`, `Zhonya's Hourglass`, `Highlander`, `Tactical Retreat`, `Smite`, `Soraka, Wanderer`. `Counter Strike` perde o `prevent it`; `Void Hatchling` perde a substituicao de reveal.
- regra relacionada: familia `replacement_effect`; regras para `would`/`instead`.
- impacto provavel no produto final: relacoes tratam recall/banish/draw como efeito normal e perdem que o evento original foi impedido/substituido.
- recomendacao: criar regras especificas para `would ... instead`, `the next time ... prevent`, `if ... would ...` e diferenciar efeito produzido de replacement.
- teste que deveria existir: goldens para `Guardian Angel`, `Counter Strike`, `Soraka, Wanderer` e `Void Hatchling`.

### A-02 - Negacao (`can't/don't`) ausente ou invertida

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: exemplos sem restricao util: `Rockfall Path` (`Units can't be played here`), `Tianna Crownguard` (`opponents can't gain points`), `Maduli` (`I can't be readied`), `Noxus Saboteur` (`can't be revealed`), `LeBlanc Everywhere` (`don't trigger`), `Brynhir` (`opponents can't play cards`), `Lilting Lullaby` (`controller can't play spells`). Mais grave: algumas negacoes viram evento positivo de movimento: `Vilemaw's Lair`, `Determined Sentry`, `Minotaur Reckoner`, `Vex, Apathetic`.
- regra relacionada: negative guards; familias `restriction_or_permission`, `movement_modifier`, `ready_exhaust_effect`.
- impacto provavel no produto final: cartas restritivas sao categorizadas como produtoras dos eventos proibidos ou ficam sem categoria.
- recomendacao: adicionar guards de negacao e regras de restricao para `can't/don't`.
- teste que deveria existir: goldens negativos para movimento em `Determined Sentry` e `Vilemaw's Lair`; goldens positivos de restricao para `Rockfall Path`, `Maduli` e `Brynhir`.

### A-03 - `choose one` modal nao existe como semantica

- categoria do achado: regra ausente
- severidade: alta
- confianca: alta
- evidencia: sem regra para headers/opcoes. Ficam descobertas: `Disposal Order`, `Flurry of Feathers`, `Curtain Call`, `Rocket Barrage`. `Udyr` e `Aphelios` tem trigger/cost, mas nao tem fato de modo escolhido nem memoria de `nao escolhido antes`.
- regra relacionada: `choice_modal`, `modal_option`.
- impacto provavel no produto final: similaridade e UI nao conseguem agrupar cartas modais nem diferenciar escolha de alvo vs escolha de modo.
- recomendacao: preservar e extrair grupos modais com `choice_group_id`, `option_index`, `selection_constraint`.
- teste que deveria existir: goldens para `Curtain Call`, `Rocket Barrage` e `Disposal Order`.

### A-04 - `copy` / `becomes` / attached-copy incompletos

- categoria do achado: regra ausente
- severidade: alta
- confianca: media
- evidencia: `Svellsongur` nao tem fato para `copy that unit's text ... for as long as this is attached`. `Deceiver`, `Mirror Image` e `Keeper of Masks` criam Reflection token, mas nao emitem copy para `becomes a copy`. `Reflection` e `Zilean` estao cobertos, mas sao padroes estreitos. Tambem ha lacunas em attached: `Grandmaster at Arms` so tem custo, `Gearhead` fica sem fato, `Brutalizer` perde condicao estruturada de attachment.
- regra relacionada: `copy_effect`, `token_creation`, `attachment`.
- impacto provavel no produto final: cartas de copia/token-copy nao se relacionam corretamente e podem parecer apenas token generators.
- recomendacao: criar regras para `becomes a copy`, `copy text`, `for as long as attached`, e contexto do host anexado.
- teste que deveria existir: goldens para `Svellsongur`, `Mirror Image`, `Deceiver`, `Keeper of Masks`.

### A-05 - `up to` tem cobertura superficial

- categoria do achado: categorizacao incorreta
- severidade: media
- confianca: media
- evidencia: todas as 20 linhas tem algum fato, mas ha perdas concretas: `Targon's Peak` e `Dark Child` tratam ready de runas como `unit_ready`; `Forge of the Future` perde `Recycle up to 4`; `Moonfall`/`Flash` duplicam `move` com target `up`; `Piercing Light` perde o segundo alvo; `Salvage` perde `kill up to one gear`; `Elder Dragon` perde a escolha por localizacao.
- regra relacionada: quantificadores/cardinalidade; `move_unit`, `ready_unit`, `recycle_card`, `kill_gear`.
- impacto provavel no produto final: quantidades e escopos opcionais ficam errados ou incompletos.
- recomendacao: modelar cardinalidade (`max_targets`) e alvo plural/opcional de forma estruturada, e bloquear regex legado que captura `up` como target.
- teste que deveria existir: goldens para `Targon's Peak`, `Forge of the Future`, `Moonfall`, `Piercing Light`, `Salvage`.

### A-06 - `additional cost` so cobre um formato estreito

- categoria do achado: regra ausente
- severidade: media
- confianca: alta
- evidencia: a regra cobre bem `You may {verb} ... as an additional cost to play me/this`, mas falha em `As an additional cost...`, `As you play...`, `[Accelerate] ... enter ready`, e payoff condicionado por `if you paid the additional cost`. Exemplos: `Sacrifice`, `Heedless Resurrection`, `Meditation`, `Wallop`, `Call to Glory`, `Kraken Hunter`, `Brazen Buccaneer`, `Legion Quartermaster`, `Stalking Wolf`, `Commander Ledros`.
- regra relacionada: `additional_cost_to_play_self`, `cost_or_requirement`.
- impacto provavel no produto final: custos adicionais e payoffs condicionados ficam desconectados.
- recomendacao: separar custo adicional de payoff condicionado por custo; expandir formas gramaticais.
- teste que deveria existir: goldens para `Sacrifice`, `Meditation`, `Wallop`, `Kraken Hunter`.

### A-07 - `more/less` mistura threshold, desconto e aumento de custo

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Vaults of Helia` e `Vex, Cheerless` tem custo `more`, mas saem como `reduce_cost`. Thresholds como `costs :rb_energy_5: or more` ou `cost no more than` geram `generic_cost_reduction` ou `activation_cost` indevidos: `Lady of Luminosity`, `Defy`, `Fate Weaver`, `Lux, Illuminated`, `Fizz`, `Rell`, `Jayce`, `Glasc Mixologist`.
- regra relacionada: `generic_cost_reduction`; familia `cost_modifier`.
- impacto provavel no produto final: falso positivo forte em relacoes de desconto/custo.
- recomendacao: dividir custo em threshold, condicao, reducao, ignorar custo e aumento.
- teste que deveria existir: goldens negativos para `Lady of Luminosity`, `Defy`, `Lux, Illuminated`, `Vaults of Helia`.

### A-08 - `swap` de stat sem fato

- categoria do achado: regra ausente
- severidade: media
- confianca: alta
- evidencia: `Switcheroo` (`Swap the Might of two units...`) nao emite fato. A taxonomia menciona swap em movimento, mas nao ha regra para troca de stat.
- regra relacionada: `stat_modifier`, `swap`.
- impacto provavel no produto final: cartas de troca de Might nao entram em filtros/relacoes de modificacao de stat.
- recomendacao: criar predicado `swap_stat` com `stat: might`, dois alvos e duracao.
- teste que deveria existir: golden para `Switcheroo`.

## Candidatas para goldens negativos

| Carta | Motivo do golden negativo |
| --- | --- |
| `The Candlelit Sanctum` | `don't back` nao deve virar restricao `prevent` |
| `Warmog's Armor` / `Cithria` | `don't have a buff` e condicao, nao proibicao |
| `Seal of Strength` / `Honeyfruit` / `Gold` | reminder `can't be reacted to` nao deve virar lock especifico da carta sem escopo |
| `King's Edict` | `you don't control` e `hasn't been chosen` nao sao modal `choose one` |
| `Blind Fury` | `Choose one and banish it` e escolha de alvo/card, nao header modal |
| `Irelia, Graceful` | `spells that choose me` nao e modal choice |
| `Baited Hook` | `Might up to 1 more than...` e threshold, nao contagem de alvo |
| `Lady of Luminosity` / `Lux, Illuminated` | `costs N or more` nao deve virar `reduce_cost` |
| `Defy` / `Spectral Matron` | `cost no more than` e filtro de alvo/play, nao desconto |
| `Vaults of Helia` / `Vex, Cheerless` | `cost more` deve ser aumento, nunca `reduce_cost` |
| `The Academy` / `Temporal Portal` / `Syndra` | Repeat reminder nao e additional cost de play-self |
| `Conscription` / `Safety Inspector` | `if paid additional cost` e condicao de payoff, nao novo custo |
| Weaponmaster cards | `even if already attached` nao e `while attached` modifier |
| `Targon's Peak` | `ready up to 2 runes` nao deve virar token/unit ready |
| `Zilean, Time Mage` | `additional copy` replacement nao e `becomes a copy` |
| `Reflection` | `don't get play effects` deve proteger contra copy-rule generica excessiva |
