N,K = map(int,input().split())
lst = list(map(int,input().split()))

gap = []
for i in range(N-1):
    gap.append(lst[i+1]-lst[i])

gap.sort()

ans = 0
for i in range(N-K):
    ans += gap[i]
print(ans)