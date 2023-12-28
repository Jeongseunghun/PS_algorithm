import heapq

n = int(input())
h = []

for _ in range(n):
    lst = list(map(int,input().split()))
    if lst[0] == 0:
        if h:
            print(-heapq.heappop(h))
        else:
            print(-1)
    else:
        for i in range(lst[0]):
            heapq.heappush(h,-lst[i+1])
        