from collections import deque
N = int(input())
num = list(map(int,input().split()))

q = deque()
for i in range(1,N+1):
    q.append([i,num[i-1]])

res = []
while q:
    x,ans = q.popleft()
    res.append(x)
    if ans > 0:
        q.rotate(-(ans-1))
    else:
        q.rotate(-ans)
    
print(*res)