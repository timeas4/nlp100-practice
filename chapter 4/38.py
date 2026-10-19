#TF・IDF
import gzip
import json
import re
import math
from collections import Counter
from sudachipy import Dictionary, SplitMode

tokenizer = Dictionary().create()

def remove_markup(text):
    text = re.sub(r"\'{2,5}", '', text)
    text = re.sub(r'\[\[(?:[^|]*?\|)?(.+?)\]\]', r'\1', text)
    text = re.sub(r'\[https?://[^\s]*?\s(.+?)\]', r'\1', text)
    text = re.sub(r'\[https?://[^\]]+\]', '', text)
    text = re.sub(r'\{\{lang\|[^|]+\|(.+?)\}\}', r'\1', text)
    text = re.sub(r'\{\{仮リンク\|(.+?)\|.+?\}\}', r'\1', text)
    text = re.sub(r'\{\{.*?\}\}', '', text, flags=re.DOTALL)
    text = re.sub(r'<ref.*?/>', '', text, flags=re.DOTALL)
    text = re.sub(r'<ref.*?>.*?</ref>', '', text, flags=re.DOTALL)
    text = re.sub(r'<.*?>', '', text)
    return text.strip()

# 全記事の名詞を収集しIDFを計算
N = 0
df = Counter()           # 各名詞が出現する記事数
japan_nouns = Counter()  # 日本記事内の名詞頻度

with gzip.open('jawiki-country.json.gz', 'rt') as f:
    for line in f:
        item = json.loads(line)
        N += 1
        clean_text = remove_markup(item['text'])
        nouns_in_article = set()
        for m in tokenizer.tokenize(clean_text, SplitMode.C):
            if m.part_of_speech()[0] == '名詞' and m.surface().strip():
                surface = m.surface()
                if item['title'] == '日本':
                    japan_nouns[surface] += 1
                nouns_in_article.add(surface)
        for noun in nouns_in_article:
            df[noun] += 1

total_japan_nouns = sum(japan_nouns.values())

results = []
for noun, count in japan_nouns.items():
    tf = count / total_japan_nouns
    idf = math.log(N / df[noun])
    tfidf = tf * idf
    results.append((noun, tf, idf, tfidf))

results.sort(key=lambda x: x[3], reverse=True)

print(f'{"名詞":<15}{"TF":>12}{"IDF":>12}{"TF-IDF":>12}')
for noun, tf, idf, tfidf in results[:20]:
    print(f'{noun:<15}{tf:>12.6f}{idf:>12.6f}{tfidf:>12.6f}')

'''
韓国                 0.005768    2.468906    0.014242
Wikipedia          0.002472    5.513429    0.013630
宇宙                 0.003296    3.567519    0.011759
生活保護               0.002060    5.513429    0.011359
朝鮮籍                0.002060    5.513429    0.011359
籍                  0.002884    3.903991    0.011260
A                  0.005356    1.875843    0.010048
81                 0.002884    3.210844    0.009261
信頼                 0.002472    3.721669    0.009201
朝鮮語                0.001648    5.513429    0.009087
km2                0.003708    2.422386    0.008983
戦後                 0.003296    2.422386    0.007985
明治                 0.001648    4.820282    0.007944
朝鮮人                0.001648    4.820282    0.007944
中国                 0.005356    1.470377    0.007876
%                  0.032963    0.235314    0.007757
方言                 0.003296    2.217592    0.007310
高齢                 0.001648    4.414816    0.007276
日本国籍               0.001648    4.414816    0.007276
くに                 0.001236    5.513429    0.006815
'''
