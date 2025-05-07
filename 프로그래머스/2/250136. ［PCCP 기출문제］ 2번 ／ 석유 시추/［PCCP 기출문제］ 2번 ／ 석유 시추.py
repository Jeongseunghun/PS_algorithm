from collections import deque

def solution(land):
    answer = 0
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    def bfs(i,j,visited):
        q = deque()
        q.append((i,j))
        visited[i][j] = 1
        y_lst = set()
        y_lst.add(j)
        oil = 1
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    y_lst.add(ny)
                    oil += 1
        return [y_lst,oil],visited
    
    N = len(land)
    M = len(land[0])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    
    col_sum = [0 for _ in range(M)]
    
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and land[i][j] == 1:
                lst,visited = bfs(i,j,visited)
                for x in lst[0]:
                    col_sum[x] += lst[1]
    
    return max(col_sum)