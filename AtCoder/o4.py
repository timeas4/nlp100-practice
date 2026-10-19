N, K = map(int, input().split())
S = input().split()
result = [word for word in S if len(word) >= K]
print(*result)

