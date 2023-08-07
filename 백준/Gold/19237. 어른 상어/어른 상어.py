N,M,K = map(int,input().split())
#격자
board = [list(map(int,input().split())) for _ in range(N)]
#상어 방향
shark_d = list(map(int,input().split()))
#상어별 방향 우선순위
shark_prior = []
for i in range(M):
    tmp = []
    for j in range(4):
        tmp.append(list(map(int,input().split())))
    shark_prior.append(tmp)

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#[상어 번호 0, 향수 남은 시간 1], 방향
shark_info = [[[0,0] for _ in range(N)] for _ in range(N)]

#냄새 뿌리기
def smell():
    for i in range(N):
        for j in range(N):
            #냄새가 있으면
            if shark_info[i][j][1] > 0:
                shark_info[i][j][1] -= 1
            #상어가 존재하면
            if board[i][j] != 0:
                #상어번호 입력, 냄새 뿌리기
                shark_info[i][j] = [board[i][j], K]
                
#상어 이동
def move():
    new_d = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if board[x][y] != 0:
                d = shark_d[board[x][y] - 1]
                Flag = False
                for i in shark_prior[board[x][y] - 1][d - 1]:
                    nx = x + dx[i-1]
                    ny = y + dy[i-1]
                    if 0 <= nx < N and 0 <= ny < N:
                        #냄새 없으면
                        if shark_info[nx][ny][1] == 0:
                            shark_d[board[x][y] - 1] = i
                            #상어 옮기기
                            if new_d[nx][ny] == 0:
                                new_d[nx][ny] = board[x][y]
                            #상어 겹치면 작은 번호 상어
                            else:
                                new_d[nx][ny] = min(board[x][y],new_d[nx][ny])
                            Flag = True
                            break
                if Flag:
                    continue
                
                #주변에 냄새가 모두 있으면
                for i in shark_prior[board[x][y] - 1][d - 1]:
                    nx = x + dx[i-1]
                    ny = y + dy[i-1]
                    if 0 <= nx < N and 0 <= ny < N:
                        if shark_info[nx][ny][0] == board[x][y]:
                            shark_d[board[x][y] - 1] = i
                            new_d[nx][ny] = board[x][y]
                            break
    return new_d
                  
ans = 0 
while True:
    smell()
    new_d = move()
    board = new_d
    ans+=1
    
    chk = True
    for i in range(N):
        for j in range(N):
            if board[i][j] > 1:
                chk = False
    if chk:
        print(ans)
        break
    if ans>= 1000:
        print(-1)
        break
                          