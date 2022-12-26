from collections import deque
MAX= 10 ** 5

N,K = map(int,input().split())

def bfs(N,K):
    Q = deque([N])
    dist= [0] * (MAX + 1)
    
    while Q:
        cur = Q.popleft()
        if cur ==K:
            print(dist[cur])
            break
        
        for nx in (cur -1, cur +1 , cur *2):
            if 0<=nx <=MAX and not dist[nx]:
                dist[nx] = dist[cur] +1
                Q.append(nx)
                
bfs(N,K)