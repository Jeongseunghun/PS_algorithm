from collections import deque
from itertools import combinations

N,M = map(int,input().split())
lab = [list(map(int,input().split())) for _ in range(N)]

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(v):
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    q = deque()
    
    for x,y in v:
        q.append((x,y))
        visited[x][y] = 0
    
    tmp = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1:
                    if lab[nx][ny] == 2:
                        q.append((nx,ny))
                        visited[nx][ny] = visited[x][y] + 1
                    elif lab[nx][ny] == 0:
                        q.append((nx,ny))
                        visited[nx][ny] = visited[x][y] + 1
                        tmp = max(tmp,visited[nx][ny])
    
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0 and visited[i][j] == -1:
                return inf
    
    return tmp

#바이러스 좌표
virus = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i,j))

#활성 바이러스 조합
active_virus = []
for i in combinations(virus,M):
    active_virus.append(i)

#하나씩 탐색
ans = 1e9
inf = 1e9
for i in active_virus:
    tmp = bfs(i)
    ans = min(ans,tmp)


if ans != inf:
    print(ans)
else:
    print(-1)