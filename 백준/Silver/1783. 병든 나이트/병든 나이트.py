from collections import deque

N, M = map(int,input().split())

res = 0
if N == 1:
    res = 1
elif N == 2:
    if M >=1 and M <= 6:
        res = (M+1) // 2
    elif M >= 7:
        res = 4
elif N >= 3:
    if M <= 6:
        res = min(M,4)
    elif M >= 7:
        res = M-2
print(res)