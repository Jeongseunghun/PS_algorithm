from collections import deque

N,M = map(int,input().split())
loc = [list(map(int,input())) for _ in range(N)]

#벽 부순적 있으면 z=1, 없으면 z=0
visited = [[[0,0] for _ in range(M)] for _ in range(N)]

#상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    while q:
        x,y,z = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][z]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            
            #벽 부순적없고 벽밖에 없을 때
            if loc[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append((nx,ny,1))
                
            elif loc[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx,ny,z))
    
    return -1
            
print(bfs())