N,M,x,y,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
move = list(map(int,input().split()))

#동0,서1,북2,남3
dx = [0,0,-1,1]
dy = [1,-1,0,0]

#명령 좌표 인덱스에 맞춰주기
move = [i-1 for i in move]

##우/좌/하/상/위/아래
dice = [0 for _ in range(6)]


#주사위 굴리기
def turn(i):
    
    #우좌하상위아래
    right,left,down,up,top,bottom = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
    
    #동
    if i == 0:
        #우,좌,위,아래 바뀜
        dice[0],dice[1],dice[4],dice[5] = bottom, top, right, left
    #서
    elif i == 1:
        #우,좌,위,아래 바뀜
        dice[0],dice[1],dice[4],dice[5] = top, bottom, left, right
    
    #남
    elif i == 2:
         #하,상,위,아래 바뀜
        dice[2],dice[3],dice[4],dice[5] = top, bottom, up, down
    
    #북
    elif i == 3:
        #하,상,위,아래 바뀜
        dice[2],dice[3],dice[4],dice[5] = bottom, top, down, up
       

for i in move:
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 > nx or nx >= N or 0 > ny or ny >= M:
        continue
    turn(i)
    
    #지도 숫자가 0이면
    if board[nx][ny] == 0:
        #주사위 아랫면 복사
        board[nx][ny] = dice[5]
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0
    
    x,y = nx,ny
    print(dice[4])
    