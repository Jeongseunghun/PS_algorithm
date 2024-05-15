from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    q = deque()
    q.append((coins[0],coins[1],coins[2],coins[3],0))
    while q:
        x1,y1,x2,y2,cnt = q.popleft()
        if cnt >= 10:
            return -1
        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            if 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M:
                if board[nx1][ny1] == "#":
                    nx1,ny1 = x1,y1
                if board[nx2][ny2] == "#":
                    nx2,ny2 = x2,y2
                q.append((nx1,ny1,nx2,ny2,cnt+1))
                continue
            elif 0 <= nx1 < N and 0 <= ny1 < M:
                return cnt+1
            elif 0 <= nx2 < N and 0 <= ny2 < M:
                return cnt+1
            else:
                continue
 
                
N, M = map(int,input().split())
board = [list(input()) for _ in range(N)]

coins = []

for i in range(N):
    for j in range(M):
        if board[i][j] == "o":
            coins.append(i)
            coins.append(j)

cnt = bfs()
print(cnt)