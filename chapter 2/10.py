#行数のカウント#
def count_lines(file_path):
    with open(file_path, 'r') as file: #with構文を使用してファイルを開く
        lines = file.readlines() #readlines()を使用してファイルの内容を読み込む
        return len(lines)#行数を返す
    
file_path = 'popular-names.txt' #ファイルのパスを指定
line_count = count_lines(file_path)
print(line_count) #wc popular-names.txt