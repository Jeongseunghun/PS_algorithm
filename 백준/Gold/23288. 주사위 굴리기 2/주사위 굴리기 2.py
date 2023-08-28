from collections import deque

N,M,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

#위상우좌하아래
dice = [1,2,3,4,5,6]


#주사위 굴러감
def turn(i,x,y):
    
    global dice
    # 동쪽
    if i == 0:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    # 남쪽
    elif i == 1:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    # 서쪽
    elif i == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    # 북쪽
    else:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
        
    #바닥면과 칸 수 비교
    if dice[-1] > board[x][y]:
        i = (i+1) % 4
    elif dice[-1] < board[x][y]:
        i = (i-1) % 4
    
    return i

#점수획득
def score(score,x,y):
    visited = [[False]* M for _ in range(N)]
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    
    s_sum = 0
    while q:
        x,y = q.popleft()
        s_sum += score
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if board[nx][ny] == score:
                    q.append((nx,ny))
                    visited[nx][ny] = True
    
    return s_sum


#우하좌상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

#시작 좌표,방향
x,y,d = 0,0,0
cnt = 0
for _ in range(K):
    nx = x + dx[d]
    ny = y + dy[d]
    #범위 넘으면 이동 방향을 반대로
    if 0>nx or nx >= N or 0>ny or ny >= M:
        nx = x + dx[d] * (-1)
        ny = y + dy[d] * (-1)
        d = (d+2) % 4
        
    d = turn(d,nx,ny)
    cnt += score(board[nx][ny],nx,ny)
    
    x,y = nx,ny

print(cnt)