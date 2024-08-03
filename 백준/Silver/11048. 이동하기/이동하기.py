N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

dp = [[0] * (M+1) for _ in range(N+1)]

for x in range(1,N+1):
    for y in range(1,M+1):
        dp[x][y] = max(dp[x][y-1],dp[x-1][y-1],dp[x-1][y]) + board[x-1][y-1]    

print(dp[N][M])