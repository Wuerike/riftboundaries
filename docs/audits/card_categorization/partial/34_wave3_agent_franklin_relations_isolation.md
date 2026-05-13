# Onda 3 - agente Franklin - cartas sem relacao, broad-only e high-degree

## Escopo

Auditoria nao mutante da onda 3 sobre cartas sem relacao, broad-only e high-degree.

O agente informou que nao editou arquivos. Leu os artefatos pedidos e fez agregacoes somente leitura sobre `cards_normalized.json`, `cards_semantic_facts.jsonl` e `cards_card_relations.jsonl`.

## Base

- Cartas: 767.
- Fatos: 5428.
- Relacoes: 9884.
- Sem relacao: 100.
- Broad-only: 22.
- Broad relations: 3438, todas por `spell_card_can_be_countered`.
- P95 de grau: 68.

Evidencias principais: quality report, dataset report, relation rules, builder.

## Achados

### A1 - `spell_card_can_be_countered` transforma counterabilidade generica em grafo principal

- categoria do achado: integracao entre etapas
- severidade: alta
- confianca: alta
- evidencia: `spell_card_can_be_countered` gera 3438 relacoes, 34.78% do grafo; `Abandon` tem grau 471, sendo 398 broad; `Not So Fast` e `Repulse` tem 400, sendo 398 broad. A regra esta marcada `broad: true`, mas `build_identity_event_relations` ainda emite `enables` e `enabled_by`.
- regra relacionada: `identity_event_relations.spell_card_can_be_countered`.
- impacto provavel no produto final: counter spells viram hubs artificiais e 22 spells parecem conectadas mesmo sem relacao semantica util.
- recomendacao: mover para tipo separado, como `rules_interaction/counterability`, ou excluir de grau/ranking/high-signal por padrao.
- teste que deveria existir: fixture com as 9 cartas de counter garantindo que `spell_card_can_be_countered` nao conta para `high_signal_degree`.

### A2 - As 22 broad-only sao spells sem high-signal; algumas sao lacunas reais, outras sao efeitos unicos

- categoria do achado: regra ausente
- severidade: alta
- confianca: alta
- evidencia: todas as broad-only tem grau 18, explicado por 9 counter cards x 2 direcoes. Exemplos com lacuna real: `Fading Memories`, `Keeper's Verdict`, `Mystic Reversal`, `Switcheroo`, `Turn to Dust` tem `relation_candidate_fact_count=0` ou so keyword marker apesar de texto relacional.
- regra relacionada: lacuna entre extracao semantica e `similarity/event_enables`.
- impacto provavel no produto final: cartas como `Keeper's Verdict` e `Turn to Dust` parecem apenas counteraveis, nao cartas de remocao, Temporary ou manipulacao de zona.
- recomendacao: extrair fatos para `give [Temporary]`, `place on top/bottom of Main Deck`, `gain control of spell`, `swap Might`, e so depois gerar high-signal.
- teste que deveria existir: goldens exatos para `Fading Memories`, `Keeper's Verdict`, `Mystic Reversal`, `Switcheroo`, `Turn to Dust` exigindo fatos nao-keyword.

### A3 - 100 cartas sem relacao misturam vanilla esperado, fato unico e regra faltante

- categoria do achado: regra ausente
- severidade: media-alta
- confianca: alta
- evidencia: das 100 isoladas, 56 estao como `missing_relation_rule` e 44 como `likely_vanilla_or_low_relational_text`. Distribuicao maior: `movement/location=29`, `stat/buff/damage_modifier=18`, `vanilla/no_text=14`, `cost/resource=11`. Tambem ha 736 candidate facts nao ligados; top predicados: `observe_event=320`, `pay=70`, `move=51`, `require=49`, `draw=49`, `attach=39`.
- regra relacionada: `event_enables` cobre poucas familias; `similarity` exige chave compativel e pula chaves largas.
- impacto provavel no produto final: parte das isoladas e correta, mas cartas com texto operacional somem do explorer.
- recomendacao: nao tentar zerar `cards_without_relations`; separar `isolada esperada` de `isolada por lacuna`. Priorizar `move`, `attach`, `damage`, `prevent`, `gain_keyword`, `Temporary`, `play restriction`.
- teste que deveria existir: auditor deve falhar se carta com fato candidato forte fica grau 0 sem justificativa allowlisted.

### A4 - Fatos bons ficam unicos por chaves de similaridade estreitas ou por grupos largos pulados

- categoria do achado: regra ausente
- severidade: media
- confianca: alta
- evidencia: `Ahri, Inquisitive` tem `modify_stat -2 might` + triggers `self_attacks/self_defends`, mas grau 0; `Fortified Position` e `Block` geram `gain_keyword shield`, mas a chave inclui alvo/duracao/keywords de modo estreito. Ao mesmo tempo, `draw 1 required` e `require while` sao pulados como broad (`Skipped Similarity Keys`).
- regra relacionada: `similarity`, `secondary_key_families`, limites `max_similar_facts_per_key=35`.
- impacto provavel no produto final: efeitos de combate, Shield/Assault/Tank, draw condicionado e modifiers de Might ficam inconsistentes.
- recomendacao: criar familias intermediarias: `combat_might_modifier`, `keyword_grant_by_keyword`, `temporary_grant`, `damage_modifier`, `movement_to_zone`, com strength menor quando alvo/duracao divergir.
- teste que deveria existir: `Ahri` deve relacionar com debuffs de Might compativeis; `Block/Fortified Position/Chakram Dancer` devem compartilhar familia `grant Shield`, sem cair no broad `require while`.

### A5 - Hubs high-signal ainda tem fan-out generico e duplicacao por `derived_synergy`

- categoria do achado: integracao entre etapas
- severidade: alta
- confianca: alta
- evidencia: `Karma, Channeler` grau 173 por recycle; `Mistfall` 163 por buff; `Altar of Memories`, `Vicious Snapjaws`, `Vanguard Helm`, `Viktor, Leader` ficam acima de 100 por death rules. `derived_synergy` transforma todo `enables` em `deck_synergy`, dobrando familias genericas.
- regra relacionada: `event_enables`, `derived_synergy`, `resource_synergy`.
- impacto provavel no produto final: relacoes reais existem, mas o ranking supervaloriza triggers genericos como `quando recicla`, `quando buffa` e `quando unidade morre`.
- recomendacao: marcar como broad/low-signal regras genericas com alto fan-out, deduplicar `enables + derived_synergy` por par/familia, e exigir controlador/objeto mais especifico para death/buff/recycle.
- teste que deveria existir: `Altar of Memories -> Atakhan` nao deve aparecer simultaneamente por generic death, friendly death e derived synergy sem dedupe.

## Relacoes faltantes prioritarias

- `equipment_attached`/`equipment_detached`: `Angle Shot` deveria ligar com payoffs como `Aphelios, Exalted` e `Jax, Unrelenting`.
- `Temporary granted`: `Fading Memories` e `Turn to Dust` deveriam ligar com `Petal Pixie`, `Bashful Bloom`, `Black Flame Altar`, `LeBlanc, Everywhere at Once`.
- `zone removal`: `Keeper's Verdict` precisa fato `unit -> main_deck top_or_bottom`.
- `prevent/replacement`: `Counter Strike`, `Unyielding Spirit`, `Lotus Trap` precisam familia de prevencao/modificacao de dano.
- `play restriction`: `Rockfall Path`, `Brynhir Thundersong`, `Noxus Saboteur` precisam fatos de restricao, nao so trigger/keyword.

## Validacao

Comandos somente leitura executados: `rg`, `Get-Content`, agregacoes Python sobre JSON/JSONL e `git status --short`. Nao rodou builders/auditors que escrevem saida. Estado final observado: `M goal.md` e `?? docs/`; sem alteracoes.
