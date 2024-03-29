from collections import deque
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    rainbow_cnt = 0
    rainbow = []
    blocks = []
    color = board[x][y]
    cnt = 1
    blocks.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] != -1 and visited[nx][ny] == 0:
                    if board[nx][ny] == color or board[nx][ny] == 0:
                        visited[nx][ny] = 1
                        blocks.append((nx,ny))
                        cnt+=1
                        q.append((nx,ny))
                        if board[nx][ny] == 0:
                            rainbow_cnt+=1
                            rainbow.append((nx,ny))

    for x,y in rainbow:
        visited[x][y] = 0

    return (cnt,rainbow_cnt,blocks)

#가장 큰 블록 그룹 찾고 제거
def big_group():
    visited = [[0 for _ in range(N)] for _ in range(N)]
    tmp_lst = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and visited[i][j] == 0:
                tmp = bfs(i,j,visited)
                if tmp[0] >= 2:
                    tmp_lst.append(tmp)
    tmp_lst.sort(key=lambda x: (x[0],x[1],x[2]),reverse=True)

    return tmp_lst

#제거 후 점수 계산
def cal_score(lst):

    for x,y in lst[2]:
        board[x][y] = -2

    global score
    score += lst[0]**2
    return score

def gravity(board):
    for i in range(N-2,-1,-1):
        for j in range(N):
            if board[i][j] > -1:
                r = i
                while True:
                    if 0 <= r+1 < N and board[r+1][j] == -2:
                        board[r+1][j] = board[r][j]
                        board[r][j] = -2
                        r+=1
                    else:
                        break
    return board

def rotate():
    global board
    lst = []
    for i in range(N-1,-1,-1):
        tmp_lst = []
        for j in range(N):
            tmp_lst.append(board[j][i])
        lst.append(tmp_lst)

    board = lst
    return board

score = 0
while True:
    tmp_lst = big_group()
    if len(tmp_lst) == 0:
        break
    score = cal_score(tmp_lst[0])
    board = gravity(board)
    board = rotate()
    board = gravity(board)

print(score)