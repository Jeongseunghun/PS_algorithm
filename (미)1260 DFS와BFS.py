from collections import deque
from re import L
import sys
input = sys.stdin.readline

N,M,V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
     u,v = map(int,input().split())
     graph[u].append(v)
     graph[v].append(u)


def dfs(start):
     print(start,end=' ')
     visited[start] = True
     for i in graph[start]:
          if not visited[i]:
               dfs(i)
               visited[i] = True
     

def bfs(start):
     q=deque([start])
     visited[start]=True
     while q:
          now=q.popleft()
          print(now, end= ' ')
          for i in graph[now]:
               if not visited[i]:
                    q.append(i)
                    visited[i]=True

for i in range(len(graph)):
     graph[i].sort()
          

dfs(V)
visited = [False] * (N+1)
print()
bfs(V)
            




    
    
