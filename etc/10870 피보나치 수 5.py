# N = int(input())

# DP = [0,1]
# for i in range(2,N+1):
#     DP.append(DP[i-2] + DP[i-1])
    

# print(DP[N])


n = int(input())

dp =[0,1]

for i in range(2,n+1):
    dp.append(dp[i-2]+dp[i-1])

print(dp[n])