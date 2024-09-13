N,M = map(int,input().split())
lst = [int(input()) for _ in range(M)]
ans = 0
s = 1
e = max(lst)
while s<=e:
    mid = (s+e) // 2
    cnt = 0 
    for i in range(len(lst)):
        if lst[i] % mid != 0:
            cnt+= 1
        cnt+= lst[i] // mid
    if cnt <= N:
        e = mid-1
        ans= mid
    else:
        s = mid+1
 

print(ans)