from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#녹음
def melt(w,board):
    next_w = deque()
    while w:
        x, y = w.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not 0 <= nx < R or not 0 <= ny < C:
                continue
            if board[nx][ny] == 'X':
                next_w.append((nx,ny))
                board[nx][ny] = '.'

    return next_w


def chk(board,visited,q):
    next_q = deque()
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            return True,None

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not 0 <= nx < R or not 0 <= ny < C:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == 'X':
                next_q.append((nx,ny))
            else:
                q.append((nx,ny))
            visited[nx][ny] = True

    return False, next_q

R, C = map(int, input().split())
board = []
swan = []

q,next_q,w,next_w = deque(),deque(),deque(),deque()

for i in range(R):
    row = list(input())
    board.append(row)
    for j in range(C):
        if row[j] == 'L':
            swan.extend([i, j])
        if row[j] == "." or row[j] == "L":
            w.append((i,j))

sx, sy, ex, ey = swan
cnt = -1

visited = [[0] * C for _ in range(R)]
q.append((sx,sy))
visited[sx][sy] = 1

while True:
    cnt+=1
    found, next_q = chk(board,visited,q)
    if found:
        break
    w = melt(w,board)
    q = next_q

print(cnt)