N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

visited = [False] * N
ans = []
def dfs():
    if len(ans) == M:
        print(*ans)
        return
    tmp = 0
    for i in range(N):
        if visited[i] == False and tmp != lst[i]:
            visited[i] = True
            ans.append(lst[i])
            tmp = lst[i]
            dfs()
            visited[i] = False
            ans.pop()

dfs()