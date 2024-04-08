import heapq

N,M = map(int,input().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    lst[a].append((b,c))
    lst[b].append((a,c))
    
dis = [1e9] * (N+1)

q = []
heapq.heappush(q,(0,1))
dis[1] = 0
while q:
    d, n = heapq.heappop(q)
    if dis[n] < d:
        continue
    for v,w in lst[n]:
        cost = d + w
        if cost < dis[v]:
            dis[v] = cost
            heapq.heappush(q,(cost,v))

print(dis[N])