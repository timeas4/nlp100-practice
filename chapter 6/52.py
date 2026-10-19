#類似度の高い単語10件
from gensim.models import KeyedVectors

# 学習済みword2vecモデルを読み込む（.binファイルなのでbinary=True）
model = KeyedVectors.load_word2vec_format(
    'GoogleNews-vectors-negative300.bin',
    binary=True
)

# "United States" とコサイン類似度が高い上位10語を取得する
# （topn=10 で上位10件、内部表記は "United_States" に注意）
results = model.most_similar('United_States', topn=10)

# 単語とその類似度を1行ずつ出力する
for word, similarity in results:
    print(word, similarity)

'''
Unites_States 0.7877249121665955
Untied_States 0.7541370391845703
United_Sates 0.7400725483894348
U.S. 0.7310773730278015
theUnited_States 0.6404393911361694
America 0.6178410649299622
UnitedStates 0.6167311668395996
Europe 0.6132988333702087
countries 0.6044804453849792
Canada 0.6019070148468018
'''