#元素記号
s="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
list = s.split()  #文字列をスペースで分割してリストにする
element_symbols = {} #キーと値のペア   []　リスト
for i, word in enumerate(list):#enumerate  dictonary
    if i in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
        element_symbols[i] = word[0]
    else:
        element_symbols[i] = word[:2]

print(element_symbols)