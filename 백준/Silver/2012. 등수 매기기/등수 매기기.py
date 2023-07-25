import sys
N = int(sys.stdin.readline())
rating = [int(input()) for _ in range(N)]

rating.sort()

ans = 0

for i in range(1,N+1):
    ans += abs(i - rating[i-1])
    
print(ans)