N = int(input())

ans = 0
for i in range(1,N+1):
    a = list(map(int,str(i)))
    if len(a) < 3:
        ans += 1
    else:
        gap = a[1]-a[0]
        cnt = 0
        for j in range(1,len(a)):
            if a[j]-a[j-1] == gap:
                cnt += 1
        if cnt == len(a)-1:
            ans+=1 

print(ans)
