import sys
sys.setrecursionlimit(10**9)

N=int(input())
pa_node = [0] * (N+1)

def dfs(v):
    for i in tree[v]:
        if not pa_node[i]:
            pa_node[i]= v
            dfs(i)
            



tree = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
dfs(1)    

for i in range(2, N+1):
    print(pa_node[i])


    