from collections import deque

board = [list(input()) for _ in range(12)]

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#연쇄(같은색 뿌요 4개 이상)
def bfs(cx,cy):
    lst = []
    q = deque()
    q.append((cx,cy))
    lst.append((cx,cy))
    color = board[cx][cy]
    visited = [[0 for _ in range(6)] for _ in range(12)]
    visited[cx][cy] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if board[nx][ny] == color and visited[nx][ny] == 0:
                    lst.append((nx,ny))
                    visited[nx][ny] = 1
                    q.append((nx,ny))
    return lst

def bomb(lst):
    for x,y in lst:
        board[x][y] = "."

#중력
def gravity():
    for j in range(6):
        for i in range(10,-1,-1):
            for c in range(11,i,-1):
                if board[i][j] != "." and board[c][j] == ".":
                    board[c][j] = board[i][j]
                    board[i][j] = "."

#Main
cnt = 0
while True:
    flag = False
    for i in range(12):
        for j in range(6):
            if board[i][j] != ".":
                lst = bfs(i,j)
                if len(lst) >= 4:
                    flag = True
                    bomb(lst)
    if flag:
        gravity()
        cnt+=1
    else:
        break

print(cnt)