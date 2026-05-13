ATENÇÃO: Rode uma análise não mutante no repo atual por 5 horas, ou até esgotar o orçamento disponível. Não altere código, configs, dados de entrada ou outputs existentes. A única escrita permitida é criar relatórios Markdown em `docs/audits/card_categorization/`.

Objetivo central: avaliar a qualidade, riscos e oportunidades de melhoria do processo de categorização das cartas. A análise deve deixar claro:
- qual é a entrada inicial do sistema;
- onde estão as cartas normalizadas;
- quais regras orientam a categorização;
- como as cartas são transformadas ao longo do pipeline;
- qual é o produto final esperado;
- onde podem surgir erros de categoria, perda de informação, inconsistência ou baixa cobertura.

Comece adquirindo conhecimento geral do repo: leia documentação existente, READMEs, scripts de pipeline, testes e configs relevantes. Depois leia o código. O maior foco deve estar em `scripts\04_cards_feature_extraction`, mas analise também as etapas anteriores e posteriores necessárias para entender contratos de entrada/saída, dependências, formatos de dados e riscos de integração.

Em todas as iterações, uma ação obrigatória é reler as cartas normalizadas e as regras de categorização relevantes. Cada ciclo deve confrontar o comportamento do código com exemplos concretos de cartas e com as regras esperadas. Não faça uma análise apenas abstrata do código.

Use subagentes com contexto limpo para análises independentes por etapa ou por tipo de risco. Cada subagente deve receber uma tarefa objetiva e produzir achados com evidências. Evite que vários agentes analisem exatamente o mesmo escopo. Sempre que possível, peça aos subagentes que validem conclusões contra cartas normalizadas e regras, não apenas contra o código.

Faça iterações de análise. Ao final de cada iteração, salve um relatório parcial contendo:
- escopo analisado;
- arquivos principais lidos;
- cartas normalizadas consultadas;
- regras de categorização consultadas;
- entendimento da entrada e saída da etapa;
- como a etapa contribui para a categorização das cartas;
- riscos/bugs encontrados;
- exemplos concretos de cartas afetadas, quando houver;
- testes faltando;
- oportunidades de melhoria;
- dúvidas ou hipóteses ainda não confirmadas.

Para cada achado, use este formato:
- categoria do achado: categorização incorreta, regra ambígua, regra ausente, parsing/normalização, integração entre etapas, arquitetura, teste faltante ou manutenção;
- severidade: crítica, alta, média ou baixa;
- confiança: alta, média ou baixa;
- evidência: arquivo, linha e/ou exemplo de carta;
- regra relacionada;
- impacto provável no produto final;
- recomendação;
- teste que deveria existir.

Priorize achados que possam causar categorização incorreta das cartas, especialmente quando:
- uma carta pode receber categoria errada;
- uma carta deveria receber uma categoria mas fica sem classificação;
- uma regra é aplicada de forma inconsistente;
- o código diverge das regras documentadas;
- cartas com textos parecidos são categorizadas de formas incompatíveis;
- mudanças nas cartas normalizadas podem quebrar silenciosamente o resultado final.

Antes de encerrar, consolide todos os relatórios em um relatório final priorizado, separando:
1. riscos críticos para a categorização correta das cartas;
2. bugs prováveis em `scripts\04_cards_feature_extraction`;
3. divergências entre regras, cartas normalizadas e implementação;
4. lacunas de teste com exemplos concretos;
5. fragilidades de arquitetura ou contratos entre etapas;
6. melhorias de manutenção.

Não implemente correções. Não faça commits. Se precisar executar comandos, prefira comandos de leitura, testes existentes e inspeção. Registre qualquer teste/comando executado e o resultado.
