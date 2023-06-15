from collections import deque

#방향
dx = [-2,-1,1,2,-2,-1,1,2]
dy = [1,2,2,1,-1,-2,-2,-1]


T = int(input())

for _ in range(T):
    l = int(input())
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    
    visited = [[0 for _ in range(l)] for _ in range(l)]
    visited[a][b] = 1
    
    def bfs(a,b,c,d):
        q = deque()
        q.append((a,b))
        while q:
            x,y = q.popleft()
            if x == c and y == d:
                print(visited[x][y] - 1)
                return
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 > nx or 0 > ny or nx >= l or ny >= l:
                    continue
                if visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
        return False
    bfs(a,b,c,d)