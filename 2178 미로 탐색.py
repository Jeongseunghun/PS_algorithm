import sys
import collections
input = sys.stdin.readline

N,M = map(int,input().split())
maze = [list(map(int, ' '.join(input()).split())) for _ in range(N)]


dx=[-1,1,0,0]
dy=[0,0,-1,1]

Q= collections.deque([(0,0)])
result=0

while Q:
    x,y = Q.popleft()
    for i in range(4):
        nx,ny = x + dx[i], y +dy[i]
        if 0 <= nx < N and 0 <=ny <M:
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] +1
                Q.append((nx,ny))

print(maze[N-1][M-1])
