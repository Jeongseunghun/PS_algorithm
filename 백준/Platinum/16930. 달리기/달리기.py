from collections import deque

N,M,K = map(int,input().split())
gym = [list(input()) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

x1,y1,x2,y2 = map(int,input().split())

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    q.append((x1-1,y1-1))
    visited[x1-1][y1-1] = 0
    while q:
        x,y = q.popleft()
        if x == x2-1 and y == y2-1:
            return print(visited[x][y])
        for i in range(4):
            for j in range(1,K+1):
                nx = x + dx[i] * j
                ny = y + dy[i] * j
                if 0 > nx or nx>=N or 0 > ny or ny >= M:
                    break
                if gym[nx][ny] == "#":
                    break
                if visited[nx][ny] == -1:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
                elif visited[nx][ny] == visited[x][y] + 1:
                    continue
                else:
                    break
    return print(-1)

bfs()
            
