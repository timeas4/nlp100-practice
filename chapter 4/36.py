#単語の出現頻度
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

word_freq = Counter()

with gzip.open('jawiki-country.json.gz', 'rt') as f:
    for line in f:
        item = json.loads(line)
        clean_text = remove_markup(item['text'])
        for m in tokenizer.tokenize(clean_text, SplitMode.C):
            surface = m.surface()
            if surface.strip():
                word_freq[surface] += 1

print('単語\t出現頻度')
for word, freq in word_freq.most_common(20):
    print(f'{word}\t{freq}')

'''
|       33281
=       31555
の      21113
、      18202
に      12675
。      12377
は      11743
が      9362
[       8219
て      7616
で      7545
を      7513
と      7110
*       7066
た      6870
-       6609
・      6476
し      5823
年      5657
）      4854
'''