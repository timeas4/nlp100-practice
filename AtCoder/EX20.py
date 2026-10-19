from collections import defaultdict
N = int(input())
L = list(map(int, input().split()))
counter = defaultdict(int)
for k in L:
    counter[k]+=1
best = max(counter,key=counter.get)
print(best,counter[best])