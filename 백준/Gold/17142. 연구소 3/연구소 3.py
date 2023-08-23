from collections import deque
from itertools import combinations

N,M = map(int,input().split())
lab = [list(map(int,input().split())) for _ in range(N)]
inf = 999999

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(v):
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    tmp = 0
    q = deque()
    for x,y in v:
        q.append((x,y))
        #활성 바이러스는 방문 체크
        visited[x][y] = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                #방문하지 않았고 빈칸이면
                if lab[nx][ny] == 0 and visited[nx][ny] == -1:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
                    tmp = max(tmp,visited[nx][ny])
                #바이러스이고 빈칸이면
                elif lab[nx][ny] == 2 and visited[nx][ny] == -1:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0 and visited[i][j] == -1:
                return inf
    return tmp
#바이러스 위치 저장
virus = []

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i,j))

#활성 바이러스 조합 생성
v_combi = []
for i in combinations(virus,M):
    v_combi.append(i)

ans = inf
#조합 하나씩 실행
for i in v_combi:
    tmp = bfs(i)
    ans = min(tmp,ans)

if ans != inf:
    print(ans)
else:
    print(-1)