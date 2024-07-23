N = int(input())
s,e = 0,0
cnt, total = 0,0

while s <= e and e <= N:
    if total > N:
        total-=s
        s+=1
    elif total < N:
        e+=1
        total += e
    else:
        cnt+=1
        e+=1
        total += e

print(cnt)