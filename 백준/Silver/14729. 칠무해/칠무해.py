import heapq

N = int(input())

lst = []
for i in range(N):
    heapq.heappush(lst,float(input()))


for _ in range(7):
    print('{:.3f}'.format(heapq.heappop(lst)))