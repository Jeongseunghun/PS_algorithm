import copy

#칸에 들어가 있는 물고기 정보
#물고기 정보 = [번호,방향]
board = [[] for _ in range(4)]

for i in range(4):
    fish = []
    space = list(map(int,input().split()))
    for j in range(4):
        fish.append([space[j*2],space[j*2+1]-1])
    board[i] = fish
#상 좌상 좌 좌하 하 우 하 우 우상
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

shark_eat = 0

def dfs(sx,sy,score,board):
    global shark_eat
    #청소년 상어 (0,0) 물고기 먹음
    score += board[sx][sy][0]
    shark_eat = max(shark_eat,score)
    board[sx][sy][0] = 0
    
    #물고기 이동
    for m in range(1,17):
        fx,fy = -1,-1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == m:
                    fx,fy = x, y
                    break
        if fx == -1 and fy == -1:
            continue
            
        fd = board[fx][fy][1]
        
        #방향
        for i in range(8):
            nd = (fd + i) % 8
            nx = fx + dx[nd]
            ny = fy + dy[nd]
            #범위 벗어나거나 상어있으면
            if not (0<=nx<4 and 0<=ny<4) or (nx == sx and ny == sy):
                continue
            board[fx][fy][1] = nd
            board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]
            break
        
    #상어 이동
    s_move = board[sx][sy][1]
    for i in range(1,4):
        nx = sx + dx[s_move]*i
        ny = sy + dy[s_move]*i
        # 범이 내에 이썩나 물고기가 있으면
        if (0<= nx < 4 and 0<= ny < 4) and board[nx][ny][0] > 0:
            dfs(nx,ny,score,copy.deepcopy(board))
            
dfs(0,0,0,board)
print(shark_eat)
