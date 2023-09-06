from collections import deque

N,M = map(int,input().split())
board = [list(map(int,input())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    visited = [[[0,0] for _ in range(M)] for _ in range(N)]
    q.append((0,0,0))
    visited[0][0][0] = 1
    while q:
        x,y,z = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny < M:
                #벽이 아니고, 방문한 적 없을 때
                if board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    q.append((nx,ny,z))
                    visited[nx][ny][z] = visited[x][y][z] + 1
                #벽이고, 부순 적 없고, 방문한 적 없을때
                elif board[nx][ny] == 1 and z == 0 and visited[nx][ny][1] == 0:
                    q.append((nx,ny,1))
                    visited[nx][ny][1] = visited[x][y][0] + 1 
              
    return -1

print((bfs()))