n = int(input())
lst = list(map(int,input().split()))
x = int(input())
lst.sort()

l = 0
r = n-1

cnt = 0
while l < r:
    if lst[l]+lst[r] == x:
        l+=1
        r-=1
        cnt+=1
    elif lst[l]+lst[r] > x:
        r-=1
    else:
        l+=1

print(cnt)
        