N,K = map(int,input().split())
num = list(map(int,input().split()))
l,r= 0,0

counter = [0] * (max(num) + 1)
ans = 0
while r < N:
    if counter[num[r]] < K:
        counter[num[r]] += 1
        r += 1
    else:
        counter[num[l]] -= 1
        l += 1
    ans = max(ans, r-l)

print(ans)
