#加法構成性によるアナロジー
from gensim.models import KeyedVectors

# 学習済みword2vecモデルを読み込む（.binファイルなのでbinary=True）
model = KeyedVectors.load_word2vec_format(
    'GoogleNews-vectors-negative300.bin',
    binary=True
)

# vec("Spain") - vec("Madrid") + vec("Athens") を計算し、
# そのベクトルとコサイン類似度が高い上位10語を求める
# positive=足すベクトル, negative=引くベクトル
results = model.most_similar(
    positive=['Spain', 'Athens'],
    negative=['Madrid'],
    topn=10
)

# 単語とその類似度を1行ずつ出力する
for word, similarity in results:
    print(word, similarity)

'''
Greece 0.6898480653762817
Aristeidis_Grigoriadis 0.560684859752655
Ioannis_Drymonakos 0.5552908778190613
Greeks 0.5450686812400818
Ioannis_Christou 0.5400862097740173
Hrysopiyi_Devetzi 0.5248444080352783
Heraklio 0.5207759141921997
Athens_Greece 0.5168809294700623
Lithuania 0.5166866183280945
Iraklion 0.5146791934967041
'''