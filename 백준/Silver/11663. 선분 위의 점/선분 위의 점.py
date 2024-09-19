N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
for _ in range(M):
    s,e = map(int,input().split())

    scnt = 0
    ecnt = 0
    
    l,r = 0,N-1
    while l <= r:
        mid = (l+r) // 2
        if lst[mid] >= s:
            r = mid-1
        else:
            l = mid+1
    scnt = r + 1
    l,r = 0,N-1
    while l <= r:
        mid = (l+r) // 2
        if lst[mid] <= e:
            l = mid+1
        else:
            r = mid-1
    ecnt = r

    print(ecnt-scnt+1)