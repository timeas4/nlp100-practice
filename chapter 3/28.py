# MediaWikiマークアップの除去
import gzip
import json
with gzip.open('jawiki-country.json.gz', 'rt') as f:
    for line in f:
        item = json.loads(line)
        if item['title'] == 'イギリス':
            text = item['text']
            break

import re
#基礎情報テンプレートの抽出
pattern = r'\{\{基礎情報.*?\n(.*?)\n\}\}'
match = re.search(pattern, text, re.DOTALL)

def remove_markup(value):
    # 強調マークアップ '''''' を除去
    value = re.sub(r'\'{2,5}', '', value)
    # 内部リンク [[記事名|表示文字]] → 表示文字
    value = re.sub(r'\[\[(?:[^|]*?\|)?(.+?)\]\]', r'\1', value)
    # 外部リンク [URL 表示文字] → 表示文字
    value = re.sub(r'\[https?://[^\s]*?\s(.+?)\]', r'\1', value)
    # 外部リンク [URL] → 空
    value = re.sub(r'\[https?://[^\]]+\]', '', value)
    # {{lang|en|text}} → text
    value = re.sub(r'\{\{lang\|[^|]+\|(.+?)\}\}', r'\1', value)
    # {{仮リンク|表示|...}} → 表示
    value = re.sub(r'\{\{仮リンク\|(.+?)\|.+?\}\}', r'\1', value)
    # 一般的な {{...}} を除去
    value = re.sub(r'\{\{.*?\}\}', '', value)
    # <br /> 等HTMLタグ
    value = re.sub(r'<.*?>', '', value)
    # <ref>...</ref>
    value = re.sub(r'<ref.*?/>', '', value)
    value = re.sub(r'<ref.*?>.*?</ref>', '', value)
    # 余分な空白を整理
    value = value.strip()
    return value

field_dict = {}
if match:
            template = match.group(1)
            for line in template.split('\n'):
                m = re.match(r'^\|(.+?)\s*=\s*(.+)$', line)
                if m:
                    value = remove_markup(m.group(2))
                    field_dict[m.group(1)] = value

for key, value in field_dict.items():
    print(f'{key}: {value}')

'''
略名: イギリス
日本語国名: グレートブリテン及び北アイルランド連合王国
公式国名: United Kingdom of Great Britain and Northern Ireland英語以外での正式国名:
国旗画像: Flag of the United Kingdom.svg
国章画像: 85px|イギリスの国章
国章リンク: （国章）
標語: {{lang|fr|神と我が権利）
国歌: God Save the Queen神よ女王を護り賜え
地図画像: Europe-UK.svg
位置画像: United Kingdom (+overseas territories) in the World (+Antarctica claims).svg
公用語: 英語
首都: ロンドン（事実上）
最大都市: ロンドン
元首等肩書: 女王
元首等氏名: エリザベス2世
首相等肩書: 首相
首相等氏名: ボリス・ジョンソン
他元首等肩書1: 貴族院議長
他元首等氏名1: ノーマン・ファウラー
他元首等肩書2: 庶民院議長
他元首等氏名2: リンゼイ・ホイル
他元首等肩書3: 最高裁判所長官
他元首等氏名3: ブレンダ・ヘイル
面積順位: 76
面積大きさ: 1 E11
面積値: 244,820
水面積率: 1.3%
人口統計年: 2018
人口順位: 22
人口大きさ: 1 E7
人口値: 6643万5600
人口密度値: 271
GDP統計年元: 2012
GDP値元: 1兆5478億and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom
GDP統計年MER: 2012
GDP順位MER: 6
GDP値MER: 2兆4337億
GDP統計年: 2012
GDP順位: 6
GDP値: 2兆3162億
GDP/人: 36,727
建国形態: 建国
確立形態1: 1707年合同法まで）
確立年月日1: 927年／843年
確立形態2: グレートブリテン王国成立（1707年合同法）
確立年月日2: 1707年5月1日
確立形態3: 1800年合同法）
確立年月日3: 1801年1月1日
確立形態4: 現在の国号「グレートブリテン及び北アイルランド連合王国」に変更
確立年月日4: 1927年4月12日
通貨: UKポンド (£)
通貨コード: GBP
時間帯: ±0
夏時間: +1
ISO 3166-1: GB / GBR
ccTLD: .uk / .gb使用は.ukに比べ圧倒的少数。
国際電話番号: 44
注記: 
'''