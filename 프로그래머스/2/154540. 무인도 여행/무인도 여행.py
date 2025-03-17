from collections import deque

def solution(maps):
    def bfs(i,j,visited):
        q = deque()
        q.append((i,j))
        tmp = [[0 for _ in range(M)] for _ in range(N)]
        
        tmp[i][j] = 1
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and maps[nx][ny] !='X':
                    tmp[nx][ny] = 1
                    q.append((nx,ny))
                    visited[nx][ny] = 1
        
        cnt = 0
        
        for i in range(N):
            for j in range(M):
                if tmp[i][j] == 1:
                    visited[i][j] = 1
                    cnt+=int(maps[i][j])
        return cnt, visited
    
    answer = []
    
    N = len(maps)
    M = len(maps[0])
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    visited = [[0 for _ in range(M)] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                cnt, visited = bfs(i,j,visited)
                answer.append(cnt)
    
    answer.sort()
    
    if not answer:
        return [-1]
    
    return answer