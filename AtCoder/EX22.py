N = int(input())
#套娃
L = [ tuple(map(int,input().split())) for i in range(N) ]
L1=sorted(L,key= lambda x:x[1])
for i in range(N):
    print(*L1[i])
for a,b in L1:
    print(a,b)