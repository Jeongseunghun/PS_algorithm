n = int(input())
lst = list(map(int,input().split()))

ans = []
ans.append(lst[0])
for i in range(1,n):
    ans.append(ans[i-1]+lst[i])

res = 0
for i in range(n-1):
    res += lst[i] * (ans[n-1]-ans[i])

print(res)