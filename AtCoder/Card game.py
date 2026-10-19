
N = int(input())
S = list(map(int,input().split()))
S.sort(reverse=True)
A = 0
B = 0
for i in range(N):
    if i%2 == 0:
        A += S[0]
        S.pop(0)
    else:
        B += S[0]
        S.pop(0)
print(A-B)


