from collections import deque

N= int(input())
loc = [list(map(int,input())) for _ in range(N)]

home = []
cnt=0

def bfs():
    #상하좌우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q= deque([(0,0)])

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx < N and 0 <= ny < N:
                if loc[nx][ny] == 1:
                    loc[nx][ny] = loc[x][y] + 1
                    q.append((nx,ny))
    home.append(loc[nx-1][ny-1])    
    cnt+=1
            
print(cnt)
for i in home:
    print(i)
                
    
