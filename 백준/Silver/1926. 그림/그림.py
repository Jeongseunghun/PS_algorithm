from collections import deque

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(a,b):
    q = deque()
    q.append((a,b))
    board[a][b] = 0
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    cnt +=1
                    q.append((nx,ny))
    return cnt               
                

count = [ bfs(i,j) for i in range(n) for j in range(m) if board[i][j] == 1]

print(len(count))
if len(count) >=1 :
    print(max(count))
else:
    print(0)
