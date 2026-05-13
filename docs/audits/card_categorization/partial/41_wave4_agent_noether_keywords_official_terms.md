# Onda 4 - keywords e termos oficiais

Escopo respeitado: somente leitura, sem edicao de arquivos.

## Achados priorizados

### 1. Accelerate tem marcador, mas nao gera semantica de entrar ready

- categoria: lacuna
- severidade: alta
- confianca: alta
- evidencia: `AccelerateText_no_enter_ready`: `24/24` cartas com Accelerate nao tem fato `enter_ready`. Ex.: `Lee Sin, Centered` tem `has_keyword=accelerate` e `pay`, mas nao `enter_ready` em `cards_semantic_facts.jsonl:2637`. A regra oficial diz que Accelerate e "If you do, I enter ready" em `core-rules.md:5327`.
- regra relacionada: `self_enters_ready` so captura `I enter ready` em `semantic_extraction_rules.json:1309`.
- impacto: busca/sinergia por entrada ready perde todas as unidades com Accelerate.
- teste recomendado: para todo fato `has_keyword=accelerate`, exigir fato derivado `enter_ready` condicionado ao custo adicional pago.

### 2. `keyword_marker` marca referencias/grants como keyword intrinseca da carta

- categoria: falso positivo
- severidade: alta
- confianca: alta
- evidencia: `Emperor of the Sands` recebe `has_keyword=equip` so porque o reminder de Weaponmaster contem `[Equip]`, em `cards_semantic_facts.jsonl:1395`. `Karthus, Eternal` recebe `has_keyword=deathknell` por `Your [Deathknell] effects...`, em `cards_semantic_facts.jsonl:2450`. `Lillia, Protector of Dreams` tambem marca `[Tank]` na carta enquanto o efeito e `Your token units have [Tank]`.
- regra relacionada: extracao legada `keyword_marker`; contratos tem regras melhores como `target_has_keywords` em `semantic_extraction_rules.json:862`.
- impacto: filtros por cartas com Tank/Equip/Deathknell ficam poluidos com cartas que apenas mencionam ou concedem keywords.
- teste recomendado: `has_keyword` so para keyword propria/intrinseca; textos `have/gain/give [Keyword]` devem gerar `keyword_grant`; referencias devem gerar descriptor separado.

### 3. `[Add]` e tratado como keyword, embora seja acao oficial

- categoria: falso positivo
- severidade: alta
- confianca: alta
- evidencia: `Seal of Strength` tem `has_keyword=add` em `cards_semantic_facts.jsonl:3958` e tambem o fato correto `add_resource` em `cards_semantic_facts.jsonl:3959`. Core rules definem Add como acao em `core-rules.md:1178` e secao propria em `core-rules.md:3701`.
- regra relacionada: ontologia tem `add_resource` como acao em `semantic_ontology.json:41`.
- impacto: contaminacao dos filtros de keyword; dupla contagem de identidade e geracao de recurso.
- teste recomendado: assertar zero fatos `predicate=has_keyword` com `payload.object.id=add`.

### 4. Padroes de Add com Energy/modificador estatico nao viram `add_resource`

- categoria: lacuna
- severidade: media
- confianca: alta
- evidencia: `Hextech Anomaly` diz `Pay any amount of [A] to [Add] that much Energy`, mas so gera `has_keyword=add`, sem `add_resource`, em `cards_semantic_facts.jsonl:2087`. `Chem-Baroness` diz `your Gold [ADD] an additional [1]` e tambem so vira keyword marker em `cards_semantic_facts.jsonl:759`.
- regra relacionada: `add_resource` espera simbolo `:rb_energy_N:` ou `:rb_rune_*:` depois de `[Add]` em `semantic_extraction_rules.json:522`.
- impacto: geracao variavel de Energy e buffs de Gold ficam invisiveis para sinergia de ramp.
- teste recomendado: cobrir `[Add] that much Energy` e `X [ADD] an additional [1]`.

### 5. Keywords oficiais sem colchetes nao viram `has_keyword`

- categoria: lacuna
- severidade: media
- confianca: alta
- evidencia: `Laurent Bladekeeper` tem `Ganking (I can move...)` em `cards_normalized.json:59820`, mas nao tem `has_keyword=ganking`; so gera permissao de movimento em `cards_semantic_facts.jsonl:2591`. `Windsinger` tem `Hidden (...)` em `cards_normalized.json:78602`, mas nao tem `has_keyword=hidden`.
- regra relacionada: `keyword_marker` aparentemente depende de `[Keyword]`.
- impacto: cobertura nominal falha quando o normalizado oficial omite colchetes.
- teste recomendado: inicio de linha `Keyword (` deve gerar `has_keyword` para keywords oficiais.

### 6. Triggers `When you conquer` nao cobertos

- categoria: lacuna
- severidade: media
- confianca: alta
- evidencia: `12` cartas com `conquer` nao tem trigger `self_conquers`/`battlefield_conquered`. Exemplos: `Might of Demacia - Starter`, `The Boss`, `Blade Dancer`, `Piltover Enforcer`, `Void Burrower`. A regra cobre `When I conquer` e `When you conquer here`, mas nao `When you conquer`.
- regra relacionada: `trigger_self_conquers` em `semantic_extraction_rules.json:77`, `trigger_battlefield_conquered` em `semantic_extraction_rules.json:97`.
- impacto: efeitos de legend/spell ligados ao jogador conquistar nao entram em `enabled_by`.
- teste recomendado: `When you conquer[, or hold]` deve mapear para evento do jogador/controlador, sem capturar meras referencias como `conquer effects`.

### 7. Weaponmaster/Equip em Emperor of the Sands esta submodelado

- categoria: lacuna + falso positivo
- severidade: media
- confianca: media
- evidencia: `Emperor of the Sands` deveria conceder Weaponmaster a Sand Soldiers e permitir Equip com desconto; fatos mostram `has_keyword=weaponmaster` e `has_keyword=equip`, mas nao modelam `keyword_grant`/attach para o alvo em `cards_semantic_facts.jsonl:1394`.
- regra relacionada: `weaponmaster_equip` exige texto mais especifico `to me` em `semantic_extraction_rules.json:677`.
- impacto: sinergias de Equipment/attach em tokens ficam incompletas.
- teste recomendado: fixture para `Sand Soldiers you play have [Weaponmaster]...` esperando `keyword_grant` ao token e efeito de attach/desconto referenciado.

## Goldens e controles positivos

- Channel: `22/22` textos com `channel(s)` tem fato `channel`; bom caso em Obelisk/Startipped/Ripper's Bay.
- Recall: `12/12` textos com `recall` tem `return_to_hand`; bom sinal para regra `recall_unit`.
- Recycle: cobertura boa em acoes e triggers; `Abandon` gera `recycle` corretamente em `cards_semantic_facts.jsonl:7`.
- Repeat effect textual: `Sprite Fountain` gera `repeat_effect` corretamente em `cards_semantic_facts.jsonl:4328`.
- Score: `Ahri, Alluring` gera `score` e trigger de hold corretamente em `cards_semantic_facts.jsonl:37`.
- Slow/Fast: nao encontrei ocorrencia em regras/cartas/fatos no escopo lido.

## Comandos somente leitura usados

```powershell
Get-ChildItem -LiteralPath <arquivo> | Select-Object FullName,Length,LastWriteTime
Get-Content -LiteralPath <arquivo> -TotalCount N
rg -n "Assault|Tank|Deflect|Ganking|Hidden|Deathknell|Reaction|Slow|Fast|Equip|Repeat|Accelerate|Channel|Recycle|Buff|Recall|\bAdd\b|Score|Conquer" <arquivos>
Get-Content -LiteralPath data/processed/cards/normalized/cards_normalized.json -Raw | ConvertFrom-Json
Get-Content -LiteralPath data/processed/cards/semantic/cards_semantic_facts.jsonl | ForEach-Object { $_ | ConvertFrom-Json }
rg -n -C 3 "Laurent Bladekeeper|Windsinger|Sprite Fountain|Baron Nashor" data/processed/cards/normalized/cards_normalized.json
rg -n "Lee Sin, Centered|Legion Rearguard|Nilah, Joyful Ascetic" data/processed/cards/semantic/cards_semantic_facts.jsonl
```
