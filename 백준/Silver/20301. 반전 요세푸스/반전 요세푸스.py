from collections import deque

N,K,M = map(int,input().split())

lst = deque()
for i in range(1,N+1):
    lst.append(i)

cnt = 0
while lst:
    if cnt == M:
        lst = deque(reversed(lst))
        cnt=0
   
    for i in range(K-1):
        lst.append(lst.popleft())
    print(lst.popleft())
    cnt+=1