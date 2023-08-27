N,K = map(int,input().split())
#색깔 저장
board = [list(map(int,input().split())) for _ in range(N)]
#말 번호 저장
players = [[[] for _ in range(N)] for _ in range(N)]

#말 번호 별 (위치,방향) 저장
horse = [[] for _ in range(K+1)]

for i in range(1,K+1):
    x,y,d = map(int,input().split())
    players[x-1][y-1].append(i)
    horse[i] = [x-1,y-1,d-1]

#우좌상하
dx = [0,0,-1,1]
dy = [1,-1,0,0]

#흰색
def white(x,y,nx,ny,num,hd):
    #현재 말 + 위에 있는 말들 다 이동
    current = players[x][y].index(num)
    q = players[x][y][current:]

    players[nx][ny] += q
    #말 위치 정보 갱신
    if q:
        for i in q:
            horse[i][0] = nx
            horse[i][1] = ny
    
    players[x][y] = players[x][y][:current]
    horse[num] = [nx,ny,hd]
    #4개 이상 쌓여있으면 즉시 종료
    if len(players[nx][ny]) >= 4:
        print(cnt)
        exit()
    

#빨간색
def red(x,y,nx,ny,num,hd):
    current = players[x][y].index(num)
    q = players[x][y][current:]
    #반대로 돌려줌
    q.reverse()

    players[nx][ny] += q
    #말 위치 정보 갱신
    if q:
        for i in q:
            horse[i][0] = nx
            horse[i][1] = ny
    
    players[x][y] = players[x][y][:current]
    horse[num] = [nx,ny,hd]
    #4개 이상 쌓여있으면 즉시 종료
    if len(players[nx][ny]) >= 4:
        print(cnt)
        exit()

#파란색
def blue(x,y,d,num):
    nd = 0
    #우 -> 좌
    if d == 0:
        nd = 1
    #좌 -> 우
    elif d == 1:
        nd = 0
    #상 -> 하
    elif d == 2:
        nd = 3
    #하 -> 상
    elif d == 3:
        nd = 2
    
    nx = x + dx[nd]
    ny = y + dy[nd]
    
    #방향 바꿔주기
    horse[num][2] = nd
    if nx<0 or nx>=N or ny<0 or ny>=N:
        return
    if board[nx][ny] == 0:
        white(x,y,nx,ny,num,nd)
        return
    elif board[nx][ny] == 1:
        red(x,y,nx,ny,num,nd)
        return
    elif board[nx][ny] == 2:
        return


#말 이동
def move(k):

    return
cnt = 0
while cnt <= 1000:
    #턴 추가 
    cnt += 1
    #말 순서대로 실행
    for k in range(1,K+1):
        hx,hy,hd = horse[k]
        
        nx = hx + dx[hd]
        ny = hy + dy[hd]
        #체스판을 벗어나면
        if 0 > nx or N <= nx or 0 > ny or N <= ny:
            blue(hx,hy,hd,k)
        elif board[nx][ny] == 0:
            white(hx,hy,nx,ny,k,hd)
        elif board[nx][ny] == 1:
            red(hx,hy,nx,ny,k,hd)
        elif board[nx][ny] == 2:
            blue(hx,hy,hd,k)
        
print(-1)
                    