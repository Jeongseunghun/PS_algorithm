from collections import deque

N,M,V = map(int,input().split())
visited = [False] * (N+1)

node = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)


def dfs(v):
    visited[v] = True
    for i in node[v]:
        if visited[i] == False:
            print(i,end =" ")
            dfs(i)
            
print(V, end =" ")
dfs(V)
print()

# def bfs(v):
#     visited[v] = True
#     for i in node[v]:
#         if visited[i] == False:
#             bfs(v)

def bfs(start):
     visited = [False] * (N+1)
     q=deque([start])
     visited[start]=True
     while q:
          now=q.popleft()
          print(now, end= ' ')
          for i in node[now]:
               if not visited[i]:
                    q.append(i)
                    visited[i]=True
        
bfs(V)
    
    