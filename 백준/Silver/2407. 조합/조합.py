n,m = map(int,input().split())

ans = 1
for i in range(m,0,-1):
    ans *= n
    n-=1

tmp = 1
for i in range(1,m+1):
    tmp *= i

ans //= tmp

print(ans)