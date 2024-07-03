import sys
input = sys.stdin.readline

M,N = map(int,input().split())
K = int(input())
board = [list(input()) for _ in range(M)]

#정글(j),바다(o),얼음(i)
dp = [[[0,0,0] for _ in range(N+1)] for _ in range(M+1)]

for i in range(1,M+1):
    for j in range(1,N+1):
        for t in range(3):
            dp[i][j][t] = dp[i-1][j][t] + dp[i][j-1][t] - dp[i-1][j-1][t]
                
        if board[i-1][j-1] == 'J':
                dp[i][j][0] += 1
        elif board[i-1][j-1] == 'O':
                dp[i][j][1] += 1
        elif board[i-1][j-1] == 'I':
                dp[i][j][2] += 1

for _ in range(K):
    a,b,c,d = map(int,input().split())
    ans = [0,0,0]
    for t in range(3):
        ans[t] = dp[c][d][t] - dp[c][b-1][t] - dp[a-1][d][t] + dp[a-1][b-1][t]
    print(*ans)