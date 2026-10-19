#1列目を出力
def print_first_column(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        first_10_lines = lines[:10] #先頭の10行を取得
        for line in first_10_lines:
            first_column = line.split('\t')[0] #タブで分割して1列目を取得
            print(first_column)

file_path = 'popular-names.txt' #ファイルのパスを指定
print_first_column(file_path) #cut -f 1 popular-names.txt|head