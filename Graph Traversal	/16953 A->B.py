from collections import deque

A,B = map(int,input().split())

q = deque()
q.append((A,1))

while q:
    n,c = q.popleft()
    if n>B:
        continue
    if n==B:
        print(c)
        break
    q.append((n*10+1,c+1))
    q.append((n*2,c+1))
else:
    print(-1)  
    
    
    