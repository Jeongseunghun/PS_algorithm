N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
ans = []
def dfs():
    if len(ans) == M:
        print(*ans)
        return
    tmp = 0
    for i in range(N):
        if tmp != lst[i]:
            tmp = lst[i]
            ans.append(lst[i])
            dfs()
            ans.pop()

dfs()