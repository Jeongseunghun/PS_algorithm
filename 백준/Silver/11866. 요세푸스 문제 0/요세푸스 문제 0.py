from collections import deque

N,K = map(int,input().split())
lst = [i for i in range(1,N+1)]
q = deque(lst)

ans = []

while q:
    q.rotate(-K+1)
    ans.append(q.popleft())

print(str(ans).replace('[','<').replace(']','>'))