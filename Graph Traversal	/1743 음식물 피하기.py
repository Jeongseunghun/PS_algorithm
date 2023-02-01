from collections import deque

N,M,K = map(int,input().split())
lst = [[0] * M for _ in range(N)]
for i in range(K):
    r,c = map(int,input().split())
    lst[r-1][c-1] = 1

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()

visited = [[0]* M for _ in range(N)]

def bfs():
    t=1
    q.append((i,j))
    visited[i][j] = 1
    while q:
        x,y = q.popleft()   
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<N and 0<=ny<M and lst[nx][ny] == lst[x][y] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                t+=1
                q.append((nx,ny))
    
    return t
                
ans = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1 and visited[i][j] == 0:
            ans = max(ans,bfs())
            
            

print(ans)