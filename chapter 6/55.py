#アナロジータスクでの正解率
# 54で作った結果ファイルを読み込み、
# 意味的アナロジー(semantic)と文法的アナロジー(syntactic)の正解率を計算する
# セクション名が "gram" で始まるものを文法的、それ以外を意味的とする

sem_correct = 0   # 意味的：正解数
sem_total = 0     # 意味的：総数
syn_correct = 0   # 文法的：正解数
syn_total = 0     # 文法的：総数

with open('questions-words-result.txt', 'r', encoding='utf-8') as f:
    for line in f:
        cols = line.split()
        # cols = [セクション, 1列目, 2列目, 3列目, 正解(4列目), 予測語, 類似度]
        section = cols[0]
        correct_answer = cols[4]   # 正解（元データの4列目）
        predicted = cols[5]        # モデルの予測語

        if section.startswith('gram'):
            # 文法的アナロジー
            syn_total += 1
            if predicted == correct_answer:
                syn_correct += 1
        else:
            # 意味的アナロジー
            sem_total += 1
            if predicted == correct_answer:
                sem_correct += 1

# 正解率を出力する
print(f'意味的アナロジー正解率: {sem_correct / sem_total:.4f}')
print(f'文法的アナロジー正解率: {syn_correct / syn_total:.4f}')

'''
意味的アナロジー正解率: 0.7309
文法的アナロジー正解率: 0.7400
'''