#Ward法によるクラスタリング
from gensim.models import KeyedVectors
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import numpy as np

model = KeyedVectors.load_word2vec_format(
    'GoogleNews-vectors-negative300.bin', binary=True
)

# --- 国名を収集（57と同じ）---
countries = set()
with open('questions-words.txt', 'r', encoding='utf-8') as f:
    section = ''
    for line in f:
        line = line.strip()
        if line.startswith(':'):
            section = line[2:]
            continue
        if section in ('capital-common-countries', 'capital-world'):
            words = line.split()
            countries.add(words[1])
            countries.add(words[3])
countries = [c for c in countries if c in model]
country_vecs = np.array([model[c] for c in countries])

# --- Ward法による階層型クラスタリング ---
# method='ward' でWard法を指定する
linkage_result = linkage(country_vecs, method='ward')

# --- デンドログラムとして可視化 ---
plt.figure(figsize=(16, 8))
dendrogram(linkage_result, labels=countries)
plt.title('Ward法による国名の階層型クラスタリング')
plt.tight_layout()
plt.savefig('58_dendrogram.png')   # 画像として保存
plt.show()

'''
58_dendrogram.png
'''