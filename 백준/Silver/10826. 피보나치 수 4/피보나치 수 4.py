n = int(input())

dp = [0,1]
for i in range(2,n+1):
    dp.append(dp[i-1] + dp[i-2])

if n == 0:
    print(0)
else:
    print(dp[-1])