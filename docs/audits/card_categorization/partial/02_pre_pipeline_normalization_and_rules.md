# Auditoria parcial 02 - entrada, normalizacao e regras

## Escopo analisado

Esta rodada revisou a entrada do pipeline antes da extracao semantica:

- origem oficial em `data/raw/cards.json`;
- normalizacao em `data/processed/cards/normalized/cards_normalized.json`;
- relacao entre texto normalizado, variantes de texto e regras oficiais;
- achatamento de HTML/listas em linhas;
- uso atual de `rules_lines`, `effect_lines` e `rule_variants` pela etapa 04.

## Artefatos relidos

- `data/raw/cards.json`
- `data/processed/cards/normalized/cards_normalized.json`
- `data/processed/rules/core-rules.md`
- `scripts/01_cards_extraction/fetch_cards.py`
- `scripts/01_cards_extraction/README.md`
- `scripts/02_rules_formatter/README.md`
- `scripts/03_cards_formatter/README.md`
- `scripts/03_cards_formatter/normalize_cards.py`
- `scripts/04_cards_feature_extraction/README.md`
- `scripts/04_cards_feature_extraction/contracts/semantic_extraction_rules.json`
- `scripts/04_cards_feature_extraction/contracts/feature_relation_taxonomy.json`

## Cartas confrontadas

- `Gold`
- `The Boss`
- `Emperor of the Sands`
- `Veteran Poro`
- `Wuju Master`
- `Green Father`
- `Bloodharbor Ripper`
- `Disposal Order`
- `Rabadon's Deathcrown`
- `Janna, Savior`
- `Vaults of Helia`
- `The Academy`

## Regras oficiais confrontadas

- `core-rules.md:732`: rules text impresso fica inativo enquanto a carta esta attached.
- `core-rules.md:738`: texto concedido ou appended continua ativo mesmo quando a carta esta attached.
- `core-rules.md:740-755`: define Effect Text; effect text fica inativo salvo quando a carta com effect text esta attached, e entao e appended ao rules text da carta top-most.
- `core-rules.md:3840-3852`: cartas attached mostram effect text e might bonus; top-most card recebe effect text appended; rules text de cartas attached fica inativo.
- `core-rules.md:5060-5063`, `core-rules.md:5090`, `core-rules.md:5140`: reforcam que effect text so aplica quando attached.
- `core-rules.md:5125-5134`: texto inativo nao processa instrucoes, mas ainda pode ser referenciado para elegibilidade.

## Comandos executados e resultado

- `git status --short`: antes desta rodada, apenas `M goal.md` preexistente e `?? docs/`.
- PowerShell com `ConvertFrom-Json`: `950` printings brutas, `767` cartas normalizadas e `44` cartas normalizadas com `rule_variants`.
- `rg -n "play_id|rule_variants|rules_lines|effect_lines|html_to_lines|richest|signature"` em `normalize_cards.py` e README da etapa 03: confirmou que o agrupamento preserva texto principal e variantes.
- `rg -n "effect text|Effect Text|attached|append|appended|inactive|active"` em `core-rules.md`: confirmou a semantica oficial de `effect_lines`.
- `rg -n "__NEXT_DATA__|blades|cards|items"` em `fetch_cards.py`: confirmou dependencia de estrutura fixa do HTML Next.js.
- Consultas em `cards_normalized.json`: amostraram variantes de `Gold`, `The Boss`, `Emperor of the Sands` e `Veteran Poro`.

## Achados

### 1. Aquisicao raw depende de caminho estrutural fragil do site oficial

- categoria do achado: fragilidade de entrada
- severidade: media
- confianca: alta
- evidencia: `scripts/01_cards_extraction/fetch_cards.py:31` extrai `__NEXT_DATA__` por regex e `scripts/01_cards_extraction/fetch_cards.py:39` acessa diretamente `data['props']['pageProps']['page']['blades'][2]['cards']['items']`. O README da etapa 01 tambem descreve essa dependencia da pagina Next.js (`scripts/01_cards_extraction/README.md:9`).
- impacto: uma reordenacao de `blades`, mudanca no shape JSON ou alteracao no HTML pode produzir falha ou dataset incompleto sem diferenciar problema de scraping de mudanca real de cartas.
- recomendacao: salvar metadados da captura junto do raw dataset, incluindo URL, data, hash do HTML/JSON, contagem esperada por set e caminho estrutural usado; validar schema minimo antes de sobrescrever `data/raw/cards.json`.
- teste faltante: smoke test offline com fixture de `__NEXT_DATA__` e assert de caminho estrutural, contagem minima e campos obrigatorios por carta.

### 2. `play_id` agrupa por assinatura jogavel sem incluir texto de regras

- categoria do achado: perda de informacao potencial
- severidade: media
- confianca: alta
- evidencia: `scripts/03_cards_formatter/README.md:32-42` documenta `play_id`, `signature`, texto limpo e `rule_variants`. Em `normalize_cards.py`, `gameplay_signature` e usada para agrupar printings (`scripts/03_cards_formatter/normalize_cards.py:298`, `scripts/03_cards_formatter/normalize_cards.py:313`), enquanto o texto escolhido para a carta normalizada vem do `richest_printing` (`scripts/03_cards_formatter/normalize_cards.py:330-370`). O texto de regras divergente e preservado em `rule_variants`, mas nao faz parte da chave de agrupamento.
- dados concretos: `44` cartas normalizadas tem `rule_variants`.
- exemplos:
  - `Gold`: uma variante tem `[Reaction][>] Kill this, :rb_exhaust:: [Add]...`; outra tem `Kill this, :rb_exhaust:: [Reaction] - [Add]...`.
  - `The Boss`: uma variante cura, exausta e recalls a unidade; outra recalls exhausted em vez de heal/exhaust/recall.
  - `Emperor of the Sands`: uma variante diz `Your Sand Soldiers have [Weaponmaster]`; outra restringe a `Sand Soldiers you play`.
  - `Veteran Poro`: uma variante inclui reminder de Weaponmaster com reducao e attach mesmo ja attached; outra mantem apenas `[Weaponmaster]`.
- impacto: fatos e relacoes passam a representar a printing escolhida como principal, nao necessariamente todas as semanticas oficiais preservadas nas variantes.
- recomendacao: escolher explicitamente uma politica: fatos por printing, fatos por variante, ou alerta de divergencia semantica manual. O estado atual deve pelo menos reportar quais variantes nao foram modeladas.
- teste faltante: auditoria que falhe ou avise quando `rule_variants.Count > 1` e as variantes alteram verbos semanticos como `heal`, `exhaust`, `recall`, `have`, `you play`.

### 3. `rule_variants` sao preservadas, mas etapa 04 ignora essa fonte textual

- categoria do achado: divergencia entre contrato e implementacao
- severidade: media
- confianca: alta
- evidencia: `normalize_cards.py` grava `rule_variants` (`scripts/03_cards_formatter/normalize_cards.py:260`, `scripts/03_cards_formatter/normalize_cards.py:370`). A etapa 04 declara entrada em `cards_normalized.json` (`scripts/04_cards_feature_extraction/README.md:217`) e processa texto normalizado, mas `extract_semantic_facts.py` itera apenas `rules_lines` e `effect_lines`; a primeira auditoria local ja confirmou os pontos `scripts/04_cards_feature_extraction/extract_semantic_facts.py:26` e `:2172`.
- impacto: a existencia de variantes fica invisivel para `cards_semantic_facts.jsonl`, `cards_card_relations.jsonl` e `card_explorer_dataset.json`.
- recomendacao: adicionar campo de proveniencia `printing_scope` ou `variant_scope`; enquanto isso nao existir, gerar warning em `cards_semantic_audit_report.md` para toda carta com variante textual sem fato equivalente.
- teste faltante: `Gold`, `The Boss`, `Emperor of the Sands` e `Veteran Poro` como exemplos de regressao.

### 4. `effect_lines` sao tratadas como texto ativo da propria carta

- categoria do achado: divergencia com regras oficiais
- severidade: alta
- confianca: alta
- evidencia: as regras oficiais dizem que Effect Text fica inativo salvo quando a carta com effect text esta attached (`core-rules.md:752`, `core-rules.md:5140`) e que, quando ativo, ele e appended ao rules text da carta top-most (`core-rules.md:755`, `core-rules.md:3846`, `core-rules.md:5063`). `Rabadon's Deathcrown` tem `effect_lines: Your spells and abilities deal 3 Bonus Damage (while this is attached).` A etapa 04 gera fato `static_modifier / modify_stat` com `source_field: effect_lines`, `payload.modality: static` e sem modelar `attached_only` ou o fato de que o beneficio pertence ao objeto top-most.
- impacto: o frontend e as relacoes podem tratar uma gear como se tivesse modificador global proprio, quando pela regra esse texto so aplica enquanto attached e e appended a outro objeto.
- recomendacao: modelar `text_zone_semantics`: `rules_lines` ativos por default; `effect_lines` com `activation_context: attached`, `applies_to: top_most_card`, e `inactive_until_attached`.
- teste faltante: golden para `Rabadon's Deathcrown` exigindo contexto attached-only no payload e proibindo classificacao como modificador estatico incondicional.

### 5. Modal choices sao achatados em linhas independentes

- categoria do achado: perda de estrutura
- severidade: alta
- confianca: alta
- evidencia: `html_to_lines` transforma HTML em lista simples (`scripts/03_cards_formatter/normalize_cards.py:120`, `:160`, `:162`). `Disposal Order` normalizada fica com tres linhas: `[Reaction]`, `Choose one -`, `Choose up to 3 cards... recycle them.`, `Draw 1.`. O inventario reconhece `choice_modal` (`data/processed/cards/inventory/cards_taxonomy_alignment.md:67`), mas os fatos gerados tratam recycle e draw como outputs requeridos separados.
- impacto: cartas de escolha aparecem como se executassem todas as opcoes, inflando filtros, similaridade e relacoes.
- recomendacao: preservar estrutura de lista/modal em normalizacao ou reconstruir grupos na etapa 04 com `choice_group_id`, `choice_mode: choose_one`, `option_index` e `exclusive: true`.
- teste faltante: golden para `Disposal Order` exigindo que `recycle` e `draw` estejam no mesmo grupo modal exclusivo.

### 6. Regras oficiais existem, mas ainda nao validam fatos

- categoria do achado: contrato incompleto
- severidade: media
- confianca: alta
- evidencia: `README.md:103` mostra ligacao planejada de `rulesOut` para fatos; `README.md:157` e `README.md:169` dizem que `core-rules.json` existe, mas ainda nao esta ligado aos fatos das cartas. A etapa 02 produz `core-rules.md/json/jsonl` (`scripts/02_rules_formatter/README.md:20-22`).
- impacto: bugs como `effect_lines` ativo por default e texto negativo gerando fatos positivos nao sao barrados por uma regra oficial verificavel.
- recomendacao: comecar por validacoes de alto retorno: active/inactive text, attached/effect text, modal choice, optional/required, negacao e replacement effects.
- teste faltante: auditoria que associe cada familia semantica critica a pelo menos uma regra oficial ou marque a lacuna explicitamente.

## Testes faltando

- Fixture de scraping com schema e contagem esperada.
- Auditoria semantica de `rule_variants`.
- Golden de `effect_lines` com contexto attached-only.
- Golden de modal choices com exclusividade.
- Ligacao minima fato -> regra oficial para zonas de texto, active/inactive, attached e escolhas.

## Conclusao parcial

A etapa de normalizacao preserva informacao suficiente para uma auditoria humana, mas a etapa 04 consome uma versao achatada e de escopo unico do texto. Isso e o principal ponto de fragilidade antes mesmo dos regexes: variantes, effect text e choices chegam ao extractor sem o contexto necessario para categorizar corretamente.
