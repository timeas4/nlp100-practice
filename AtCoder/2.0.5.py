N = int(input())

# p[i] : 組織 i の親組織 
#-1 :占位符，也是根结点
p = [-1] + list(map(int, input().split()))

# 2 次元配列 children
# children[i] : 組織 i の子組織の一覧 であるような 2 次元配列
children = [[] for _ in range(N)]
#子节点开始，将子节点i插入对应父节点p[i]
for i in range(1, N):
    children[p[i]].append(i)

# 再帰関数 complete_time
# 入力 : 組織番号 x
# 出力 : 組織 x に子組織からの報告書が揃った時刻（報告書を親組織へ送った時刻）
def complete_time(x):
    # ここに実装する
    if  len(children[x]) == 0:
        return 0
    time = []
    for y in children[x]:
        time.append(complete_time(y)+1)
    return max(time)


    
    ...


# 組織 0 の元に報告書が揃う時刻を出力
print(complete_time(0))


'''
6
0 0 1 1 4

8
7 4 0 3 2 4 2
'''