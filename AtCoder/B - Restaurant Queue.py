from collections import deque
Q = int(input())
X1 = deque([])
X2 =[]
for _ in range(Q):
    #用row这种来代替a，b输入
    row  = list(map(int, input().split()))
    if row[0] == 1:
       X1.append(row[1])
    elif row[0] == 2:
        X2.append(X1.popleft())

print(*X2,sep="\n")



