def find(x):
    if x == parents[x]:
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

def kruskal(edge):
    ans = 0
    m = 0
    for c,a,b in edge:
        if find(a) != find(b):
            union(a,b)
            ans += c
            m = max(c,m)
    return ans,m

N,M = map(int,input().split())
parents = [i for i in range(N+1)]

edge = []
for i in range(M):
    a,b,c = map(int,input().split())
    edge.append((c,a,b))

edge.sort()

ans,m = kruskal(edge)

print(ans-m)