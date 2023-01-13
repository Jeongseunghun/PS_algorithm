import math

n = int(input())

dp = [0,1]

for i in range(2,n+1):
    min_val = 4
    for j in range(int(math.sqrt(i)),0,-1):
        min_val = min(min_val, dp[i-j**2]+1)
    dp.append(min_val)
    
print(min_val)
        
        
        
    