# Data Extraction Scripts

Esta subpasta contém os scripts responsáveis por raspar e baixar os dados brutos de Riftbound.

## Arquivos

### `fetch_cards.py`
**Para que serve:** É o script principal que se conecta ao site oficial do Riftbound (galeria de cartas) e extrai o banco de dados oficial completo.
**Como funciona:** Ele baixa o HTML inicial da página `https://riftbound.leagueoflegends.com/en-us/card-gallery/`. Como a página é renderizada com Next.js, todo o banco de dados de cartas é injetado estaticamente em uma tag invisível (`<script id="__NEXT_DATA__">`). O script usa Regex e `json` para capturar esse estado e salva todos os conjuntos (Origins, Unleashed, Spiritforged) no arquivo `data/raw/cards.json`.

### `find_urls.py`
**Para que serve:** É um script auxiliar de investigação.
**Como funciona:** Ele foi usado para escanear a estrutura do site oficial em busca das referências às CDNs (ex: `cdn.rgpub.io`) e IDs de cada set de cartas. Pode ser útil no futuro caso a estrutura da Riot mude e precisemos investigar a nova localização dos dados.

### `requirements.txt`
**Para que serve:** Dependências necessárias para rodar os scripts de extração.
**Como usar:**
```bash
pip install -r scripts/01_cards_extraction/requirements.txt
```
