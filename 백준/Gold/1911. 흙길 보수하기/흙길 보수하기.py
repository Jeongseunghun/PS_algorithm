N,L = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
lst = sorted(lst,key = lambda x : (x[0],x[1]))

ans = 0
start = lst[0][0]

for x,y in lst:
    if x > start:
        start = x

    if (y-start) % L == 0:
        ans += (y-start) // L
        start = y
    else:
        ans += (y-start) // L + 1
        start = y + (L-(y-start)% L)
    

print(ans)
    