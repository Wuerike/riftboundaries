import os
import json
import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path

# Configurações de diretórios
PROJECT_ROOT = Path(__file__).parent.parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

# URL da Galeria de Cartas Oficial
GALLERY_URL = "https://riftbound.leagueoflegends.com/en-us/card-gallery/"

def ensure_directories():
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

def fetch_cards_official():
    target_file = RAW_DATA_DIR / "cards.json"
    print(f"[*] Acessando a Galeria Oficial: {GALLERY_URL}...")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(GALLERY_URL, headers=headers, timeout=10)
        response.raise_for_status()
        
        # O Next.js injeta todo o estado inicial no HTML dentro dessa tag
        match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', response.text)
        if not match:
            print("[ERRO] Não foi possível encontrar os dados injetados na página.")
            return
            
        data = json.loads(match.group(1))
        
        # Navegando pela estrutura do Next.js para achar a lista de cartas
        cards = data['props']['pageProps']['page']['blades'][2]['cards']['items']
        
        print(f"[+] Sucesso! Encontradas {len(cards)} cartas no total.")
        
        # Contagem por set para logs
        sets_count = {}
        for c in cards:
            if 'set' in c and 'value' in c['set']:
                set_id = c['set']['value']['id']
                sets_count[set_id] = sets_count.get(set_id, 0) + 1
        
        for k, v in sets_count.items():
            print(f"    - Set {k}: {v} cartas")
            
        with open(target_file, "w", encoding="utf-8") as f:
            json.dump(cards, f, indent=2, ensure_ascii=False)
            
        print(f"[OK] Todas as cartas salvas com sucesso em: {target_file}")
        
    except Exception as e:
        print(f"[ERRO] Falha ao raspar a galeria oficial: {e}")

def main():
    ensure_directories()
    fetch_cards_official()
    print("\n[+] Extração de dados oficiais finalizada!")

if __name__ == "__main__":
    main()
