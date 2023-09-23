from collections import deque

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def in_air():
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                elif board[nx][ny] == 1:
                    visited[nx][ny]+= 1
                    
    return False

def chk(x,y,air_board,tmp_board):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if air_board[nx][ny] != -1:
                if board[nx][ny] == 0:
                    cnt +=1
    
    if cnt >= 2:
        tmp_board[x][y] = 0
        

ans = 0

while True:
 
    
    visited = [[0 for _ in range(M)] for _ in range(N)]       
         
    in_air()

    ans +=1

    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                board[i][j] = 0
    
    cnt = 0
    for i in range(N):
        cnt += sum(board[i])
    if cnt == 0:
        break

print(ans)