N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

dp = [[[0]*3 for _ in range(N)] for _ in range(N)]

#0:가로 / 1:세로 / 2:대각선
dp[0][1][0] = 1
for i in range(N):
    for j in range(1,N):
        #벽일때
        if board[i][j] == 1:
            continue

        #가로 이동
        dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]
        #세로 이동
        dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
        #대각선 이동
        if board[i-1][j] != 1 and board[i][j-1] != 1:
            dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2])