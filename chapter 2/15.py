#ファイルをN分割する
with open('popular-names.txt', 'r') as file:
    lines = file.readlines() #ファイルの内容をリストとして読み込む

n = 10
size = len(lines) // n
for i in range(n):
    start = i * size
    # 最後のファイルは残り全部を含む
    end = (i+1) * size if i < n-1 else len(lines)
    with open(f'part_{i+1}.txt', 'w') as f:
        f.write(''.join(lines[start:end])) #2780行を10分割して278行ずつ保存

# split -l 278 popular-names.txt output_  #splitコマンドを使用してファイルを分割
