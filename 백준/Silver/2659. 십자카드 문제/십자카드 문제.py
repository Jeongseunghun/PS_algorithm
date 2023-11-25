from collections import deque

lst = list(map(int,input().split()))

def num(n):
    min = int(''.join(map(str,n)))
    for i in range(1,4):
        tmp = int(''.join(map(str,n[i:]+n[:i])))
        if min > tmp:
            min = tmp
    
    return min

a = num(lst)

cnt = 1
for i in range(1111, a):
    if '0' not in list(str(i)) and i == num(list(map(int,str(i)))):
        cnt+=1

print(cnt)
