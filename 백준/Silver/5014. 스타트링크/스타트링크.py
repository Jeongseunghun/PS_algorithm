from collections import deque

F,S,G,U,D = map(int,input().split())


dx = [U,-D]

def bfs(S,G):
    q = deque()
    ele=[-1]*(F+1)
    q.append(S)
    ele[S] = 0
    
    while q:
        x = q.popleft()
        
        if x == G:
            return ele[x]
        
        for i in range(2):
            nx = x+dx[i]
            if 0<nx<=F and ele[nx] == -1:
                q.append(nx)
                ele[nx] = ele[x] + 1
    return "use the stairs"

print(bfs(S,G))
                
