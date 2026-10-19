#１列目の文字列の異なり
with open('popular-names.txt', 'r') as file:
    unique_names = set() #異なる名前を格納するためのセットを作成(集合 独一)
    for line in file:
        name = line.split('\t')[0] #行をタブで分割し、1列目の名前を取得（x、y）
        unique_names.add(name) #セットに名前を追加（重複は自動的に排除される）
    
    print(len(unique_names)) #cut -f 1 popular-names.txt | sort | uniq | wc -l