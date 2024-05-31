import sys
input = sys.stdin.readline

N = int(input())
dp = [3,7]
if N == 1:
    print(3)
else:
    for i in range(2,N):
        dp.append((2*dp[i-1] + dp[i-2]) % 9901)
    print(dp[N-1]) 
    