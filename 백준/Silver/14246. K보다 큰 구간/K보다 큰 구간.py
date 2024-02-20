n = int(input())
lst = list(map(int,input().split()))
k = int(input())

l = 0
r = 0

cnt = 0
s = 0
while r <= n:
    s = sum(lst[l:r])
    if s > k:
        cnt+=len(lst[r-1:])
        l+=1
    else:
        r+=1

print(cnt)