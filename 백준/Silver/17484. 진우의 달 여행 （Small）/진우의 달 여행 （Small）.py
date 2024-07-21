#좌하 하 우하
dx = [1,1,1]
dy = [-1,0,1]

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

dp = [[[0,0,0] for _ in range(M)] for _ in range(N)]

for i in range(M):
    for j in range(3):
        dp[0][i][j] = board[0][i]
    
for x in range(1,N):
    for y in range(M):
        for i in range(3):
            if (y==0 and i == 0) or (y== M-1 and i == 2):
                dp[x][y][i] = int(1e9)
                continue
            if i == 0:
                dp[x][y][0] = board[x][y] + min(dp[x-1][y-1][1], dp[x-1][y-1][2])

            elif i == 1:   
                dp[x][y][1] = board[x][y] + min(dp[x-1][y][0], dp[x-1][y][2])
            else:
                dp[x][y][2] = board[x][y] + min(dp[x-1][y+1][0], dp[x-1][y+1][1])

ans = int(1e9)        
for i in dp[N-1]:
    ans = min(ans,min(i))

print(ans)