def find(v):
    if v == root[v]:
        return v
    root[v] = find(root[v])
    return root[v]

def union(a,b):
    r1 = find(a)
    r2 = find(b)
    
    if rank[r1] > rank[r2]:
        root[r2] = r1
    elif rank[r1] < rank[r2]:
        root[r1] = r2
    else:
        root[r2] = r1
        rank[r1] += 1
    
    return

n,m = map(int,input().split())
root = [i for i in range(n)]
rank = [0 for _ in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    if find(a) == find(b):
        print(i+1)
        exit()
    union(a,b)

print(0)
    
    