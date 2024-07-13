N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

max_benefit = -1e9

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + board[i-1][j-1]

for size in range(N):
    for i in range(N-size):
        for j in range(N-size):
            sx,sy = i,j
            ex,ey = i+size,j+size
            tmp_benefit = dp[ex+1][ey+1] - dp[ex+1][sy] - dp[sx][ey+1] + dp[sx][sy]
            max_benefit = max(max_benefit,tmp_benefit)

print(max_benefit)
    
