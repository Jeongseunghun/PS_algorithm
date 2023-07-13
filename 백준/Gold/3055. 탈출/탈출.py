from collections import deque

R,C = map(int,input().split())
forest = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()

def bfs(a,b):
    while q:
        x,y = q.popleft()
        if forest[a][b] == "S":
            return visited[a][b]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if forest[nx][ny] == "." or forest[nx][ny] == 'D':
                    if forest[x][y]=="S":
                        forest[nx][ny] = "S"
                        q.append((nx,ny))
                        visited[nx][ny] = visited[x][y] + 1
                if forest[nx][ny] == "." or forest[nx][ny] == 'S':
                    if forest[x][y] == "*":
                        q.append((nx,ny))
                        forest[nx][ny] = "*"
                
    return "KAKTUS"       
                 

for i in range(R):
    for j in range(C):
        if forest[i][j] == 'S':
            q.append((i,j))
        elif forest[i][j] == "D":
            ax,ay = i,j
            
for x in range(R):
    for y in range(C):
        if forest[x][y] == "*":
            q.append((x,y))


print(bfs(ax,ay))    
