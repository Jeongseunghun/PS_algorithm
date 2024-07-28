R,C = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(R)]
T = int(input())

cnt = 0
for i in range(R-2):
    for j in range(C-2):
        lst = []
        for x in range(3):
            for y in range(3):
                lst.append(board[i+x][j+y])
        lst.sort()
        if lst[4] >= T:
            cnt+=1

print(cnt)
        
        
        
        