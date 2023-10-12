from collections import deque

N,M = map(int,input().split())
lst = list(map(int,input().split()))
q = deque([i for i in range(1,N+1)])

cnt = 0
for i in lst:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) <= len(q) // 2:
                q.rotate(-1)
                cnt+=1
            else:
                q.rotate(1)
                cnt+=1

print(cnt)