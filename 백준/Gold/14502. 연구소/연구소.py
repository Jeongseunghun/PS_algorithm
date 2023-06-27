from collections import deque
import copy
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
RS = [ list(map(int,input().split())) for _ in range(N) ]

visited= [[0 for _ in range(M)] for _ in range(N)]

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs():
    q = deque()
    tmp_RS = copy.deepcopy(RS)
    
    #큐에 바이러스 위치 넣기
    for i in range(N):
        for j in range(M):
            if tmp_RS[i][j] == 2:
                q.append((i,j))
    
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<N and 0<=ny<M:
                if tmp_RS[nx][ny] == 0:
                    tmp_RS[nx][ny] = 2
                    q.append((nx,ny))
                    
    global answer
    cnt = 0
    
    for i in range(N):
        cnt+=tmp_RS[i].count(0)
    
    answer = max(cnt,answer)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if RS[i][j] == 0:
                RS[i][j] = 1
                wall(cnt+1)
                RS[i][j] = 0
                

            
answer = 0
wall(0)
print(answer)      
        
