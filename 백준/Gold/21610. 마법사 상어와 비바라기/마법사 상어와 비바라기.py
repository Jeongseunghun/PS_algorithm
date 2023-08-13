from collections import deque

N, M = map(int,input().split())
#바구니에 저장된 물 격자
board = [list(map(int,input().split())) for _ in range(N)]
command = [list(map(int,input().split())) for _ in range(M)]

#비구름 위치 저장
cloud = [[0 for _ in range(N)] for _ in range(N)]

        
#초기 비구름
cloud[N-1][0],cloud[N-1][1],cloud[N-2][0],cloud[N-2][1] = 1,1,1,1

#좌 좌상 상 우상 우 우하 하 좌하
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

#물복사버그
def watercopy(board,tmp,cloud,m_q):
    
    while m_q:
        x,y = m_q.popleft()
        cnt = 0
        for i in range(1,5):
            nx = x + dx[2*i-1]
            ny = y + dy[2*i-1]
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny] >= 1:
                    cnt += 1
        board[x][y] += cnt

    for i in range(N):
        for j in range(N):
            if board[i][j] >=2:
                if (i,j) not in tmp:
                    cloud[i][j] = 1
                    board[i][j] -= 2
    return cloud
                        

#비바라기
def rain(cloud,d,s):
    global board
    
    #현재 비구름 좌표
    q = []
    for i in range(N):
        for j in range(N):
            if cloud[i][j] == 1:
                q.append((i,j))
    #이동한 비구름 좌표(=물 증가한 비구름 좌표)
    m_q = deque()
    
    #이동한 비구름 좌표 저장
    tmp = []
    #비구름 이동
    for x,y in q:
        nx = (x + dx[d-1] * s) % N
        ny = (y + dy[d-1] * s) % N
        #물의 양 1 증가
        board[nx][ny] += 1
        m_q.append((nx,ny))
        tmp.append((nx,ny))
    
    #비구름 초기화(모두 사라짐)
    cloud = [[0 for _ in range(N)] for _ in range(N)]
    
    #물복사버그 시전
    cloud = watercopy(board,tmp,cloud,m_q)

    return cloud


for d,s in command:
    cloud = rain(cloud,d,s)
    # print("board:",board)
    # print("cloud:",cloud)
    

#바구니에 들어있는 물 합 구하기
ans = 0   
for i in range(N):
    for j in range(N):
        ans += board[i][j]
print(ans)    
