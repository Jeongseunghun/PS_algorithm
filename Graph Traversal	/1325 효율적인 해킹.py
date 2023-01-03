from collections import deque
import sys
input = sys.stdin.readline


N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]

res = []  

def bfs(v):
    q=deque([v])
    visited = [False] * (N+1)
    cnt = 1
    visited[v]=True
    while q:
        x=q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt+=1
    return cnt


for _ in range(M):
    a,b = map(int,input().split())
    graph[b].append(a)

 
for i in range(1,N+1):
    res.append(bfs(i)) 
    
ans = max(res)

        
for i in range(len(res)):
    if ans == res[i]:
        print(i+1,end = " ")