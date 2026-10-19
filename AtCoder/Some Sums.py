N,A,B = map(int,input().split())
S = 0
for i in range(1,N+1):
    sum = 0
    j = i
    while(i>0):
        sum +=i%10
        i//=10
    if sum <= B and sum >= A:
        S  += j
print(S)


