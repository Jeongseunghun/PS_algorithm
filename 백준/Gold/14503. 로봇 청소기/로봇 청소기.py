N,M = map(int,input().split())
r,c,d = map(int,input().split())
loc = [list(map(int,input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

#청소한 칸
cnt = 1

#북0 동1 남2 서3
dx=[-1,0,1,0]
dy=[0,1,0,-1]

visited[r][c] = 1

while True:
    flag = 0
    for i in range(4):
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        d = (d+3) % 4
        if 0 <= nx < N and 0 <= ny < M and loc[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt+=1
                r = nx
                c = ny
                flag = 1
                break
    if flag == 0:
        if loc[r-dx[d]][c-dy[d]] == 1:
            print(cnt)
            break
        else:
            r,c = r-dx[d],c-dy[d]
        
    
    
    

