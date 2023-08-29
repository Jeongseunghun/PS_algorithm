N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
ans = []
def dfs(cnt):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(N):
        ans.append(lst[i])
        dfs(cnt+1)
        ans.pop()

dfs(0)