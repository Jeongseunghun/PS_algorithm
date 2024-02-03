from collections import deque

n = int(input())
m = [0,0]
s = []
for _ in range(n):
    lst = list(map(int,input().split()))
    if lst[0] == 1:
        s.append(lst[1])
    else:
        s.pop(0)
    
    if m[0] < len(s):
        m[0] = len(s)
        m[1] = s[-1]
    elif m[0] == len(s):
        m[1] = min(m[1],s[-1])

print(m[0],m[1])