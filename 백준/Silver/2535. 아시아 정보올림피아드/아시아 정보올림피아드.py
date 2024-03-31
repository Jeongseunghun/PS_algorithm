N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

lst.sort(key = lambda x : -x[2])

ans = []
for s in lst:
    if len(ans) == 3:
        break
    cnt = 0
    for i in ans:
        if i[0] == s[0]:
            cnt+=1
    if cnt < 2:
        ans.append(s)


for i in ans:
    print(i[0],i[1])