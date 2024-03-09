N = int(input())
lst = list(map(int,input().split()))

s = 0
e = N-1
x,y = 0,0
standard = 2000000000


while s<e:
    chemi = lst[s] + lst[e]
    if abs(chemi) <= standard:
        x = lst[s]
        y = lst[e]
        standard = abs(chemi)
        
    if chemi <= 0:
        s+=1
    else:
        e-=1

print(x,y)