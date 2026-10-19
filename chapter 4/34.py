#主述の関係
import spacy

nlp = spacy.load('ja_ginza', exclude=['compound_splitter'])

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

doc = nlp(text)
for token in doc:
    if token.text == 'メロス' and token.dep_ == 'nsubj': #「メロス」のトークンを抽出
        print(token.head.text) #「メロス」の親のトークンを表示1的

'''
激怒
牧人
'''