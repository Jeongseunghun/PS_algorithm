N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

tmp = []
def dfs():
    if len(tmp) == M:
        print(*tmp)
        return
    for i in lst:
        if i not in tmp:
            tmp.append(i)
            dfs()
            tmp.pop()

dfs()