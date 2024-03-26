from collections import deque
import heapq

dx = [0,0,-1,1]
dy = [-1,1,0,0]
inf = 1e9

def dijkstra():
    h = []
    heapq.heappush(h, (board[0][0], 0, 0))
    board[0][0] = 0
    while h:
        c,x,y = heapq.heappop(h)
        if x == N-1 and y == N-1:
            print("Problem {}: {}".format(cnt,visited[N-1][N-1]))
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                nc = c+board[nx][ny]
                if visited[nx][ny] > nc:
                    visited[nx][ny] = nc
                    heapq.heappush(h,(nc,nx,ny))
cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    board = [list(map(int,input().split())) for _ in range(N)]
    visited = [[inf for _ in range(N)] for _ in range(N)]
    dijkstra()
    cnt+=1