k = int(input())
n = int(input())
down_lst = list(input())
board = [[0] for _ in range(n)]

#가려진 가로줄 행 번호
hidden = 0
for i in range(n):
    line = list(input())
    for j in range(k-1):
        #가로막대가 아니면 0
        if line[j] == '*':
            board[i].append(0)
        #가로막대면 1
        elif line[j] == '-':
            board[i].append(1)
        #?면 2
        else:
            board[i].append(2)
            board[i][0] = 2
            hidden = i

up_board = [[0]*k for _ in range(hidden)]
up_lst = [chr(i+65) for i in range(k)]

#위
for i in range(hidden):
    for j in range(k):
        up_board[i][j] = board[i][j]

for i in range(hidden):
    for j in range(k-1):
        if up_board[i][j+1] == 1:
            up_lst[j],up_lst[j+1] = up_lst[j+1],up_lst[j]




down_board = [[0]*k for _ in range(n-hidden-1)]

#아래
for i in range(n-hidden-1):
    for j in range(k):
        down_board[i][j] = board[i+hidden+1][j]


for i in range(n-hidden-2,-1,-1):
    for j in range(k-1):
        if down_board[i][j+1] == 1:
            down_lst[j],down_lst[j+1] = down_lst[j+1],down_lst[j]



ans_lst = ['*' for _ in range(k-1)]

for i in range(k-1):
    if up_lst[i] != down_lst[i]:
        if up_lst[i] == down_lst[i+1]:
            ans_lst[i] = '-'
        elif up_lst[i] == down_lst[i-1]:
            continue
        else:
            ans_lst = ['x'] * (k-1)
            break

# #출력
# for i in range(n):
#     for j in range(k):
#         print(board[i][j],end = " ")
#     print()
    

for i in range(len(ans_lst)):
    print(ans_lst[i],end="")