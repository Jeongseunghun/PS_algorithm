from collections import deque

N,Q = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(2**N)]
L = list(map(int,input().split()))

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#회전
def rotate(board,l):
    new_graph = [[0 for _ in range(2**N)] for _ in range(2**N)]
    
    for i in range(0,2**N,2**l):
        for j in range(0,2**N, 2**l):
            for k in range(2**l):
                for m in range(2**l):
                    new_graph[i+k][j+m] = board[i + (2**l - 1 -m)][j+k]    

    return new_graph

#얼음 계산
def ice(board):
    new_board = [[0 for _ in range(2**N)] for _ in range(2**N)]
    
    for x in range(2**N):
        for y in range(2**N):
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 2**N and 0 <= ny < 2**N:
                    if board[nx][ny] > 0:
                        cnt+=1
            if cnt < 3:
                if board[x][y] - 1 >0:
                    new_board[x][y] = board[x][y] - 1
            else:
                new_board[x][y] = board[x][y]
    return new_board

#가장 큰 덩어리 구하기
res = 0
def bfs(x,y):
    global res
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    ice_size = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 2**N and 0 <= ny < 2**N:
                if board[nx][ny] > 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    ice_size+=1
                    q.append((nx,ny))
    res = max(ice_size,res)         

#파이어스톰 Q번 반복
for l in L:
    board = rotate(board,l)
    board = ice(board)

#남아 있는 얼음 합
ans = sum([sum(i) for i in board])

print(ans)
#가장 큰 덩어리가 차지하는 칸
visited = [[0 for _ in range(2**N)] for _ in range(2**N)]
for i in range(2**N):
    for j in range(2**N):
        if board[i][j] > 0 and visited[i][j] == 0:
            bfs(i,j)
print(res)
