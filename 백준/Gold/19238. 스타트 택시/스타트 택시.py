from collections import deque

N,M,Oil = map(int,input().split())
boundary = [list(map(int,input().split())) for _ in range(N)]
tx,ty = map(int,input().split())
tx-=1
ty-=1
#출발 정보
s_board = []
#도착 정보
e_board = []
for i in range(M):
    sx,sy,ex,ey = map(int,input().split())
    #승객 번호,x좌표,y좌표
    s_board.append([sx-1,sy-1])
    e_board.append([ex-1,ey-1])
    
#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#
def shortest_find(tx,ty):
    q = deque()
    q.append((tx,ty))
    visited =[[0 for _ in range(N)] for _ in range(N)]
    mindis = 1e9
    candi = []
    while q:
        x, y = q.popleft()
        if visited[x][y] > mindis:
            break
        if [x,y] in s_board:
            mindis = visited[x][y]
            candi.append((x,y))
            
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and boundary[nx][ny] != 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    
    if candi:
        candi.sort()
        return visited[candi[0][0]][candi[0][1]], candi[0][0], candi[0][1]
    else:
        return -1,-1,-1

#목적지 거리구하기
def bfs(start,end):
    global x,y
    q = deque()
    q.append(start)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    while q:
        x,y = q.popleft()
        #도착지에 도착하면
        if [x,y] == end:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                #벽이 아니고 방문한적 없으면
                if boundary[nx][ny] != 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    return visited[x][y],x,y

for _ in range(M):
    dis,x,y = shortest_find(tx,ty)
    if dis == -1 or Oil - dis < 0:
        Oil = -1
        break
    Oil -= dis
    idx = s_board.index([x,y])
    s_board[idx] = [-1,-1]
    dis2,x2,y2 = bfs([x,y],e_board[idx])
    if [x2,y2] != e_board[idx] or Oil - dis2 < 0:
        Oil = -1
        break
    
    Oil += dis2
    tx,ty = x2,y2
    

print(Oil)
