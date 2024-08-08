import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
depth = [0 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
sum_depth = 0

def dfs_iterative(start):
    stack = deque([start])
    while stack:
        i = stack.pop()
        visited[i] = 1
        for j in graph[i]:
            if visited[j] == 0:
                depth[j] = depth[i] + 1
                stack.append(j)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dfs_iterative(1)

for i in range(2, N+1):
    if len(graph[i]) == 1:
        sum_depth += depth[i]

if sum_depth % 2 == 1:
    print('Yes')
else:
    print('No')