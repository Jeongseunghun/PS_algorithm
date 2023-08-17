M,S = map(int,input().split())

#물고기와 상어 이동 방향 정보, 복제 정보를 지닌 격자
board = [[[[],[]] for _ in range(4)] for _ in range(4)]

#냄새 저장
fish_smell = [[0 for _ in range(4)] for _ in range(4)]

for i in range(M):
    x,y,d = map(int,input().split())
    board[x-1][y-1][0].append(d-1)

#상어 위치(-1)
sx,sy = map(int,input().split())
sx-=1
sy-=1
path = []
max_fish_cnt = -1

#좌 좌상 상 우상 우 우하 하 좌하
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

#1. 복제 마법 시전
def copy_start():
    for i in range(4):
        for j in range(4):
            for d in board[i][j][0]:
                board[i][j][1].append(d)

#2. 물고기 이동
def fish_move():
    position = []
    for i in range(4):
        for j in range(4):
            while board[i][j][0]:
                flag = False
                k = board[i][j][0].pop()
                for _ in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    #범위 내, 물고기 냄새 X, 상어 X
                    if 0<=nx<4 and 0<=ny<4 and fish_smell[nx][ny] ==0 and not(nx == sx and ny == sy):
                        position.append((nx,ny,k))
                        flag = True
                        break
                    k = (k-1)%8
                #이동할 곳 없을 때 이동하지 않은 정보
                if flag == False:
                    position.append((i,j,k))
    return position
    
#상좌하우
sdx = [-1,0,1,0]
sdy = [0,-1,0,1]

visited = [[False for _ in range(4)] for _ in range(4)]
#3.상어 이동 선택 및 이동
def select_shark_move(r,c,fish_cnt,move_cnt,tmp_path):
    global sx,sy,visited,max_fish_cnt,path
    if move_cnt == 3:
        if max_fish_cnt < fish_cnt:
            max_fish_cnt = fish_cnt
            path = [d for d in tmp_path]
        return
    
    for d in range(4):
        nx = r + sdx[d]
        ny = c + sdy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                next_fish_cnt = fish_cnt + len(board[nx][ny][0])
                select_shark_move(nx,ny,next_fish_cnt,move_cnt+1,tmp_path+[d])
                visited[nx][ny] = False
            else:
                select_shark_move(nx,ny,fish_cnt,move_cnt+1,tmp_path+[d])
    

def shark_move():
    global sx,sy,board,fish_smell
    for d in path:
        sx = sx + sdx[d]
        sy = sy + sdy[d]
        if board[sx][sy][0]:
            board[sx][sy][0] = []
            fish_smell[sx][sy] = 3    

#4.물고기 냄새 갱신
def smell_out():
    global fish_smell
    for i in range(4):
        for j in range(4):
            if fish_smell[i][j] > 0:
                fish_smell[i][j] -= 1

#5.복제 마법 완료
def dup():
    for i in range(4):
        for j in range(4):
            while board[i][j][1]:
                board[i][j][0].append(board[i][j][1].pop())

#S번 시행
for _ in range(S):
    copy_start()
    position = fish_move()
    for r,c,dir in position:
        board[r][c][0].append(dir)
    
    path = []
    max_fish_cnt = -1
    
    select_shark_move(sx,sy,0,0,[])
    shark_move()
    
    smell_out()
    
    dup()

#격자에 있는 물고기 수
ans = 0
for i in range(4):
    for j in range(4):
        ans += len(board[i][j][0])
print(ans)