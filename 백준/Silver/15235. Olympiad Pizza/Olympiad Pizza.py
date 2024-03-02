from collections import deque

N = int(input())
q = deque()
lst = list(map(int,input().split()))
time = 0
for i in range(N):
    q.append((i,time,lst[i]))
    
cnt = [0] * N
while q:
    time+=1
    num,t,pizza = q.popleft()
    if pizza-1 > 0:
        q.append((num,time,pizza-1))
    if pizza-1 == 0:
        cnt[num] = time

print(*cnt)