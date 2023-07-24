from collections import deque

M,N,K = map(int,input().split())
dist = [list(map(int,input().split())) for _ in range(K)]

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

paper = [[0 for _ in range(N)] for _ in range(M)]

for i in range(K):
    wid = dist[i][2]-dist[i][0]
    hei = dist[i][3]-dist[i][1]
    for k in range(dist[i][0],dist[i][0]+wid):
        for j in range(dist[i][1],dist[i][1]+hei):
            paper[j][k] = 1

            

tmp = []

def bfs(x,y):
    q = deque()
    q.append((x,y))
    paper[x][y] = 1
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N:
                if paper[nx][ny] == 0:
                    paper[nx][ny] = 1
                    q.append((nx,ny))
                    cnt += 1
        
    tmp.append(cnt)
    
for i in range(M):
    for j in range(N):
        if paper[i][j] == 0:
            bfs(i,j)

tmp.sort()     
print(len(tmp))
print(*tmp)