# Onda 1 - agente Hooke - modalidade, negacao e parsing de clausulas

## Escopo

Auditoria somente leitura, independente de relatorios anteriores, focada em bugs semanticos de `scripts/04_cards_feature_extraction`: modalidade, negacao, `prevent`, `optional/must/required` e parsing de clausulas.

O agente informou que nao editou arquivos. `git status` antes/depois continuou com alteracoes pre-existentes: `M goal.md`, `?? docs/`.

## Arquivos lidos

- `data/processed/cards/normalized/cards_normalized.json`
- `data/processed/cards/semantic/cards_semantic_facts.jsonl`
- `scripts/04_cards_feature_extraction/extract_semantic_facts.py`
- `scripts/04_cards_feature_extraction/contracts/semantic_extraction_rules.json`
- `scripts/04_cards_feature_extraction/contracts/semantic_quality_policy.json`
- `scripts/04_cards_feature_extraction/contracts/semantic_golden_examples.json`
- `README.md`
- `build_card_relations.py`
- `feature_relation_taxonomy.json`

Observacao do agente: os caminhos `scripts/04_cards_feature_extraction/semantic_quality_policy.json` e `semantic_golden_examples.json` nao existem diretamente na pasta; os arquivos reais estao em `contracts/`.

## Entrada e saida da etapa

- Entrada principal: `cards_normalized.json` com 767 cartas e linhas `rules_lines`/`effect_lines`.
- Contrato: regras de extracao com 23 triggers, 5 condicoes, 4 custos, 100 efeitos e 1 reminder.
- Saida auditada: `cards_semantic_facts.jsonl`, com 5428 fatos, sendo 1759 por regras de contrato, 658 por regras legadas e 3011 estruturais.

## Como contribui para categorizacao

Os fatos semanticos alimentam relacoes e filtros posteriores: `enables`, `enabled_by`, `similar_effect`, `deck_synergy`, filtros por predicado, modalidade, alvo e evento. `build_card_relations.py` usa `payload.modality` em chaves de similaridade e usa `clause_group_id` para anexar contexto de trigger. Portanto, modalidade ou negacao errada muda diretamente categorias, similaridade e sinergias.

## Cartas consultadas

Evidencia principal: `Abandoned Hall`, `Star Spring`, `Whirlwind`, `Dancing Grenade`, `The Candlelit Sanctum`, `Forgotten Library`, `Unlicensed Armory`, `Vilemaw's Lair`, `Counter Strike`, `Highlander`, `Altar of Blood`, `Power Nexus`, `Emperor's Dais`, `Sigil of the Storm`, `Shard of Undoing`, `Mageseeker Warden`, `Rockfall Path`, `Guardian Angel`, `Zhonya's Hourglass`.

Amostra adicional: `Bandle Tree`, `Ripper's Bay`, `Valley of Idols`, `Gutter Palace`, `Arena Bar`, `Ancient Henge`, `Cursed Sarcophagus`, `Promising Future`, `Fire Below the Mountain`, `Honeyfruit`, `Poro Snax`, `The Zero Drive`.

## Regras consultadas

Principais: `activation_cost`, `draw_cards`, `look_reveal_top_deck`, `deal_damage`, `move_unit`, `recall_unit`, `recycle_card`, `recycle_rune`, `kill_each_player_unit`, `kill_opponent_unit`, `prevent_spell_ability_damage`, `prevent_target_combat_damage_dealt`, `prevent_chosen_by_enemy_spells`, `token_play_copy_replacement`, triggers de `self_played`, `spell_played`, `battlefield_conquered`.

Politica: `optional_governors`, `relational_keywords`, buckets `kill/heal/replacement` e `permission/restriction`. Golden examples: 40 exemplos; cobrem alguns casos, mas sao minimos e deixam lacunas relevantes.

## Achados

### 1. Modalidade por linha inteira

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Dancing Grenade` tem `Deal 2 to a unit` emitido como `modality=optional` porque a mesma linha depois contem `may play`. `The Candlelit Sanctum`/`Forgotten Library` marcam `look` obrigatorio como optional por causa de `You may recycle`. `Unlicensed Armory` marca custo `Discard 1, :rb_exhaust:` como optional por causa de `you may pay` posterior.
- regra relacionada: `line_has_optional_governor` + `payload_with_line_modality`; muitas regras usam `modality: line_optional`.
- impacto provavel no produto final: efeitos obrigatorios entram em buckets opcionais de similaridade/filtro.
- recomendacao: resolver modalidade por clausula/span da evidencia, nao pela linha inteira.
- teste que deveria existir: golden com `Dancing Grenade`, `The Candlelit Sanctum` e `Unlicensed Armory` exigindo obrigatoriedade correta.

### 2. Governadores opcionais estreitos

- categoria do achado: regra ausente
- severidade: media-alta
- confianca: alta
- evidencia: `Abandoned Hall` (`they may give...`) gera `modify_stat required`; `Star Spring` (`they may move...`) gera `move required`; `Whirlwind` (`each player may return...`) gera `return_to_hand required`. Metrica: 224 linhas com `may`; 5 nao sao reconhecidas pelo governor atual.
- regra relacionada: `optional_governors` so cobre `you may`, `may pay`, `may exhaust`, `may discard`, `may kill`, `may play`, `may reveal`.
- impacto provavel no produto final: acoes opcionais de outros atores parecem obrigatorias.
- recomendacao: parser modal ator-agnostico: `<actor> may <verb>`.
- teste que deveria existir: expected facts opcionais para `Abandoned Hall`, `Star Spring`, `Whirlwind`.

### 3. `must` quase nao preservado

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: ha 74 linhas com `must`, mas so 1 fato com `modality=must` em toda a saida. `Sigil of the Storm` (`you must recycle`) vira `required`; `Shard of Undoing` (`each opponent must kill`) vira `required`; reminders de Tank/Deflect frequentemente nao viram custo/restricao.
- regra relacionada: `build_kill_rule_facts` so detecta `must` se a evidencia capturada ainda contem a palavra; outros builders nao detectam `must`.
- impacto provavel no produto final: `must` fica indistinguivel de efeito obrigatorio comum.
- recomendacao: centralizar modalidade `may/must/can/cannot/only` por clausula.
- teste que deveria existir: `Sigil of the Storm`, `Shard of Undoing`, `Tank`, `Deflect`, `The Harrowing`.

### 4. Negacao invertida em evento positivo

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `Vilemaw's Lair` (`Units can't move from here to base`) gera `event_produced/move required`; `Mageseeker Warden` gera `prevent ready` e tambem fato positivo `ready`; `Rockfall Path` (`Units can't be played here`) nao gera restricao.
- regra relacionada: `move_unit` usa guard fragil `(?<!can )`; `ready_unit` nao exclui spans negados; regras `prevent_*` sao pontuais.
- impacto provavel no produto final: cartas que proibem movimento/ready/play passam a habilitar esses eventos.
- recomendacao: detectar spans negados e bloquear builders positivos dentro deles; emitir `restriction_or_permission/prevent`.
- teste que deveria existir: `Vilemaw's Lair` sem `event_produced move`; `Mageseeker Warden` sem `ready`; `Rockfall Path` com `prevent play`.

### 5. `prevent` e replacement `would/instead` incompletos

- categoria do achado: regra ausente
- severidade: alta
- confianca: alta
- evidencia: `Counter Strike` so emite `draw`; nao emite `prevent it`. `Highlander`, `Altar of Blood`, `Guardian Angel` e `Zhonya's Hourglass` emitem basicamente `recall`/`kill`, mas perdem `would die`, `heal`, `exhaust`, `instead` e a prevencao/replacement do evento de morte/dano.
- regra relacionada: so ha prevencao especifica para `Prevent all spell and ability damage` e alguns `can't`; `recall_unit` modela `recall it instead` como movimento simples.
- impacto provavel no produto final: protecao, substituicao e prevencao nao entram em categorias/sinergias.
- recomendacao: builder de replacement com `prevented_event`, `replacement_outputs`, condicao e polaridade.
- teste que deveria existir: `Counter Strike`, `Highlander`, `Altar of Blood`, `Guardian Angel`, `Zhonya's Hourglass`.

### 6. Parsing de custo/clausula por `activation_split`

- categoria do achado: parsing/normalizacao
- severidade: alta
- confianca: alta
- evidencia: 169 fatos `activation_cost`; 81 tem evidencia suspeita. `Altar of Blood` tem 3 runas no texto e so 2 no payload; `Power Nexus` tem 4 e so 3; `Emperor's Dais` captura trigger/efeito/token dentro da evidencia de custo; `Unlicensed Armory` transforma custo obrigatorio em optional.
- regra relacionada: `activation_split` divide no ultimo `": "` da linha, confundindo fechamento de simbolo `:rb_*:` com delimitador de habilidade.
- impacto provavel no produto final: filtros por custo e sinergia de recurso ficam subcontados ou ligados a clausula errada.
- recomendacao: separar parsing de custos ativados (`::`, `-`, listas antes do delimitador) de `may pay X to...`; nunca cortar simbolo antes do `:` final.
- teste que deveria existir: contagem exata de simbolos para `Altar of Blood`/`Power Nexus` e evidencia exata em `Emperor's Dais`.

### 7. `clause_group_id` granular demais

- categoria do achado: arquitetura
- severidade: media-alta
- confianca: alta
- evidencia: `line_clause_group_id` cria um unico grupo por linha. Linhas multi-sentenca como `Ivern, Nurturer`, `Emperor's Dais` e `The Candlelit Sanctum` misturam trigger, custo, escolha opcional, `then` e payoff no mesmo grupo.
- regra relacionada: relacoes usam `trigger_context_by_clause` para anexar contexto de trigger por `clause_group_id`.
- impacto provavel no produto final: similaridade e sinergia herdam triggers/condicoes que pertencem a outra sentenca.
- recomendacao: introduzir grupos por clausula com indices e links `if/then/if you do/instead`.
- teste que deveria existir: fixtures que validem grupos separados para linhas multi-sentenca.

## Testes faltando

- Assercoes negativas: texto com `can't` nao pode gerar `event_produced` positivo para o mesmo verbo.
- Modalidade por span: fato antes de `may` na mesma linha nao herda `optional`.
- Cobertura de `must` para verbos nao-kill.
- Contagem exata de simbolos de custo.
- Replacement/prevent com `would die`, `would be dealt damage`, `instead`.
- Golden examples completos, nao so minimos, para cartas com varias clausulas.

## Melhorias

- Criar um objeto interno `Clause` com `text`, `span`, `modality`, `polarity`, `condition_id` e `parent_clause_id`.
- Mover guards de negacao para camada comum antes dos builders.
- Adicionar metricas de auditoria: `linhas com must sem fato must`, `fatos optional cuja evidencia antecede may`, `negated span gerando evento positivo`.
- Permitir expected `forbidden facts` nos golden examples.

## Duvidas

- `must` deve ser modalidade distinta no produto final ou deve continuar normalizado como `required`? A taxonomia sugere que deve ser distinto.
- Reminders de keywords como Tank/Deflect devem gerar fatos funcionais de custo/atribuicao, ou so keyword identity?
- Replacement com recall deve ser categorizado como movimento produzido, prevencao de morte/dano, ou ambos ligados por clausula?

## Comandos executados

- `Get-Location`, `git status --short`: confirmou workspace e estado pre-existente.
- `Get-ChildItem` nos arquivos obrigatorios: confirmou arquivos; apontou que policy/golden estao em `contracts/`.
- `rg --files ...`: mapeou arquivos da etapa 04 e dados semantic/normalized.
- `Get-Content` em contratos e script: leitura pontual de regras, policy, golden e codigo.
- Scripts Python somente leitura: contaram 767 cartas, 5428 fatos, modalidades, linhas `may/must`, custos suspeitos e cruzaram cartas normalizadas com fatos emitidos.
- `rg -n` em codigo/regras/relacoes: localizou funcoes e regras citadas. Um `rg` combinado falhou por quoting/regex no PowerShell; foi substituido por buscas menores.
