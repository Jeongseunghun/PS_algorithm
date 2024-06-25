N, M = map(int,input().split())
lst = list(map(int,input().split()))

s = max(lst)
e = sum(lst)

ans = 0
while s <= e:
    mid = (s+e) // 2
    
    cnt = 1
    total = 0
    for i in lst:
        if total + i > mid:
            total = 0
            cnt +=1
        total+=i
    
    if cnt > M:
        s = mid+1
    else:
        e = mid-1
        ans = mid

print(ans)