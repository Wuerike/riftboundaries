# Tasks - melhoria das relacoes entre cartas

Este plano foi montado a partir de `00_consolidated_audit.md` e de uma
verificacao somente leitura nos contratos, scripts, reports processados e
frontend. Nenhuma correcao de pipeline havia sido executada naquele momento.

## Base usada para priorizacao original

- Dataset do baseline original: `767` cartas, `5428` fatos e `9884` relacoes.
- Relacoes broad: `3438`, `34.78%` do grafo, dominadas por
  `spell_card_can_be_countered`.
- `deck_synergy`: `1056` relacoes no dataset, mas nao renderizadas pelo
  frontend atual.
- Lacunas do baseline original: `100` cartas sem relacao, `22` broad-only, `104` cartas com
  texto rico sem relacao util, `736` fatos candidatos nao usados por relacoes.
- Proveniencia dos fatos: `3011` estruturais, `1759` por contrato e `658`
  legados.
- Arquivos de maior impacto:
  - `scripts/04_cards_feature_extraction/extract_semantic_facts.py`
  - `scripts/04_cards_feature_extraction/build_card_relations.py`
  - `scripts/04_cards_feature_extraction/contracts/semantic_extraction_rules.json`
  - `scripts/04_cards_feature_extraction/contracts/semantic_relation_rules.json`
  - `scripts/04_cards_feature_extraction/contracts/feature_relation_taxonomy.json`
  - `scripts/04_cards_feature_extraction/contracts/semantic_quality_policy.json`
  - `scripts/05_web_dataset/build_card_explorer_dataset.py`
  - `scripts/05_web_dataset/audit_card_explorer_dataset.py`
  - `web/app/app.js`

## Status apos implementacao

- Dataset regenerado em 2026-05-13: `767` cartas, `6311` fatos e `14590`
  relacoes.
- Relacoes high-signal: `9701`; relacoes broad: `4889` (`33.51%`).
- Lacunas atuais: `42` cartas sem relacao, `0` broad-only, `0` cartas com
  linhas relacionais descobertas sem fato e `501` fatos candidatos ainda nao
  usados por relacoes. Desses, `232` sao acionaveis no report: `220` pedem
  regra de relacao, `1` pede correcao de extracao e `11` sao `weak_fact`;
  outros `269` entram como `intentional_ignored`.
- Validacao: `73/73` exemplos dourados, `90` fixtures de regressao,
  `119` expected facts, `51` forbidden facts, `46` expectativas de relacao,
  `16` invariantes de relacao, `6` invariantes de dataset, invariantes verdes,
  auditoria semantica com `0` erros, `179` warnings e `0.984` de cobertura.
- Broad-only restantes: nenhum.
- Rodada auditada: custo/desconto. `Atakhan` e `Poppy, Defender of the
  Meek` nao emitem mais pagamento de Energy falso a partir de texto "cost less";
  `Raging Firebrand` preserva alvo `spell`, controlador `you` e duracao
  `this_turn`; descontos grandes entram em `similar_effect` por
  `secondary:cost_reduction`.
- Rodada seguinte auditada: trigger de vitoria em combate. `When I/you win a
  combat` emite `combat_won`, `Glorious Executioner` se conecta a outros draws
  por `when=combat_won`, e relacoes com contexto registram
  `match.supporting_fact_ids` para que triggers usados como contexto nao contem
  como fatos soltos.
- Rodada seguinte auditada: contexto de custos em similaridade. Custos na mesma
  clausula entram em chaves `:cost=...` e em `match.supporting_fact_ids` apenas
  quando a relacao contextual e emitida; isso reduziu `pay`/`exhaust` soltos e
  derrubou `attachment/copy` sem relacao de `39` para `2` sem aumentar broad.
- Rodada seguinte auditada: contexto de requisitos em similaridade. Fatos
  `require` com estados como `while_attacker` entram em chaves `:require=...`
  da mesma clausula e em `match.supporting_fact_ids`; isso reduziu `require`
  soltos de `41` para `36` sem aumentar broad.
- Rodada seguinte auditada: matriz acionavel de fatos soltos. Triggers de ciclo
  listados em `relation_event_ignore` agora sao classificados como
  `intentional_ignored`, e `Draw 1` obrigatorio sem contexto especifico tambem
  e tratado como skip amplo intencional. Custos de ativacao apenas com
  `:rb_exhaust:` do proprio card tambem sao contexto; isso separa os fatos
  nao acionaveis dos que ainda pedem regra, correcao de extracao ou triagem.
- Rodada seguinte auditada: cobertura de duplicatas de fatos relacionais.
  Duplicatas equivalentes de `reduce_cost` agora herdam cobertura quando uma
  copia ja foi usada em relacao; isso reduziu fatos soltos de `439` para `414`
  e reduziu `reduce_cost` acionavel de `39` para `14`.
- Rodada seguinte auditada: priorizacao da matriz P1.1. O report agora separa
  `top_actionable_unlinked_predicates` de `top_needs_relation_rule_predicates`;
  `require` ficou majoritariamente como `needs_extraction_fix` (`34`) por
  faltar efeito condicional extraido na mesma linha.
- Rodada seguinte auditada: custos malformados na matriz. Custos cujo payload
  contem mais simbolos gerados do que a evidencia mostra entram como
  `needs_extraction_fix`; em seguida o parser deixou de gerar simbolos falsos
  como `pay :rb_rune_fury:`, derrubando as correcoes de extracao restantes para
  `34` fatos `require` sem efeito extraido na mesma linha.
- Rodada seguinte auditada: duplicatas de custos e sinergia de XP. Duplicatas
  `pay`/`spend` na mesma linha herdam cobertura quando uma copia equivalente ja
  foi usada, e `gain_xp`/custos de XP agora geram `deck_synergy` exata por
  `cost:xp:N`; isso adicionou `75` relacoes high-signal sem novo broad reason.
- Rodada seguinte auditada: proveniencia de dedupe. Relacoes colapsadas por
  mesma carta/razao agora preservam os `source_fact_id`/`target_fact_id`
  colapsados em `match.supporting_fact_ids`, entao o auditor nao trata fatos
  cobertos por relacao deduplicada como soltos.
- Rodada seguinte auditada: enablement de triggers observados. `friendly_unit_dies`
  agora habilita triggers `self_dies`, e `equipment_attached` habilita triggers
  de attach; isso adicionou `582` relacoes high-signal sem novo broad reason e
  reduziu `observe_event` em `needs_relation_rule` de `18` para `3`.
- Rodada seguinte auditada: sinergia parcial de Energy. Produtores de Energy
  agora se conectam a custos de Energy `3+` por `cost:energy:partial` com
  cobertura `partial` e strength reduzida; isso adicionou `60` relacoes
  high-signal sem novo broad reason e reduziu `pay` em `needs_relation_rule` de
  `5` para `2`.
- Rodada seguinte auditada: similaridade de caps/thresholds de custo. Restricoes
  `cost_cap_constraint` e `cost_threshold` entram em similaridade por chave de
  custo estavel, sem virar `resource_synergy`; isso adicionou `6` relacoes
  high-signal e reduziu caps/thresholds soltos de `11` para `5`.
- Rodada seguinte auditada: primeira fatia P1.2 de stats/damage. Buffs
  temporarios de Might em si mesmo, modificadores attached-only, escalas
  variaveis de Might e dano escalado por Might entram em chaves secundarias
  especificas; isso adicionou `26` relacoes high-signal e novas expectativas
  para Draven/Kha'Zix, Brutalizer/Soul Sword, Dr. Mundo/Draven e dano por Might.
- Rodada seguinte auditada: primeira fatia P1.3 de play-from-zone. Efeitos que
  jogam unidade, spell ou gear de `hand`, `trash` ou `banished` agora entram em
  similaridade por zona, tipo e modificador de custo quando houver pares
  compativeis; isso adicionou `22` relacoes high-signal e cobriu exemplos como
  The Harrowing/Undying Loyalty, Here to Help/Rift Herald e Fizz/Annie.
- Rodada seguinte auditada: primeira fatia P1.2 de grants por keyword. Grants
  com multiplas keywords agora tambem emitem chaves secundarias por keyword,
  familia de alvo, duracao, modalidade e contexto; isso adicionou `26` relacoes
  high-signal, conectou `Block` a grants temporarios de Shield/Tank e reduziu
  `gain_keyword` em `needs_relation_rule` de `7` para `6`.
- Rodada seguinte auditada: enablement de self-discard. Efeitos de descarte sem
  alvo parseado agora habilitam triggers `self_discarded`, mantendo fora efeitos
  de descarte com alvo explicito; isso adicionou `40` relacoes high-signal e
  reduziu `observe_event` em `needs_relation_rule` de `3` para `2`.
- Rodada seguinte auditada: sinergia parcial de XP. Produtores de XP agora se
  conectam a custos de XP `4+` por `cost:xp:partial`, com cobertura `partial`
  e strength reduzida; isso adicionou `30` relacoes high-signal e reduziu
  `spend` em `needs_relation_rule` de `3` para `2`.
- Rodada seguinte auditada: descontos pequenos de Energy. Reducoes exatas de
  custo `1` ou `2` Energy agora entram em similaridade secundaria apenas quando
  ha familia de alvo nao generica (`spell`, `unit`, `gear` etc.); isso adicionou
  `4` relacoes high-signal, conectou `Irelia`/`Vex` e `Monch`/`Spoils of War`,
  reduziu cartas sem relacao de `48` para `46` e reduziu `reduce_cost` em
  `needs_relation_rule` de `14` para `6`.
- Rodada seguinte auditada: custos de Deflect pagos por oponente. Custos com
  evidencia `Opponents must pay` nao entram mais em `resource_synergy`, contexto
  de custo ou chaves `:cost=...`; eles sao classificados como
  `intentional_ignored`, removendo falsos hubs de `cost:rune:any` enquanto
  relacoes reais de keyword Deflect continuam por `keyword_grant`.
- Rodada seguinte auditada: consistencia de reports web. O builder do dataset
  passou a usar matching token-aware para keywords relacionais, alinhando
  `cards_with_uncovered_relational_lines` com a auditoria e evitando falso
  positivo como `ready` dentro de `already`.
- Rodada seguinte auditada: self-scaling Might e permissao de movimento. Efeitos
  de Might escalado em si mesmo agora conectam `Dr. Mundo`, `Draven`, `Ornn`,
  `Petal Pixie` e `Sett, Kingpin`; efeitos que movem unidades amigas agora
  geram `deck_synergy` para `Stealthy Pursuer`. Isso adicionou `36` relacoes
  high-signal sem novo broad reason, reduziu cartas sem relacao de `49` para
  `46`, `movement/location` em `needs_relation_rule` de `17` para `15` e
  `stat/buff/damage_modifier` de `17` para `14`.
- Rodada seguinte auditada: `combat_might_modifier` para Assault/Shield
  intrinsecos. Reminders `[Assault]`/`[Shield]` agora emitem fatos
  `modify_stat` condicionados por `while_attacker`/`while_defender`;
  similaridade preserva o contexto de combate, inclusive em Equipment
  attached-only, e a regressao impede relacoes entre attacker/defender
  disjuntos. Isso adicionou `35` fatos e `202` relacoes high-signal sem novo
  broad reason, reduziu cartas sem relacao de `46` para `39` e deixou apenas
  `1` `needs_extraction_fix`.
- Rodada seguinte auditada: trigger de movimento de unidade inimiga. `When you
  move an enemy unit` agora emite trigger `unit_moved` em vez de tambem virar
  movimento produzido; cartas que movem unidades inimigas, como `Temptation`,
  geram `deck_synergy` para `Blast Cone`. Isso removeu o falso produtor da
  linha de trigger, adicionou `16` sinergias direcionadas e fechou a rodada em
  `15196` relacoes, `10450` high-signal e `112` warnings semanticos.
- Rodada seguinte auditada: Bonus Damage e modificadores de dano. Fatos
  `bonus_damage_added`/`damage_modified` nao caem mais na chave generica
  `secondary:stat_family`, e similaridade de dano preserva amount, fonte do
  dano, alvo, duracao, modalidade e contexto. Isso removeu falsos links entre
  `Ravenborn Tome` e efeitos permanentes de Bonus Damage; `Ravenborn Tome`
  continua sem relacao ate haver uma regra precisa para "next spell" ou spells
  que causam dano. A rodada fecha em `15188` relacoes e `10442` high-signal.
- Rodada seguinte auditada: falso grant de `[Stun]`. `Heroic Charge` preserva
  o evento produzido `stun` e o buff de Might, mas nao emite mais
  `gain_keyword` para `[Stun]`, que e acao/estado e nao keyword concedida.
  Isso removeu `1` fato falso, baixou `stat/buff/damage_modifier` solto de
  `21` para `20` e voltou a matriz para `337` candidatos sem relacao.
- Rodada seguinte auditada: keywords concedidas. As chaves genericas
  `secondary:keyword:*` foram removidas de `keyword_grant`; grants agora usam
  `keyword`, familia de alvo, duracao, modalidade e contexto, com expansao de
  alvos multi-kind como `gear+unit` para familias individuais. Isso removeu
  links falsos por keyword isolada, preservou o par preciso
  `Fading Memories`/`Turn to Dust` por `Temporary` em `gear`, adicionou um
  invariante de relacao para grants e fechou a rodada em `15048` relacoes,
  `10302` high-signal, `46` cartas sem relacao e `0` broad-only.
- Rodada seguinte auditada: contexto intrinseco de keywords de combate.
  `Assault` e `Shield` agora podem alinhar chaves de `keyword_grant` pelo
  contexto semantico do proprio keyword (`while_attacker`/`while_defender`)
  mesmo quando so um lado tem fato `require` extraido. Isso conectou
  `Lord Broadmane` a grants temporarios de `Assault`, manteve `Block`/`Chakram
  Dancer` em contexto de defensor e fechou a rodada em `15056` relacoes,
  `10310` high-signal, `45` cartas sem relacao e `0` broad-only.
- Rodada seguinte auditada: contrato broad no dataset. Relacoes classificadas
  como broad por threshold ou flag explicita agora saem no dataset publicado
  com `match.broad=true` e `match.broad_reason`; a suite ganhou invariante de
  dataset para impedir regressao. `Not So Fast` e `Repulse` continuam com
  `398` relacoes broad cada, mas so `2` high-signal entram nas lanes padrao.
- Rodada seguinte auditada: fechamento P0.7. O arquivo de relacoes emitido nao
  possui duplicatas exatas nem duplicatas visuais por `(source, target, tipo,
  reason)`; relacoes colapsadas preservam ids em `supporting_fact_ids` e o
  report publica `duplicate_relation_candidates=1508` e
  `collapsed_relations=1508`. `derived_synergy` esta desabilitado e coberto por
  invariante para nao duplicar `enables`.
- Rodada seguinte auditada: fechamento P0.3. `Altar of Blood` agora extrai o
  custo opcional de tres runas pago pelo controlador do objeto afetado, e
  `cost_polarity_and_resource_synergy_are_consistent` bloqueia regressao em
  `cost more` como `reduce_cost`, caps como pagamentos e `resource_synergy`
  apontando para fatos que nao sao custos reais. A rodada fechou em `15108`
  relacoes, `10340` high-signal, `4768` broad, `45` cartas sem relacao e `0`
  broad-only.
- Rodada seguinte auditada: fechamento P0.4. Prevent e replacement agora tem
  chaves secundarias separadas: `Counter Strike` conserva similaridade de
  prevencao de dano, enquanto `Highlander`/`Soraka`, `Guardian Angel`,
  `Zhonya's Hourglass` e `Altar of Blood` usam modo de replacement com evento
  substituido. A suite ganhou invariantes para nao misturar modos de
  replacement e para impedir que `prevented_action` emita o mesmo positivo no
  mesmo `source_ref`. A rodada fechou em `15118` relacoes, `10350`
  high-signal, `4768` broad, `45` cartas sem relacao e `0` broad-only.
- Rodada seguinte auditada: fechamento P0.1. A suite de regressao cobre os
  fixtures minimos com fatos esperados/proibidos, expectativas de relacao e
  invariantes de dataset. `Ahri, Inquisitive` entrou para travar trigger
  attack/defend e modificador negativo de Might sem falso `keyword_grant`.
- Rodada seguinte auditada: fechamento P0.5. Modalidade passou a usar contexto
  de evidencia em vez da linha inteira nos pontos criticos, `Repeat` agora sai
  como custo adicional opcional, escolhas inline como `Buhru Captain` recebem
  `choice_group_id`/`option_index`, e reminders de buff nao viram efeitos reais.
  `Valley of Idols` preserva o custo opcional de `[Buff]` sem depender do
  reminder; a rodada fechou em `14709` relacoes, `9941` high-signal, `4768`
  broad, `45` cartas sem relacao e `0` broad-only.
- Rodada seguinte auditada: fechamento P0.6. `effect_lines` de Gear/Equipment
  agora recebem contexto attached-only por padrao, textos de habilidades
  concedidas nao emitem attach/detach imediato, e as chaves secundarias de
  similaridade preservam `activation_context` para separar efeito attached-only
  de efeito sempre ativo. A rodada fechou em `14649` relacoes, `9881`
  high-signal, `4768` broad, `44` cartas sem relacao e `0` broad-only.
- Rodada final auditada: fechamento P1/P2. Recursos `[Add]` agora preservam
  multiplos simbolos, `that much`, adicionalidade e cobertura parcial;
  `similar_effect` pula chaves genericas auditaveis; familias de swap, prevent,
  score, token copy, keyword reference/grant/intrinseca e triggers de
  conquista/hold do jogador ganharam fixtures. O dataset web publica snapshot
  datado, manifest de relation types, campos obrigatorios, thresholds e fatos
  compactos por relacao; a UI exibe reason/evidence sem abrir JSON raw. A
  rodada final ficou em `6311` fatos, `14590` relacoes, `9701` high-signal,
  `4889` broad, `42` cartas sem relacao, `0` broad-only, `0` linhas
  relacionais descobertas sem fato, `73/73` goldens e invariantes verdes.

## Regra de prioridade

- P0: remove falsos positivos que hoje fazem cartas parecerem relacionadas por
  motivos errados.
- P1: cobre falsos negativos grandes, principalmente fatos bons que nao viram
  relacoes.
- P2: melhora contrato produto/dataset/frontend e reduz custo de manutencao.

## P0 - bloquear relacoes erradas antes de aumentar cobertura

- [x] P0.1 Criar uma suite de regressao que prove ausencia de relacoes/fatos
      indevidos.
  - Motivo: os goldens atuais validam presenca minima, mas nao impedem
    `reduce_cost` indevido, negacao positiva, choice simultaneo ou broad
    aparecendo como recomendacao forte.
  - Escopo provavel: `semantic_golden_examples.json`,
    `validate_semantic_golden_examples.py`, novos testes/invariantes para fatos,
    relacoes e dataset.
  - Fixtures minimas: `Vaults of Helia`, `Safety Inspector`,
    `Mageseeker Warden`, `Rockfall Path`, `Disposal Order`,
    `Dancing Grenade`, `The Academy`, `Rabadon's Deathcrown`, `Svellsongur`,
    `Counter Strike`, `Angle Shot`, `Ahri, Inquisitive`, `Ravenborn Tome`.
  - Entregaveis:
    - [x] Goldens positivos e negativos por carta.
    - [x] Invariantes de fatos para polaridade, negacao, replacement,
          modalidade, choice, attachment e evidence.
    - [x] Invariantes de relacao para broad default, dedupe, high-signal,
          broad-only e `missing_relation_rule`.
    - [x] Invariantes de dataset/frontend para todos os `relation_type`
          publicados.
  - Aceite:
    - [x] Os bugs conhecidos falham antes das correcoes e passam depois.
    - [x] Cada fixture possui expected facts e forbidden facts.
    - [x] Pelo menos uma verificacao prova que uma carta rica nao pode ficar
          degree 0 ou broad-only sem diagnostico explicito.

- [x] P0.2 Rebaixar ou ocultar por padrao as relacoes broad de
      `spell_card_can_be_countered`.
  - Motivo: `spell_card_can_be_countered` gera `3438` relacoes e cria hubs como
    `Abandon`, `Flurry of Feathers`, `Defy`, `Not So Fast` e `Repulse`. Isso
    domina a experiencia de cartas relacionadas e mascara relacoes especificas.
  - Escopo provavel: `semantic_relation_rules.json`,
    `semantic_quality_policy.json`, `build_card_relations.py`,
    `build_card_explorer_dataset.py`, `audit_card_explorer_dataset.py`,
    `web/app/app.js`.
  - Entregaveis:
    - [x] Persistir `match.broad=true` e um `broad_reason` estavel no dataset.
    - [x] Separar `relation_count`, `high_signal_relation_count`,
          `broad_relation_count` e `broad_only` no dataset.
    - [x] Frontend deve ordenar e contar por high-signal por padrao.
    - [x] Broad deve ficar em lane secundaria, toggle explicito ou final da
          ordenacao, nunca como recomendacao principal.
  - Aceite:
    - [x] `Not So Fast` e `Repulse` nao aparecem como hubs principais apenas
          por counterability.
    - [x] Relacoes broad nao entram nas lanes default/high-signal.
    - [x] O report de qualidade continua exibindo o volume broad para auditoria.

- [x] P0.3 Corrigir polaridade de custo antes de usar custo em `resource_synergy`
      ou `similar_effect`.
  - Motivo: `cost more`, `cost no more than`, thresholds e restricoes podem virar
    `reduce_cost`, criando links de desconto/recurso falsos. `Vaults of Helia`
    e o exemplo principal.
  - Escopo provavel: `extract_semantic_facts.py`,
    `semantic_extraction_rules.json`, `semantic_facts_schema.json`,
    `semantic_ontology.json`, `build_card_relations.py`.
  - Entregaveis:
    - [x] Separar `increase_cost`, `reduce_cost`, `cost_cap_constraint`,
          `cost_threshold`, `additional_cost`, `ignore_cost`, `optional_cost` e
          `cost_payment`.
    - [x] Marcar custos como pagaveis, opcionais, parciais ou restricoes de
          selecao.
    - [x] Bloquear `resource_synergy` para caps/thresholds e reducoes que nao
          sao pagamentos reais.
    - [x] Ajustar chaves para XP, Energy, runas e custos compostos.
  - Fixtures minimas: `Vaults of Helia`, `Vex, Cheerless`, `Defy`,
    `Lux, Illuminated`, `Blood Rose`, `Voidreaver`, `Power Nexus`,
    `Altar of Blood`, `Honeyfruit`, `Jhin`.
  - Nota de implementacao: `optional_cost` fica representado como
    `payload.modality=optional`; `cost_payment` fica representado por fatos
    `activated_ability_cost`/`additional_cost` com `predicate=pay|spend|...` e
    `payload.costs`.
  - Aceite:
    - [x] `cost more` nunca emite `reduce_cost`.
    - [x] `cost no more than` gera restricao/cap, nao pagamento.
    - [x] `resource_synergy` so conecta produtor a consumidor quando a saida
          cobre um custo real ou quando o score indicar cobertura parcial.

- [x] P0.4 Implementar guards comuns para negacao, restricao, prevent e
      replacement antes da emissao de eventos positivos.
  - Motivo: `can't`, `cannot`, `don't`, `prevent` e `would/instead` podem gerar
    o evento que deveriam bloquear. Isso cria relacoes exatamente opostas ao
    texto da carta.
  - Escopo provavel: `extract_semantic_facts.py`,
    `semantic_extraction_rules.json`, `semantic_facts_schema.json`,
    `audit_semantic_facts.py`, `build_card_relations.py`.
  - Entregaveis:
    - [x] Camada comum de negacao por clausula, antes das regras especificas e
          legadas.
    - [x] Fatos de `prevent` e replacement com evento substituido, output,
          duracao, alvo e modalidade.
    - [x] Regra de exclusao: `prevented_action=X` nao pode coexistir no mesmo
          `source_ref` com output positivo `X`, salvo replacement explicito.
    - [x] Diagnostic para fatos negativos que nao possuem familia relacional.
  - Fixtures minimas: `Safety Inspector`, `Mageseeker Warden`, `Rockfall Path`,
    `Counter Strike`, `Highlander`, `Guardian Angel`, `Zhonya's Hourglass`,
    `Soraka, Wanderer`, `Zilean, Time Mage`, `Vilemaw's Lair`.
  - Aceite:
    - [x] `don't kill a unit` nao gera `kill` positivo.
    - [x] `can't ready enemy units and gear` nao gera `ready` positivo.
    - [x] `Units can't be played here` nao gera evento produzido de `play`.
    - [x] Replacement/prevent gera relacoes de prevencao/substituicao, nao
          relacoes de producao do evento bloqueado.

- [x] P0.5 Preservar choices, modais e modalidade por clausula.
  - Motivo: `Choose one`, bullets modais, `or`, `not already chosen`, `you may`
    e `they may` sao achatados. Opcoes exclusivas saem como efeitos
    simultaneos e fatos obrigatorios.
  - Escopo provavel: `normalize_cards.py`, `extract_semantic_facts.py`,
    `semantic_extraction_rules.json`, `semantic_facts_schema.json`,
    `semantic_golden_examples.json`, `build_card_relations.py`.
  - Entregaveis:
    - [x] Preservar ou reconstruir grupos `choice_group_id`,
          `option_group_id`, `option_index`, `choice_mode` e exclusividade.
    - [x] Modalidade por clausula/evidencia, nao por linha inteira.
    - [x] Distinguir escolha de alvo de escolha de modo.
    - [x] Modelar `Repeat` como custo adicional e instancia repetida, sem
          duplicar efeitos como se fossem incondicionais.
  - Fixtures minimas: `Disposal Order`, `Dancing Grenade`, `The Academy`,
    `The Candlelit Sanctum`, `Unlicensed Armory`, `Rocket Barrage`,
    `Curtain Call`, `Aphelios`, `Udyr`, `King's Edict`, `Buhru Captain`.
  - Aceite:
    - [x] Opcoes exclusivas nao geram relacoes de todos os payoffs ao mesmo
          tempo.
    - [x] `you may` nao torna obrigatorio ou opcional o trecho errado.
    - [x] `they may` e `each player may` sao preservados como opcionais quando
          o texto exigir.

- [x] P0.6 Modelar `effect_lines` de Gear/Equipment como attached-only.
  - Motivo: textos de Effect Text em Gear/Equipment sao extraidos como
    modificadores ativos da carta solta. `Rabadon's Deathcrown` hoje aparece
    como modificador estatico de Bonus Damage e se liga por similaridade a
    efeitos que nao dependem de estar attached.
  - Escopo provavel: `normalize_cards.py`, `extract_semantic_facts.py`,
    `semantic_extraction_rules.json`, `semantic_facts_schema.json`,
    `build_card_relations.py`, `core-rules` como referencia.
  - Entregaveis:
    - [x] Payload padrao para `source_field=effect_lines` em Gear/Equipment com
          `activation_context=attached`, `inactive_until_attached=true` e
          `applies_to=top_most_card`.
    - [x] Relacoes de attach/detach/copy usando direcao explicita: quem equipa,
          quem recebe, o que fica ativo.
    - [x] Similaridade deve diferenciar efeito estatico global de efeito
          attached-only.
  - Fixtures minimas: `Rabadon's Deathcrown`, `Svellsongur`, `Veiled Temple`,
    `Heimerdinger, Inventor`, `Forge of the Fluft`, `Grandmaster at Arms`,
    `Spinning Axe`.
  - Aceite:
    - [x] Effect Text attached-only nao aparece como modificador incondicional.
    - [x] Relacoes de equipment conectam cartas por attach/detach/contexto
          attached, nao por bonus sempre ativo.

- [x] P0.7 Dedupar relacoes equivalentes e impedir que `derived_synergy`
      amplifique ruido.
  - Motivo: `deck_synergy` pode duplicar `enables` com a mesma evidencia e pares
    repetidos. Isso inflaciona contagem e ordenacao.
  - Escopo provavel: `build_card_relations.py`, `semantic_relation_rules.json`,
    `card_explorer_dataset_report`, `card_explorer_quality_report`.
  - Entregaveis:
    - [x] Dedupe por `(source_card, target_card, relation_type, reason,
          source_fact_id, target_fact_id)` e tambem por razao normalizada para
          visualizacao.
    - [x] `derived_synergy` so deve existir quando adiciona evidencia nova ou
          uma interpretacao diferente de deckbuilding.
    - [x] Reportar `duplicate_relation_candidates` e `collapsed_relations`.
  - Fixtures minimas: `Abandon -> Karma, Channeler`, `Adaptatron -> Mistfall`,
    `Peak Guardian -> Mistfall`.
  - Aceite:
    - [x] `deck_synergy` nao repete `enables` sem motivo novo.
    - [x] Contagens do frontend nao inflam por multiplas relacoes equivalentes.

## P1 - aumentar cobertura high-signal sem reintroduzir ruido

- [x] P1.1 Criar uma matriz de fatos candidatos nao usados por relacoes.
  - Motivo: o report aponta `2024` fatos candidatos, `350` sem relacao e `96`
    acionaveis apos separar triggers contextuais, `Draw 1` generico, custos
    `:rb_exhaust:` contextuais e custos de Deflect pagos por oponente como
    `intentional_ignored`, alem de cobrir duplicatas equivalentes ja usadas.
    Desses acionaveis, `90` sao `needs_relation_rule`, `1` como
    `needs_extraction_fix` e `5` como `weak_fact`.
    As maiores lacunas de regra por predicado sao `modify_stat`, `move`,
    `gain_keyword`, `play`, `reduce_cost`, `cost_cap_constraint`,
    `kill`, `ready`, `channel`, `spend`, `banish`, `discard`,
    `observe_event` e `prevent`.
  - Escopo provavel: `audit_card_explorer_dataset.py`,
    `build_card_relations.py`, `semantic_quality_policy.json`.
  - Entregaveis:
    - [x] Para cada predicado/familia, classificar como `needs_relation_rule`,
          `needs_extraction_fix`, `intentional_ignored` ou `weak_fact`.
    - [x] Reportar exemplos por carta e por bucket.
    - [x] Gerar uma allowlist curta para cartas realmente isoladas/vanilla.
  - Aceite:
    - [x] Toda carta rica sem high-signal possui causa acionavel.
    - [x] `missing_relation_rule` diferencia fato bom nao consumido de fato ruim.

- [x] P1.2 Adicionar familias de relacao para modificadores de stats, Might,
      damage e keywords concedidas.
  - Motivo: cartas como `Ahri, Inquisitive`, `Fiora, Peerless`,
    `Fortified Position`, `Ravenborn Tome`, `Forbidding Waste`, `Block` e
    `Chakram Dancer` tem fatos uteis, mas ficam degree 0 ou broad-only.
  - Escopo provavel: `build_card_relations.py`,
    `semantic_relation_rules.json`, `feature_relation_taxonomy.json`.
  - Entregaveis:
    - [x] Primeira fatia de similaridade secundaria para buffs temporarios de
          Might em si mesmo, modificadores attached-only, escala variavel de
          Might e dano escalado por Might.
    - [x] Primeira fatia de similaridade secundaria por keyword concedida,
          com familia de alvo, duracao, modalidade e contexto.
    - [x] Familia `combat_might_modifier` com alvo, sinal, amount, duracao e
          contexto de ataque/defesa.
    - [x] Familia `damage_modifier` para Bonus Damage e modificacao de dano
          com alvo/fonte/duracao.
    - [x] Filtro de falso `keyword_grant` para `[Stun]` quando o texto ja
          produz evento `stun`.
    - [x] Remover chaves genericas `secondary:keyword:*` para grants e
          preservar keyword, familia de alvo, duracao, modalidade e contexto,
          com familias individuais para alvo multi-kind.
    - [x] Contexto intrinseco de `Assault`/`Shield` em grants para alinhar
          `while_attacker`/`while_defender` mesmo quando o reminder nao emite
          fato `require` dos dois lados.
    - [x] Familia `keyword_grant_by_keyword` e `temporary_grant` para
          `gain/give/have [Keyword]`.
    - [x] Similaridade secundaria deve usar alvo, controlador, duracao, amount
          e keyword.
  - Aceite:
    - [x] `Ahri, Inquisitive`, `Fiora, Peerless`, `Fortified Position` e
          `Ravenborn Tome` deixam de ser degree 0 quando houver pares
          semanticamente equivalentes.
    - [x] Grants de `[Shield]`, `[Tank]`, `[Temporary]` e afins nao viram
          `has_keyword` intrinseco.

- [x] P1.3 Cobrir relacoes de movimento, zona, play restriction e localizacao.
  - Motivo: bucket `movement/location` ainda concentra `6` cartas sem relacao, e
    cartas como `Mageseeker Warden`, `Vilemaw`, `Carnivorous Snapvine`,
    `Keeper's Verdict`, `Minefield`, `The Candlelit Sanctum` e `Baron Pit`
    dependem de zona/localizacao.
  - Escopo provavel: `semantic_extraction_rules.json`,
    `build_card_relations.py`, `semantic_ontology.json`,
    `feature_relation_taxonomy.json`.
  - Entregaveis:
    - [x] Primeira fatia de similaridade secundaria para `play_from_zone`, com
          tipo da carta, zona de origem, contexto e modificador de custo.
    - [x] Trigger de movimento de unidade inimiga sem gerar evento positivo
          falso na propria clausula de trigger.
    - [x] Chaves relacionais para `movement_to_zone`, `return_to_hand`,
          `top_or_bottom_deck`, `play_to_base_only`, `cannot_play_here`,
          `battlefield_replace` e `location_permission`.
    - [x] Distinguir movimento real de restricao/permissao.
    - [x] Distinguir destino `base`, `battlefield`, `hand`, `main_deck`,
          `trash`, `banished`, `here`, `anywhere` e `top/bottom`.
  - Aceite:
    - [x] `Mageseeker Warden` e `Rockfall Path` geram relacoes de restricao,
          nao eventos positivos.
    - [x] `Keeper's Verdict` e `The Candlelit Sanctum` conectam por zone
          movement quando houver pares compativeis.

- [x] P1.4 Corrigir e ampliar sinergia de recursos.
  - Motivo: Basic Runes viram cartas vanilla, `[Add]` e parcialmente tratado
    como keyword, `rainbow` e `any` divergem, e `resource_synergy` ignora parte
    de rune-any ou liga custo parcial sem sinalizar insuficiencia.
  - Escopo provavel: `extract_semantic_facts.py`,
    `semantic_extraction_rules.json`, `build_card_relations.py`,
    `semantic_ontology.json`.
  - Entregaveis:
    - [x] Fatos normativos para Basic Runes.
    - [x] Parser de `[Add]` com multiplos simbolos, `that much Energy` e
          `additional [1]`.
    - [x] Normalizacao unica para `rune:any`/`rune:rainbow` em outputs, custos
          e relation keys.
    - [x] Sinergia parcial para custos altos de XP (`cost:xp:partial`) com
          strength reduzida por cobertura.
    - [x] Scoring de custo parcial: produtor de 1 rune nao deve parecer cobrir
          custo de 2 sem penalty.
  - Fixtures minimas: `Seal of Strength`, `Hextech Anomaly`, `Chem-Baroness`,
    `Bloodharbor Ripper`, `Gold`, `Honeyfruit`, `Malzahar, Fanatic`,
    `Ancient Henge`, `Power Nexus`, `Altar of Blood`, Basic Runes.
  - Aceite:
    - [x] `Gold -> Power Nexus`, `Honeyfruit -> Power Nexus` e
          `Ancient Henge -> Power Nexus` aparecem quando semanticamente validos.
    - [x] `[Add]` nunca aparece como `has_keyword=add`.
    - [x] Custo variavel e custo opcional nao recebem o mesmo strength de custo
          base obrigatorio.

- [x] P1.5 Refinar `similar_effect` para usar chaves especificas por familia.
  - Motivo: chaves largas conectam efeitos apenas por output bruto. Exemplos
    incluem dano sem amount/alvo, resource rainbow conflado com rune especifica
    e Might buffs com contextos diferentes.
  - Escopo provavel: `build_card_relations.py`,
    `semantic_relation_rules.json`, `semantic_quality_policy.json`.
  - Entregaveis:
    - [x] Chaves secundarias por familia: damage, stat modifier, movement,
          keyword grant, score, attach/detach, replacement/prevent, control,
          copy/swap.
    - [x] Normalizar target/controller/location/duration/modality/amount.
    - [x] Skips auditaveis para chaves broad demais com exemplos de cartas
          afetadas.
  - Aceite:
    - [x] `similar_effect` nao conecta cartas apenas por `draw 1`, `repeat`,
          `self_ready` ou `card_recycled` quando o contexto diverge.
    - [x] O report mostra `skipped_similarity_keys` com criterio centralizado.

- [x] P1.6 Cobrir familias ricas ausentes: replacement/prevent, attachment,
      copy, swap, control, score/win, temporary e token creation.
  - Motivo: `Goodall` e o crosscheck local apontam blind spots recorrentes em
    texto rico sem relacao util.
  - Escopo provavel: `semantic_extraction_rules.json`,
    `build_card_relations.py`, `feature_relation_taxonomy.json`,
    `semantic_facts_schema.json`.
  - Entregaveis:
    - [x] `replacement_would_instead` e `prevent_next_damage`.
    - [x] `equipment_attached_modifier`, `grant_activated_ability`,
          `copy_attached_unit_text`, `detach_equipment`.
    - [x] `control_change`, `swap_location`, `copy_or_becomes`,
          `score_restriction`, `combat_win_trigger`, `token_copy_create`.
    - [x] `temporary_grant` com duracao e morte no inicio da fase correta.
  - Fixtures minimas: `Counter Strike`, `Highlander`, `Svellsongur`,
    `Veiled Temple`, `Mirror Image`, `Keeper of Masks`, `Switcheroo`,
    `Mystic Reversal`, `Possession`, `Tianna Crownguard`,
    `Forgotten Monument`, `Glorious Executioner`, `Zilean, Time Mage`,
    `Baron Nashor`, `Green Father`, `Fading Memories`, `Turn to Dust`.
  - Aceite:
    - [x] Cada familia nova gera pelo menos relacoes high-signal quando existem
          pares compativeis.
    - [x] Eventos produzidos sem observadores ficam em `intentional_ignored`,
          `missing_relation_rule` ou `missing_extraction_producer/observer`.

- [x] P1.7 Separar keyword intrinseca, grant e referencia.
  - Motivo: `keyword_marker` marca referencias e grants como `has_keyword`, e
    keywords oficiais sem colchetes podem nao ser detectadas.
  - Escopo provavel: `extract_semantic_facts.py`,
    `semantic_extraction_rules.json`, `semantic_ontology.json`,
    `build_card_relations.py`.
  - Entregaveis:
    - [x] `has_keyword` somente para keyword propria/intrinseca.
    - [x] `keyword_grant` para `gain/give/have [Keyword]`, com alvo, duracao e
          condicao.
    - [x] `keyword_reference` para textos que mencionam keyword sem conceder.
    - [x] Fatos funcionais normativos para keywords oficiais quando a regra
          tiver efeito relacional.
  - Fixtures minimas: `Emperor of the Sands`, `Karthus, Eternal`,
    `Lillia, Protector of Dreams`, `Fading Memories`, `Turn to Dust`,
    `Fiora, Victorious`, `Syndra, Transcendent`, `Laurent Bladekeeper`,
    `Windsinger`.
  - Aceite:
    - [x] Referencias a Deathknell/Tank/Equip nao viram keyword propria.
    - [x] Grants temporarios aparecem nos filtros e em relacoes de grant.

- [x] P1.8 Completar triggers oficiais usados por relacoes.
  - Motivo: `When you conquer` nao e coberto com a mesma consistencia de
    `When I conquer` e `When you conquer here`.
  - Escopo provavel: `semantic_extraction_rules.json`,
    `semantic_ontology.json`, `build_card_relations.py`.
  - Entregaveis:
    - [x] Normalizar subject/controlador de triggers: self, you, friendly,
          enemy, here.
    - [x] Conectar triggers de conquista/hold/attack/defend a produtores
          compativeis quando houver evento relacional.
    - [x] Primeira fatia de enablement para `self_discarded`, conectando
          descartes sem alvo explicito a cartas com "When you discard me".
  - Fixtures minimas: `Might of Demacia - Starter`, `The Boss`,
    `Blade Dancer`, `Piltover Enforcer`, `Void Burrower`.
  - Aceite:
    - [x] Cartas que observam conquista do jogador deixam de ficar sem
          `enabled_by` por falta de trigger.

## P2 - contrato de produto, manutencao e rastreabilidade

- [x] P2.1 Tornar o contrato dataset/frontend explicito para cada
      `relation_type`.
  - Motivo: o builder publica `enabled_by`, `enables`, `similar_effect` e
    `deck_synergy`; o frontend atual usa apenas `enabled_by`, `enables` e
    `similar_effect`.
  - Escopo provavel: `build_card_explorer_dataset.py`,
    `audit_card_explorer_dataset.py`, `web/app/app.js`, `web/app/README.md`.
  - Entregaveis:
    - [x] Manifest no dataset com `relation_types`, labels, visibilidade padrao,
          broad policy e campos obrigatorios.
    - [x] Frontend renderiza, filtra ou oculta explicitamente cada tipo.
    - [x] Teste/snapshot de paridade entre dataset e `RELATION_TYPES` do app.
  - Aceite:
    - [x] Nenhum tipo de relacao publicado fica invisivel por acidente.
    - [x] `deck_synergy` so entra no produto quando os P0/P1 de ruido estiverem
          resolvidos ou marcado como experimental.

- [x] P2.2 Preservar evidencia e payload suficiente no dataset web para depurar
      cada relacao.
  - Motivo: a UI e os reports escondem parte da causa da categorizacao. Isso
    dificulta entender por que duas cartas foram conectadas.
  - Escopo provavel: `build_card_explorer_dataset.py`,
    `audit_card_explorer_dataset.py`, `web/app/app.js`.
  - Entregaveis:
    - [x] Compactar fatos sem perder `fact_id`, role, type, predicate, payload
          essencial, evidence, source field/line e extractor/rule.
    - [x] Cada relacao deve manter `match.reason`, `match.broad`, `strength`,
          source/target facts e diagnosticos.
    - [x] UI deve exibir reason/evidence de forma legivel em detalhe ou
          inspecao.
  - Aceite:
    - [x] Um usuario consegue explicar a relacao sem abrir JSON raw.
    - [x] Vazio por filtro e vazio por falta de cobertura aparecem como estados
          diferentes.

- [x] P2.3 Centralizar criterios de auditoria relacional.
  - Motivo: builder, quality audit e docs podem discordar sobre uncovered lines,
    broad-only, high-degree e coverage.
  - Escopo provavel: `semantic_quality_policy.json`,
    `build_card_relations.py`, `build_card_explorer_dataset.py`,
    `audit_card_explorer_dataset.py`.
  - Entregaveis:
    - [x] Um unico criterio para `broad_reasons`, `broad_only`,
          `high_signal_relation_count`, `missing_relation_rule`,
          `uncovered_relational_lines` e `intentional_ignored`.
    - [x] Reports devem registrar versao, data do snapshot, thresholds e fontes.
    - [x] Comparacao de snapshot para detectar regressao de contagens.
  - Aceite:
    - [x] Builder e quality report concordam nas mesmas contagens centrais.
    - [x] Mudanca de threshold aparece no diff dos reports.

- [x] P2.4 Fazer extracao variant-aware ou warning persistente para
      `rule_variants`.
  - Motivo: `play_id` colapsa printings com textos oficiais diferentes. A
    extracao principal usa uma printing escolhida, o que pode criar ou perder
    relacoes.
  - Escopo provavel: `normalize_cards.py`, `extract_semantic_facts.py`,
    `build_card_relations.py`, dataset web.
  - Entregaveis:
    - [x] Fatos por variante quando o texto alterar comportamento.
    - [x] Warning/diagnostic persistente para cartas com variantes ainda nao
          modeladas.
    - [x] Dataset deve indicar quando relacoes derivam de texto variante.
  - Aceite:
    - [x] As `44` cartas com `rule_variants` nao sao tratadas como semanticamente
          identicas sem aviso.

- [x] P2.5 Reduzir dependencia de regras legadas.
  - Motivo: existem `658` fatos `legacy_rule`; contratos revisaveis e Python
    legado podem emitir fatos duplicados ou contraditorios.
  - Escopo provavel: `extract_semantic_facts.py`,
    `semantic_extraction_rules.json`, `validate_semantic_contracts.py`.
  - Entregaveis:
    - [x] Inventariar fatos legados por familia e risco relacional.
    - [x] Migrar familias de alto impacto para contrato declarativo.
    - [x] Criar limite esperado para `legacy_rule_count` e duplicatas
          contrato/legado.
  - Aceite:
    - [x] Casos como `Janna, Savior` e `Arachnoid Horror` nao duplicam ou
          contradizem fatos por regras sobrepostas.
    - [x] Reducao de legado nao remove cobertura sem golden equivalente.

- [x] P2.6 Fortalecer schema, ontologia e source evidence dos fatos.
  - Motivo: payloads aninhados usam shapes/enums nao cobertos e o relation
    builder assume campos como `target`, `destination`, `keywords`, `amounts`,
    `duration` e `modality`.
  - Escopo provavel: `semantic_facts_schema.json`, `semantic_ontology.json`,
    `semantic_contracts.py`, `validate_semantic_contracts.py`,
    `build_card_relations.py`.
  - Entregaveis:
    - [x] Schema para payloads de custo, choice, replacement, attachment,
          movement, keyword grant, score e resource.
    - [x] Invariante de `source_ref`: campo, linha, unit_text e evidence
          verificavel.
    - [x] Normalizacao de enums aninhados usados em relations.
  - Aceite:
    - [x] Todo fato textual aponta para linha e substring verificavel.
    - [x] O builder nao precisa inferir shapes inconsistentes em tempo de
          relacao.

- [x] P2.7 Atualizar documentacao de estado e guias de operacao apos correcoes.
  - Motivo: README e docs podem ficar defasados em relacao aos reports gerados,
    dando falsa seguranca.
  - Escopo provavel: `README.md`,
    `scripts/04_cards_feature_extraction/README.md`,
    `scripts/05_web_dataset/README.md`, `web/app/README.md`, reports em
    `data/processed`.
  - Entregaveis:
    - [x] Snapshots datados de fatos, relacoes, broad share, cartas sem relacao,
          broad-only e relacoes por tipo.
    - [x] Guia de interpretacao de `broad`, `high_signal`, `deck_synergy`,
          `missing_relation_rule` e allowlists.
    - [x] Checklist de comandos para regenerar e auditar artefatos.
  - Aceite:
    - [x] A documentacao nao contradiz os reports atuais.
    - [x] Um mantenedor consegue executar a pipeline e entender as mudancas de
          qualidade relacional.

## Ordem sugerida de execucao

- [x] 1. Implementar P0.1 para criar rede de seguranca e reproduzir os bugs
      conhecidos.
- [x] 2. Resolver P0.2 a P0.7 para remover relacoes falsas e ruido de
      ordenacao.
- [x] 3. Executar P1.1 para transformar lacunas em familias relacionais
      acionaveis.
- [x] 4. Implementar P1.2 a P1.8 por familia, sempre com fixtures e reports.
- [x] 5. Fechar P2.1 a P2.3 antes de expor novas lanes no frontend.
- [x] 6. Tratar P2.4 a P2.7 como maturidade de pipeline e manutencao.

## Comandos de validacao

Executados nesta rodada. Devem ser usados novamente apos implementacoes futuras.

- [x] `python -m py_compile scripts\04_cards_feature_extraction\extract_semantic_facts.py scripts\04_cards_feature_extraction\build_card_relations.py scripts\04_cards_feature_extraction\validate_semantic_golden_examples.py scripts\05_web_dataset\build_card_explorer_dataset.py scripts\05_web_dataset\audit_card_explorer_dataset.py`
- [x] `python scripts/04_cards_feature_extraction/validate_semantic_contracts.py`
- [x] `python scripts/04_cards_feature_extraction/validate_semantic_golden_examples.py`
- [x] `python scripts/04_cards_feature_extraction/extract_semantic_facts.py`
- [x] `python scripts/04_cards_feature_extraction/audit_semantic_facts.py`
- [x] `python scripts/04_cards_feature_extraction/build_card_relations.py`
- [x] `python scripts/05_web_dataset/build_card_explorer_dataset.py`
- [x] `python scripts/05_web_dataset/audit_card_explorer_dataset.py`
- [x] `node --check web\app\app.js`
- [x] `git diff --check`

## Definition of done global

- [x] Nenhum P0 conhecido produz relacao/fato positivo falso.
- [x] Broad relations nao dominam resultado default nem contagem de
      high-signal.
- [x] `deck_synergy` tem contrato claro: renderizado, oculto explicitamente ou
      experimental.
- [x] Cartas com texto rico sem relacao util caem para uma allowlist pequena e
      explicada.
- [x] Reports de cards, relacoes, dataset e frontend concordam sobre contagens
      principais.
- [x] Cada nova familia relacional tem fixtures reais, criterios de ausencia de
      falsos positivos e evidencia depuravel no dataset.
