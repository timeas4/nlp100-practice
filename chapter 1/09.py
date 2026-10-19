#Typoglycemia
import random
def typoglycemia(s):
    if len(s) <= 4:
        return s
    else:
        middle = list(s[1:-1]) #文字列の先頭と末尾を除いた部分をリストに変換
        random.shuffle(middle)
        return s[0] + ''.join(middle) + s[-1] #joinでリストを文字列に変換
input = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(' '.join([typoglycemia(s) for s in input.split()])) #区切り文字.join(リスト) 1と２の間にスペースを入れてリストの要素を結合する
