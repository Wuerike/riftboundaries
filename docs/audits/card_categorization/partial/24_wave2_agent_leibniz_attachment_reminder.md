# Onda 2 - agente Leibniz - attachment, effect_lines e reminder text

## Escopo

Auditoria somente leitura da onda 2 sobre attachment, `effect_lines` e reminder text.

O agente informou que nao editou arquivos. `git status --short` ficou com alteracoes preexistentes: `M goal.md`, `?? docs/`.

## Achados

### 1. Equip usa reminder como fonte funcional e duplica custo

- categoria do achado: categorizacao incorreta
- severidade: critica
- confianca: alta
- evidencia: `Warmog's Armor` gera custo com duas runas Body a partir de `[Equip] :rb_rune_body: (:rb_rune_body:` (`cards_semantic_facts.jsonl:5191`). O mesmo padrao aparece em `Brutalizer`, `Hexdrinker`, `Rabadon's Deathcrown`, `Shurelya's Requiem` e `Svellsongur`; em `Svellsongur`, `[1][C]` vira duas energias + duas runas (`cards_semantic_facts.jsonl:4514`).
- regra relacionada: reminder nao tem funcao de jogo (`core-rules.md:684`); Equip ja e short funcional de `[Cost]: Attach...` (`core-rules.md:5818`).
- impacto provavel no produto final: filtros/sinergias por custo de Equip ficam inflados; attach fica ancorado no reminder, nao no keyword.
- recomendacao: parsear `Equip [Cost]` diretamente e ignorar o parentetico para custo/attach.
- teste que deveria existir: golden para `Warmog's Armor` e `Svellsongur` exigindo custo exato, sem duplicacao.

### 2. `effect_lines` viram fatos ativos sem contexto de attached/appended

- categoria do achado: divergencia entre regras, cartas normalizadas e implementacao
- severidade: alta
- confianca: alta
- evidencia: `Rabadon's Deathcrown` gera `modify_stat/static_modifier` sem condicao de attached, e a evidencia remove `(while this is attached)` (`cards_semantic_facts.jsonl:3464`). `Shurelya's Requiem`, `Brutalizer`, `Hexdrinker` e `Warmog's Armor` tambem geram fatos de `effect_lines`.
- regra relacionada: Effect Text e inativo salvo se attached e e anexado ao Top-Most card (`core-rules.md:752`, `core-rules.md:755`, `core-rules.md:5096`).
- impacto provavel no produto final: downstream trata efeitos de equipamento como ativos na propria carta, nao como texto appended ao alvo equipado.
- recomendacao: fatos de `effect_lines` precisam de `activation_context: while_attached` e alvo `top_most/attached_unit`, ou ficar fora de relacoes high-signal.
- teste que deveria existir: qualquer fato com `source_field=effect_lines` deve carregar contexto attached/inactive.

### 3. Reminder text ainda produz fatos funcionais

- categoria do achado: parsing/normalizacao
- severidade: alta
- confianca: alta
- evidencia: `Warmog's Armor` cria `modify_stat +1 might` a partir do parentetico `If I don't have a buff...` (`cards_semantic_facts.jsonl:5185`). `Gearhead` cria `activation_cost` a partir do reminder de `[Accelerate]`, ainda por cima perdendo a runa Mind (`cards_semantic_facts.jsonl:1811`).
- regra relacionada: reminder nao altera funcao de jogo (`core-rules.md:684`). O normalizador achata HTML para texto sem separar parenteticos (`normalize_cards.py:128`).
- impacto provavel no produto final: explicacoes viram efeitos/custos duplicados ou parciais.
- recomendacao: segmentar reminder antes da extracao e permitir no maximo fatos explicativos/keyword identity, nao `event_produced`, `cost_or_requirement` ou `state_or_modifier`.
- teste que deveria existir: negativos para `Warmog's Armor` e `Gearhead`.

### 4. Attach explicito de Grandmaster at Arms nao gera evento `attach`

- categoria do achado: regra ausente
- severidade: alta
- confianca: alta
- evidencia: `Grandmaster at Arms` tem duas linhas `Attach a detached/attached Equipment...` (`cards_normalized.json:20704`), mas os fatos gerados sao apenas custos `pay` (`cards_semantic_facts.jsonl:1903`, `cards_semantic_facts.jsonl:1904`).
- regra relacionada: `attach_equipment` so aceita objetos como `this|it|that Equipment|one of...` (`semantic_extraction_rules.json:713`).
- impacto provavel no produto final: a principal carta de mover/anexar Equipment nao entra em filtros/sinergias de attachment.
- recomendacao: ampliar o padrao para `a detached Equipment you control` e `an attached Equipment you control`.
- teste que deveria existir: golden exigindo dois fatos `predicate=attach` para `Grandmaster at Arms`.

### 5. Svellsongur perde a copia de texto para `effect_text`

- categoria do achado: regra ausente
- severidade: media-alta
- confianca: alta
- evidencia: a linha `copy that unit's text to this Equipment's effect text...` esta normalizada (`cards_normalized.json:11453`), mas os fatos de `Svellsongur` cobrem so identidade, custo Equip, attach e keyword (`cards_semantic_facts.jsonl:4509`).
- regra relacionada: copy text; effect text.
- impacto provavel no produto final: uma mecanica central de text-copy/effect-text nao aparece em relacoes nem filtros.
- recomendacao: criar fato `copy_text`/`append_effect_text` com duracao `while_attached` e origem `attached_unit.rules_text`.
- teste que deveria existir: golden para `Svellsongur` exigindo copia para `effect_text`.

### 6. Recall de The Boss e modelado como move/return_to_hand

- categoria do achado: categorizacao incorreta
- severidade: media
- confianca: alta
- evidencia: `The Boss` gera `predicate=return_to_hand`, `fact_type=movement`, `event.id=unit_moved` para `recall it instead` (`cards_semantic_facts.jsonl:4613`).
- regra relacionada: Recall e para Base e nao e Move (`core-rules.md:4193`, `core-rules.md:4196`).
- impacto provavel no produto final: recall entra como movimento/retorno a mao, contaminando filtros de movement.
- recomendacao: separar `recall` de `move` e de `return_to_hand`.
- teste que deveria existir: golden negativo proibindo `event.id=unit_moved` em `The Boss`.

## Controles

`Gold`, `Seal of Strength` e `Honeyfruit` nao mostraram fato funcional extraido do reminder `Abilities that add resources can't be reacted to.` Os fatos principais de recurso/custo parecem coerentes dentro deste escopo.

## Comandos e testes

Principais comandos:

- `rg --files`
- `rg -n` nas cartas-alvo
- consultas PowerShell com `ConvertFrom-Json` sobre `cards_normalized.json` e `cards_semantic_facts.jsonl`
- leituras numeradas de `core-rules.md`, `normalize_cards.py`, `extract_semantic_facts.py`, `semantic_extraction_rules.json` e `feature_relation_taxonomy.json`

Teste executado:

```powershell
python scripts\04_cards_feature_extraction\validate_semantic_contracts.py
```

Resultado: passou com `Semantic contracts valid; no new domain leakage found.`

O agente nao rodou validadores que escrevem reports por padrao para manter a auditoria nao mutante.
