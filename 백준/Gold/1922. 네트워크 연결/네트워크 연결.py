def find(a):
    if a == parents[a]:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def union(a,b):
    A = find(a)
    B = find(b)
    if A < B:
        parents[B] = A
    elif A > B:
        parents[A] = B

N = int(input())
M = int(input())

parents = []
for i in range(N+1):
    parents.append(i)

edge = []
for i in range(M):
    a,b,c = map(int,input().split())
    edge.append((c,a,b))

edge.sort()

ans = 0
for c,a,b in edge:
    if find(a) != find(b):
       union(a,b)
       ans+=c

print(ans)