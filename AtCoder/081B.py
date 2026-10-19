N = int(input())
S = list(map(int,input().split()))
flag = 0
for i in range(10**5):
   for j in range(N):
     if S[j]%2 == 0:
          S[j] //=2
     else:
          flag =1
   if flag == 1:
       break

print(i)
    


