import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())

tree = [[] for _ in range(N+1)]

for i in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

par = [0] * (N+1)

def dfs(v):
    for i in tree[v]:
        if par[i] == 0:
            par[i] = v
            dfs(i)

dfs(1)
for i in range(2,N+1):
    print(par[i])
        



    