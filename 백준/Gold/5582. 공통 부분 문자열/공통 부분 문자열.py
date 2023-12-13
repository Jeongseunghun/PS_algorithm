A = input()
B = input()

dp = [[0] * len(B) for _ in range(len(A))]
ans = 0

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans,dp[i][j])
    
print(ans)