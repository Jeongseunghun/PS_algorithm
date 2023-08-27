N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
lst = []
def dfs(cnt):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(cnt,len(num)):
        if num[i] not in lst:
            lst.append(num[i])
            dfs(i)
            lst.pop()

dfs(0)