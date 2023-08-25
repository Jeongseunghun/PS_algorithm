N,M = map(int,input().split())

lst = []
def dfs(cnt):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(cnt,N+1):
        lst.append(i)
        dfs(i)
        lst.pop()
            
dfs(1)