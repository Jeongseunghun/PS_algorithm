T = int(input())
for _ in range(T):
    N = int(input())
    X = list(map(int,input().split()))
    dp = [0] * N
    dp[0] = X[0]
    for i in range(1,N):
        dp[i] = max(dp[i-1]+X[i],X[i])
    
    print(max(dp))