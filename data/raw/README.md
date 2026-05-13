# Dados Brutos (`data/raw/`)

Este diretório contém os dados originais do projeto Riftbound, intocados, para servirem de base para a construção do grafo. **Não modifique os arquivos desta pasta manualmente.**

## O que deve estar aqui?

1. **`cards.json`**: O banco de dados completo de cartas extraído do site oficial (gerado pelo script `scripts/01_cards_extraction/fetch_cards.py`).
2. **Arquivos PDF**: Manuais oficiais baixados do [Riftbound Rules Hub](https://riftbound.leagueoflegends.com/en-us/rules-hub/).
   * Ex: `core-rules-20260330.pdf`
   * Ex: `tournament-rules-20260429.pdf`

Qualquer processamento ou enriquecimento desses dados (ex: embeddings, limpeza de texto) deverá salvar os resultados na pasta `data/processed/`, mantendo os arquivos desta pasta íntegros.
