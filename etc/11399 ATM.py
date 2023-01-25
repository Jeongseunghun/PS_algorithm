from curses.ascii import NL


N=int(input())
a=list(map(int,input().split()))
    
a.sort()
acc = 0 
val = 0
    
for i in range(N):
    val += (acc+a[i])
    acc += a[i]

    
print(val)