def dfs(lst,K,tmp,idx):
    if len(tmp) == 6:
        print(*tmp)
        return
    for i in range(idx,K):
        tmp.append(S[i])
        dfs(lst,K,tmp,i+1)
        tmp.pop()

while True:
    lst = list(map(int,input().split()))
    K = lst[0]
    S = lst[1:]
    if K == 0:
        break
    tmp = []
    dfs(S,K,tmp,0)
    print()