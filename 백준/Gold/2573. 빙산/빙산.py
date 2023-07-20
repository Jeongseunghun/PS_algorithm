from collections import deque
import copy

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]


year = 0

def melt():
    q = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:    
                q.append((i,j))
    tmp = copy.deepcopy(graph)
    while q:
        cnt = 0
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if tmp[nx][ny] == 0:
                    cnt+=1
        if graph[x][y] - cnt >=0:
            graph[x][y] -= cnt
        elif graph[x][y] - cnt < 0:
            graph[x][y] = 0
        
    global year                                 
    year+=1
 

def ice(graph,x,y):
    ice_cnt = 0
    q = deque()
    q.append((x,y))        
    while q:
        x,y = q.popleft()
        visited[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] != 0:
                visited[nx][ny] = 0
                q.append((nx,ny))
                ice_cnt += 1
    return ice_cnt

while True:
    melt()
    visited = copy.deepcopy(graph)
    count = [ice(graph,i,j) for i in range(N) for j in range(M) if visited[i][j] != 0]
    if len(count) >= 2:
        print(year)
        exit(0)
    total = 0
    for i in range(N):
        total+=sum(graph[i])
    if total == 0:
        print(0)
        exit(0)
    

        


                
                
                
    





