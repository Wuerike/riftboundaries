# Auditoria consolidada - categorizacao de cartas

Este arquivo consolida as auditorias em `docs/audits/card_categorization/`.
Os achados repetidos entre relatorios foram deduplicados: quando varias ondas
descreviam a mesma causa raiz, ela aparece uma unica vez aqui, com exemplos e
fontes combinadas.

## Sequencia de leitura

1. Escopo, numeros e leitura rapida.
2. Entrada, normalizacao e contrato entre etapas.
3. Regras oficiais, keywords e termos do jogo.
4. Extracao semantica de fatos.
5. Relacoes, dataset web e frontend.
6. Testes/invariantes recomendados.
7. Priorizacao de correcao.
8. Arquivos principais envolvidos.
9. Mapa de cobertura dos parciais.
10. Conclusao.

## 1. Escopo e numeros de referencia

A auditoria foi somente leitura: nao houve alteracao de codigo, contratos, dados
raw ou artefatos processados durante as auditorias originais.

Numeros recorrentes usados como baseline:

| Item | Valor |
|---|---:|
| Printings em `data/raw/cards.json` | 950 |
| Cartas normalizadas | 767 |
| Cartas com `rule_variants` | 44 |
| Fatos semanticos | 5428 |
| Fatos de campo estrutural | 3011 |
| Fatos por regra contratual | 1759 |
| Fatos por regra legada | 658 |
| Golden examples atuais | 40 exemplos / 73 fatos esperados |
| Relacoes | 9884 |
| Relacoes broad | 3438 |
| Broad share | 0.3478 |
| `deck_synergy` geradas | 1056 |
| Cartas sem relacao | 100 |
| Cartas broad-only | 22 |
| Cartas com texto rico sem relacao util | 104 |

Leitura rapida: a cobertura numerica parece alta e a auditoria semantica atual
chega a reportar `0` warnings, mas ha falsos positivos e falsos negativos
concretos. Os riscos centrais sao polaridade de custo invertida, negacao virando
evento positivo, escolhas exclusivas emitidas como efeitos simultaneos, texto de
equipamento tratado como sempre ativo e relacoes broad dominando a experiencia
do explorador.

## 2. Entrada, normalizacao e contrato entre etapas

### 2.1 Aquisicao raw e estrutura do site oficial

- Severidade: media.
- Problema: a aquisicao raw depende de caminhos estruturais do site oficial.
  Mudancas pequenas no HTML/estrutura podem quebrar a coleta ou mudar a
  interpretacao sem falha explicita.
- Impacto: regressao silenciosa antes da normalizacao.
- Fontes: `02_pre_pipeline_normalization_and_rules.md`.

### 2.2 `play_id` colapsa variantes semanticamente diferentes

- Severidade: alta.
- Problema: `play_id` agrupa por assinatura jogavel sem incluir texto de regras.
  Variantes oficiais ficam preservadas em `rule_variants`, mas a extracao
  principal usa `rules_lines`/`effect_lines` da carta escolhida, normalmente a
  richest printing.
- Impacto: cartas com divergencias oficiais entre printings podem herdar uma
  semantica unica, mesmo quando a variante altera comportamento.
- Exemplos de origem: cartas com `rule_variants` em 44 grupos.
- Fontes: `02_pre_pipeline_normalization_and_rules.md`,
  `12_wave1_agent_hegel_pre_pipeline_normalization.md`,
  `16_wave1_agent_meitner_stage_contracts.md`,
  `32_wave3_agent_dalton_sampling.md`.

### 2.3 `richest_printing` nao e oracle semantico

- Severidade: media-alta.
- Problema: a printing com mais texto pode ser a mais informativa para exibicao,
  mas nao necessariamente a fonte canonica correta para extracao semantica.
- Impacto: divergencias oficiais sao registradas como informacao lateral, nao
  como insumo auditavel de fatos.
- Recomendacao: marcar cartas com variantes como risco ate existir extracao
  variant-aware ou validacao contra regras oficiais.
- Fontes: `12_wave1_agent_hegel_pre_pipeline_normalization.md`,
  `32_wave3_agent_dalton_sampling.md`.

### 2.4 Hierarquia de texto e perdida cedo demais

- Severidade: alta.
- Problema: bullets, headers modais, blocos `Choose one`, reminder text, texto
  entre aspas e `effect_lines` sao achatados em linhas simples. O downstream
  tenta reconstruir modalidade, contexto e agrupamento por regex.
- Impacto: escolha exclusiva vira multiplos fatos requeridos; reminder e texto
  anexado vazam como efeito da carta fonte; custo/trigger/payoff ficam no mesmo
  escopo amplo; `clause_group_id` criado por linha mistura sentencas diferentes
  e pode anexar trigger/condicao a payoff errado.
- Exemplos: `Disposal Order`, `The Academy`, `Dancing Grenade`,
  `Rabadon's Deathcrown`, `Svellsongur`, `Aphelios`, `Udyr`,
  `The Candlelit Sanctum`.
- Fontes: `02_pre_pipeline_normalization_and_rules.md`,
  `12_wave1_agent_hegel_pre_pipeline_normalization.md`,
  `15_wave1_agent_hooke_clause_modality_negation.md`,
  `23_wave2_agent_pascal_modals_choices.md`,
  `24_wave2_agent_leibniz_attachment_reminder.md`,
  `31_wave3_agent_ramanujan_core_rules.md`.

### 2.5 Contratos existem, mas a semantica real ainda esta dividida

- Severidade: alta.
- Problema: parte da semantica esta em JSON revisavel e parte permanece em
  Python legado. A etapa ainda emite 658 fatos `legacy_rule`.
- Impacto: alterar contratos nao altera necessariamente todo comportamento real;
  regras especificas e genericas podem emitir fatos duplicados ou contraditorios.
- Exemplos: `Janna, Savior` com fato correto e fato legado de movimento; `Arachnoid
  Horror` com trigger duplicado.
- Fontes: `03_feature_extraction_findings.md`,
  `11_wave1_agent_kant_contracts_goldens.md`,
  `26_wave2_agent_boole_test_invariants.md`.

## 3. Regras oficiais, keywords e termos do jogo

### 3.1 Regras oficiais ainda nao validam fatos

- Severidade: alta.
- Problema: `core-rules.json`/`core-rules.md` existem e sao consultaveis, mas nao
  validam automaticamente os fatos emitidos. Regras de Effect Text, Runas,
  Accelerate, Equip, Repeat, Tank, Deflect e outras aparecem parcialmente ou como
  marcadores nominais.
- Impacto: o pipeline pode contrariar regra oficial sem warning.
- Fontes: `02_pre_pipeline_normalization_and_rules.md`,
  `31_wave3_agent_ramanujan_core_rules.md`,
  `41_wave4_agent_noether_keywords_official_terms.md`.

### 3.2 Effect Text de Gear/Equipment tratado como sempre ativo

- Severidade: critica.
- Problema: textos de `effect_lines` em Gear/Equipment sao extraidos como fatos
  ativos ou modificadores estaticos, sem contexto `attached`.
- Impacto: carta solta parece conceder bonus/efeito que so deve valer quando
  attached/top-most.
- Exemplos: `Rabadon's Deathcrown`, `Svellsongur`, `Veiled Temple`,
  `Heimerdinger, Inventor`, `Forge of the Fluft`.
- Correcao recomendada: payload com `activation_context: attached`,
  `applies_to: top_most_card`, `inactive_until_attached` e direcao explicita de
  attach/detach/copy.
- Fontes: `00_final_prioritized_report.md`,
  `12_wave1_agent_hegel_pre_pipeline_normalization.md`,
  `24_wave2_agent_leibniz_attachment_reminder.md`,
  `31_wave3_agent_ramanujan_core_rules.md`,
  `43_wave4_agent_goodall_false_negatives.md`.

### 3.3 Basic Runes, `[Add]`, Energy e `rainbow/any`

- Severidade: alta.
- Problemas deduplicados:
  - Basic Runes ficam como cartas vanilla por falta de fatos funcionais derivados
    das regras oficiais.
  - `[Add]` e tratado como keyword (`has_keyword=add`) apesar de ser acao oficial.
  - Padroes como `[Add] that much Energy` e `Gold [ADD] an additional [1]` nao
    viram `add_resource`.
  - `[Add]` com multiplos simbolos pode ser truncado.
  - `rainbow` e `any` nao sao normalizados de forma consistente para sinergia.
- Exemplos: `Seal of Strength`, `Hextech Anomaly`, `Chem-Baroness`,
  `Bloodharbor Ripper`, Basic Runes.
- Fontes: `31_wave3_agent_ramanujan_core_rules.md`,
  `35_wave3_agent_harvey_runes_resources.md`,
  `41_wave4_agent_noether_keywords_official_terms.md`,
  `49_wave4_local_crosscheck.md`.

### 3.4 Keywords oficiais: marker nominal vs funcao

- Severidade: alta.
- Problema: varias keywords oficiais aparecem como `has_keyword` ou nem aparecem,
  mas faltam fatos funcionais normativos.
- Evidencia consolidada:
  - `Hidden`: 38 cartas, so 3 fatos funcionais.
  - `Deathknell`: 24 cartas, so 1 fato funcional.
  - `Reaction`: 96 cartas, so 10 fatos funcionais.
  - `Tank`, `Deflect`, `Ganking`, `Assault` e `Shield` tambem ficam
    majoritariamente como marcadores.
  - `temporary/granted keyword`: 84 cartas com sinal textual; 29 foram
    classificadas como alto risco por poucos fatos uteis, falta de relacao ou
    relacoes apenas broad.
- Falsos positivos: `keyword_marker` marca referencias/grants como keyword
  intrinseca da carta.
- Exemplos: `Emperor of the Sands` recebe `has_keyword=equip` via reminder de
  Weaponmaster; `Karthus, Eternal` recebe `has_keyword=deathknell` por referencia;
  `Lillia, Protector of Dreams` menciona Tank em alvo; `Fading Memories`,
  `Turn to Dust`, `Fiora, Victorious` e `Syndra, Transcendent` precisam de grant
  funcional, duracao e, para `[Temporary]`, efeito de morte na fase correta.
- Falsos negativos: keywords sem colchetes, como `Ganking (...)` e `Hidden (...)`,
  podem nao gerar `has_keyword`.
- Recomendacao: separar `has_keyword` intrinseco, `keyword_grant`,
  `keyword_reference`, duracao/condicao do grant e fatos funcionais normativos.
- Fontes: `41_wave4_agent_noether_keywords_official_terms.md`,
  `43_wave4_agent_goodall_false_negatives.md`,
  `49_wave4_local_crosscheck.md`.

### 3.5 Accelerate, Equip, Repeat, Recall, Channel e Recycling

- Severidade: media-alta.
- Achados unicos:
  - `Accelerate` gera marcador/custo, mas nao fato derivado de entrar ready.
  - Equip/Weaponmaster ficam submodelados quando concedidos a tokens ou quando o
    texto nao segue formato estreito.
  - `Repeat` e escolhas modais podem ser achatados como efeito normal; tambem
    faltam custo adicional completo, instancias repetidas e permissao oficial de
    repetir com os mesmos ou diferentes modos/alvos.
  - `Recall` tem boa cobertura nominal, mas alguns casos sao modelados como
    movimento/return_to_hand mesmo quando a regra/texto diz que nao e move.
  - `Channel` e `Recycle` tem controles positivos, mas ainda precisam de testes
    contra falsos positivos e contexto de custo/trigger.
- Exemplos: `Lee Sin, Centered`, `Emperor of the Sands`, `Rocket Barrage`,
  `Curtain Call`, `The Boss`, `Sprite Fountain`, `Abandon`.
- Fontes: `23_wave2_agent_pascal_modals_choices.md`,
  `24_wave2_agent_leibniz_attachment_reminder.md`,
  `31_wave3_agent_ramanujan_core_rules.md`,
  `35_wave3_agent_harvey_runes_resources.md`,
  `41_wave4_agent_noether_keywords_official_terms.md`.

### 3.6 Triggers oficiais incompletos

- Severidade: media.
- Problema: triggers `When you conquer` nao sao cobertos pela mesma familia de
  `When I conquer` e `When you conquer here`.
- Impacto: efeitos ligados ao jogador/controlador conquistar ficam fora de
  `enabled_by`.
- Exemplos: `Might of Demacia - Starter`, `The Boss`, `Blade Dancer`,
  `Piltover Enforcer`, `Void Burrower`.
- Fontes: `41_wave4_agent_noether_keywords_official_terms.md`.

## 4. Extracao semantica de fatos

### 4.1 Polaridade de custo invertida

- Severidade: critica.
- Problema: regras de custo capturam `cost more`, thresholds e restricoes de custo
  como reducao.
- Exemplo principal: `Vaults of Helia` diz que unidades non-token custam mais para
  jogar; o fato gerado e `reduce_cost`/`play_cost_reduced`.
- Outros casos: `cost no more than`, `or more`, `cost more/less`, custos compostos,
  `additional cost` e `ignore cost`.
- Impacto: relacoes de desconto/sinergia de recurso ficam erradas.
- Correcao recomendada: separar `increase_cost`, `reduce_cost`,
  `cost_cap_constraint`, `cost_threshold`, `additional_cost`, `ignore_cost`,
  `optional_cost` e `cost_payment`.
- Fontes: `00_final_prioritized_report.md`,
  `03_feature_extraction_findings.md`,
  `13_wave1_agent_lagrange_corpus_patterns.md`,
  `19_wave1_local_crosscheck.md`,
  `21_wave2_agent_carver_cost_resource.md`,
  `31_wave3_agent_ramanujan_core_rules.md`.

### 4.2 Custos ativados e `activation_split`

- Severidade: alta.
- Problemas deduplicados:
  - `activation_cost` captura linhas que parecem trigger/condicao, nao habilidade
    ativada.
  - Custos `Spend N XP` aparecem no texto, mas o payload perde XP.
  - Custos com multiplos simbolos, rune + energy + exhaust + kill self, ficam
    truncados ou apenas em `evidence`.
  - Custos dentro de replacement/prevention podem ser parseados como activated
    ability.
- Exemplos: `Poro Snax`, linhas com `Spend N XP`, replacement com `would/instead`.
- Recomendacao: parsear custo como lista estruturada de componentes e preservar
  papel de trigger, custo, condicao e payoff.
- Fontes: `15_wave1_agent_hooke_clause_modality_negation.md`,
  `16_wave1_agent_meitner_stage_contracts.md`,
  `21_wave2_agent_carver_cost_resource.md`,
  `22_wave2_agent_sartre_replacement_negation.md`,
  `29_wave2_local_crosscheck.md`,
  `35_wave3_agent_harvey_runes_resources.md`,
  `44_wave4_agent_erdos_test_invariants.md`.

### 4.3 Negacao, restricao, prevent e replacement viram fatos positivos

- Severidade: critica.
- Problema: `can't`, `cannot`, `don't`, `doesn't`, `not`, `prevent`,
  `would/instead` e `next time ... would` nao compartilham guards robustos.
- Exemplos:
  - `Safety Inspector`: `don't kill a unit` gera fato positivo de kill.
  - `Mageseeker Warden`: `can't ready enemy units and gear` gera restricao e tambem
    fato positivo `ready`.
  - `Rockfall Path`: `Units can't be played here` nao deve gerar evento produzido
    de play.
  - `Counter Strike`, `Highlander`, `Tactical Retreat`, `Altar of Blood`,
    `Soraka, Wanderer`, `Zilean, Time Mage`: replacement/prevent subextraido.
- Impacto: cartas que impedem uma acao podem ser categorizadas como produtoras da
  propria acao.
- Recomendacao: camada comum de guards de negacao/restricao/prevention e fatos
  especificos de replacement com evento substituido, output, duracao e modalidade.
- Fontes: `00_final_prioritized_report.md`,
  `01_overview_and_core_risks.md`,
  `13_wave1_agent_lagrange_corpus_patterns.md`,
  `15_wave1_agent_hooke_clause_modality_negation.md`,
  `19_wave1_local_crosscheck.md`,
  `22_wave2_agent_sartre_replacement_negation.md`,
  `29_wave2_local_crosscheck.md`,
  `31_wave3_agent_ramanujan_core_rules.md`,
  `43_wave4_agent_goodall_false_negatives.md`,
  `44_wave4_agent_erdos_test_invariants.md`.

### 4.4 Modalidade opcional aplicada no escopo errado

- Severidade: alta.
- Problema: `line_has_optional_governor` aplica optionalidade a todos os fatos da
  linha quando encontra `you may`, mesmo que apenas uma clausula seja opcional.
- Tambem ha o problema inverso: governadores opcionais de outros atores (`they
  may`, `each player may`) ficam fora da lista estreita atual e viram fatos
  obrigatorios.
- Exemplos: `Dancing Grenade`, `The Academy`, `Altar of Memories`.
- Exemplos de opcionais nao reconhecidos: `Abandoned Hall`, `Star Spring`,
  `Whirlwind`.
- Impacto: filtros e relacoes confundem custo opcional, payoff obrigatorio,
  reminder text e efeito condicionado.
- Recomendacao: modalidade por clausula/evidencia, com `clause_group_id`,
  `option_group_id`, custo/payoff separados e reminder fora do escopo funcional.
- Fontes: `00_final_prioritized_report.md`,
  `01_overview_and_core_risks.md`,
  `03_feature_extraction_findings.md`,
  `15_wave1_agent_hooke_clause_modality_negation.md`,
  `23_wave2_agent_pascal_modals_choices.md`,
  `26_wave2_agent_boole_test_invariants.md`,
  `44_wave4_agent_erdos_test_invariants.md`.

### 4.5 Choices, modais e `or` inline

- Severidade: alta.
- Problema: `Choose one`, bullets modais, `or`, `not already chosen` e escolha de
  alvo/modo nao geram estrutura modal. As opcoes saem como efeitos simultaneos.
- Exemplos: `Disposal Order`; linhas com `Repeat`; textos com `top or bottom`;
  escolhas que devem guardar memoria de opcoes ja escolhidas.
- Recomendacao: payload com `choice_group_id`, `choice_mode`,
  `option_index`, exclusividade, memoria de escolha e distincao entre target
  choice e mode choice.
- Fontes: `00_final_prioritized_report.md`,
  `02_pre_pipeline_normalization_and_rules.md`,
  `13_wave1_agent_lagrange_corpus_patterns.md`,
  `19_wave1_local_crosscheck.md`,
  `23_wave2_agent_pascal_modals_choices.md`,
  `31_wave3_agent_ramanujan_core_rules.md`.

### 4.6 Reminder text e texto entre aspas vazam como efeito

- Severidade: alta.
- Problema: reminder text e texto citado podem gerar fatos funcionais da carta
  fonte.
- Exemplos: Equip duplicando custo via reminder; `Play a ready token` interpretado
  como acao `ready`; textos de copy/effect text virando efeito ativo.
- Impacto: ruido de categoria e relacoes falsas.
- Recomendacao: classificar `reminder`, `quoted_card_text`, `copied_text` e
  `rules_text` antes da extracao de fatos.
- Fontes: `01_overview_and_core_risks.md`,
  `03_feature_extraction_findings.md`,
  `16_wave1_agent_meitner_stage_contracts.md`,
  `24_wave2_agent_leibniz_attachment_reminder.md`,
  `31_wave3_agent_ramanujan_core_rules.md`,
  `32_wave3_agent_dalton_sampling.md`.

### 4.7 Copy, becomes, swap, control, score/win e zone movement

- Severidade: alta.
- Problema: familias de texto rico ficam ausentes, pouco especificas ou sem
  relacao consumidora.
- Familias e exemplos:
  - `copy/becomes`: `Mirror Image`, `Keeper of Masks`, `Svellsongur`, `Zilean,
    Time Mage`.
  - `swap`: `Switcheroo`, `Green Father`.
  - `control`: `Mystic Reversal`, `Possession`, `Dancing Grenade`, `Detonate`.
  - `score/win`: `Tianna Crownguard`, `Forgotten Monument`,
    `Glorious Executioner`, `Nidalee, Cat Form`, `Draven, Showboat`.
  - `zone movement`: `Minefield`, `The Candlelit Sanctum`, `Flame Chompers`,
    `Stellacorn Herder`, `Keeper's Verdict`.
  - `token creation`: `Zilean, Time Mage`, `Baron Nashor`, `Green Father`.
  - `play restriction`: `Brynhir Thundersong`, `Lilting Lullaby`, `Rockfall Path`.
  - `temporary/granted keyword`: `Fading Memories`, `Turn to Dust`,
    `Last Stand`, `Shadow's Call`, `Fiora, Victorious`.
  - `stat modifier/swap`: `Switcheroo`, `Ahri, Inquisitive`,
    `Fiora, Peerless`.
- Impacto: busca, filtros e relacoes nao representam mecanicas importantes.
- Fontes: `13_wave1_agent_lagrange_corpus_patterns.md`,
  `24_wave2_agent_leibniz_attachment_reminder.md`,
  `32_wave3_agent_dalton_sampling.md`,
  `43_wave4_agent_goodall_false_negatives.md`,
  `49_wave4_local_crosscheck.md`.

### 4.8 Schema, ontologia e evidencia dos fatos

- Severidade: alta.
- Problemas deduplicados:
  - Schema de payload nao cobre todos os shapes reais.
  - Ontologia nao cobre enums aninhados usados em fatos.
  - `source_ref` existe, mas `evidence` nem sempre ancora de forma verificavel no
    `unit_text`.
  - `web_uses` e decorativo/inconsistente com builders.
  - Shapes negativos e duplicados vazam downstream como efeitos positivos.
- Recomendacao: invariantes obrigatorios para `source_ref`, `line_index`,
  `line_text`, `evidence`, `unit_text`, role/type/predicate/payload e payloads de
  custo/choice/replacement/attachment.
- Fontes: `11_wave1_agent_kant_contracts_goldens.md`,
  `26_wave2_agent_boole_test_invariants.md`,
  `33_wave3_agent_kepler_payload_schema.md`,
  `44_wave4_agent_erdos_test_invariants.md`.

### 4.9 Quantificadores, `must`, estado vs acao e stats

- Severidade: media-alta.
- Problemas deduplicados:
  - `must` quase nao e preservado: foram encontradas 74 linhas com `must`, mas
    apenas 1 fato com `modality=must`; o restante fica indistinto de `required`.
  - `up to` tem cobertura superficial: ha algum fato nas 20 linhas encontradas,
    mas cardinalidade, alvo opcional, alvo plural e escopo frequentemente ficam
    em `raw`, duplicam parse ou sao perdidos.
  - Estado de entrada e adjetivo podem virar acao produzida, como `ready token`
    interpretado como evento `ready`; `up` tambem pode vazar como alvo por regex
    legado.
  - Modificadores de Might/stat e `swap` tem fatos ausentes ou pouco consumidos
    por relacoes de alto sinal.
- Exemplos: `Sigil of the Storm`, `Shard of Undoing`, `Targon's Peak`,
  `Forge of the Future`, `Moonfall`, `Flash`, `Piercing Light`, `Salvage`,
  `Elder Dragon`, `Bashful Bloom`, `Mirror Image`, `Switcheroo`,
  `Ahri, Inquisitive`, `Fiora, Peerless`.
- Recomendacao: modelar modalidade `may/must/can/cannot/only` por clausula,
  cardinalidade (`min/max_targets`), estado de entrada separado de evento, e
  `swap_stat`/`modify_stat` com alvo, stat, quantidade, duracao e contexto.
- Fontes: `01_overview_and_core_risks.md`,
  `13_wave1_agent_lagrange_corpus_patterns.md`,
  `15_wave1_agent_hooke_clause_modality_negation.md`,
  `32_wave3_agent_dalton_sampling.md`,
  `44_wave4_agent_erdos_test_invariants.md`.

## 5. Relacoes, dataset web e frontend

### 5.1 `spell_card_can_be_countered` domina o grafo

- Severidade: alta.
- Problema: `spell_card_can_be_countered` responde por 3438 relacoes, todas broad,
  e cria hubs artificiais.
- Exemplos de hubs:
  - `Abandon`: grau total 471, broad 398.
  - `Flurry of Feathers`: grau total 421, broad 398.
  - `Defy`: grau total 414, broad 398.
  - `Not So Fast` e `Repulse`: apenas 2 relacoes non-broad contra 398 broad.
- Impacto: rankings e lanes do explorer exibem "ser spell/counteravel" como se
  fosse sinergia de deckbuilding.
- Recomendacao: marcar broad, rebaixar/excluir por padrao e mover para categoria
  separada como interacao ampla, nao `enables`.
- Fontes: `04_downstream_web_and_reports.md`,
  `14_wave1_agent_faraday_relations_web.md`,
  `25_wave2_agent_lovelace_relations_similarity.md`,
  `34_wave3_agent_franklin_relations_isolation.md`,
  `36_wave3_agent_hilbert_frontend_product.md`,
  `39_wave3_local_crosscheck.md`,
  `42_wave4_agent_newton_relation_false_positives.md`,
  `49_wave4_local_crosscheck.md`.

### 5.2 `similar_effect` usa chaves largas demais

- Severidade: alta.
- Problema: similaridade agrupa efeitos por verbo/output amplo, ignorando contexto,
  alvo, quantidade, escopo, duracao e condicao.
- Exemplos:
  - `Abandon` comparado a bounce de unidade/gear por `return_to_hand`.
  - Dano 1 multi-alvo agrupado com dano 8 a uma unidade.
  - Rune rainbow conflui com rune especifica.
  - Mesmo par pode aparecer repetido por multiplos fatos.
- Recomendacao: incluir target, amount, cardinalidade, contexto, duracao e rune
  especifica nas chaves; deduplicar por `(source_card, target_card, relation_type,
  reason)` na visualizacao.
- Fontes: `14_wave1_agent_faraday_relations_web.md`,
  `25_wave2_agent_lovelace_relations_similarity.md`,
  `42_wave4_agent_newton_relation_false_positives.md`.

### 5.3 `resource_synergy` mistura pagamento real, custo opcional e restricao

- Severidade: alta.
- Problema: geracao de recurso casa com qualquer mencao de custo/restricao ampla.
- Exemplos:
  - `cost no more than` tratado como pagamento.
  - Custo opcional de Accelerate tratado como custo base.
  - Gerar 1 rune casa com custos de 2+ runes sem modelar contribuicao parcial.
- Impacto: quando `deck_synergy` for exposto, geradores de recurso podem virar
  hubs falsos.
- Recomendacao: usar apenas custos pagaveis reais para sinergia forte; reduzir
  score para pagamento parcial; excluir caps/thresholds.
- Fontes: `14_wave1_agent_faraday_relations_web.md`,
  `21_wave2_agent_carver_cost_resource.md`,
  `25_wave2_agent_lovelace_relations_similarity.md`,
  `35_wave3_agent_harvey_runes_resources.md`,
  `42_wave4_agent_newton_relation_false_positives.md`.

### 5.4 `derived_synergy` duplica relacoes e amplifica ruido

- Severidade: media-alta.
- Problema: `deck_synergy` pode repetir a mesma evidencia de `enables` com strength
  menor, e tambem duplicar pares por multiplos fatos.
- Exemplos: `Abandon -> Karma, Channeler`, `Adaptatron -> Mistfall`,
  `Peak Guardian -> Mistfall`.
- Impacto: se exibida no frontend sem dedupe, a categoria inflara contagens e
  repetira recomendacoes.
- Fontes: `14_wave1_agent_faraday_relations_web.md`,
  `25_wave2_agent_lovelace_relations_similarity.md`,
  `42_wave4_agent_newton_relation_false_positives.md`.

### 5.5 Fatos bons nao viram relacoes

- Severidade: alta.
- Problema: melhorar a extracao nao basta; varios fatos funcionais nao sao
  consumidos pela taxonomia relacional.
- Exemplos:
  - `Ahri, Inquisitive`: `modify_stat` e `observe_event`, grau 0.
  - `Ravenborn Tome`: `pay` e `modify_stat`, grau 0.
  - `Carnivorous Snapvine`: `damage` e `observe_event`, grau 0.
  - Basic Runes e cartas com texto rico ficam sem relacao ou broad-only.
- Familias blind spot: `zone_movement`, `cost_resource`,
  `replacement_prevent_negation`, `attachment_gear`, `temporary`, `token_create`,
  `copy`, `swap`, `score_win`, `control`.
- Eventos produzidos sem observadores tambem precisam de classificacao: exemplos
  reportados incluem `spell_countered`, `gear_dies`, `unit_moved`,
  `token_created`, `equipment_detached`, `damage_dealt`, `card_banished`,
  `unit_dies`, `card_discarded` e `card_moved`; `self_discarded` apareceu como
  observado sem producer correspondente.
- Recomendacao: criar familias intermediarias de relacao para fatos funcionais e
  diagnostico `missing_relation_rule` quando uma carta rica fica degree 0/broad-only.
- Fontes: `14_wave1_agent_faraday_relations_web.md`,
  `25_wave2_agent_lovelace_relations_similarity.md`,
  `34_wave3_agent_franklin_relations_isolation.md`,
  `39_wave3_local_crosscheck.md`,
  `44_wave4_agent_erdos_test_invariants.md`,
  `43_wave4_agent_goodall_false_negatives.md`,
  `49_wave4_local_crosscheck.md`.

### 5.6 Dataset web e frontend perdem contrato util

- Severidade: alta.
- Problemas deduplicados:
  - `deck_synergy` existe no dataset, mas nao e renderizado no frontend.
  - Facetas publicadas pelo dataset nao aparecem na sidebar.
  - Filtros do dataset nao tem paridade com filtros do frontend.
  - Filtros sao globais e aplicados ao card relacionado, nao necessariamente a
    relacao.
  - Filtros/indices como `tags`, `produced_events`, `outputs`, `power` e
    modalidade existem ou sao derivados em etapas diferentes, mas nao formam um
    contrato unico entre builder, auditor e UI.
  - Vazio por filtro e vazio por falta de cobertura sao indistinguiveis.
  - Evidencia, reason, payload e ordenacao escondem a causa da categorizacao.
  - `RELATION_TYPES` e reports usam criterios divergentes.
- Recomendacao: dataset lossless para semantica usavel, preservando `fact_id`,
  role/type/predicate/payload, evidence/source, `match.reason`, `match.broad`,
  `strength`, diagnostics e filtros alinhados.
- Fontes: `04_downstream_web_and_reports.md`,
  `14_wave1_agent_faraday_relations_web.md`,
  `26_wave2_agent_boole_test_invariants.md`,
  `36_wave3_agent_hilbert_frontend_product.md`,
  `44_wave4_agent_erdos_test_invariants.md`.

### 5.7 Broad-only, high-degree e lacunas mascaradas

- Severidade: alta.
- Problema: `degree` alto ou relacao broad existente pode mascarar ausencia de
  relacao util. As 22 cartas broad-only sao principalmente spells sem sinal alto;
  parte tem efeito especifico que deveria gerar familia propria.
- Evidencia consolidada:
  - 100 cartas ficam sem relacao.
  - 22 cartas ficam broad-only.
  - 104 cartas com texto rico ficam sem relacao util.
  - P95 de grau reportado: 68; hubs artificiais passam muito acima disso por
    counterability.
- Exemplos: `Acceptable Losses`, `Keeper's Verdict`, `Angle Shot`,
  `Turn to Dust`, `Mystic Reversal`, `Ravenborn Tome`.
- Recomendacao: separar `relation_count`, `high_signal_relation_count`,
  `broad_only`, `missing_relation_rule`, `intentional_ignored` e
  `missing_extraction_producer/observer` nos reports e no dataset.
- Fontes: `34_wave3_agent_franklin_relations_isolation.md`,
  `39_wave3_local_crosscheck.md`,
  `43_wave4_agent_goodall_false_negatives.md`,
  `44_wave4_agent_erdos_test_invariants.md`,
  `49_wave4_local_crosscheck.md`.

### 5.8 Reports e documentacao podem dar falsa seguranca

- Severidade: media-alta.
- Problema: reports discordam sobre linhas relacionais descobertas, a auditoria
  semantica pode dizer `No issues`, e documentacao de estado atual tem contagens
  defasadas.
- Impacto: sinais de qualidade numerica ocultam lacunas semanticas reais.
- Recomendacao: centralizar criterios de `uncovered relational lines`,
  `broad_only`, `missing_relation_rule`, e datar snapshots de README/report.
- Fontes: `01_overview_and_core_risks.md`,
  `04_downstream_web_and_reports.md`,
  `11_wave1_agent_kant_contracts_goldens.md`,
  `14_wave1_agent_faraday_relations_web.md`,
  `36_wave3_agent_hilbert_frontend_product.md`.

## 6. Testes e invariantes recomendados

### 6.1 Lacuna principal dos testes atuais

- Goldens atuais testam presenca minima, nao ausencia de fatos indevidos.
- Falta suite independente de regressao para bugs reais ja encontrados.
- Falta limite esperado para `legacy_rule_count` e duplicatas contrato x legado.
- Falta paridade entre extracao, relacoes, dataset web, auditor web e frontend.
- Fontes: `00_final_prioritized_report.md`,
  `11_wave1_agent_kant_contracts_goldens.md`,
  `26_wave2_agent_boole_test_invariants.md`,
  `44_wave4_agent_erdos_test_invariants.md`.

### 6.2 Invariantes de fatos

Implementar testes para:

1. Polaridade de custo: `cost more` nunca vira `reduce_cost`; `cost no more than`
   vira restricao/cap, nao pagamento.
2. Negacao/restricao: `can't`, `cannot`, `don't`, `prevent`, `instead` nao geram
   evento produzido positivo.
3. Replacement: `would/instead` preserva evento substituido, output, duracao e
   modalidade.
4. Modalidade por clausula: `you may` nao contamina fatos obrigatorios da linha.
5. Choices: `Choose one` e `or` exclusivo preservam `choice_group_id` e
   `option_index`.
6. Trigger nao e efeito: trigger observado e payoff produzido ficam em fatos
   separados.
7. Reminder/quoted/effect text: reminder e texto copiado/anexado nao viram efeito
   ativo da carta fonte.
8. Attachment: attach e detach preservam direcao.
9. Keyword grant: `gain/give/have [Keyword]` gera `keyword_grant`, nao apenas
   `has_keyword`.
10. `must`, `up to` e estado de entrada preservam modalidade, cardinalidade e
    diferenca entre estado e evento.
11. Source evidence: todo fato textual aponta para campo, linha e substring
    verificavel.

### 6.3 Invariantes de relacao e web

Implementar testes para:

1. `spell_card_can_be_countered` sempre `broad=true`, rebaixado e fora das lanes
   default/high-signal.
2. `similar_effect` inclui alvo, amount, escopo, duracao e contexto nas chaves.
3. `resource_synergy` distingue pagamento real, custo opcional, custo parcial,
   cap/threshold e reducao.
4. `deck_synergy` nao duplica `enables` sem evidencia nova.
5. Carta com texto relacional forte nao pode ficar `degree=0` ou `broad_only` sem
   allowlist/diagnostico.
6. Eventos produzidos sem observadores entram em `intentional ignored`,
   `missing relation rule` ou `missing extraction producer/observer`.
7. Dataset web preserva fatos compactos, payload, evidence, reason, broad flag,
   counts e filtros alinhados ao frontend.
8. Modificadores de Might/stat, grants temporarios, control, score/win e zone
   movement geram pelo menos relacoes de familia quando existirem pares
   semanticamente equivalentes.

### 6.4 Ordem recomendada da suite

1. `contract_static_tests`: schema, ontology, extraction rules, relation rules e
   vazamento de dominio.
2. `fact_golden_tests`: fixtures reais com expected facts de alto nivel.
3. `fact_invariant_tests`: source_ref, evidence, modality, role/predicate/payload.
4. `relation_golden_tests`: `enables`, `enabled_by`, `similar_effect` e
   `deck_synergy` em fixtures pequenas.
5. `relation_quality_tests`: broadness, broad-only, skipped similarity e relation
   candidates sem link.
6. `web_dataset_tests`: compactacao lossless, filtros, counts, broad flags e
   diagnostics.

### 6.5 Fixtures prioritarias de regressao

Usar como fixtures reais, combinando expected facts positivos e forbidden facts:

1. Custo/recurso: `Vaults of Helia`, `Vex, Cheerless`, `Defy`, `Lux,
   Illuminated`, `Blood Rose`, `Voidreaver`, `Power Nexus`, `Altar of Blood`,
   `Honeyfruit`, `Jhin`.
2. Modalidade/choice: `Dancing Grenade`, `The Academy`, `The Candlelit Sanctum`,
   `Unlicensed Armory`, `Disposal Order`, `Rocket Barrage`, `Curtain Call`,
   `Aphelios`, `Udyr`, `King's Edict`, `Buhru Captain`.
3. Negacao/replacement: `Safety Inspector`, `Mageseeker Warden`, `Vilemaw's
   Lair`, `Rockfall Path`, `Counter Strike`, `Highlander`, `Guardian Angel`,
   `Zhonya's Hourglass`, `Soraka, Wanderer`.
4. Attachment/reminder/copy: `Rabadon's Deathcrown`, `Svellsongur`,
   `Grandmaster at Arms`, `Angle Shot`, `Spinning Axe`, `Mirror Image`,
   `Keeper of Masks`, `Reflection`.
5. Texto rico/downstream: `Switcheroo`, `Mystic Reversal`, `Possession`,
   `Minefield`, `Keeper's Verdict`, `Forgotten Monument`, `Tianna Crownguard`,
   `Ahri, Inquisitive`, `Fiora, Peerless`, `Ravenborn Tome`, `Acceptable Losses`.

## 7. Priorizacao consolidada

### P0 - corrigir antes de confiar na categorizacao

1. Polaridade de custo: `Vaults of Helia` e familia `cost more/no more than`.
2. Guards de negacao/prevent/replacement: `Safety Inspector`,
   `Mageseeker Warden`, `Rockfall Path`, `Counter Strike`, `Zilean, Time Mage`.
3. Choices exclusivos e modalidade por clausula: `Disposal Order`,
   `Dancing Grenade`, `The Academy`.
4. `effect_lines` attached-only e Equipment/Gear: `Rabadon's Deathcrown`,
   `Svellsongur`, `Veiled Temple`.
5. Broad de counter: filtrar/rebaixar `spell_card_can_be_countered` por padrao no
   dataset/frontend.
6. Goldens negativos para garantir ausencia de fatos indevidos.

### P1 - reduzir falsos positivos e falsos negativos grandes

1. Parse estruturado de custos ativados, XP, runas, energy, exhaust e kill self.
2. Separar contratos revisaveis de regras legadas ou limitar fatos legados por
   familia.
3. `keyword_grant` vs `has_keyword` vs referencia; cobrir keywords oficiais sem
   colchetes e grants temporarios.
4. Basic Runes, `[Add]`, Energy variavel, XP, `rainbow/any`.
5. Replacement/prevent completo, control, attach/detach, copy/becomes, score/win,
   swap, play restriction, temporary e zone movement.
6. `similar_effect`, `resource_synergy` e `derived_synergy` com chaves/dedupe mais
   especificos.
7. Modalidade `must`, governadores opcionais de outros atores, `up to`,
   cardinalidade e diferenca entre estado de entrada e acao.
8. Diagnostico de cartas com texto rico sem relacao util.

### P2 - maturidade de produto e manutencao

1. Extracao variant-aware para `rule_variants` ou warning persistente.
2. Paridade de `deck_synergy`, facetas e filtros entre dataset, auditor e frontend.
3. Centralizacao dos criterios de uncovered relational lines, broad-only e reports.
4. Atualizacao/datacao de documentacao com snapshots de contagem.
5. Expor evidencia, reason e payload de forma depuravel no frontend.

## 8. Arquivos principais envolvidos em correcoes futuras

- `scripts/04_cards_feature_extraction/extract_semantic_facts.py`
- `scripts/04_cards_feature_extraction/contracts/semantic_extraction_rules.json`
- `scripts/04_cards_feature_extraction/contracts/semantic_golden_examples.json`
- `scripts/04_cards_feature_extraction/contracts/semantic_facts_schema.json`
- `scripts/04_cards_feature_extraction/contracts/semantic_ontology.json`
- `scripts/04_cards_feature_extraction/contracts/semantic_relation_rules.json`
- `scripts/04_cards_feature_extraction/contracts/feature_relation_taxonomy.json`
- `scripts/04_cards_feature_extraction/audit_semantic_facts.py`
- `scripts/04_cards_feature_extraction/build_card_relations.py`
- `scripts/05_web_dataset/build_card_explorer_dataset.py`
- `scripts/05_web_dataset/audit_card_explorer_dataset.py`
- `web/app/app.js`

## 9. Mapa de cobertura dos parciais

Este mapa substitui a reproducao literal dos parciais. Cada linha indica onde os
topicos/problemas encontrados em cada arquivo foram incorporados neste
consolidado.

| Parcial | Topicos/problemas consolidados | Secoes |
|---|---|---|
| `00_final_prioritized_report.md` | P0/P1/P2, custo invertido, negacao, modalidade, choices, Effect Text attached-only, bugs provaveis e lacunas de teste | 1, 3.2, 4.1-4.6, 6, 7 |
| `01_overview_and_core_risks.md` | fluxo entrada/saida, opcionalidade por linha, negacao positiva, `ready token`, `rule_variants`, broad no frontend, docs defasadas | 1, 2.2, 4.3-4.6, 4.9, 5.1, 5.8 |
| `02_pre_pipeline_normalization_and_rules.md` | aquisicao raw fragil, `play_id`, `rule_variants`, `effect_lines`, choices achatados, regras oficiais sem validacao | 2.1-2.4, 3.1-3.2, 4.5 |
| `03_feature_extraction_findings.md` | custo `more` como reducao, duplicacao contrato/legado, triggers duplicados, optionalidade, negacao, `ready token`, choices, `effect_lines`, auditoria sem warning | 2.5, 4.1, 4.3-4.6, 4.9, 5.8, 6 |
| `04_downstream_web_and_reports.md` | `deck_synergy` invisivel, broad sem filtro, filtros sem paridade, reports divergentes, erros upstream no produto, docs desatualizadas | 5.1, 5.4, 5.6-5.8 |
| `10_extended_run_index.md` | escopo estendido, restricoes somente leitura e inventario das ondas | 1, 9 |
| `11_wave1_agent_kant_contracts_goldens.md` | goldens minimos, auditoria `No issues`, regras sobrepostas, schema incompleto, semantica legada | 2.5, 4.8, 5.8, 6.1 |
| `12_wave1_agent_hegel_pre_pipeline_normalization.md` | variantes colapsadas, `richest_printing`, reminder misturado, hierarquia modal perdida, equipment sem contexto attached | 2.2-2.4, 3.2, 4.6 |
| `13_wave1_agent_lagrange_corpus_patterns.md` | `would/instead`, negacao, `choose one`, copy/becomes, `up to`, additional cost, more/less, swap, goldens negativos | 4.1, 4.3, 4.5, 4.7, 4.9, 6.5 |
| `14_wave1_agent_faraday_relations_web.md` | hubs broad, `deck_synergy`, `resource_synergy`, `derived_synergy`, similaridade larga, fatos sem relacao, filtros e reports divergentes | 5.1-5.8 |
| `15_wave1_agent_hooke_clause_modality_negation.md` | modalidade por linha, governadores opcionais estreitos, `must`, negacao, prevent/replacement, `activation_split`, `clause_group_id` | 2.4, 4.2-4.4, 4.9, 6.2 |
| `16_wave1_agent_meitner_stage_contracts.md` | reminder executavel, activation como trigger, XP perdido, variantes ignoradas, runas fora do contrato, `deck_synergy` invisivel | 2.2, 3.3, 4.2, 4.6, 5.4, 5.6 |
| `19_wave1_local_crosscheck.md` | `generic_cost_reduction` em limites, `can't move` positivo, `or` inline, `effect_lines` sem contexto, goldens negativos | 3.2, 4.1, 4.3, 4.5-4.6, 6.5 |
| `21_wave2_agent_carver_cost_resource.md` | XP spend perdido, truncamento de simbolos, thresholds como reducao, cost more/less composto, additional/ignore cost, resource synergy falsa | 3.3, 4.1-4.2, 5.3, 6.5 |
| `22_wave2_agent_sartre_replacement_negation.md` | replacement solto, delayed prevent ausente, negacao positiva, negacoes sem fato, custo dentro de replacement | 4.2-4.3, 6.2 |
| `23_wave2_agent_pascal_modals_choices.md` | `Choose one`, flattening de bullets, Repeat/modal, inline `or`, memoria de escolha, escolha de alvo vs modo | 2.4, 3.5, 4.5, 6.5 |
| `24_wave2_agent_leibniz_attachment_reminder.md` | Equip reminder duplicando custo, `effect_lines` ativas, reminder funcional, attach ausente, Svellsongur copy, Recall de The Boss | 3.2, 3.5, 4.6-4.7, 6.5 |
| `25_wave2_agent_lovelace_relations_similarity.md` | `similar_effect` largo, broad de counter, `resource_synergy`, `derived_synergy`, fatos isolados | 5.1-5.5 |
| `26_wave2_agent_boole_test_invariants.md` | invariantes/goldens, duplicacao de trigger, modalidade, regras especificas/genericas, web matcher divergente, broad, paridade web, maturidade de contratos | 2.5, 5.1, 5.6-5.8, 6 |
| `29_wave2_local_crosscheck.md` | activation captura trigger/condicao, XP perdido, replacement pouco modelado, `would/instead/prevent` com custos opcionais e outputs | 4.2-4.3, 6.2 |
| `31_wave3_agent_ramanujan_core_rules.md` | reminder, Effect Text de Gear, Recall, modes/choices, additional/ignore costs, replacement/prevent, Basic Runes, Equip/Repeat/Accelerate, Tank/Deflect | 3.1-3.5, 4.1, 4.3, 4.5-4.6 |
| `32_wave3_agent_dalton_sampling.md` | custos com simbolos, reminder/aspas, copy, modais, score/win, Recall, broad-only/texto rico, variants | 2.2, 4.2, 4.5-4.7, 4.9, 5.7 |
| `33_wave3_agent_kepler_payload_schema.md` | schema/payload incompleto, ontologia, evidencia/source_ref, `web_uses`, shapes negativos/duplicados | 4.8, 5.6, 6.2 |
| `34_wave3_agent_franklin_relations_isolation.md` | counterability como grafo principal, 22 broad-only, 100 sem relacao, fatos bons isolados, hubs high-signal com fan-out generico | 5.1, 5.4-5.5, 5.7 |
| `35_wave3_agent_harvey_runes_resources.md` | Basic Runes vanilla, `[Add]` truncado, XP, `rainbow/any`, custos condicionais/variaveis, Channel/Recycling | 3.3, 3.5, 4.2, 5.3 |
| `36_wave3_agent_hilbert_frontend_product.md` | `deck_synergy` invisivel, broad como recomendacao, vazio filtro/cobertura, filtros globais, facetas ausentes, evidencia/ordenacao, reports divergentes | 5.1, 5.4, 5.6, 5.8 |
| `39_wave3_local_crosscheck.md` | cartas sem relacao com fatos uteis, runas sem relacao, broad-only com efeitos concretos, hubs de counter | 3.3, 5.1, 5.5, 5.7 |
| `41_wave4_agent_noether_keywords_official_terms.md` | Accelerate, keyword marker em referencias/grants, `[Add]`, Add Energy/static, keywords sem colchetes, `When you conquer`, Weaponmaster/Equip | 3.3-3.6 |
| `42_wave4_agent_newton_relation_false_positives.md` | counter broad, similaridade generica, resource synergy com custo/restricao, `derived_synergy` duplicada | 5.1-5.4 |
| `43_wave4_agent_goodall_false_negatives.md` | temporary/granted keyword, replacement/prevent, attachment/equipment, control, swap, score/win, zone movement, copy, token creation, play restriction | 3.4, 4.3, 4.7, 5.5, 5.7 |
| `44_wave4_agent_erdos_test_invariants.md` | suite independente: trigger vs efeito, modalidade, activation payload, evidence, negacao, replacement, Might similarity, keyword grant, attach/detach, broad, broad-only, dataset lossless, linha relacional sem fact, eventos sem observadores | 4.2-4.9, 5.1, 5.5-5.8, 6 |
| `49_wave4_local_crosscheck.md` | cobertura de termos oficiais, keywords defensivas/permissao, texto rico sem relacao, broad de counter, blind spots e broad-only especifico | 3.4, 4.7, 5.1, 5.5, 5.7 |
| `99_completion_audit.md` | checklist de escopo, restricoes e conclusao da auditoria original | 1, 9, 10 |

## 10. Conclusao

O pipeline ja tem bons artefatos de rastreabilidade, mas a categorizacao ainda
nao deve ser tratada como fonte confiavel de produto sem corrigir a falsa
semantica de alto impacto. A ordem segura e corrigir primeiro fatos errados
(polaridade, negacao, modalidade, choices e contexto attached), depois ampliar
familias ausentes, e so entao otimizar cobertura e experiencia do explorador.
