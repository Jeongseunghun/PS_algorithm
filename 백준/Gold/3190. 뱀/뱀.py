from collections import deque

N = int(input())
K = int(input())
apple = [[0]*N for _ in range(N)]
for i in range(K):
    a,b= map(int,input().split())
    apple[a-1][b-1] = 1
    
L = int(input())
trans = []
for i in range(L):
    c,d = map(str,input().split())
    trans.append((int(c),d))

#
dx=[0,1,0,-1]
dy=[1,0,-1,0]
nd,nx,ny = 0,0,0
time,i=0,0

q= deque()
q.append((nx,ny))
while True:
    nx = nx + dx[nd]
    ny = ny + dy[nd]
    time+= 1
    if nx<0 or nx>= N or ny<0 or ny>= N or (nx,ny) in q:
        break
    q.append((nx,ny))
    if apple[nx][ny] == 0:
        q.popleft()
    else:
        apple[nx][ny] = 0
    
    if time == trans[i][0]:
        if trans[i][1]== "L":
            nd = (nd-1) % 4
        else:
            nd = (nd+1) % 4
        if i +1 < len(trans):
            i+=1
    
print(time)
        
    