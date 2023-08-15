from collections import deque

N,M,K = map(int,input().split())
#추가되는 양분의 양
A = [list(map(int,input().split())) for _ in range(N)]

#양분 칸
board = [[5 for _ in range(N)] for _ in range(N)]

#나무 나이 저장(3차원)
trees = [[deque() for _ in range(N)] for _ in range(N)]

for i in range(M):
    x,y,z = map(int,input().split())
    trees[x-1][y-1].append(z)


def spring_summer():     

    for i in range(N):
        for j in range(N):
            dead_tree = 0
            new_tree = deque()
            for k in trees[i][j]:
                if board[i][j] >= k:
                    board[i][j] -= k
                    new_tree.append(k + 1)
                #땅에 양분이 부족
                else:
                    dead_tree += k//2
            trees[i][j] = new_tree
            board[i][j] += dead_tree


def fall_winter():
    tmp_trees = []
    
    #좌 좌상 상 우상 우 우하 하 좌하
    dx = [0,-1,-1,-1,0,1,1,1]
    dy = [-1,-1,0,1,1,1,0,-1]
    
    for i in range(N):
        for j in range(N):
            for k in trees[i][j]:
                if k % 5 == 0:
                    for d in range(8):
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if 0 <= nx < N and 0<= ny < N:
                            tmp_trees.append((nx,ny))
            #양분 추가(겨울)
            board[i][j] += A[i][j]
            
    for r,c in tmp_trees:
        trees[r][c].appendleft(1)
    
    


for _ in range(K):
    spring_summer()
    fall_winter()

ans = 0
for i in range(N):
    for j in range(N):
        for k in trees[i][j]:
            if k:
                ans+=1
print(ans)