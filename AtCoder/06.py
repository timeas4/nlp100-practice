
def add_vals(a, start):
    # リスト a の各要素に対し、先頭から順に start, start+1, start+2,... を足し込む
    for i in range(len(a)):
        a[i] += i + start

a = [3,1,2]
b = [4,5,6]
c = [3,3,1]
add_vals(a, 0) # start = 0 -> 0,1,2... が足し込まれる
add_vals(b, 0)
add_vals(c, 1) # start = 1 -> 1,2,3... が足し込まれる
