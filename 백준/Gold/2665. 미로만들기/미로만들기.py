from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    q.append((0,0))
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[0][0] = 1
    while q:
        x,y = q.popleft()
        if x == N-1 and y == N-1:
            print(visited[x][y]-1)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if board[nx][ny] == "1":
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx,ny))
                elif board[nx][ny] == "0":
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))

N = int(input())
#1: 흰 방, 2: 검은 방
board = [list(input()) for _ in range(N)]

bfs()