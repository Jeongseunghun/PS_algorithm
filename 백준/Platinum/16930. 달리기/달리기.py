from collections import deque

n,m,k=map(int,input().split())
dx,dy=[1,-1,0,0],[0,0,1,-1]
vis=[[-1]*m for _ in range(n)]
a=[list(input()) for _ in range(n)]
x1,y1,x2,y2=map(int,input().split())

q=deque()
q.append((x1-1,y1-1))
vis[x1-1][y1-1]=0
while q:
    y,x=q.popleft()
    if y==x2-1 and x==y2-1:
        print(vis[y][x])
        exit()
    for i in range(4):
        for num in range(1,k+1):
            xx=x+dx[i]*num
            yy=y+dy[i]*num
            if xx<0 or xx>=m or yy<0 or yy>=n: break
            if a[yy][xx]=='#':break
            if vis[yy][xx] == -1:
                q.append((yy,xx))
                vis[yy][xx]=vis[y][x]+1
            elif vis[yy][xx]==vis[y][x]+1: continue #일단 쭉 가본다
            else: break # 더 큰길은 탐색하지 않는다

print(-1)