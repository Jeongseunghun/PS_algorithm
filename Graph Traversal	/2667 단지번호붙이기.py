from collections import deque

N= int(input())
loc = [list(map(int,input())) for _ in range(N)]



def bfs(loc,x,y):
    #상하좌우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q= deque()
    q.append((x,y))
    loc[x][y] = 0
    cnt=1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0> nx or nx >= N or 0 > ny or ny >= N:
                continue
                
            if loc[nx][ny] == 1:
                loc[nx][ny] = 0
                q.append((nx,ny))
                cnt+=1
    return cnt


count = [bfs(loc,i,j) for i in range(N) for j in range(N) if loc[i][j] == 1]
count.sort()
print(len(count))

for i in count:
    print(i)
                
    
