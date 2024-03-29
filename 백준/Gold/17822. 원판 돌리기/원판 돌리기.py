from collections import deque

N,M,T = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

#원판 회전하기
def rotate(x,d,k):
    q = deque()
    q.extend(board[x])
    #0이면 시계방향
    if d == 0:
        q.rotate(k)
    #1이면 반시계방향
    else:
        q.rotate(-k)
    
    board[x] = list(q)

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#인접한 수 지우기
def erase(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    val = board[x][y]
    board[x][y] = 0
    cnt = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > ny or ny >= M:
                if y == 0:
                    ny = M-1
                elif y == M-1:
                    ny = 0
            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny] == False:
                    if board[nx][ny] == val:
                        q.append((nx,ny))
                        board[nx][ny] = 0
                        visited[nx][ny] = True
                        cnt+=1
    if cnt == 0:
        board[x][y] = val
                    
    return cnt

def c_sum():
    #평균 구하기
    c_sum = 0
    circle_cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                circle_cnt += 1
                c_sum += board[i][j]

    
    if circle_cnt == 0:
        return False
    avg = c_sum / circle_cnt
    #빼주고 더하기
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                if board[i][j] > avg:
                    board[i][j] -= 1
                elif board[i][j] < avg:
                    board[i][j] += 1
                    
    return True

for _ in range(T):
    x,d,k = map(int,input().split())
    chk_sum = 0
    for i in range(N):
        chk_sum += sum(board[i])
        if (i+1) % x == 0:
            rotate(i,d,k)
    if chk_sum == 0:
        break
    else:
        visited = [[False for _ in range(M)] for _ in range(N)]
        cnt = 0
        for i in range(N):
            for j in range(M):
                if visited[i][j] == False and board[i][j] != 0:
                    cnt += erase(i,j)
        if cnt == 0:
            c_sum()

ans = 0
for i in range(N):
    ans += sum(board[i])

print(ans)