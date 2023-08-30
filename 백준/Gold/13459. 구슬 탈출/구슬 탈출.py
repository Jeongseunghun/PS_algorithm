from collections import deque

N,M = map(int,input().split())
board = [list(input()) for _ in range(N)]

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#끝까지 이동
def move(x,y,dx,dy):
    cnt = 0
    while board[x+dx][y+dy] != "#" and board[x][y] != 'O': 
        x+=dx
        y+=dy
        cnt+=1
    return x,y,cnt
    

def bfs(rx,ry,bx,by,depth):
    q = deque()
    visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    q.append((rx,ry,bx,by,depth))
    visited[rx][ry][bx][by] = True
    while q:
        rx,ry,bx,by,depth = q.popleft()
        if depth > 10:
            break
        for i in range(4):
            nrx,nry,rcnt = move(rx,ry,dx[i],dy[i])
            nbx,nby,bcnt = move(bx,by,dx[i],dy[i])
            #파란 구슬 O 아닐 때
            if board[nbx][nby] != 'O':
                #빨간 구슬 O면 종료
                if board[nrx][nry] == 'O':
                    print(1)
                    return
                #구슬 겹치면
                if nrx == nbx and nry == nby:
                    #빨간 구슬이 더 이동했으면
                    if rcnt>bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx,nry,nbx,nby,depth+1))    
    
    print(0)

rx,ry,bx,by = 0,0,0,0
for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            rx,ry = i,j
        if board[i][j] == "B":
            bx,by = i,j

bfs(rx,ry,bx,by,1)