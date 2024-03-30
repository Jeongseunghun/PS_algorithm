n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    tmp = min(a,b)
    ans = 0
    while tmp:
        if a % tmp == 0 and b % tmp == 0:
            ans = a//tmp * b//tmp * tmp
            break
        tmp-=1
    print(ans)