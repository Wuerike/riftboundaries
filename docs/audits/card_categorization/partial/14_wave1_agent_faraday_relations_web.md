# Onda 1 - agente Faraday - relacoes, dataset web e frontend

## Escopo

Auditoria nao mutante de `build_card_relations.py`, `semantic_relation_rules.json`, `semantic_quality_policy.json`, `cards_card_relations.jsonl`, `scripts/05_web_dataset` e `web/app`.

Tambem foram lidos para confronto:

- `cards_normalized.json`
- `cards_semantic_facts.jsonl`
- `card_explorer_dataset.json`
- relatorios web e de relacoes existentes

O agente informou que nenhum arquivo foi editado e que nao executou builders/auditors que escrevem saida; a validacao foi feita lendo artefatos e rodando consultas Python somente leitura sobre JSON/JSONL.

## Entrada e saida conferida

- Cartas normalizadas: 767.
- Fatos semanticos: 5428.
- Relacoes: 9884.
- Tipos: `similar_effect=4746`, `enabled_by=2041`, `enables=2041`, `deck_synergy=1056`.
- Dataset web preserva todos os IDs: 9884/9884 relacoes em outgoing e incoming; 5428/5428 fatos.
- Filtros no dataset: `domains`, `card_types`, `tags`, `keywords`, `triggers`, `produced_events`, `outputs`, `predicates`, `energy`, `might`, `power`.

## Achados

### F1 - `spell_card_can_be_countered` cria hubs broad artificiais

- categoria do achado: integracao entre etapas
- severidade: alta
- confianca: alta
- evidencia: a regra em `semantic_relation_rules.json` liga todo `spell` a todo fato `counter`, gerando 3438 relacoes, 34.78% do grafo. `Acceptable Losses` (`Each player kills one of their gear`) e `Progress Day` (`Draw 4.`) ficam com 18 relacoes so porque sao spells counteraveis. `Abandon` tem 471 relacoes, 398 broad; `Wind Wall` tem 410, 398 broad.
- regra relacionada: `spell_card_can_be_countered`.
- impacto provavel no produto final: o frontend mostra `Enabled Cards/Enablers` como se counterabilidade fosse sinergia ou relacao estrategica.
- recomendacao: mover essa familia para `rules_interaction` ou `counterability`, ocultar/demotar por padrao e excluir de scoring/contadores principais.
- teste que deveria existir: teste de broad garantindo que `spell_card_can_be_countered` nao entra em ranking/contadores default.

### F2 - `deck_synergy` existe no dataset mas e invisivel no frontend

- categoria do achado: integracao entre etapas
- severidade: alta
- confianca: alta
- evidencia: `build_card_explorer_dataset.py` inclui `deck_synergy`, mas `web/app/app.js` define `RELATION_TYPES = ["enabled_by", "enables", "similar_effect"]`. `Dragonsoul Sage` tem 58 outgoing `deck_synergy` e so 5 relacoes visiveis no app. `Bushwhack` tem 63 incoming `deck_synergy`; `Mistfall` tem 51 incoming `deck_synergy`; nada disso aparece como lane.
- regra relacionada: `deck_synergy` em `semantic_relation_rules.json`.
- impacto provavel no produto final: uma das quatro familias geradas e documentadas nao e exploravel.
- recomendacao: adicionar lane/filtro de `deck_synergy` com direcao clara, ou remover essa familia do contrato web ate existir UX para ela.
- teste que deveria existir: snapshot de contrato frontend: todo relation type do dataset deve ser renderizado ou explicitamente ignorado.

### F3 - `resource_synergy` gera sinergia falsa por custo amplo

- categoria do achado: categorizacao incorreta
- severidade: media-alta
- confianca: alta
- evidencia: `resource_synergy` produziu 415 relacoes; `cost:energy:1` sozinho gerou 348. Exemplos: `Dragonsoul Sage` `[Add] energy 1` -> `Ancient Warmonger` `[Accelerate] energy 1` e plausivel, mas tambem -> `Atakhan` por texto de custo reduzido e -> `Vex, Cheerless` por `spells cost less`, que nao sao custos pagaveis diretos.
- regra relacionada: `resource_synergy`; familias de custo.
- impacto provavel no produto final: deck synergy mistura gerador de recurso, custo adicional, custo ativado e redutor de custo.
- recomendacao: separar `pay_cost`, `additional_cost`, `activated_cost`, `cost_reduction`; `resource_synergy` deve mirar so custos pagaveis consumiveis.
- teste que deveria existir: gerador de recurso nao deve ligar a redutores de custo.

### F4 - `derived_synergy` duplica relacoes e amplifica regras genericas

- categoria do achado: integracao entre etapas
- severidade: media
- confianca: alta
- evidencia: toda relacao `enables` vira `deck_synergy`. `Atakhan -> Altar of Memories` aparece duas vezes: `synergy_from_friendly_unit_dies...` e `synergy_from_generic_unit_death...`.
- regra relacionada: `derived_synergy`.
- impacto provavel no produto final: quando `deck_synergy` for exibida, havera duplicidade e peso artificial para a mesma interacao.
- recomendacao: deduplicar por par + familia semantica, preferindo a regra mais especifica.
- teste que deveria existir: teste de dedupe de `deck_synergy` derivada por par de cartas.

### F5 - Similaridade falsa por chaves largas e condicoes perdidas

- categoria do achado: categorizacao incorreta
- severidade: media-alta
- confianca: alta
- evidencia:
  - `Arena Kingpin` (`I enter ready`) similar a `Breakneck Mech` (`I enter ready if you control another Mech`) e `Bandle Soldier` (`[Level 3] I enter ready`).
  - `Bellows Breath` (`Deal 1 to up to three units`) similar a `Final Spark` (`Deal 8 to a unit`) via `secondary:damage:positive:unit`.
  - `Abandon` (`Return [spell] to hand`) similar a `Downwell` (`Return all units and gear`) por chave `unit_recalled` sem alvo forte.
- regra relacionada: `similarity`.
- impacto provavel no produto final: `Similar Effects` parece preciso, mas agrupa cards operacionalmente diferentes.
- recomendacao: incluir gates/condicoes (`if`, level, paid cost), quantidade, alvo, controller e escopo na chave; reduzir cap por chave e marcar grupos com muitos cards como broad.
- teste que deveria existir: goldens negativos de similaridade para `Arena Kingpin/Breakneck Mech`, `Bellows Breath/Final Spark`, `Abandon/Downwell`.

### F6 - Ha fatos bons que nao viram relacoes

- categoria do achado: regra ausente
- severidade: media
- confianca: alta
- evidencia: 1766 fatos candidatos; 736 nao usados em relacao. Top unlinked: `observe_event=320`, `pay=70`, `move=51`, `require=49`, `draw=49`. Exemplos: `Ahri, Inquisitive` tem `modify_stat` + triggers `self_attacks/self_defends` e 0 relacoes; `Mageseeker Warden` tem permissoes/restricoes de play/ready e 0 relacoes; `Vilemaw` tem prevent + draw on hold e 0 relacoes.
- regra relacionada: `semantic_relation_rules.json`; relation readiness.
- impacto provavel no produto final: isolamento real ainda existe, especialmente stat/location/permission.
- recomendacao: criar familias estreitas para modificadores de Might/damage, permissoes de play/move, prevencao e triggers de hold/conquer.
- teste que deveria existir: auditoria de fatos candidatos sem relacao por familia de alta prioridade.

### F7 - Filtros do dataset e frontend divergem

- categoria do achado: integracao entre etapas
- severidade: media
- confianca: alta
- evidencia: dataset tem `tags=113`, `produced_events=22`, `outputs=43`, `power=4`; frontend expoe so domain/type/trigger/keyword/energy/might/predicate. Alem disso, filtros sao por carta relacionada inteira, nao pela relacao. Exemplo: filtro `draw` pode manter `Keeper of the Hammer` numa relacao de `gain_xp`, porque a carta tambem tem predicado `draw`.
- regra relacionada: contrato do dataset web.
- impacto provavel no produto final: usuario pensa filtrar relacoes, mas filtra atributos globais da carta.
- recomendacao: expor filtros omitidos ou remove-los do contrato; adicionar filtros por `relation.match`, `source_fact_id/target_fact_id` e evidencia.
- teste que deveria existir: teste de paridade de filtros e teste de filtro por relacao, nao so por carta.

### F8 - Divergencia entre relatorios web

- categoria do achado: manutencao
- severidade: baixa-media
- confianca: alta
- evidencia: `build_card_explorer_dataset.py` usa substring simples para linhas relacionais. Isso marca falso positivo em `Rockfall Path` por `play` dentro de `played` e `Curtain Call` por `ready` dentro de `already`. O auditor de qualidade usa tokenizacao com borda e reporta 0 uncovered lines. O README de `scripts/05_web_dataset` tambem esta defasado: cita 5382 fatos e 9047 relacoes, mas o dataset atual tem 5428 e 9884.
- regra relacionada: `semantic_quality_policy.json` / `relational_keywords`.
- impacto provavel no produto final: relatorios e documentacao passam sinais conflitantes.
- recomendacao: compartilhar a mesma funcao de tokenizacao e atualizar o README a partir do dataset atual.
- teste que deveria existir: teste unico de tokenizacao de `relational_keywords` usado por builder e auditor.

## Testes faltando

- Snapshot de contrato frontend: todo relation type e filtro do dataset deve ser renderizado ou explicitamente ignorado.
- Goldens negativos para similaridade: `Arena Kingpin/Breakneck Mech`, `Bellows Breath/Final Spark`, `Abandon/Downwell`.
- Teste para broad: `spell_card_can_be_countered` nao pode entrar em ranking/contadores default.
- Teste para `resource_synergy`: gerador de recurso nao deve ligar a redutores de custo.
- Teste de dedupe de `deck_synergy` derivada por par de cartas.
- Teste unico de tokenizacao de `relational_keywords` usado por builder e auditor.

## Comandos usados

- `git status --short`
- `rg --files`
- `Get-Content -Raw ...` nos contratos, scripts e frontend.
- `rg -n "relation|similar|synerg|deck|filter|dataset" ...`
- Consultas Python somente leitura para contar cartas/fatos/relacoes, validar IDs preservados e extrair exemplos concretos.

O agente nao rodou `build_card_relations.py`, `build_card_explorer_dataset.py` nem `audit_card_explorer_dataset.py` porque escrevem arquivos por padrao.
