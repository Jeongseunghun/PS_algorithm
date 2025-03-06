from collections import deque

def solution(maps):    
    def bfs(s,e):
        for i in range(N):
            for j in range(M):
                #시작 좌표
                if maps[i][j] == s:
                    sx,sy = i,j
                #도착 좌표
                if maps[i][j] == e:
                    ex,ey = i,j
        
        q = deque()
        q.append((sx,sy,0))
        visited = [[0 for _ in range(M)] for _ in range(N)]
        visited[sx][sy] = 1
        while q:
            x,y,ans = q.popleft()
            if x == ex and y == ey:
                return ans
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]   
                if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1         
                    q.append((nx,ny,ans+1))
        
        return -1
                
    N = len(maps)
    M = len(maps[0])
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    stol = bfs('S','L')
    ltoe = bfs('L','E')
    
    if stol == -1 or ltoe == -1:
        return -1
    
    return stol+ltoe