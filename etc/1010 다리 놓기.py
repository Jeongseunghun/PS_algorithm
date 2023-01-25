dp = [0] * 31
dp[0] = 1
dp[1] = 1

for i in range(2, 31):
    dp[i] = dp[i-1] * i

T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    a= dp[M-N]
    b= dp[M]
    c= dp[N]
    
    print((b//a)//c)
    