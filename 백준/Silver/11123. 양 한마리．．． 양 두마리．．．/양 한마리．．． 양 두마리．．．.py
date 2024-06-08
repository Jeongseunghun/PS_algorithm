from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and visited[nx][ny] == 0 and board[nx][ny] == "#":
                visited[nx][ny] = 1
                q.append((nx,ny))
    
    return

T = int(input())
for _ in range(T):
    cnt = 0
    H,W = map(int,input().split())
    board = [list(input()) for _ in range(H)]
    visited = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if board[i][j] == "#" and visited[i][j] == 0:
                bfs(i,j)
                cnt+=1

    print(cnt)
    