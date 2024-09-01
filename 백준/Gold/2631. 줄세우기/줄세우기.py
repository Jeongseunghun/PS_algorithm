# 코드를 작성해주세요
N = int(input())
lst = [int(input()) for _ in range(N)]

dp= [1 for _ in range(N)]
m = 0

for i in range(1,N):
    for j in range(i):
        if lst[i] > lst[j]:
            m = max(m,dp[j])
        
    dp[i] = m + 1
    m = 0

print(N-max(dp))
        
    