#선공이 O, 후공이 X

def solution(board):
    first = 0
    second = 0
    fttt = False
    sttt = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                first += 1
            elif board[i][j] == 'X':
                second += 1
    
    #8가지 경우의 수
    #가로
    for i in range(3):
        if board[i] == 'OOO':
            fttt = True
        elif board[i] == 'XXX':
            sttt = True
    #세로
    for i in range(3):
        ver = ''
        for j in range(3):
            ver += board[j][i]
        if ver == 'OOO':
            fttt = True
        elif ver == 'XXX':
            sttt = True
    #대각선
    lcross = board[0][0] + board[1][1] + board[2][2]
    rcross = board[0][2] + board[1][1] + board[2][0]
    
    if lcross == 'OOO' or rcross == 'OOO':
        fttt = True
    if lcross == 'XXX' or rcross == 'XXX':
        sttt = True

    if first < second:
        return 0
    if abs(first-second) > 1:
        return 0
    #O가 이겼을 때
    if fttt:
        if first <= second:
            return 0
        if second > 4:
            return 0
    #X가 이겼을 때
    if sttt:
        if first > second:
            return 0
        if first > 4:
            return 0
        
        
    return 1