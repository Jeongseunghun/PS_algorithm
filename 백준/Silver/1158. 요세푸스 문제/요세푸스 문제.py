from collections import deque

N,K = map(int,input().split())

lst = deque([i for i in range(1,N+1)])

ans = []

while len(lst) > 0:
    lst.rotate(-(K-1))
    ans.append(lst.popleft())

print(str(ans).replace('[','<').replace(']','>'))