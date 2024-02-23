N,K = map(int,input().split())
lst = list(map(int,input().split()))

lst.extend(lst)
ans = sum(lst[:K])
res = ans
for i in range(N):
    res -= lst[i]
    res += lst[i+K]
    ans = max(res,ans)
print(ans)