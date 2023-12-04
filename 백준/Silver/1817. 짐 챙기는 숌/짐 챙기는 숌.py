N,M = map(int,input().split())
cnt = 0

if N == 0:
    print(0)
else:
    lst = list(map(int,input().split()))
    tmp = 0
    cnt = 1
    for i in lst:
        if i+tmp <= M:
            tmp+=i
        else:
            tmp = i
            cnt += 1
    print(cnt)