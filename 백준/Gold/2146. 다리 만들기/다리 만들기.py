from collections import deque

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#섬 구분 지어주기
def bfs(x,y,c):
    q = deque()
    q.append((x,y))
    board[x][y] = c
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append((nx,ny))
                    board[nx][ny] = c
                    visited[nx][ny] = 1
                    
#이어주기
def connect(island):
    global ans
    q = deque()
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == island:
                q.append((i,j))
                dist[i][j] = 0
                
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny] > 0 and board[nx][ny] != island:
                    ans = min(ans,dist[x][y])
                    return
                if board[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))             
                    
island_cnt = 1
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == 0 :
            island_cnt += 1
            bfs(i,j,island_cnt)
          
ans = 99999  


for i in range(2,island_cnt+1):
    connect(i)
    
print(ans)