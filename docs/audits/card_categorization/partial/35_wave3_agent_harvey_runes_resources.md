# Onda 3 - agente Harvey - runas, recursos, XP e sinergias

## Escopo

Auditoria nao mutante da onda 3 sobre runas, recursos, XP, Add/Channel/Recycle e sinergias.

O agente informou que nao editou arquivos. `git status --short` mostrou apenas `M goal.md` e `?? docs/`, sem edicoes dele.

## Achados

### 1. Basic Runes viram cartas vanilla

- categoria do achado: regra ausente
- severidade: alta
- confianca: alta
- evidencia: `Body/Calm/Chaos/Fury/Mind/Order Rune` tem so `has_card_type` e `has_domain`; zero `add_resource`, zero `recycle`, zero relacoes. Mas `core-rules.md` 163.2 define duas habilidades sempre presentes: exhaust para Add energia e recycle para Add poder do dominio.
- regra relacionada: regras oficiais de Basic Runes.
- impacto provavel no produto final: runas basicas nao aparecem como fontes centrais de recursos.
- recomendacao: injetar fatos normativos para Basic Runes a partir do tipo/dominio.
- teste que deveria existir: cada Basic Rune deve emitir `[E] -> add 1 energy` e `Recycle this -> add 1 rune:<domain>`.

### 2. `[Add]` com multiplos simbolos e truncado

- categoria do achado: parsing/normalizacao
- severidade: alta
- confianca: alta
- evidencia: no corpus ha 26 linhas com `[Add]`; 3 tem multiplos simbolos e as 3 perdem output:
  - `Honeyfruit` Level 6: texto `[Add] :rb_energy_1::rb_rune_rainbow:`; fato so `energy=1`.
  - `Jhin, Murderous Artist`: mesmo truncamento.
  - `Malzahar, Fanatic`: texto adiciona duas `:rb_rune_rainbow:`; fato so uma.
- regra relacionada: `semantic_extraction_rules.json` `add_resource` captura um unico `symbol`.
- impacto provavel no produto final: filtros e sinergias de output ficam incompletos.
- recomendacao: capturar todos os simbolos em `[Add]`.
- teste que deveria existir: `[Add] :rb_energy_1::rb_rune_rainbow:` deve gerar dois amounts; `[Add] :rb_rune_rainbow::rb_rune_rainbow:` deve gerar dois rune-any ou amount 2.

### 3. `Spend N XP` continua quebrado em custos ativados

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: 12 linhas contem `Spend N XP`; so 3 linhas geram payload de custo XP. As 4 activations de `Blood Rose`, `Voidreaver` e `Keeper of the Hammer` geram custo apenas com `exhaust`, apesar da evidencia conter `Spend N XP`.
- regra relacionada: custos de XP; `activation_cost`.
- impacto provavel no produto final: XP gainers so se relacionam por similaridade entre si; nao habilitam consumidores de XP. `resource_synergy` envolvendo XP: 0.
- recomendacao: parsear `Spend N XP` em custos e incluir XP em relacoes ou eixo `xp_progression`.
- teste que deveria existir: `Blood Rose` `{xp:3}+exhaust`; `Voidreaver` `{xp:1}+exhaust` e `{xp:2}+exhaust`; `Keeper of the Hammer` `{xp:3}+exhaust`; `Crowd Favorite`/`Megatusk`/`Enthralling Protector` tambem devem emitir custo XP.

### 4. `rainbow` vs `any` quebra rune-any downstream

- categoria do achado: integracao entre etapas
- severidade: alta
- confianca: alta
- evidencia: outputs de Add normalizam `:rb_rune_rainbow:` para `domain:any`, mas custos vindos de `symbol_costs()` ficam `domain:rainbow`. `build_card_relations.py` tambem ignora `domain:any` em `cost:rune:*`. Resultado: 11 produtores de rune-any, incluindo `Gold`, `Honeyfruit`, `Malzahar`, `Ancient Henge`, geram 0 `resource_synergy`.
- regra relacionada: normalizacao de rune-any/rainbow; `resource_synergy`.
- impacto provavel no produto final: `Gold` nao conecta a consumidores rune-any; `Power Nexus`/`Altar of Blood` nao conectam a produtores rainbow/any.
- recomendacao: normalizar `rainbow` e `any` no mesmo dominio em outputs, custos e relation keys.
- teste que deveria existir: `Gold -> Power Nexus`, `Honeyfruit -> Power Nexus`, `Ancient Henge -> Power Nexus` devem ter relacao de recurso por `rune:any`.

### 5. Custos condicionais e variaveis estao sendo classificados/truncados

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia:
  - `Power Nexus` tem 4 `:rb_rune_rainbow:` no texto, mas payload captura 3.
  - `Altar of Blood` tem 3, payload captura 2.
  - `Ancient Henge` tem custo `Pay any amount of Energy`, mas o custo emitido e so `exhaust`.
  - `Malzahar` perde o custo `Kill a friendly unit or gear`; so `exhaust` entra como custo.
- regra relacionada: `activation_split()` divide por `": "` e corta simbolo final; `parse_non_symbol_costs()` cobre `Kill this`, mas nao `Kill a friendly unit or gear` nem energia variavel.
- impacto provavel no produto final: custos reais somem; alguns efeitos de custo aparecem como outputs soltos.
- recomendacao: parser de custos variaveis e condicionais com escopo proprio, sem usar split fragil.
- teste que deveria existir: `Power Nexus` deve ter 4 rune-any; `Altar of Blood` 3 rune-any; `Ancient Henge` deve ter custo variavel de energia e output variavel rune-any; `Malzahar` deve ter custo kill unit/gear + exhaust.

### 6. Channel/Recycling: um falso positivo e um controle positivo

- categoria do achado: categorizacao incorreta
- severidade: media
- confianca: alta
- evidencia: `Catalyst of Aeons` gera dois facts `channel`: um para `Channel 2 runes exhausted` e outro falso para `If you couldn't channel 2 runes this way`. Ja `Sigil of the Storm -> Battle Mistress` funciona corretamente via `rune_recycled_enables_rune_recycled`.
- regra relacionada: `channel_rune`; `rune_recycled_enables_rune_recycled`.
- impacto provavel no produto final: Channel pode duplicar outputs em textos com condicao negativa.
- recomendacao: negative guard para `couldn't channel`, mantendo relacoes positivas de recycle.
- teste que deveria existir: nao emitir `channel` a partir de `couldn't channel`; manter `Sigil of the Storm` habilitando `Battle Mistress`.

## Comandos principais

- `rg --files`
- `git status --short`
- `rg -n "(basic rune|rune|gold|channel|recycle|xp|\\[add\\]|rainbow|cost)" ...`
- leituras com `Get-Content` de `core-rules.md`, contracts, reports e `build_card_relations.py`
- consultas Python somente leitura em `cards_normalized.json`, `cards_semantic_facts.jsonl`, `cards_card_relations.jsonl` e reports web/semantic

## Goldens prioritarios

Positivos:

- Basic Runes
- `Gold`
- `Honeyfruit`
- `Jhin`
- `Malzahar`
- `Ancient Henge`
- `Power Nexus`
- `Blood Rose`
- `Voidreaver`
- `Keeper of the Hammer`
- `Sigil of the Storm -> Battle Mistress`

Negativos:

- nao truncar simbolo final antes de `to`;
- nao gerar segundo `channel` em `couldn't channel`;
- nao tratar Basic Runes como vanilla;
- nao deixar `rune:any` sem resource synergy;
- nao passar golden apenas por fato minimo quando custos/relacoes essenciais estao ausentes.
