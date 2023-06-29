from collections import deque

while True:
    w,h= map(int,input().split())
    
    if w == 0 and h == 0:
        exit(0)
    
    land = []
    for i in range(h):
        land.append(list(map(int,input().split())))
        
        
    ans = 0
    
    #상하좌우좌상좌하우상우하
    dx=[-1,1,0,0,-1,1,-1,1]
    dy=[0,0,-1,1,-1,-1,1,1]
    
    def bfs(a,b):
        q = deque()
        q.append((a,b))
        cnt = 0
        while q:
            x,y = q.popleft()
            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or ny<0 or nx>=h or ny>=w or land[nx][ny] == 0:
                    continue
                if land[nx][ny] == 1:
                    land[nx][ny] = 0
                    q.append((nx,ny))
        cnt+=1
            
        return cnt
                
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1:
                ans+=bfs(i,j)
    
    print(ans)
                   
    
        