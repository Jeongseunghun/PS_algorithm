from collections import deque

t = int(input())

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]      
            
def bfs(x,y):
    q.append((x,y))
    visited[x][y] = 1
    while q:
        qlen = len(q)
        while qlen:
            x,y = q.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<h and 0<=ny<w:
                    if maze[nx][ny] == '.' and visited[nx][ny] == 0:
                        visited[nx][ny]=visited[x][y] + 1
                        q.append((nx,ny))
                elif 0>nx or nx>=h or ny<0 or ny>=w:
                    print(visited[x][y])
                    return
            qlen -= 1
        spread()
    print("IMPOSSIBLE")
    return

#fire
def spread():
    qlen= len(fq)
    while qlen:
        x,y = fq.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<h and 0<=ny<w:
                if maze[nx][ny] == '.':
                    fq.append((nx,ny))
                    maze[nx][ny] = '*'  
        qlen -=1
                        
                        


for _ in range(t):
    w,h = map(int,input().split())
    maze = [list(map(str,input())) for _ in range(h)]
    fq,q= deque(),deque()
    visited=[[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if maze[i][j] == '@':
                a,b = i,j
                maze[i][j] = '.'
            if maze[i][j] == '*':
                fq.append((i,j))
    
    spread()
    bfs(a,b)
    
    
    
    