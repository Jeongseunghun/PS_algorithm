import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N = int(input())
parent = [i for i in range(N+1)]
for _ in range(N-2):
    a,b = map(int,input().split())
    union(a,b)

lst = []
for i in range(1,N+1):
    if i == parent[i]:
        lst.append(i)
        
print(*lst)
     

