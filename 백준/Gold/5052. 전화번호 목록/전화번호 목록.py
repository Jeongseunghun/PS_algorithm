t = int(input())
for _ in range(t):
    flag = 'YES'
    n = int(input())
    lst = [input() for _ in range(n)]
    lst.sort()
    for i in range(n-1):
        if lst[i] == lst[i+1][:len(lst[i])]:
            flag = 'NO'
    print(flag)