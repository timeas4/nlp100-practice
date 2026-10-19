#動詞
import spacy

nlp = spacy.load('ja_ginza', exclude=['compound_splitter']) #nlpオブジェクトの生成

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

doc = nlp(text) #テキストを処理して、Docオブジェクトを生成
for token in doc:
    if token.pos_ == 'VERB': #動詞のトークンを抽出
        print(token.text)

'''
激怒
邪智
除か
なら
決意
わから
ある
吹き
遊ん
暮し
来
対し
あっ
'''
