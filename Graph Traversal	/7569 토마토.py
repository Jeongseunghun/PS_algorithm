from collections import deque

M,N,H = map(int,input().split())
tomato = [[list(map(int,input().split())) for _ in range(N)] for i in range(H)]

#상하좌우위아래
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,1,-1]

q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                q.append((i,j,k))


def bfs():
    while q:
        z,x,y = q.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0<=nx<N and 0<=ny<M and 0<=nz<H and tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = tomato[z][x][y] + 1
                q.append((nz,nx,ny))

bfs()


z=1
res = -1
for i in tomato:
    for j in i:
        for k in j:
            if k==0:
                z=0
            res = max(res,k)

if z == 0:
    print(-1)
elif res==1:
    print(0)
else:
    print(res-1)
