import heapq

N = int(input())
time = []
for i in range(N):
    s,a = map(int,input().split())
    time.append([s,a])
time.sort()
h = []
ans = 1
heapq.heappush(h,time[0][1])
for i in range(1,N):
    if time[i][0] >= h[0]:
        heapq.heappop(h)
    else:
        ans+=1
    heapq.heappush(h,time[i][1])

print(ans)