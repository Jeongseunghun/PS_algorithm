from collections import deque

N,M,K,X = map(int,input().split())

board = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    board[a].append(b)

dis = [-1] * (N+1)
dis[X] = 0

def bfs(X):
    q = deque()
    q.append(X)
    
    while q:
        x = q.popleft()
        for i in board[x]:
            if dis[i] == -1:
                dis[i] = dis[x] + 1
                q.append(i)

bfs(X)
chk = False
for j in range(1,N+1):
    if dis[j] == K:
        print(j)
        chk = True

if chk == False:
    print(-1)