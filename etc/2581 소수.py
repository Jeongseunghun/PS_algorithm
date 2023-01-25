M=int(input())
N=int(input())

lst = []

for i in range(M,N+1):
    cnt = 0
    for j in range(1,i+1):
        if i % j == 0:
            cnt+=1
    if cnt == 2:
        lst.append(i)

if len(lst) > 0:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)