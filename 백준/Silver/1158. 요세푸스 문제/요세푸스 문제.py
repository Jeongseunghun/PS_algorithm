from collections import deque

N,K = map(int,input().split())

lst = deque([i for i in range(1,N+1)])

ans = []

while len(lst) > 0:
    lst.rotate(-(K-1))
    ans.append(lst.popleft())

res = '<'
for i in range(N-1):
    res+=str(ans[i])
    res+=', '
res += str(ans[-1])
res += '>'

print(res)