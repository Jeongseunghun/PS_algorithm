N = int(input())
lst = []

command = [input().split(" ") for _ in range(N)]

for i in command:
    if i[0] == "push":
        lst.append(i[1])
    elif i[0] == 'pop':
        if len(lst)>0:
            print(lst[-1])
            lst.pop()
        else:
            print(-1)
    elif i[0] == 'size':
        print(len(lst))
    elif i[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'top':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
        
        
        
