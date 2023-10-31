import heapq
N = int(input())
q = []

for _ in range(N):
    lst = list(map(int,input().split()))
    if not q:
        for i in lst:
            heapq.heappush(q,i)
    else:
        for i in lst:
            if q[0] < i:
                heapq.heappush(q,i)
                heapq.heappop(q)

print(q[0])