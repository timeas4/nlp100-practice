#JSONデータの読み込み
import gzip
import json
with gzip.open('jawiki-country.json.gz', 'rt') as f:   #gzip形式のファイルをテキストモードで開く
    for line in f:   #1行に1記事の情報がJSON形式で格納される
        item = json.loads(line)
        if item['title'] == 'イギリス':
            text = item['text']
            print(text)
            break   #イギリスの記事を見つけたらループを抜ける
