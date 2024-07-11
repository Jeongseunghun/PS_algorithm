N = int(input())
lst = list(map(int,input().split()))

dp = [0] * N

for i in range(1,N):
    if lst[i-1] > lst[i]:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]

Q = int(input())
for _ in range(Q):
    x,y = map(int,input().split())
    ans = dp[y-1] - dp[x-1]
    print(ans)