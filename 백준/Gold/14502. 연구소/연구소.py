import copy
from itertools import combinations
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(tmp_board):
    q = deque()
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for i in virus_lst:
        q.append(i)
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and tmp_board[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    tmp_board[nx][ny] = 2

    res = 0
    for i in range(N):
        for j in range(M):
            if tmp_board[i][j] == 0:
                res+=1

    return res


N,M = map(int,input().split())
# 0: 빈칸, 1: 벽, 2: 바이러스
board = [list(map(int,input().split())) for _ in range(N)]

#바이러스 위치
virus_lst = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus_lst.append((i,j))

wall = []
for i in range(N):
    for j in range(M):
        if board[i][j] != 1 and board[i][j] != 2:
            wall.append((i,j))
#벽 좌표 후보
wall_candi = []
for i in combinations(wall,3):
    wall_candi.append(i)

ans = 0
for i in wall_candi:
    tmp_board = copy.deepcopy(board)
    #벽 세우기
    for j in i:
        tmp_board[j[0]][j[1]] = 1

    res = bfs(tmp_board)
    ans = max(ans,res)

print(ans)