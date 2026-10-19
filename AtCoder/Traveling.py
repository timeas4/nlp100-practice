N = int(input())
Deer = []
zero =(0,0,0)
Deer.append(zero)
for i in range(N):
    S = tuple(map(int,input().split()))
    Deer.append(S)
#for-else语句，完美解决循环完成后判断
for i in range(1,len(Deer)):
    x = abs(Deer[i][1]-Deer[i-1][1])
    y = abs(Deer[i][2]-Deer[i-1][2])
    t = abs(Deer[i][0] - Deer[i-1][0])
    if  not(t >= x+y and t%2 ==(x+y)%2):
        print("No")
        break
else:
    print("Yes")