from collections import deque

N = int(input())
q = deque([i for i in range(1,N+1)])

ans = []
while len(q):
    res = q.popleft()
    q.rotate(-1)
    ans.append(res)

print(*ans)
    
