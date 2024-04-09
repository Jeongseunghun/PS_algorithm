from collections import deque

def bfs(num):
    q = deque()
    q.append(num)
    visited = [0 for _ in range(n + 1)]
    while q:
        x = q.popleft()
        for i in lst[x]:
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)

    return visited


n = int(input())
m = int(input())
lst = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)


visited = bfs(1)

cnt = 0
for i in range(2,n+1):
    if 0 < visited[i] <= 2:
        cnt+=1

print(cnt)