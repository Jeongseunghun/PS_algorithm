N = int(input())
lst = list(map(int,input().split()))

s = 0
e = N-1

ans = 2000000000
x,y = 0,N-1
while s<e:
    if abs(lst[s] + lst[e]) < ans:
        ans = abs(lst[s] + lst[e])
        x,y = s,e
    if lst[s] + lst[e] <= 0:
        s+=1
    else:
        e-=1
print(lst[x],lst[y])