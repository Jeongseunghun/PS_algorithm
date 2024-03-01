from itertools import combinations
import math

n = int(input())

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    A = find(a)
    B = find(b)
    if A == B:
        return True
    elif A > B:
        parents[A] = B
    elif A < B:
        parents[B] = A

def kruskal(edges):
    edges.sort(key = lambda x : x[2])
    ans = 0
    for edge in edges:
        u,v,w = edge
        if find(u) != find(v):
            union(u,v)
            ans+=w
    return ans
    

edges = []
lst = []
parents = [i for i in range(n+1)]
for i in range(1,n+1):
    x,y = map(float,input().split())
    lst.append((i,x,y))

for x,y in combinations(lst,2):
    edges.append((x[0],y[0],math.sqrt((x[1]-y[1])**2 + (x[2]-y[2])**2)))

ans = kruskal(edges)


print(f"{ans:.2f}")