N,M = map(int,input().split())
board = [list(map(int,input())) for _ in range(N)]

max_num = 0
rect = 0
while rect < N:
    for i in range(N-rect):
        for j in range(M-rect):
            if board[i][j] == board[i+rect][j+rect] and board[i][j] == board[i][j+rect] and board[i][j] == board[i+rect][j]:
                max_num = max((rect+1)**2,max_num)

    rect+=1

print(max_num)