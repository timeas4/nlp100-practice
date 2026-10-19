#各行の1列目の文字列の出現頻度を求め、出現頻度の高い順に並べる
with open('popular-names.txt', 'r') as file:
    names_count = {} #名前の頻度を格納するための辞書
    for line in file:
        name = line.split('\t')[0]  #行をタブで分割し、1列目の名前を取得
        if name in names_count:
            names_count[name]+=1 #名前がすでに辞書に存在する場合はカウントを増やす
        else:
            names_count[name] = 1 #名前が辞書に存在しない場合は新たに追加してカウントを1にする

sorted_names = sorted(names_count.items(), key=lambda x: x[1],reverse=True) #tupleを頻度でソート 
for name,count in sorted_names:
    print(f'{name}: {count}') #cut -f 1 popular-names.txt | sort | uniq -c | sort -rn