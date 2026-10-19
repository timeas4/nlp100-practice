#カテゴリ名の抽出
import gzip
import json
with gzip.open('jawiki-country.json.gz', 'rt') as f:
    for line in f:
        item = json.loads(line)
        if item['title'] == 'イギリス':
            text = item['text']
            break

import re
for line in text.split('\n'):
    match = re.match(r'^\[\[Category:(.+)\]\]$', line) #カテゴリ名を正規表現で抽出 .+ group(1)でカテゴリ名を取得
    if match:
        print(match.group(1)) #カテゴリ名を出力

'''
イギリス|*
イギリス連邦加盟国
英連邦王国|*
G8加盟国
欧州連合加盟国|元
海洋国家
現存する君主国
島国
1801年に成立した国家・領域
'''