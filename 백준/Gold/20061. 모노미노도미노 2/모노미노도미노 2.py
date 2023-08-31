N = int(input())
#초록색 보드
g_board = [[0 for _ in range(4)] for _ in range(6)]
#파란색 보드
b_board = [[0 for _ in range(6)] for _ in range(4)]

#초록색 보드에 블록 쌓기
def green_insert(t,y):
    x = 0
    #1*1블록 / 2*1 세로블록
    if t == 1 or t == 3:
        for i in range(6):
            if g_board[i][y] == 1:
                break
            x+=1
        x-=1
        if t == 3:
            g_board[x-1][y] = 1
        g_board[x][y] = 1

    #1*2가로블록
    elif t == 2:
        for i in range(6):
            if g_board[i][y] == 1 or g_board[i][y+1] == 1:
                break
            x+=1
        x-=1
        g_board[x][y], g_board[x][y+1] = 1,1

#파란색 보드에 블록 쌓기
def blue_insert(t,x):
    y = 0
    # 1*1블록 / 1*2가로블록
    if t == 1 or t == 2:
        for i in range(6):
            if b_board[x][i] == 1:
                break
            y+=1
        y-=1
        if t == 2:
            b_board[x][y-1] = 1
        b_board[x][y] = 1

    # 2*1 세로블록
    elif t == 3:
        for i in range(6):
            if b_board[x][i] == 1 or b_board[x+1][i] == 1:
                break
            y+=1
        y-=1
        b_board[x][y],b_board[x+1][y] = 1,1

#블록 제거
def delete(color, idx):
    #초록 블록일 때
    if color == "g":
        for i in range(idx,-1,-1):
            if i == 0:
                for j in range(4):
                    g_board[i][j] = 0
            else:
                for j in range(4):
                    g_board[i][j] = g_board[i-1][j]

    #파란 블록일 때
    elif color == "b":
        for i in range(idx,-1,-1):
            if i == 0:
                for j in range(4):
                    b_board[j][i] = 0
            else:
                for j in range(4):
                    b_board[j][i] = b_board[j][i-1]

#초록 블록 제거 후 스코어 더해주기
def chk_score():
    global score
    for i in range(6):
        blocks = 0
        for j in range(4):
            if g_board[i][j]== 1:
                blocks+=1
        if blocks == 4:
            delete('g',i)
            score += 1

    for i in range(6):
        blocks = 0
        for j in range(4):
            if b_board[j][i] == 1:
                blocks +=1
        if blocks == 4:
            delete('b',i)
            score += 1

#파랑 블록 제거 후 스코어 더해주기
def green_chk_score():
    score = 0
    for i in range(6):
        if sum(g_board[i]) == 4:
            score += 1
            for j in range(4):
                g_board[i][j] = 0

    return

#연한 블록 처리
def chk_light():
    for i in range(2):
        for j in range(4):
            if g_board[i][j] == 1:
                delete('g',5)
                break

    for i in range(2):
        for j in range(4):
            if b_board[j][i] == 1:
                delete('b',5)
                break

score = 0
for _ in range(N):
    t,x,y = map(int,input().split())
    green_insert(t,y)
    blue_insert(t,x)
    chk_score()
    chk_light()

#보드에 들어있는 칸 개수
cnt = 0
for i in range(4):
    for j in range(6):
        if g_board[j][i] == 1:
            cnt+=1
        if b_board[i][j] == 1:
            cnt+=1

print(score)
print(cnt)
