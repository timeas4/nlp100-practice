#t-SNEによる可視化
from gensim.models import KeyedVectors
from sklearn.manifold import TSNE
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

# --- t-SNEで300次元を2次元に圧縮する ---
# perplexityはサンプル数より小さくする必要がある
tsne = TSNE(n_components=2, random_state=0, perplexity=30, init='pca')
embedded = tsne.fit_transform(country_vecs)

# --- 2次元散布図として可視化 ---
plt.figure(figsize=(14, 14))
plt.scatter(embedded[:, 0], embedded[:, 1])

# 各点に国名を表示する
for i, country in enumerate(countries):
    plt.annotate(country, (embedded[i, 0], embedded[i, 1]))

plt.title('t-SNE visualization of country word vectors')
plt.tight_layout()
plt.savefig('59_tsne.png')
plt.show()

'''
59_tsne.png
'''