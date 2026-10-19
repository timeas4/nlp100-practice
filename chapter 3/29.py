#国旗画像のURLを取得する
import gzip
import json
with gzip.open('jawiki-country.json.gz', 'rt') as f:
    for line in f:
        item = json.loads(line)
        if item['title'] == 'イギリス':
            text = item['text']
            break

import re
import requests
#基礎情報テンプレートの抽出
pattern = r'\{\{基礎情報.*?\n(.*?)\n\}\}'
match = re.search(pattern, text, re.DOTALL)
if match:
    template = match.group(1)
    for line in template.split('\n'):
        m = re.search(r'^\|国旗画像\s*=\s*(.+)$', line) #国旗画像の行を正規表現で抽出
        if m:
            filename = m.group(1).strip()
            break

#国旗画像のURLを取得するためのAPIリクエスト
url = 'https://en.wikipedia.org/w/api.php'
params = {
    'action': 'query',
    'titles': f'File:{filename}',
    'prop': 'imageinfo',
    'iiprop': 'url',
    'format': 'json'
}

#agentを指定してAPIリクエストを送信
response = requests.get(url, params=params, headers={'User-Agent': 'NLP100/1.0'})
data = response.json()

pages = data['query']['pages']
for page in pages.values():
    print(page['imageinfo'][0]['url'])

#https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg
