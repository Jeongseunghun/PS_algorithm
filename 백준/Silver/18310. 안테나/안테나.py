N = int(input())
lst = list(map(int,input().split()))
lst.sort()
if N % 2 == 0:
    ans = 0
    ans2 = 0
    tmp = lst[N//2-1]
    tmp2 = lst[N//2]
    for i in lst:
        ans += abs(tmp-i)
    for i in lst:
        ans2 += abs(tmp2-i)
    if ans > ans2:
        print(tmp2)
    else:
        print(tmp)
    
else:
    print(lst[N//2])
