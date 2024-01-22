import heapq

N = int(input())

cnt = 0
h = []
room = []

for _ in range(N):
    num,s,e = map(int,input().split())
    heapq.heappush(h,[s,e,num])
    
s,e,num = heapq.heappop(h)
heapq.heappush(room,e)
while h:
    s,e,num = heapq.heappop(h)
    if room[0] <= s:
        heapq.heappop(room)
    heapq.heappush(room,e)
    
print(len(room))