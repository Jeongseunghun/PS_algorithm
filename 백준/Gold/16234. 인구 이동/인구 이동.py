from collections import deque

N,L,R = list(map(int,input().split()))
A = [list(map(int,input().split())) for _ in range(N)]

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#국경선 열기
def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    #열린 나라 좌표
    friend = []
    friend.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                if L <= abs(A[nx][ny] - A[x][y]) <= R:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    friend.append((nx,ny))
                    
    return friend
                    
d = 0
while True:
    flag = 0
    #방문여부
    visited = [[0 for _ in range(N)] for _ in range(N)]
    #모든 국경선 열기
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                c = bfs(i,j)
                #인구이동
                if len(c)>1:
                    flag = 1
                    val = sum([A[x][y] for x,y in c]) // len(c)
                    for x,y in c:
                        A[x][y] = val
    if flag == 0:
        break
    d+=1

print(d)