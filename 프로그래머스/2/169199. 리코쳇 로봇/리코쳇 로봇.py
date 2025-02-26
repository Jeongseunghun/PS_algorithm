from collections import deque

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(board):
    ans = 0
    N,M = len(board),len(board[0])
    game = [[0 for _ in range(M)] for _ in range(N)]

    sx,sy = 0,0
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'D':
                game[i][j] = 1
            elif board[i][j] == 'R':
                sx,sy = i,j
            elif board[i][j] == 'G':
                game[i][j] = 2
    
    q = deque()
    q.append((sx,sy))
    
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[sx][sy] = 1
    
    while q:
        x,y = q.popleft()
        if game[x][y] == 2:
            return visited[x][y] -1
            
        for i in range(4):
            nx,ny = x,y
            while 0 <= nx + dx[i] < N and 0 <= ny + dy[i] < M and game[nx + dx[i]][ny + dy[i]] != 1:
                nx += dx[i]
                ny += dy[i]

            if visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1

    return -1