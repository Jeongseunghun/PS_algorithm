import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N,M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(x):
    visited[x]=True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)  
            


for i in range(1, N+1):
    if not visited[i]:
        dfs(i)        
        cnt +=1

            
print(cnt)
    
    