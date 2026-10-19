#Zipfの法則
import gzip
import json
import re
from collections import Counter
from sudachipy import Dictionary, SplitMode
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = ['Hiragino Sans', 'AppleGothic', 'sans-serif']

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

# 出現頻度順にソートしてZipfの法則をプロット
sorted_freqs = sorted(word_freq.values(), reverse=True)
ranks = range(1, len(sorted_freqs) + 1)

plt.figure(figsize=(8, 6))
plt.loglog(ranks, sorted_freqs, marker='.', markersize=2, linestyle='none', alpha=0.5)
plt.xlabel('頻度順位 (rank)')
plt.ylabel('出現頻度 (frequency)')
plt.title('Zipfの法則：単語頻度と順位の両対数グラフ')
plt.grid(True, which='both', alpha=0.3)
plt.tight_layout()
plt.savefig('zipf.png', dpi=150)
plt.show()
print('zipf.png に保存しました')
