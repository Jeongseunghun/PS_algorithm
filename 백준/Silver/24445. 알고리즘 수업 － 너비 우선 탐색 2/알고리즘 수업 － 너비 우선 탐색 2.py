from collections import deque

N,M,R = map(int,input().split())
node = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    node[u].append(v)
    node[v].append(u)

for i in range(1,N+1):
    node[i].sort(reverse = True)

q = deque()
q.append(R)
visited = [0 for _ in range(N+1)]
visited[R] = 1
cnt = 1

while q:
    x = q.popleft()
    for i in node[x]:
        if visited[i]:
            continue
        cnt+=1
        visited[i] = cnt
        q.append(i)

for i in range(1,N+1):
    print(visited[i])