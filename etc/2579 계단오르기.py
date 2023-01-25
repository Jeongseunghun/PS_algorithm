import sys

input = sys.stdin.readline

N=int(input())
score =[]
dp=[]

for _ in range(N):
    score.append(int(input()))


if N==1:
    print(score[0])
    exit()
elif N==2:
    print(max(score[0]+score[1],score[1]))
    exit()
    
dp.append(score[0])
dp.append(max(dp[0]+score[1],score[1]))
dp.append(max(dp[0]+score[2],score[1]+score[2]))


for i in range(3,N):
    dp.append(max(dp[i-2]+score[i],dp[i-3]+score[i-1]+score[i]))
print(dp[-1])
          
    
    

