T = int(input())

dp = [0,1,2,4]

for i in range(4, 12):
    dp.append(sum(dp[-3:]))

for _ in range(T):
    n = int(input())
    print(dp[n])