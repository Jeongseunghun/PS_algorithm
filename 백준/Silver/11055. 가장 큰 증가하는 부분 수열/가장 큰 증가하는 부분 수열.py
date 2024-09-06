N = int(input())
lst = list(map(int,input().split()))

dp = [0 for _ in range(N)]
dp[0] = lst[0]

for i in range(N):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[j]+lst[i],dp[i])
        else:
            dp[i] = max(lst[i],dp[i])
print(max(dp))