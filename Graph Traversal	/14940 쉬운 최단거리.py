from collections import deque
from re import L, X

n,m = map(int,input().split())

dis = [list(map(int,input().split())) for i in range(n)]
visited = [[False]*m for _ in range(n)]
re = [[-1]*m for _ in range(n)]
q = deque()

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    for j in range(m):
        if dis[i][j] == 2:
            q.append([i,j])
            visited[i][j] = True
            re[i][j] = 0
        elif dis[i][j] == 0:
            re[i][j] = 0


def go():
    while q:
        x,y = map(int,q.popleft())
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and not visited[nx][ny] and dis[nx][ny] == 1:
                visited[nx][ny] = True
                q.append([nx,ny])
                re[nx][ny] = re[x][y] + 1




go()

for i in range(n):
    print(" ".join(map(str,re[i])))               
        
        
        