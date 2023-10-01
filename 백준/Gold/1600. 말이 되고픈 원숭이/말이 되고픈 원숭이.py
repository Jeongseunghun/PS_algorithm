from collections import deque

K = int(input())
W,H = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(H)]


hdx = [-1,-2,-2,-1,1,2,2,1]
hdy = [-2,-1,1,2,-2,-1,1,2]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    #y,x,말의 움직임
    visited = [[[0] * (K+1) for _ in range(W)] for _ in range(H)]
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    while q:
        x,y,z = q.popleft()
        
        if x == H-1 and y == W-1:
            return visited[x][y][z] -1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #범위 내, 방문 X, 장애물 X
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][z] and not board[nx][ny]:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx,ny,z))
        
        if z < K:
            for i in range(8):
                hx = x + hdx[i]
                hy = y + hdy[i]
                if 0 <= hx < H and 0 <= hy < W and not visited[hx][hy][z+1] and not board[hx][hy]:
                    visited[hx][hy][z+1] = visited[x][y][z] + 1
                    q.append((hx,hy,z+1))
    
    return -1

print(bfs())
            