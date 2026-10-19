#カテゴリ名を含む行を抽出
import gzip
import json
with gzip.open('jawiki-country.json.gz', 'rt') as f:
    for line in f:
        item = json.loads(line)
        if item['title'] == 'イギリス':
            text = item['text']
            break

import re
for line in text.split('\n'): #記事textの内容を行ごとに分割して処理
    if re.match(r'^\[\[Category:.+\]\]$', line): #カテゴリ名を含む行を正規表現で抽出
        print(line)

'''
[[Category:イギリス連邦加盟国]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
[[Category:欧州連合加盟国|元]]
[[Category:海洋国家]]
[[Category:現存する君主国]]
[[Category:島国]]
[[Category:1801年に成立した国家・領域]]
'''
