#ランダムに各行を並び替える
import random
with open('popular-names.txt', 'r') as file:
    lines = file.readlines() #ファイルの内容をリストとして読み込む
    random.shuffle(lines) #リストの要素をランダムに並び替える
    for line in lines:
        print(line.strip()) #strip()を使用して改行を削除して出力