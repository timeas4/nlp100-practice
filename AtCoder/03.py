N, S = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# リンゴ・パイナップルをそれぞれ1つずつ購入するとき合計S円になるような買い方が何通りあるか
# ここにプログラムを追記
cou = 0
for i in range(N):
  for j in range(N):
    if A[i]+B[j] == S:
      cou+=1
print(cou)