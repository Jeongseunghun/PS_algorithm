from collections import deque

dx = [0,0,-1,1,-1,1,-1,1]
dy = [-1,1,0,0,1,-1,-1,1]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny]==0 and board[nx][ny] == 1:
                q.append((nx,ny))
                visited[nx][ny] = 1
                
    return
    
M,N = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(M)]

visited = [[0 for _ in range(N)] for _ in range(M)]

cnt = 0
for i in range(M):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == 0:
            bfs(i,j)
            cnt+=1

print(cnt)

