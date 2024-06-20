N = int(input())
lst = []
for _ in range(N):
    a,b = map(int,input().split())
    lst.append([a,b])

lst.sort(key = lambda x : x[0])

ans = lst[0][0] + lst[0][1]
for i in range(1,N):
    tmp = lst[i][0]
    if ans < tmp:
        ans = lst[i][0] +lst[i][1]
    else:
        ans += lst[i][1]
    
print(ans)