N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N+1):
    for j in range(M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]+ board[i-1][j-1]

K = int(input())
for _ in range(K):
    i,j,x,y = map(int,input().split())
    ans = dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]
    print(ans)