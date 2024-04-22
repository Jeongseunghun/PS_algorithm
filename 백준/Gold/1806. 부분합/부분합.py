N,S = map(int,input().split())
lst = list(map(int,input().split()))+[0]
l=0
r=0

ans = 1e9
total = lst[0]
cnt = 1
while l <= r and r < N:
    if total >= S:
        ans = min(ans,cnt)
        total -= lst[l]
        l += 1
        cnt-=1

    else:
        r += 1
        total += lst[r]
        cnt+=1

if ans == 1e9:
    print(0)
else:
    print(ans)