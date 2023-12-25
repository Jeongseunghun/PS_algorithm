import heapq

N = int(input())
h = []
vote = 0
for i in range(N):
    a = int(input())
    if i == 0:
        vote = a
        continue
    heapq.heappush(h,-a)

cnt = 0
while h:
    v= -heapq.heappop(h)
    if v < vote:
        break
    
    vote += 1
    cnt +=1
    heapq.heappush(h,-(v-1))

print(cnt)