#k-meansクラスタリング
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans
import numpy as np

# 学習済みモデルを読み込む
model = KeyedVectors.load_word2vec_format(
    'GoogleNews-vectors-negative300.bin', binary=True
)

# --- 国名を収集する（questions-words.txt の国-首都セクションから抽出）---
countries = set()
with open('questions-words.txt', 'r', encoding='utf-8') as f:
    section = ''
    for line in f:
        line = line.strip()
        if line.startswith(':'):
            section = line[2:]
            continue
        # 国-首都に関するセクションから国名（2列目・4列目）を取得
        if section in ('capital-common-countries', 'capital-world'):
            words = line.split()
            countries.add(words[1])
            countries.add(words[3])

# 語彙に存在する国名だけを残す
countries = [c for c in countries if c in model]

# 各国名のベクトルを行列にまとめる
country_vecs = np.array([model[c] for c in countries])

# --- k-means（k=5）---
kmeans = KMeans(n_clusters=5, random_state=0, n_init=10)
labels = kmeans.fit_predict(country_vecs)

# クラスタごとに国名を表示する
for cluster_id in range(5):
    members = [countries[i] for i in range(len(countries)) if labels[i] == cluster_id]
    print(f'クラスタ {cluster_id}: {members}')

'''
クラスタ 0: ['China', 'Nepal', 'Bahrain', 'Honduras', 'Nicaragua', 'Chile', 'Guyana', 'Peru', 'Suriname', 'Pakistan', 'Vietnam', 'Fiji', 'Samoa', 'Laos', 'Belize', 'Bhutan', 'Indonesia', 'Ecuador', 'Thailand', 'Bangladesh', 'Bahamas', 'Oman', 'Taiwan', 'Tuvalu', 'Dominica', 'Qatar', 'Jamaica', 'Philippines', 'Cuba', 'Venezuela']
クラスタ 1: ['Liberia', 'Niger', 'Angola', 'Senegal', 'Mauritania', 'Kenya', 'Burundi', 'Mozambique', 'Malawi', 'Botswana', 'Gabon', 'Tunisia', 'Uganda', 'Rwanda', 'Zambia', 'Morocco', 'Gambia', 'Zimbabwe', 'Algeria', 'Nigeria', 'Madagascar', 'Guinea', 'Namibia', 'Mali', 'Ghana']
クラスタ 2: ['Belarus', 'Lithuania', 'Kazakhstan', 'Greece', 'Malta', 'Montenegro', 'Moldova', 'Turkmenistan', 'Turkey', 'Azerbaijan', 'Russia', 'Estonia', 'Croatia', 'Serbia', 'Tajikistan', 'Albania', 'Slovakia', 'Romania', 'Armenia', 'Poland', 'Latvia', 'Cyprus', 'Ukraine', 'Macedonia', 'Bulgaria', 'Hungary', 'Uzbekistan', 'Kyrgyzstan', 'Georgia', 'Slovenia']
クラスタ 3: ['Egypt', 'Syria', 'Iran', 'Somalia', 'Sudan', 'Afghanistan', 'Jordan', 'Lebanon', 'Libya', 'Eritrea', 'Iraq']
クラスタ 4: ['Spain', 'Germany', 'Switzerland', 'Denmark', 'Liechtenstein', 'Austria', 'Greenland', 'Italy', 'Finland', 'Japan', 'Sweden', 'Australia', 'England', 'Ireland', 'France', 'Norway', 'Uruguay', 'Canada', 'Portugal', 'Belgium']
'''