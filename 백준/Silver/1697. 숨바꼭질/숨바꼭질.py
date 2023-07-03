from collections import deque

N,K = map(int,input().split())

loc = [0] * (100001)

def bfs(N):
    q= deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            return loc[x]
        for nx in (x-1,x+1,2*x):
            if 0<=nx<=100000 and loc[nx] == 0:
                q.append(nx)
                loc[nx] = loc[x] + 1
        

print(bfs(N))
