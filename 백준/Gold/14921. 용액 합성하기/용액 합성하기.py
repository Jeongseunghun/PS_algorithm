N = int(input())
lst = list(map(int,input().split()))

s=0
e=N-1
ans = 200000000
while s<e:
    chemi = lst[s] + lst[e]
    if abs(ans) >= abs(chemi):
        ans = chemi

    if chemi > 0:
        e-=1
    elif chemi < 0:
        s+=1
    else:
        break   

print(ans)