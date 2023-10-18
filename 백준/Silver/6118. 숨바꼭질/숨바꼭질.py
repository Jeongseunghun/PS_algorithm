from collections import deque

N,M = map(int,input().split())

lst = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)
visited = [0 for _ in range(N+1)]
def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1
    while q:
        x = q.popleft()
        for i in lst[x]:
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)
bfs()
print(visited.index(max(visited)),max(visited)-1,visited.count(max(visited)))
        