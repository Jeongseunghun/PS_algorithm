#Prim
import heapq

V,E = map(int,input().split())
board = [[] for _ in range(V+1)]

visited = [0 for _ in range(V+1)]
h = [[0,1]]
ans = 0
cnt = 0

for _ in range(E):
    a,b,c = map(int,input().split())
    board[a].append([c,b])
    board[b].append([c,a])

while h:
    if cnt == V:
        break

    c,b = heapq.heappop(h)
    if visited[b] == 0:
        visited[b] = 1
        ans+=c
        cnt+=1
        for i in board[b]:
            heapq.heappush(h,i)
    
print(ans)