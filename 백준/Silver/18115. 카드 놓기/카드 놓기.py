from collections import deque

N = int(input())
A = list(map(int,input().split()))
A.reverse()

ans = deque()
for i in range(N):
    if A[i] == 1:
        ans.appendleft(i+1)
    elif A[i] == 2:
        ans.insert(1,i+1)
    else:
        ans.append(i+1)

print(*ans)