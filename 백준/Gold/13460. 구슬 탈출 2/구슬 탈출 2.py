from collections import deque

N,M = map(int,input().split())
board = [list(input()) for _ in range(N)]
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def move(x,y,dx,dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x+=dx
        y+=dy
        cnt+=1
    
    return x,y,cnt

def bfs():
    while q:
        rx,ry,bx,by,depth = q.popleft()
        if depth > 10:
            break
        for i in range(4):
            nrx,nry,rcnt = move(rx,ry,dx[i],dy[i])
            nbx,nby,bcnt = move(bx,by,dx[i],dy[i])
            if board[nbx][nby] != 'O':
                if board[nrx][nry] == 'O':
                    print(depth)
                    return
                #구슬이 겹치면
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                #방문 체크
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx,nry,nbx,nby,depth+1))
    
    print(-1)    

q = deque()
rx,ry,bx,by = 0,0,0,0
for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            rx,ry = i,j
        if board[i][j] == "B":
            bx,by = i,j
#빨간 구슬과 파란 구슬 위치 정보, depth
q.append((rx,ry,bx,by,1))
visited[rx][ry][bx][by] = True
bfs()