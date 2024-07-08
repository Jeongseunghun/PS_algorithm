T = int(input())

dp = [1]
for i in range(1,2501):
    t = 0
    for j in range(i):
        t += dp[j] * dp[i-j-1]
        t %= 1000000007
    dp.append(t)

for _ in range(T):
    L = int(input())
    if L % 2 == 1:
        print(0)
    else:
        print(dp[L//2])
    