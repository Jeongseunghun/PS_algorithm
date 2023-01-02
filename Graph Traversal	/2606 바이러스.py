import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
e = int(input())

lst = [[] for _ in range(n+1)]
for i in range(e):
    a,b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

visited  = [False] * (n+1)

def dfs(v):
    visited[v] = True
    for i in lst[v]:
        if visited[i] == False:
            dfs(i)
dfs(1)
print(sum(visited)-1)
    