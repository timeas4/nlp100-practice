#円周率
s="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list = []   #リスト
for i in s.split():
    list.append(len(i.strip(",."))) #単語の前後にあるカンマとピリオドを削除してから、単語の長さをリストに追加する
print(list)