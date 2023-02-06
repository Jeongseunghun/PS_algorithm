N,M = map(int,input().split())

import sys
from collections import deque
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
shark_list = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def bfs(x, y):
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque([(x, y, 0)])
    visited[x][y] = True
    dx = [-1, -1, -1, 0, 1, 0, 1, 1]
    dy = [-1, 0, 1, 1, 1, -1, 0, -1]
    while q:
        x, y, distance = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if shark_list[nx][ny] == 0:
                    q.append((nx, ny, distance+1))
                    visited[nx][ny] = True
                else:
                    return distance+1
for i in range(n):
    for j in range(m):
        if shark_list[i][j] == 0:
            ans = max(ans, bfs(i, j))

print(ans)