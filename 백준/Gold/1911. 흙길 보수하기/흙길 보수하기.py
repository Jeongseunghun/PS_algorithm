N,L = map(int,input().split())
lst = []
for _ in range(N):
    s,e = map(int,input().split())
    lst.append([s,e])

lst = sorted(lst,key = lambda x : (x[0],x[1]))

l = lst[0][0]
ans = 0

for x,y in lst:
    if x > l:
        l = x
    tmp = y - l
    if tmp % L == 0:
        cnt = tmp // L
        l = y
    else:
        cnt = tmp // L + 1
        l = y + (L-tmp%L)
    
    ans += cnt

print(ans)
            
        
    
    
        