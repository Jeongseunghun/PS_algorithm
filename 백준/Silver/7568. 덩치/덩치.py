N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int,input().split())))

ans = [0]*N
for i in range(len(lst)):
    a,b = lst[i][0],lst[i][1]
    cnt = 1
    for x,y in lst:
        if a < x and b < y:
            cnt+=1
    ans[i]= cnt
    
print(*ans)