H,W = map(int,input().split())
lst = list(map(int,input().split()))
res = 0

for i in range(1,W-1):
    start = max(lst[:i])
    end = max(lst[i+1:])
    
    short = min(start,end)
    
    if lst[i] < short:
        res += short - lst[i]

print(res)
        
            