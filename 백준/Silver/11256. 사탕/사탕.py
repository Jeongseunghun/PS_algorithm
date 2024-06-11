T = int(input())
for _ in range(T):
    J,N = map(int,input().split())
    lst = []
    for _ in range(N):
        r,c = map(int,input().split())
        lst.append(r*c)
    lst.sort(reverse = True)
    sum = 0
    for i in range(N):
        sum += lst[i]
        if sum >= J:
            break
    print(i+1) 
    
