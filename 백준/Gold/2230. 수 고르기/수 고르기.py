N,M = map(int,input().split())
lst = [int(input()) for _ in range(N)]
lst.sort()
s = 0
e = 0
ans = lst[-1] - lst[0]
while s <= e and e < N:
    if lst[e]-lst[s] < M:
        e += 1
    else:
        ans = min(ans,lst[e]-lst[s])
        s +=1
    
print(ans)