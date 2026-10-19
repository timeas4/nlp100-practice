#セクション構造
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
    match = re.match(r'^(=+)(.+)\1$', line) #セクション名を正規表現で抽出 =+, .+, \1  .+ group(2)
    if match:
        title = match.group(2).strip('= ') #セクション名の前後にある=と空白を削除
        level = len(match.group(1)) #セクションのレベルを取得
        print(f'Level {level}: {title}') #セクションのレベルとセクション名を出力


'''
Level 2: 国名
Level 2: 歴史
Level 2: 地理
Level 3: 主要都市
Level 3: 気候
Level 2: 政治
Level 3: 元首
Level 3: 法
Level 3: 内政
Level 3: 地方行政区分
Level 3: 外交・軍事
Level 2: 経済
Level 3: 鉱業
Level 3: 農業
Level 3: 貿易
Level 3: 不動産
Level 3: エネルギー政策
Level 3: 通貨
Level 3: 企業
Level 4: 通信
Level 2: 交通
Level 3: 道路
Level 3: 鉄道
Level 3: 海運
Level 3: 航空
Level 2: 科学技術
Level 2: 国民
Level 3: 言語
Level 3: 宗教
Level 3: 婚姻
Level 3: 移住
Level 3: 教育
Level 3: 医療
Level 2: 文化
Level 3: 食文化
Level 3: 文学
Level 3: 哲学
Level 3: 音楽
Level 4: ポピュラー音楽
Level 3: 映画
Level 3: コメディ
Level 3: 国花
Level 3: 世界遺産
Level 3: 祝祭日
Level 3: スポーツ
Level 4: サッカー
Level 4: クリケット
Level 4: 競馬
Level 4: モータースポーツ
Level 4: 野球
Level 4: カーリング
Level 4: 自転車競技
Level 2: 脚注
Level 2: 関連項目
Level 2: 外部リンク
'''