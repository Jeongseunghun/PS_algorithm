T = int(input())
for _ in range(T):
    lst = list(input().split())
    while True:
        crying = list(input().split())
        for i in range(len(lst)):
            if lst[i] == crying[2]:
                lst[i] = ""
        if ''.join(crying) == "whatdoesthefoxsay?":
            break
    
    for i in lst:
        if i != "":
            print(i,end = " ")