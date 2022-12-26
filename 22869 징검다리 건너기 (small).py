N,K=map(int,input().split())
stone = list(map(int,input().split()))
dp = [0] * N
dp[0] = 1

for i in range(N-1):
    for j in range(i+1,N):
        if dp[i] and (j-i) * (1+abs(stone[j]-stone[i])) <= K:
            dp[j] = 1

print("YES" if dp[N-1] else "NO")
        
    
    
