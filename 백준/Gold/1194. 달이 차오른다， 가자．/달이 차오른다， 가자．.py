from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

keyDict = ['a','b','c','d','e','f']
doorDict = ['A','B','C','D','E','F']

def bfs(i,j):
    visited = [[[0]*64 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((i,j,0))
    cnt = -1
    visited[i][j][0] = 1
    while q:
        x,y,z = q.popleft()
        if board[x][y] == '1':
            cnt = visited[x][y][z] - 1
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != "#" and visited[nx][ny][z] == 0:
                #열쇠면
                if board[nx][ny] in keyDict:
                    nz = z | (1<< (ord(board[nx][ny]) - ord('a')))
                    if visited[nx][ny][nz] == 0:
                        q.append((nx,ny,nz))
                        visited[nx][ny][nz] = visited[x][y][z] + 1
                #문이면
                elif board[nx][ny] in doorDict:
                    if z & (1 << (ord(board[nx][ny]) - ord('A'))):
                        q.append((nx,ny,z))
                        visited[nx][ny][z] = visited[x][y][z] + 1

                #길이면
                else:
                    q.append((nx,ny,z))
                    visited[nx][ny][z] = visited[x][y][z] + 1

    return cnt

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            ans = bfs(i,j)
            print(ans)