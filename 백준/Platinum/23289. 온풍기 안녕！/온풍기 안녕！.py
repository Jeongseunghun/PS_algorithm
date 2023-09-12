import copy
from collections import deque

R,C,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(R)]
W = int(input())

#온도 저장하는 방
room = [[0 for _ in range(C)] for _ in range(R)]

#세로벽, 가로벽
ver_wall = [[0 for _ in range(C)] for _ in range(R)]
hor_wall = [[0 for _ in range(C)] for _ in range(R)]

for i in range(W):
    x,y,t = map(int,input().split())
    #0이면 가로
    if t == 0:
        hor_wall[x-1][y-1] = 1
    #1이면 세로
    elif t == 1:
        ver_wall[x-1][y-1] = 1

#0우좌상하
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

#벽 체크
def up(i,j,k):
    if hor_wall[i][j] == 1:
        return 0
    if not (0<=i+dx[k]< R and 0<= j+dy[k] < C):
        return 0
    return 1

def left(i,j,k):
    if (0<=i+dx[k]< R and 0<= j+dy[k] < C):
        if ver_wall[i+dx[k]][j+dy[k]] == 0:
            return 1
    return 0
    
def down(i,j,k):
    if (0<=i+dx[k]<R and 0<= j+dy[k]<C):
        if hor_wall[i+dx[k]][j+dy[k]] == 0:
            return 1
    return 0
    
def right(i,j,k):
    if ver_wall[i][j] == 1:
        return 0
    if not (0<=i+dx[k]<R and 0<= j+dy[k]<C):
        return 0
    return 1

#온풍기 바람 나옴(온도 상승)
def temp_up():
    #온풍기 위치,방향 저장
    airs = []
    for i in range(R):
        for j in range(C):
            if 1<= board[i][j] <= 4:
                airs.append((i,j,board[i][j]))
    #온풍기 위치,방향
    for x,y,d in airs:
        tmp = [[0 for _ in range(C)] for _ in range(R)]
        x, y = x + dx[d], y + dy[d]
        #바람이 나오는 방향에 있는 칸은 항상 온도가 5
        tmp[x][y] = 5
        
        q = deque()
        q.append((x,y,5))
        while q:
            px,py,temp = q.popleft()
            
            if temp == 0:
                break
            #우
            if d == 1:
                #우상단 벽 체크
                if up(px,py,3):
                    #오른쪽 벽 체크
                    if right(px-1,py,1): 
                        q.append((px-1,py+1,temp-1))
                        tmp[px-1][py+1] = temp - 1
                #우 벽 체크
                if right(px,py,1):
                    q.append((px,py+1,temp-1))
                    tmp[px][py+1] = temp - 1
                #우하단 벽 체크
                if down(px,py,4):
                    if right(px+1,py,1):
                        q.append((px+1,py+1,temp-1))
                        tmp[px+1][py+1] = temp - 1
                        
            #좌
            elif d == 2:
                #좌상단 벽 체크
                if up(px,py,3):
                    if left(px-1,py,2):
                        q.append((px-1,py-1,temp-1))
                        tmp[px-1][py-1] = temp - 1
                
                #좌 벽 체크
                if left(px,py,2):
                    q.append((px,py-1,temp-1))
                    tmp[px][py-1] = temp - 1
                
                #좌하단 벽 체크
                if down(px,py,4):
                    if left(px+1,py,2):
                        q.append((px+1,py-1,temp-1))
                        tmp[px+1][py-1] = temp - 1
            
            #상
            elif d == 3:
                #좌상단 벽 체크
                if left(px,py,2):
                    if up(px,py-1,3):
                        q.append((px-1,py-1,temp-1))
                        tmp[px-1][py-1] = temp - 1
                
                #상단 벽 체크
                if up(px,py,3):
                    q.append((px-1,py,temp-1))
                    tmp[px-1][py] = temp - 1
                
                #우상단 벽 체크
                if right(px,py,1):
                    if up(px,py+1,3):
                        q.append((px-1,py+1,temp-1))
                        tmp[px-1][py+1] = temp - 1
            
            #하
            elif d == 4:
                #좌하단 벽 체크
                if left(px,py,2):
                    if down(px,py-1,4):
                        q.append((px+1,py-1,temp-1))
                        tmp[px+1][py-1] = temp - 1
                
                #하단 벽 체크
                if down(px,py,4):
                    q.append((px+1,py,temp-1))
                    tmp[px+1][py] = temp - 1
                
                #우하단 벽 체크
                if right(px,py,1):
                    if down(px,py+1,4):
                        q.append((px+1,py+1,temp-1))
                        tmp[px+1][py+1] = temp - 1
    
        for i in range(R):
            for j in range(C):
                room[i][j] += tmp[i][j]
            

#온도 조절 
def temp_control():
    tmp = copy.deepcopy(room)
    
    for i in range(R):
        for j in range(C):
            #우
            if right(i,j,1):
                nx = i + dx[1]
                ny = j + dy[1]
                give = abs(room[i][j]-room[nx][ny])//4 
                if room[i][j] > room[nx][ny]:
                    tmp[i][j] -= give
                elif room[i][j] < room[nx][ny]:
                    tmp[i][j] += give
                
            #좌
            if left(i,j,2):
                nx = i + dx[2]
                ny = j + dy[2]
                give = abs(room[i][j]-room[nx][ny])//4
                if room[i][j] > room[nx][ny]:
                    tmp[i][j] -= give
                elif room[i][j] < room[nx][ny]:
                    tmp[i][j] += give
                    
            #상
            if up(i,j,3):
                nx = i + dx[3]
                ny = j + dy[3]
                give = abs(room[i][j]-room[nx][ny])//4
                if room[i][j] > room[nx][ny]:
                    tmp[i][j] -= give
                elif room[i][j] < room[nx][ny]:
                    tmp[i][j] += give
            
            #하
            if down(i,j,4):
                nx = i + dx[4]
                ny = j + dy[4]
                give = abs(room[i][j]-room[nx][ny])//4
                if room[i][j] > room[nx][ny]:
                    tmp[i][j] -= give
                elif room[i][j] < room[nx][ny]:
                    tmp[i][j] += give
      
    return tmp
            
#바깥쪽 온도 감소
def temp_down():
    for i in range(R):
        for j in range(C):
            cnt = 0 # 범위를 벗어나는 개수
            for k in range(1, 4+1):
                mx = i + dx[k]
                my = j + dy[k]

                if not (0 <= mx < R and 0 <= my < C):
                    cnt += 1

            if cnt != 0:
                if room[i][j] > 0:
                    room[i][j] -= 1
            
#온도 검사
def temp_chk():
    for i in range(R):
        for j in range(C):
            if board[i][j] == 5:
                if room[i][j] < K:
                    return False
    return True
        
cho = 0
while True:
    
    #온도 상승
    temp_up()
    
    #온도 조절
    room = temp_control()
    
    #바깥쪽 온도 감소
    temp_down()
    
    #초콜릿 하나 먹음
    cho += 1
    
    #조사하는 칸 온도 검사
    if temp_chk():
        break
    
    if cho > 100:
        cho = 101
        break
            
print(cho)