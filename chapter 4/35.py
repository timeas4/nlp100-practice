#係り受け木
import spacy
from spacy import displacy

nlp = spacy.load('ja_ginza', exclude=['compound_splitter'])

doc = nlp('メロスは激怒した。')

# SVGファイルに保存
svg = displacy.render(doc, style='dep', jupyter=False)
output_path = 'dep_tree.svg'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(svg)
print(f'係り受け木を {output_path} に保存しました')

# テキストでも表示
print()
def print_tree(token, depth=0):
    indent = '  ' * depth
    label = f'--[{token.dep_}]--> {token.head.text}' if token.dep_ != 'ROOT' else '(ROOT)'
    print(f'{indent}{token.text} {label}')
    for child in sorted(token.children, key=lambda t: t.i):
        print_tree(child, depth + 1)

root = next(t for t in doc if t.dep_ == 'ROOT')
print_tree(root)

'''
係り受け木を dep_tree.svg に保存しました

激怒 (ROOT)
  メロス --[nsubj]--> 激怒
    は --[case]--> メロス
  し --[aux]--> 激怒
  た --[aux]--> 激怒
  。 --[punct]--> 激怒
'''
