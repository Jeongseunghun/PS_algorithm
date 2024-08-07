from itertools import combinations

N,M = map(int,input().split())
graph = [[1e9] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(N+1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
node = [i for i in range(1,N+1)]
c = list(combinations(node,2))

res = [1e9, 1, 2]

for i in c:
    a,b = i
    tmp = 0
    for j in node:
        tmp += min(graph[j][a],graph[j][b])
    if res > [tmp,a,b]:
        res = [tmp,a,b]
    
print(res[1],res[2],res[0]*2)
