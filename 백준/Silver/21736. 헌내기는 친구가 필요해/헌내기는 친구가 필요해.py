from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(i,j):
    global cnt
    
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if board[nx][ny] == 'O':
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                elif board[nx][ny] == 'P':
                    cnt+=1
                    visited[nx][ny] = 1
                    q.append((nx,ny))

N,M = map(int,input().split())
board = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == "I":
            bfs(i,j)
if cnt>0:
    print(cnt)
else:
    print("TT")

