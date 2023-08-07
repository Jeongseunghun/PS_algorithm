from collections import deque

N,L,R = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#국경선 조건 확인하고 여는 함수
def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    
    #국경선 공유한 나라 좌표 저장
    country = []
    country.append((x,y))
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(A[nx][ny]-A[x][y]) <= R:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    country.append((nx,ny))
    
    return country
    

ans = 0
#국경선 열고 인구 이동 반복하기
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                c = bfs(i,j)
                #국경선 공유한 나라가 있을 때
                if len(c) > 1:
                    flag = 1
                    val = sum([A[x][y] for x,y in c]) // len(c)
                    for a,b in c:
                        A[a][b] = val
    if flag == 0:
        break
    ans+=1

print(ans)