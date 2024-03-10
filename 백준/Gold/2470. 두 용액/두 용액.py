N = int(input())
lst = list(map(int,input().split()))
lst.sort()

s=0
e=N-1

standard = 2000000000
x,y = 0,0
while s < e:
    chemi = lst[s]+lst[e]
    if abs(chemi) <= standard:
        standard = abs(chemi)
        x = lst[s]
        y = lst[e]
    
    if chemi > 0:
        e-=1
    else:
        s+=1

print(x,y)