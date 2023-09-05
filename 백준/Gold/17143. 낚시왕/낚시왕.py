R,C,M = map(int,input().split())

board = [[[] for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    #속력,방향,크기
    board[r-1][c-1].append((s,d-1,z))

#땅에 가까운 상어 잡기
def fisher_catch(loc):
    global sum
    for i in range(R):
        #상어가 있으면
        if len(board[i][loc]) != 0:
            sum+=board[i][loc][0][2]
            board[i][loc].pop()
            break
            
#상하우좌
dx = [-1,1,0,0]
dy = [0,0,1,-1]

#상어 이동
def shark_move():
    global board
    tmp_board = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j]:
                x,y = i,j
                s,d,z = board[i][j][0]
                move = 0
                #s번 움직임
                while s > move:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < R and 0 <= ny < C:
                        x,y = nx,ny
                        move += 1
                    else:
                        if d == 0:
                            d = 1
                        elif d == 1:
                            d = 0
                        elif d == 2:
                            d = 3
                        elif d == 3:
                            d = 2
                        continue
                tmp_board[x][y].append((s,d,z))
    
    board = tmp_board
    
    #한 칸에 중복 시 큰 상어만 살아남기
    for i in range(R):
        for j in range(C):
            if 1 < len(board[i][j]):
                board[i][j].sort(key = lambda x: x[2], reverse = True)
                while 1 < len(board[i][j]):
                    board[i][j].pop()
                
sum = 0
for loc in range(C):
    fisher_catch(loc)
    shark_move()

print(sum)