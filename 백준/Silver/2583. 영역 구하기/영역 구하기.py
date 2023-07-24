from collections import deque
M,N,K = map(int,input().split())

paper = [[0] * N for _ in range(M)]

#칠하기
for i in range(K):
    sx,sy,ex,ey = map(int,input().split())
    for i in range(sx,ex):
        for j in range(M-sy-1,M-ey-1,-1):
            paper[j][i] = 1
    
    
#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
    cnt = 1
    q = deque()
    q.append((x,y))
    paper[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N:
                if paper[nx][ny] == 0:
                    paper[nx][ny] = 1
                    q.append((nx,ny))
                    cnt+=1
    tmp.append(cnt)
    
tmp = []
for i in range(M):
    for j in range(N):
        if paper[i][j] == 0:
            bfs(i,j)

tmp.sort()
print(len(tmp))
for i in tmp:
    print(i,end = " ")


