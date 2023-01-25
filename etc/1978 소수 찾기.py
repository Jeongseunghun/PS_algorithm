N = int(input())
lst = list(map(int,input().split()))
cnt = 0
for i in lst:
    prime=0
    for j in range(1,i+1):
        if i % j == 0:
            prime+=1
    if prime == 2:
        cnt+=1

print(cnt)
        



