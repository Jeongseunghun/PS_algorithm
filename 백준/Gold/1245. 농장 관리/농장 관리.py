from collections import deque

dx = [0,0,-1,1,1,1,-1,-1]
dy = [-1,1,0,0,1,-1,-1,1]

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

def bfs(sx,sy):
    global cnt
    q = deque()
    q.append((sx,sy))
    Flag = True
    while q:
        x,y = q.popleft()
        visited[x][y] = 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == board[x][y] and visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                elif board[nx][ny] > board[x][y]:
                    Flag = False
                    
    return Flag
    
cnt = 0
visited = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            Flag = bfs(i,j)
            if Flag:
                cnt+=1
print(cnt)