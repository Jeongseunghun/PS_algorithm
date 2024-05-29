from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(i,j):
    sheep = 0
    wolf = 0
    q = deque()
    q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != "#" and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                if board[nx][ny] == 'v':
                    wolf +=1
                elif board[nx][ny] == 'o':
                    sheep += 1
    if sheep > wolf:
        wolf = 0
    else:
        sheep = 0
    
    return sheep,wolf

R,C = map(int,input().split())
board = [list(input()) for _ in range(R)]

visited = [[0 for _ in range(C)] for _ in range(R)]

s = 0
w = 0
for i in range(R):
    for j in range(C):
        if visited[i][j] == 0:
            ts,tw=bfs(i,j)
            s+=ts
            w+=tw

print(s,w)
            