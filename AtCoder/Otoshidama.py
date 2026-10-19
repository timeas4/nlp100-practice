#error 恰好为N，而不是比较，而且用exit（）退出
N,Y = map(int,input().split())
flag = 0
for i in range(N+1):
    for j in range(N+1-i):
        k = N-i-j
        if 10000*i+5000*j+1000*k == Y:
            print(i,j,k)
            exit()
print(-1,-1,-1)
