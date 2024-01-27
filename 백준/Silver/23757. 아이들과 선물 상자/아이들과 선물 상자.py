import heapq

N, M = map(int,input().split())
C = []
for i in list(map(int,input().split())):
    heapq.heappush(C,-i)
W = list(map(int,input().split()))

flag = True
for i in W:
    x = -heapq.heappop(C)
    if x-i < 0:
        flag = False
        break
    heapq.heappush(C,-(x-i))

if flag:
    print(1)
else:
    print(0)
