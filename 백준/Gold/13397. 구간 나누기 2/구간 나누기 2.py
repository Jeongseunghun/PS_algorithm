def chk(mid):
    global ans
    cnt = 1
    nmin = 10000
    nmax = 0
    for i in range(N):
        nmin = min(nmin,lst[i])
        nmax = max(nmax,lst[i])
    
        if nmax-nmin > mid:
            cnt += 1
            nmin = nmax = lst[i]
    
    return M >= cnt
        
N,M = map(int,input().split())
lst = list(map(int,input().split()))
ans = 10000
s = 0
l = max(lst)

while s <= l:
    mid = (s+l) // 2
    
    if chk(mid):
        l = mid - 1
        ans = min(ans,mid)
    else:
        s = mid + 1

print(ans)
    