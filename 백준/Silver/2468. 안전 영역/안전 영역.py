from collections import deque

N = int(input())
loc = [list(map(int,input().split())) for _ in range(N)]

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

max_h = 0
for i in range(N):
    for j in range(N):
        max_h = max(max_h,loc[i][j])


def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = -1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = -1

res = 0
for cnt in range(max_h):
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if loc[i][j] <= cnt:
                visited[i][j] = -1
    c = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:         
                bfs(i,j)
                c+=1
    res = max(res,c)


print(res)
                
        
    
    
        