import sys
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = board[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
    
K = int(input())
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    ans = dp[x2][y2] - dp[x1-1][y2]-dp[x2][y1-1] + dp[x1-1][y1-1]
    print(ans)