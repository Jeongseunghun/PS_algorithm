N = int(input())
M = int(input())
lst = list(map(int,input().split()))

lst.sort()
l,r = 0, len(lst) - 1

cnt = 0

while l < r:
    s_num = lst[l] + lst[r]
    if s_num < M:
        l += 1
    elif s_num > M:
        r -= 1
    else:
        cnt+=1
        l+=1
        r-=1

print(cnt)