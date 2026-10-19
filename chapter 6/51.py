#単語の類似度
from gensim.models import KeyedVectors

# 学習済みword2vecモデルを読み込む（.binファイルなのでbinary=True）
model = KeyedVectors.load_word2vec_format(
    'GoogleNews-vectors-negative300.bin',
    binary=True
)

# "United States" と "U.S." のコサイン類似度を計算する
# （"United States" は内部的に "United_States"、"U.S." は "U.S." と表記される点に注意）
similarity = model.similarity('United_States', 'U.S.')

print(similarity)

'''
0.73107743
'''