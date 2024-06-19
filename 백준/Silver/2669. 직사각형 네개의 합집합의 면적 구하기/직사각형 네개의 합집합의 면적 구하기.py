board = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    lx,ly,rx,ry = map(int,input().split())
    for i in range(lx,rx):
        for j in range(ly,ry):
            board[i][j] +=1 

cnt = 0
for i in range(101):
    for j in range(101):
        if board[i][j] != 0:
            cnt+= 1

print(cnt)