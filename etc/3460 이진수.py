T = int(input())
for _ in range(T):
    n = int(input())
    a=list(format(n,'b'))
    a.reverse()
    for i in range(len(a)):
        if a[i] == '1':
            print(i, end= " ")
    
    