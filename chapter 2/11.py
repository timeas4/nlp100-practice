#先頭からN行を出力
def print_first_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        for i in range(n):
            print(file.readline().strip()) #strip()を使用して改行を削除

file_path = 'popular-names.txt' #ファイルのパスを指定
n =  10 #行数を指定
print_first_n_lines(file_path, n) #head  popular-names.txt
