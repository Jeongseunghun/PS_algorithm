from collections import deque

N = int(input())
r1,c1,r2,c2 = map(int,input().split())

board = [[0 for _ in range(N)] for _ in range(N)]

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def bfs():
    q = deque()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    q.append((r1,c1))
    board[r1][c1] = 1
    while q:
        x,y = q.popleft()
        visited[x][y] = 1
        if x == r2 and y == c2:
            print(board[x][y]-1)
            exit()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                board[nx][ny] = board[x][y] + 1
    print(-1)

bfs()
            