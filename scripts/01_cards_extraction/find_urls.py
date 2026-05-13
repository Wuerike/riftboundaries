import requests
import json
import re

url = 'https://riftbound.leagueoflegends.com/en-us/card-gallery/'
headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get(url, headers=headers)
r.raise_for_status()

match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', r.text)
data = json.loads(match.group(1))

cards = data['props']['pageProps']['page']['blades'][2]['cards']['items']
print(f"Total cards found in page config: {len(cards)}")

unl_cards = [c for c in cards if 'set' in c and c['set']['value']['id'] == 'UNL']
print(f"UNL cards found: {len(unl_cards)}")
if unl_cards:
    print(json.dumps(unl_cards[0], indent=2))
    
ogs_cards = [c for c in cards if 'set' in c and c['set']['value']['id'] == 'OGS']
print(f"OGS cards found: {len(ogs_cards)}")

