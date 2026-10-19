#3列目の数値の降順に各行を並び替える reverse=True
with open('popular-names.txt', 'r') as file:
    lines = file.readlines() #ファイルの内容をリストとして読み込む
    sorted_lines = sorted(lines, key=lambda x: int(x.split('\t')[2]), reverse=True) #intに変換して数値でソート
    for line in sorted_lines:
        print(line.strip()) #sort -k 3 -rn popular-names.txt