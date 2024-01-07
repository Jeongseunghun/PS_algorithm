import heapq

n,m = map(int,input().split())
lst = list(map(int,input().split()))

heapq.heapify(lst)

for _ in range(m):
    c1 = heapq.heappop(lst)
    c2 = heapq.heappop(lst)
    
    heapq.heappush(lst,c1+c2)
    heapq.heappush(lst,c1+c2)

print(sum(lst))


