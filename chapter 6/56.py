#WordSimilarity-353での評価#
from gensim.models import KeyedVectors
from scipy.stats import spearmanr

# 学習済みword2vecモデルを読み込む（.binなのでbinary=True）
model = KeyedVectors.load_word2vec_format(
    'GoogleNews-vectors-negative300.bin',
    binary=True
)

human_scores = []   # 人間が付けた類似度
model_scores = []   # 単語ベクトルで計算したコサイン類似度

with open('combined.csv', 'r', encoding='utf-8') as f:
    next(f)  # 1行目のヘッダーを読み飛ばす

    for line in f:
        # カンマ区切りで「単語1, 単語2, 人間スコア」に分割
        word1, word2, human = line.strip().split(',')

        # 人間の類似度（文字列→float）
        human_scores.append(float(human))

        # 単語ベクトルによるコサイン類似度
        model_scores.append(model.similarity(word1, word2))

# 2つのランキング間のスピアマン相関係数を計算する
correlation, p_value = spearmanr(human_scores, model_scores)

print(f'スピアマン相関係数: {correlation:.4f}')

'''
スピアマン相関係数: 0.7000
'''