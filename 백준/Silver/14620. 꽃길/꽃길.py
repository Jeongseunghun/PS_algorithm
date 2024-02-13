from itertools import combinations
from collections import deque

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,1,-0,0]
dy = [0,0,-1,1]


def chk(com):
    global tmp
    q = deque()
    for a,b in com:
        x, y = a,b
        q.append((x,y))
        tmp += board[x][y]
        visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 1:
                    return False
                visited[nx][ny] = 1
                tmp+=board[nx][ny]
    return True

lst = []
for i in range(1,N-1):
    for j in range(1,N-1):
        lst.append([i,j])

ans = 1e9
for i in combinations(lst,3):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    tmp = 0
    flag = chk(i)
    if flag:
        ans = min(tmp,ans)

print(ans)