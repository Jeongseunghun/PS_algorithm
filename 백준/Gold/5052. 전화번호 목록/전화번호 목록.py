import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    flag = 'YES'
    n = int(input().strip())
    lst = []
    for i in range(n):
        num = input().strip()
        lst.append(num)
    lst.sort()
    for i in range(n-1):
        for j in range(i+1,n):
            if lst[i] == lst[j][:len(lst[i])]:
                flag = 'NO'
    print(flag)
            