from collections import deque

n,m = map(int,input().split())
hx,hy = map(int,input().split())
ex,ey = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(n)]

#상하좌우
dx=[0,0,-1,1]
dy=[-1,1,0,0]


visited = [[[-1,-1] for _ in range(m)] for _ in range(n)]


def bfs():
    q= deque()
    q.append((hx-1,hy-1,0))
    visited[hx-1][hy-1][0] = 0
    while q:
        a,b,c = q.popleft()
        if a == ex-1 and b == ey-1:
            return visited[a][b][c]
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            nz = c
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maze[nx][ny]:
                if nz == 1:
                    continue
                else:
                    nz = 1
            if visited[nx][ny][nz] == -1:
                visited[nx][ny][nz] = visited[a][b][c] + 1
                q.append((nx,ny,nz))
                
    return -1
            
print(bfs())
    
    
    
    