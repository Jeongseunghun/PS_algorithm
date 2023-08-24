N,M = map(int,input().split())

lst = []

def dfs(cnt):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(cnt,N+1):
        if i not in lst:
            lst.append(i)
            dfs(i+1)
            lst.pop()
dfs(1)