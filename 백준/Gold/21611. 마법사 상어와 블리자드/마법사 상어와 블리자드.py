from collections import deque

N,M = map(int,input().split())
#구슬 정보 격자
board = [list(map(int,input().split())) for _ in range(N)]
#명령
command = [list(map(int,input().split())) for _ in range(M)]
sx,sy = (N-1)//2, (N-1)//2

#0상하좌우
d_dx = [0,-1,1,0,0]
d_dy = [0,0,0,-1,1]

#구슬 파괴
def dest(d,s):
    global board,sx,sy
    
    for i in range(1,s+1):
        nx = sx + d_dx[d]*i
        ny = sy + d_dy[d]*i
        if 0<=nx<N and 0<=nx<N:
            board[nx][ny] = 0
            
#탐색 순서 정보
arr = []

#탐색 순서 저장
def order(arr):
    x,y = N//2, N//2
    #좌하우상
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    cd = 0
    step = 0
    Flag = True
    while Flag:
        #좌, 우가 시작될 때 step증가
        if cd % 2 == 0:
            step+=1
        for _ in range(step):
            x = x + dx[cd]
            y = y + dy[cd]
            arr.append((x,y))
            if x == 0 and y == 0:
                Flag = False
                break
        cd = (cd+1) % 4

order(arr)

#빈 칸으로 이동
def fill_blank():
    q = deque()
    for x,y in arr:
        if board[x][y]:
            q.append(board[x][y])
    
    for x,y in arr:
        if q:
            board[x][y] = q.popleft()
        else:
            board[x][y] = 0

#구슬 번호에 따라 개수 추가
result = [0,0,0]

def check(num,cnt):
    if num == 1:
        result[0] += cnt
    elif num == 2:
        result[1] += cnt
    elif num == 3:
        result[2] += cnt

#구슬 폭발
def explode():
    total = 0
    num,cnt = board[arr[0][0]][arr[0][1]], 1
    bomb = [arr[0]]
    for i in range(1,len(arr)):
        #해당 숫자가 이전 숫자와 다르면
        if num != board[arr[i][0]][arr[i][1]]:
            if num and cnt >= 4:
                total += 1
                check(num,cnt)
                for a, b in bomb:
                    board[a][b] = 0
            num = board[arr[i][0]][arr[i][1]]
            bomb = []
            cnt = 0
        bomb.append(arr[i])
        cnt+=1
    
    if num and cnt >= 4:
        total += 1
        check(num,cnt)
        for a,b in bomb:
            board[a][b] = 0
                
    return total
   
for d,s in command:
    dest(d,s)
    fill_blank()
    
    while True:
        if explode():
            fill_blank()
        else:
            break
        
    num,cnt = board[arr[0][0]][arr[0][1]], 1
    tmp = deque()
    for i in range(1,len(arr)):
        if num != board[arr[i][0]][arr[i][1]]:
            tmp.append(cnt)
            tmp.append(num)
            num = board[arr[i][0]][arr[i][1]]
            cnt = 0
        cnt+=1
        
    if num:
        tmp.append(cnt)
        tmp.append(num)
    
    for x,y in arr:
        if tmp:
            board[x][y] = tmp.popleft()
        else:
            board[x][y] = 0
            
answer = 0
for i in range(1,4):
    answer += i * result[i-1]
    
print(answer)