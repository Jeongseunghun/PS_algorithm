import math

X,Y = map(int,input().split())

Z = math.floor(Y*100/X)

if Z >= 99:
    print(-1)
else:
    ans = 0
    s = 0
    e = 1000000000
    while s<=e:
        m = (s+e) // 2
        if (Y+m) * 100 // (X+m) > Z:
            ans = m
            e = m-1
        else:
            s = m+1
    print(ans)