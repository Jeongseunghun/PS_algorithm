N,K,B = map(int,input().split())
broken = [int(input()) for _ in range(B)]

cw = [1 for _ in range(N)]
for i in broken:
    cw[i-1] = 0

ans = sum(cw[:K])
res = ans
for i in range(K,N):
    res -=cw[i-K]
    res +=cw[i]
    ans = max(ans,res)

print(K-ans)