import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n,m = map(int,input().split())

parent = [i for i in range(n+1)]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

for _ in range(m):
    command,a,b = map(int,input().split())
    if command == 0:
        union(a,b)
    else:
        A = find(a)
        B = find(b)
        if A==B:
            print('YES')
        else:
            print('NO')