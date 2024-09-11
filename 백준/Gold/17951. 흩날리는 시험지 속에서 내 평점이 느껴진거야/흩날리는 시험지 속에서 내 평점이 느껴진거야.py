N,K = map(int,input().split())
lst = list(map(int,input().split()))

s = 0
e = 10**6+2

ans = 0
while s<=e:
    mid = (s+e)//2
    
    res = 0
    cnt = 0
    for i in lst:
        res+=i
        if res>= mid:
            cnt += 1
            res = 0
    
    if cnt >= K:
        ans = mid
        s = mid+1
    else:
        e = mid-1

print(ans)
         
        