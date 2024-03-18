import heapq

n = int(input())
lst = []

for _ in range(n):
    p,d = map(int,input().split())
    lst.append([p,d])

lst.sort(key = lambda x : x[1])

ans = []
for i in lst:
    heapq.heappush(ans,i[0])
    if len(ans) > i[1]:
        heapq.heappop(ans)

print(sum(ans))