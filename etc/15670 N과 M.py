N,M = map(int, input().split())

res = []

def dfs(_k):
    if len(res) == M:
        print(''.join(map(str,res)))
        return
    
    for i in range(_k,N+1):
        if i not in res:
            res.append(i)
            dfs(i+1)
            res.pop()

dfs(1)
        