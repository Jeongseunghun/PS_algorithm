S = int(input())
sum = 0
cnt = 0

while S >=sum:
    cnt+=1
    sum+=cnt
    if S<sum:
        break

print(cnt-1) 