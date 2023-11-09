import heapq,sys
input = sys.stdin.readline

N = int(input())
lst = []
cnt = 1
for i in range(N):
    s,t = map(int,input().split())
    lst.append([s,t])

lst.sort()

h = []
heapq.heappush(h,lst[0][1])

for i in range(1,N):
    if lst[i][0] < h[0]:
        heapq.heappush(h,lst[i][1])
    else:
        heapq.heappop(h)
        heapq.heappush(h,lst[i][1])

print(len(h))
        