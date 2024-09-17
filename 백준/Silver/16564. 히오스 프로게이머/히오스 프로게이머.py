def chk(mid):
    t = 0
    for i in lst:
        if i < mid:
            t += mid - i
        else:
            break
    return t

N, K = map(int,input().split())
lst = [int(input()) for _ in range(N)]

lst.sort()

s = lst[0]
e = lst[-1] + K
while s <= e:
    mid = (s+e) // 2
    tmp = chk(mid)
    
    if tmp <= K:
        s = mid+1
    else:
        e = mid-1

print(e)
        
    
    