N,L = map(int,input().split())
lst = list(map(int,input().split()))

lst.sort()

std = lst[0]
cnt = 1
for i in lst[1:]:
    if i in range(std,std+L):
        continue
    else:
        cnt+=1
        std = i

print(cnt)
    