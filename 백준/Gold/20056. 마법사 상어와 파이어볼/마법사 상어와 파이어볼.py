from collections import deque

N,M,K = map(int,input().split())
#격자
board = [[deque() for _ in range(N)] for _ in range(N)]

#fireball에 좌표추가
#board에 fireball 정보 배치
fireball = deque()
for i in range(M):
    r,c,m,s,d = map(int,input().split())
    fireball.append((r-1,c-1))
    board[r-1][c-1].append(deque((m,s,d)))
    
#상,우상,우,우하,하,좌하,좌,좌상
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]


#fireball 이동
def move():
    
    while fireball:
        x,y = fireball.popleft()
        m,s,d = board[x][y].popleft()
        
        nx = (x + dx[d] * s) % N
        ny = (y + dy[d] * s) % N
        
        #board에 이동한 fireball 정보 배치
        board[nx][ny].append(deque((m,s,d)))

#두개 이상의 파이어볼 체크
def chk():
    for x in range(N):
        for y in range(N):
            #두개 이상 파이어볼이 있으면
            if len(board[x][y]) > 1:
                mass, speed = 0, 0
                count = [0,0]
                length = len(board[x][y])
                while board[x][y]:
                    m,s,d = board[x][y].popleft()
                    #모든 질량 더해주기
                    mass += m
                    #모든 스피드 더해주기
                    speed += s
                    #방향 확인(홀수면 1에 1추가, 짝수면 0에 1추가)
                    count[d%2] +=1
                
                #질량 0 이면 없어짐
                if mass // 5 == 0:
                    continue
                #방향이 모두 홀수/짝수면
                if count[0] == 0 or count[1] == 0:
                    directions = [0,2,4,6]
                else:
                    directions = [1,3,5,7]
                    
                #board에 fireball 좌표 하나씩 추가
                for direction in directions:
                    fireball.append((x,y))
                    board[x][y].append(deque((mass//5,speed//length,direction)))
                
            #fireball이 한개면 좌표정보만 추가
            elif len(board[x][y]) == 1:
                fireball.append((x,y))


#K번 명령 반복
for _ in range(K):
    move()
    chk()

#남아있는 fireball 질량의 합
ans = 0
for i in range(N):
    for j in range(N):
        ans += sum(m[0] for m in board[i][j])
        
print(ans)