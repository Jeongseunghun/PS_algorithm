N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + board[i-1][j-1]

sum = -400000000
for x in range(1,N+1):
    for y in range(1,M+1):
        #x * y 크기의 사각형
        for i in range(x,N+1):
            for j in range(y,M+1):
                sum = max(sum,dp[i][j] -dp[x-1][j] - dp[i][y-1] + dp[x-1][y-1])
                
print(sum)