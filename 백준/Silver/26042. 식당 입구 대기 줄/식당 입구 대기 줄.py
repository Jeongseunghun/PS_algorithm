from collections import deque

N = int(input())
m = 0
n = 0
q = deque()
for _ in range(N):
    lst = list(map(int,input().split()))
    if lst[0] == 1:
        q.append(lst[1])
        if m < len(q):
            m = len(q)
            n = q[-1]
        if m == len(q):
            if q[-1] < n:
                n = q[-1]
    else:
        q.popleft()

print(m,n)