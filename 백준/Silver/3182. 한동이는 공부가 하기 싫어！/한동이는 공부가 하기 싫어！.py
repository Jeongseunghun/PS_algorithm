def dfs(i,visited):
    visited[i] = 1
    for j in lst[i]:
        if visited[j] == 0:
            dfs(j,visited)

N = int(input())

lst = [[] for _ in range(N+1)]

for i in range(1,N+1):
    s = int(input())
    lst[i].append(s)

ans = 0
num = 0
for i in range(1,N):
    visited = [0 for _ in range(N+1)]
    visited[i] = 1
    dfs(i,visited)
    if ans < sum(visited):
        ans = sum(visited)
        num = i

print(num)