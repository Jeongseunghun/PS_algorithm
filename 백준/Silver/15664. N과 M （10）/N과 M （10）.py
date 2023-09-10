N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

ans = []
visited = [False] * N

def dfs(cnt):
    if len(ans) == M:
        print(*ans)
    tmp = 0
    for i in range(cnt,N):
        if visited[i] == False and tmp != lst[i]:
            ans.append(lst[i])
            visited[i] = True
            tmp = lst[i]
            dfs(i+1)
            ans.pop()
            visited[i] = False

dfs(0)