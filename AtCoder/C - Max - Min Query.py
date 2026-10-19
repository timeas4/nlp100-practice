from collections import defaultdict
import heapq

Q =int(input())
min_heap = []
max_heap = []
count = defaultdict(int)
for _ in range(Q):
    row = list(map(int,input().split()))
    if row[0] == 1:
        count[row[1]]+=1
        heapq.heappush(min_heap,row[1])
        heapq.heappush(max_heap,-row[1])

    elif row[0] == 2:
        c = min(count[row[1]],row[2])
        count[row[1]]-=c

    elif row[0] == 3 :
        while min_heap and count[min_heap[0]]<= 0:
            heapq.heappop(min_heap)
        while max_heap and count[-max_heap[0]]<= 0:
            heapq.heappop(max_heap)
        print(-max_heap[0]-min_heap[0])


    


