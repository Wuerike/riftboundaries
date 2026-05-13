# Onda 1 - agente Kant - contratos, schema, goldens e auditorias

## Escopo

Auditoria nao mutante de `scripts/04_cards_feature_extraction`, com foco em qualidade dos contratos, schema, exemplos dourados e auditorias.

O agente informou que nao editou arquivos e nao rodou `validate_semantic_golden_examples.py` nem `audit_semantic_facts.py` com defaults porque ambos escrevem relatorios. Foram feitas apenas validacoes/leitura/analises in-memory.

## Resumo do agente

- Contratos carregam e validam: `python scripts\04_cards_feature_extraction\validate_semantic_contracts.py` retornou `Semantic contracts valid; no new domain leakage found.`
- Base lida: 767 cartas normalizadas, 5.428 fatos JSONL.
- Goldens: 40 exemplos, 73 fatos esperados, 73/73 passam.
- As linhas dos goldens batem com `cards_normalized.json`: 0 divergencias.
- Ponto principal: os goldens validam presenca minima, nao ausencia nem completude.

## Achados

### A1 - Goldens sao presenca minima, nao testam ausencia

- categoria do achado: teste faltante
- severidade: alta
- confianca: alta
- evidencia: `semantic_golden_examples.json:6` define `comparison_mode: minimum_expected_facts`. O validador so compara `semantic_role`, `fact_type`, `predicate`, `evidence` e subconjunto de `payload` em `validate_semantic_golden_examples.py:71`. `fact_id`, `clause_group_id` e `web_expectations` nao sao validados.
- exemplos concretos:
  - `Sprite Fountain`: golden espera 7 fatos, mas ha 10 fatos nas linhas douradas. Extras incluem outro `kill/self_dies`, marcador `[Temporary]` no token e `ready` para o token.
  - `Confront`: golden espera so `enter_ready`, mas a mesma linha tambem emite `Draw 1`.
  - `Rumble, Hotheaded`: golden espera 3 fatos na linha; a extracao real tem 4, incluindo o trigger `When I conquer`.
- regra relacionada: `semantic_golden_examples.json`; `validate_semantic_golden_examples.py`.
- impacto provavel no produto final: regressoes que adicionem fatos indevidos continuam passando se os fatos minimos ainda existirem.
- recomendacao: adicionar `forbidden_facts`, `exact_expected_facts` ou `max_fact_count_by_source_line`; validar `web_expectations`.
- teste que deveria existir: goldens negativos e modo exato para linhas sensiveis.

### A2 - Auditoria reporta "No issues" apesar de linhas relacionais sem fatos

- categoria do achado: teste faltante
- severidade: alta
- confianca: alta
- evidencia: `cards_semantic_audit_report.md:12` mostra 27 linhas sem fatos, `warning_count: 0` em `cards_semantic_audit_report.md:15` e `No issues found` em `cards_semantic_audit_report.md:75`. As linhas relacionais descobertas sao so listadas em cobertura; nao viram issue em `audit_semantic_facts.py:300`.
- exemplos concretos:
  - `Rockfall Path`: `Units can't be played here.` deveria virar restricao de play/location.
  - `Curtain Call`: `Choose one you haven't already chosen -` e restricao/modalidade de escolha, mas fica sem fato.
- regra relacionada: `semantic_quality_policy.json`; `audit_semantic_facts.py`.
- impacto provavel no produto final: o relatorio da sinal verde mesmo com lacunas semanticas relevantes.
- recomendacao: elevar `uncovered_relational_lines` para warning/error por politica.
- teste que deveria existir: goldens positivos/negativos para `Rockfall Path` e escolha modal.

### A3 - Regras sobrepostas geram fatos duplicados

- categoria do achado: categorizacao incorreta
- severidade: alta
- confianca: alta
- evidencia: `trigger_self_conquers_or_holds` casa `When I conquer or hold` e `trigger_self_conquers` tambem casa o prefixo `When I conquer` em `semantic_extraction_rules.json:67`. O agente detectou 18 grupos de duplicidade exata de payload por linha.
- exemplos concretos:
  - `Arachnoid Horror`: JSONL linhas 178 e 180 emitem o mesmo `trigger_observed/self_conquers`.
  - `Disposal Order`, `Kai'Sa, Evolutionary`, `Twisted Fate, Gambler`: `recycle_card` aparece duplicado por regra contratual + legado.
- regra relacionada: `trigger_self_conquers_or_holds`, `trigger_self_conquers`, `recycle_card`.
- impacto provavel no produto final: relacoes, contagens e score de sinergia podem inflar artificialmente.
- recomendacao: auditoria deveria detectar duplicidade por `(play_id, source_ref, role, type, predicate, payload)` ignorando `fact_id`/`evidence`.
- teste que deveria existir: teste de duplicidade exata por linha e payload.

### A4 - Schema de payload esta incompleto frente aos fatos reais

- categoria do achado: arquitetura
- severidade: media
- confianca: alta
- evidencia: `semantic_facts_schema.json:306` lista so 13 chaves de `payload`. Nos fatos reais aparecem chaves nao descritas: `stat` 1399 vezes, `destination` 81, `keywords` 35, `source` 28, `resource` 25, alem de `replacement`, `multiplier`, `scaling`, `prevented_action`, etc.
- exemplos concretos:
  - `Abandon`: payload usa `stat` para `energy:2`.
  - `Janna, Savior`: movimento usa `destination`.
  - `Zilean, Time Mage`: replacement usa `replacement`.
- regra relacionada: `semantic_facts_schema.json`; contratos downstream.
- impacto provavel no produto final: consumidores downstream nao tem contrato completo do shape real de `payload`.
- recomendacao: formalizar payload por `fact_type/predicate` ou declarar chaves extensives explicitamente; auditar chaves desconhecidas.
- teste que deveria existir: auditoria de chaves de payload por predicado/fact_type.

### A5 - Migracao para contratos ainda tem semantica legada

- categoria do achado: arquitetura
- severidade: media
- confianca: alta
- evidencia: `cards_semantic_audit_report.md:18` mostra `legacy_rule_count: 658`. Breakdown lido do JSONL pelo agente: `keyword_marker` 651, `recycle_card` 3, `move_unit` 3, `give_might` 1.
- exemplo concreto: `Disposal Order` tem `recycle_card` contratual e legado emitindo payload equivalente na mesma linha.
- regra relacionada: `semantic_extraction_rules.json`; `extract_semantic_facts.py`.
- impacto provavel no produto final: parte da semantica segue fora do contrato declarativo e pode duplicar regras migradas.
- recomendacao: permitir legado apenas para `keyword_marker` por enquanto; falhar ou avisar para qualquer legado semantico novo.
- teste que deveria existir: teste de budget/allowlist para `legacy_rule` por regra.

## Comandos relevantes informados pelo agente

```powershell
python scripts\04_cards_feature_extraction\validate_semantic_contracts.py
rg --files scripts\04_cards_feature_extraction
rg -n "comparison_mode|minimum_expected_facts|web_expectations" scripts\04_cards_feature_extraction\contracts\semantic_golden_examples.json
rg -n "uncovered_relational_lines|warning_count|issue_counts" scripts\04_cards_feature_extraction\audit_semantic_facts.py
```

O agente tambem usou scripts Python inline somente leitura para cruzar `cards_normalized.json`, `cards_semantic_facts.jsonl` e os goldens, sem gravar saidas.
