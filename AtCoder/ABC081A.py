S =int(input())
c = 0
while(S > 0):
    if S%10 == 1:
        c+=1
    S//=10
print(c)

