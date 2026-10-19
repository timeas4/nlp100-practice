#名詞の出現頻度
import gzip
import json
import re
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

noun_freq = Counter()

with gzip.open('jawiki-country.json.gz', 'rt') as f:
    for line in f:
        item = json.loads(line)
        clean_text = remove_markup(item['text'])
        for m in tokenizer.tokenize(clean_text, SplitMode.C):
            if m.part_of_speech()[0] == '名詞' and m.surface().strip():
                noun_freq[m.surface()] += 1

print('名詞\t出現頻度')
for word, freq in noun_freq.most_common(20):
    print(f'{word}\t{freq}')

'''
年      5657
月      2433
1       1935
thumb   1459
%       1345
GDP     1280
日      1226
px      1220
2       1127
政府    1085
人口    1048
日本    1009
こと    988
語      950
3       937
大統領  829
right   801
4       768
en      763
首相    754
'''
