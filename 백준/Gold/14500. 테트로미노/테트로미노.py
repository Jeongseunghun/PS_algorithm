N,M = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(N)]

visited= [[0 for _ in range(M)] for _ in range(N)]

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y,L,total):
    global res
    if res >= total + m*(4-L):
        return
    if L == 4:
        res = max(res,total)
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
                if L == 2:
                    visited[nx][ny] = 1
                    dfs(x,y,L+1,total+paper[nx][ny])
                    visited[nx][ny] = 0
                visited[nx][ny] = 1
                dfs(nx,ny,L+1,total+paper[nx][ny])
                visited[nx][ny] = 0





m = max(map(max,paper))
res = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i,j,1,paper[i][j])
        visited[i][j] = 0

print(res)