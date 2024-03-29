from collections import deque

board = [list(input()) for _ in range(12)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    lst = []
    lst.append((i,j))
    color = board[i][j]
    visited = [[0 for _ in range(6)] for _ in range(12)]
    visited[i][j] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<12 and 0<=ny<6:
                if visited[nx][ny] == 0 and board[nx][ny] == color:
                    lst.append((nx,ny))
                    q.append((nx,ny))
                    visited[nx][ny] = 1
    return lst

def bomb(lst):
    for x,y in lst:
        board[x][y] = "."

def gravity():
    for c in range(6):
        for i in range(10,-1,-1):
            for j in range(11,i,-1):
                if board[i][c] != '.' and board[j][c] == '.':
                    board[j][c] = board[i][c]
                    board[i][c] = "."


cnt = 0
while True:
    flag = False
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                lst = bfs(i,j)
                if len(lst) >= 4:
                    bomb(lst)
                    flag = True
    if flag:
        cnt+=1
        gravity()
    else:
        break

print(cnt)