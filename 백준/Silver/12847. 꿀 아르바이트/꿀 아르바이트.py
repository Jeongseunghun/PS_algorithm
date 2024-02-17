n,m = map(int,input().split())
lst = list(map(int,input().split()))

ans = sum(lst[:m])
res = ans
for i in range(m,n):
    res -= lst[i-m]
    res += lst[i]
    ans = max(ans,res)
print(ans)