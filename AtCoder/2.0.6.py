"""
九九の要領で N × N マスを埋めるプログラム
計算量：O(N^2)
"""

N = int(input())
table = [[0 for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        table[i][j] = (i + 1) * (j + 1)  # N × N 回実行される

for row in table:
    print(*row)

"""
N が 2 で何回割り切れるかを数えるプログラム
計算量：O(log N)
"""

N = int(input())
cnt = 0
while N % 2 == 0:
    cnt += 1
    N //= 2

print(cnt)

