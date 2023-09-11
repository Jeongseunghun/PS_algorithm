from collections import deque

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
#아기상어 초기 위치
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            sx,sy = i,j
#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    global sx,sy,shark_size
    q = deque()
    q.append((sx,sy))
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dis = [[0 for _ in range(N)] for _ in range(N)]
    lst = []
    while q:
        x,y = q.popleft()
        visited[x][y] = 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                #아기 상어 크기보다 물고기 크기가 작거나 같아야 이동 가능
                if board[nx][ny] <= shark_size and visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    dis[nx][ny] = dis[x][y] + 1
                    #상어 크기보다 작으면
                    if board[nx][ny] < shark_size and board[nx][ny] != 0:
                        lst.append([dis[nx][ny],nx,ny])
    lst.sort()
    return lst

def shark_move():
    global sx,sy,t,cnt
    dis = bfs()
    if not dis:
        print(t)
        exit()
    distance, x, y = dis[0]
    #상어 위치 갱신
    board[sx][sy] = 0
    sx,sy = x,y
    cnt+=1
    return distance

#시간
t = 0
#물고기 잡아먹은 횟수
cnt = 0
shark_size = 2
while True:
    t += shark_move()
    if cnt == shark_size:
        shark_size += 1
        cnt = 0
