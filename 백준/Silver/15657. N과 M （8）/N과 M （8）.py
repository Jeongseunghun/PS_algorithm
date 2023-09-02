N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

ans = []
def dfs(cnt):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(cnt,N):
        ans.append(lst[i])
        dfs(i)
        ans.pop()

dfs(0)
