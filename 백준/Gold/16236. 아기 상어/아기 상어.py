from collections import deque
N = int(input())

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
space = [list(map(int,input().split())) for _ in range(N)]

s_size = 2
s_eat = 0

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            space[i][j] = 0
            shark_x, shark_y = i, j


def bfs(sx,sy):
    global s_size
    q = deque()
    q.append([sx,sy])

    visited = [[False for _ in range(N)] for _ in range(N)]
    dis = [[0 for _ in range(N)] for _ in range(N)]
    can_eat_fish = []
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if space[nx][ny] <= s_size and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dis[nx][ny] = dis[x][y] + 1
                    q.append([nx,ny])
                    
                    if space[nx][ny] < s_size and space[nx][ny] != 0:
                        can_eat_fish.append([nx,ny,dis[nx][ny]])
    
    can_eat_fish.sort(key= lambda x : (x[2],x[0],x[1]))
    return can_eat_fish


#물고기 잡아먹는 누적 시간
ans = 0

while True:
    fishlst = bfs(shark_x,shark_y)
    #아무 것도 못먹으면 종료     
    if len(fishlst) == 0:
        print(ans)
        exit(0)
        
    shark_x,shark_y,move_time = fishlst[0]
    
    s_eat+=1
    
    #아기 상어 크기
    if s_size == s_eat:
        s_eat = 0
        s_size += 1
        
    space[shark_x][shark_y] = 0
    ans += move_time
    