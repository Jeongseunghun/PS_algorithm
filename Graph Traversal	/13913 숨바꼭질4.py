from collections import deque
import sys
 
sys.setrecursionlimit(1000000000)

N,K = map(int,input().split())

max_size = 100001
lst = [-1] * max_size
lst[N] = 0

q = deque()
q.append(N)

cnt = []
move_to = [0] * (max_size)

while q:
    x = q.popleft()
    if x == K:
        break
    for item in [x-1,x+1,2*x]:
        if 0 <= item < max_size:
            if lst[item] >= lst[x]+1 or lst[item] == -1:
                lst[item] = lst[x]+1
                q.append(item)
                move_to[item] = x
                
def path(n,m):
    if n!=m:
        path(n,move_to[m])
    print(m,end = " ")
               
        
print(lst[K])
path(N,K)
            