N,K = map(int,input().split())
lst = list(map(int,input().split()))

sorted_lst = sorted(lst,reverse=True)

s = 0
for i in range(K):
    s+=i

ans = sum(sorted_lst[:K]) - s

print(ans)
