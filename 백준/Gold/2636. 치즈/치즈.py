from collections import deque

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

group_cz = []
def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    cnt = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if board[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                elif board[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    cnt+=1
    
    group_cz.append(cnt)
    return cnt
                    
                                    
ans = 0
while True:

    visited = [[0 for _ in range(M)] for _ in range(N)]
    cnt = bfs()
            
    for i in range(N):
        for j in range(M):
            if visited[i][j] > 1:
                board[i][j] = 0
    ans += 1

    if cnt == 0:
        break

print(ans-1)
print(group_cz[-2])