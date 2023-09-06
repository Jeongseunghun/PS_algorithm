from collections import deque

N,M,K = map(int,input().split())
board = [list(map(int,input())) for _ in range(N)]
visited = [[[0 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]
#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    q.append((0,0,K))
    visited[0][0][K] = 1
    while q:
        x,y,k = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][k]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                #벽이고, 아직 벽을 뚫을 수 있고, 방문하지 않았다면
                if board[nx][ny] == 1 and k > 0 and visited[nx][ny][k-1] == 0:
                    visited[nx][ny][k-1] = visited[x][y][k] + 1
                    q.append((nx,ny,k-1))
                #벽이 아니고, 방문하지 않았다면
                elif board[nx][ny] == 0 and visited[nx][ny][k] == 0:
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    q.append((nx,ny,k))
    return -1

print(bfs())