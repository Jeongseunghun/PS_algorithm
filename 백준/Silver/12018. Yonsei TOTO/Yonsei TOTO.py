n,m = map(int,input().split())
lst = []
for _ in range(n):
    p,l = map(int,input().split())
    mile = list(map(int,input().split()))
    mile.sort(reverse=True)
    if len(mile) < l:
        lst.append(1)
    else:
        lst.append(mile[l-1])

lst.sort()
ans = 0
total = 0
for i in lst:
    if total+i <= m:
        total += i
        ans +=1
    else:
        break
print(ans)
    