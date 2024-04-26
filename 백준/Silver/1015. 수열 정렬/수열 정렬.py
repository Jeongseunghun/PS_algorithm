N = int(input())
lst = list(map(int,input().split()))

tmp_lst = sorted(lst)

ans = []
for i in range(N):
    ans.append([tmp_lst[i],i])

res=[]
for i in lst:
    for j in ans:
        if i == j[0]:
            res.append(j[1])
            ans.remove([j[0],j[1]])
            break

print(*res)