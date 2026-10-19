from collections import defaultdict

d1 = defaultdict(int)
N = 10
for i in range(N):
    d1[i] = i

d2 = defaultdict(int)
for i in range(N):  # range(N-1) を意図していたが誤って range(N) とした
    d2[i] = d1[i+1]  # d1[N] にアクセスしているがエラーにならない
