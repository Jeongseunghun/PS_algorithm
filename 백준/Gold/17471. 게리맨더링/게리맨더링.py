from collections import deque
from itertools import combinations

def bfs(arr):
    global lst,area
    q = deque()
    q.append(arr[0])
    num = 0
    visited = set()
    visited.add(arr[0])
    while q:
        x = q.popleft()
        num += lst[x]
        for i in area[x]:
            if i not in visited and i in arr:
                q.append(i)
                visited.add(i)
    return num,len(visited)


N = int(input())
#선거구 인구수
lst = [0] + list(map(int,input().split()))
res = 1e9

#연결 구역
area = [[] for _ in range(N+1)]
for i in range(1,N+1):
    num = list(map(int,input().split()))
    for j in range(1,len(num)):
        area[i].append(num[j])

#반만 구하면 됨
for i in range(1,N//2+1):
    #구역을 i개로 나눔
    combi = list(combinations(range(1,N+1),i))
    for c in combi:
        s1,n1 = bfs(c)
        s2,n2 = bfs([i for i in range(1,N+1) if i not in c])
        if n1 + n2 == N:
            res = min(res,abs(s1-s2))

if res != 1e9:
    print(res)
else:
    print(-1)