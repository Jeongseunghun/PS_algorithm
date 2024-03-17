N, K = map(int,input().split())

ans = 0
if N < K * (K+1) // 2:
    ans = -1
elif (N - K * (K+1) // 2) % K == 0:
    ans = K-1
else:
    ans = K
    
print(ans)