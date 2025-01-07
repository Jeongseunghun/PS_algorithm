from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    while q:
        x,y = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx,ny])
    
    return -1