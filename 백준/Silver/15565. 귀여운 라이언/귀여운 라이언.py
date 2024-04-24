N,K = map(int,input().split())
lst = list(map(int,input().split()))

lion = []
for i in range(N):
    if lst[i] == 1:
        lion.append(i)

if len(lion) < K:
    print(-1)
    exit()

ans = 1e9
for i in range(len(lion) - K + 1):
    ans = min(ans, lion[i+K-1] - lion[i] + 1)
print(ans)