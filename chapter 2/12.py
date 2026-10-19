#末尾のN行を出力
def print_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines() #リストとしてファイルの内容を読み込む
        last_n_lines = lines[-n:] #末尾のN行を取得
        for line in last_n_lines:
            print(line.strip())

file_path = 'popular-names.txt' #ファイルのパスを指定
n = 10 #行数を指定
print_last_n_lines(file_path, n) #tail  popular-names.txt

