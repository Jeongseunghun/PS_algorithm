# import sys
# input = sys.stdin.readline

# N=int(input())
# M=int(input())

# graph = [[] for _ in range(N+1)]
# for _ in range(m):
#     x,y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)

# visited = [0] * (n+1)

# def dfs(graph, v, visited):
#     visited[v] = 1
#     for i in graph[v]:
#         if visited[i] == 0:
#             dfs(graph, i, visited)
#         return True
# dfs(graph, 1, visited)
# print(sum(visited)-1)

import sys
input=sys.stdin.readline

N = int(input())
link = int(input())

l= [[] for _ in range(N+1)]

for _ in range(link):
    x,y=map(int,input().split())
    l[x].append(y)
    l[y].append(x)

visited = [False] * (N+1)

def dfs(v):
    visited[v]=True
    for i in l[v]:
        if not visited[i]:
            dfs(i)
dfs(1)
print(sum(visited)-1)
    

    
