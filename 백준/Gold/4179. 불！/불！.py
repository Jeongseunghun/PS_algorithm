from collections import deque

R,C = map(int,input().split())
board = [list(input()) for _ in range(R)]
fire = [[0 for _ in range(C)] for _ in range(R)]
jihoon = [[0 for _ in range(C)] for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while f_q:
        x,y = f_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != '#' and fire[nx][ny] == 0:
                    fire[nx][ny] = fire[x][y] + 1
                    f_q.append((nx,ny))
                
    while j_q:
        x,y = j_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if not jihoon[nx][ny] and board[nx][ny] != '#':
                    if fire[nx][ny] == 0 or fire[nx][ny] > jihoon[x][y] + 1:
                        j_q.append((nx,ny))
                        jihoon[nx][ny] = jihoon[x][y] + 1
            else:
                return jihoon[x][y]

    return "IMPOSSIBLE"

f_q = deque()
j_q = deque()

for i in range(R):
    for j in range(C):
        if board[i][j] == "F":
            fire[i][j] = 1
            f_q.append((i,j))
        if board[i][j] == "J":
            jihoon[i][j] = 1
            j_q.append((i,j))
       
print(bfs())