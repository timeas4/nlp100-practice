#タブをスペースに置換
def replace_tabs_with_spaces(file_path):
    with open(file_path, 'r') as file:
        lines= file.readlines()
        first_10_lines = lines[:10] #先頭の10行を取得
        for line in first_10_lines:
            replaced_line = line.replace('\t', ' ') #タブをスペースに置換
            print(replaced_line.strip())

file_path = 'popular-names.txt' #ファイルのパスを指定
replace_tabs_with_spaces(file_path) #expand -t 1 popular-names.txt|head


