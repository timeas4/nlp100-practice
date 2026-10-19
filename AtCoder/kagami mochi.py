
N = int(input())
S = [0]*N
for i in range(N):
    S[i] = int(input())
S.sort()
d_min = S[0]
c = 1
for j in range(1,N):
    if S[j] > d_min:
        c += 1
        d_min = S[j]
print(c)





