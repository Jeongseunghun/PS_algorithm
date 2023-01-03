from collections import deque

N,M,V = map(int,input().split())
visited = [False] * (N+1)

node = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)


def dfs(v):
    print(v,end =" ")
    visited[v] = True
    for i in node[v]:
        if visited[i] == False:
            dfs(i)
            

def bfs(v):
    visited[v] = True
    q=deque([v])
    while q:
        res = q.popleft()
        print(res,end = " ")
        for i in node[res]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True        

for i in range(len(node)):
     node[i].sort()
     
     
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)


    