#「AのB」
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
    if token.pos_ == 'NOUN': #名詞のトークンを抽出
        for child in token.children:
            if child.text == 'の' and child.dep_ == 'case': #「の」のトークンを抽出
                if token.head.pos_ == 'NOUN': #「の」の親のトークンが名詞であるかを確認
                    print(f'{token.text}の{token.head.text}')

'''
暴虐の王
村の牧人
'''
