def dis(lst):
    ans = 0
    for i in range(4):
        if lst[0][i] != lst[1][i]:
            ans+=1
        if lst[0][i] != lst[2][i]:
            ans+=1
        if lst[1][i] != lst[2][i]:
            ans+=1
    return ans


T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(input().split())
    if N > 32:
        print(0)
    else:
        res = 12
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    res = min(res, dis([lst[i],lst[j],lst[k]]))
        
        print(res)
    