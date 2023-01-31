from collections import deque

N,M = map(int,input().split())
lst = [list(input()) for _ in range(M)]

visited = [[0]*N for _ in range(M)]

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

q = deque()
w,p = 0,0

def bfs():
    t = 1
    q.append((i,j))
    visited[i][j] = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and lst[nx][ny] == lst[x][y] and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                t+=1
                q.append((nx,ny))
    return t
                

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            ans = bfs()
            if lst[i][j] == 'W':
                w += ans*ans
            else:
                p += ans*ans

print(w,p)