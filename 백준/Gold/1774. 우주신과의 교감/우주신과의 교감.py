from itertools import combinations
import math

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    A = find(a)
    B = find(b)
    if A > B:
        parents[A] = B
    elif A < B:
        parents[B] = A
        
def kruskal(edges):
    edges.sort(key = lambda x : x[2])
    ans = 0
    for edge in edges:
        u,v,w = edge
        if find(u) != find(v) :
            union(u,v)
            ans += w
    return ans

N,M = map(int,input().split())
lst = []
parents = [i for i in range(N+1)]
for i in range(1,N+1):
    x,y = map(int,input().split())
    lst.append([x,y,i])
    
for _ in range(M):
    x,y = map(int,input().split())
    union(x,y)

edges = []
for x,y in combinations(lst,2):
    edges.append((x[2],y[2],math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)))

ans = kruskal(edges)

print(f"{ans:.2f}")