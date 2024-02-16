import sys
input = sys.stdin.readline

N,X = map(int,input().split())
visit = list(map(int,input().split()))

if max(visit) == 0:
    print("SAD")
    exit(0)

ans = sum(visit[:X])
val = ans

cnt = 1

for i in range(X,N):
    val -= visit[i-X]
    val += visit[i]
    if ans < val:
        ans = val
        cnt = 1
    elif ans == val:
        cnt+=1

print(ans)
print(cnt)