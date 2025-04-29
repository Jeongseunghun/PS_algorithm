def solution(m, n, tmp_board):
    board = [list(row) for row in tmp_board]
    
    def erase():
        erase_set = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '':
                    continue
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    erase_set.update({(i,j), (i+1,j), (i,j+1), (i+1,j+1)})
        return erase_set

    def fall():
        for j in range(n):
            idx = m-1
            for i in range(m-1, -1, -1):
                if board[i][j] != '':
                    board[idx][j] = board[i][j]
                    if idx != i:
                        board[i][j] = ''
                    idx -=1
                    
    answer = 0
    while True:
        erase_set = erase()
        if not erase_set:
            break
        answer += len(erase_set)
        for x, y in erase_set:
            board[x][y] = ''
        fall()
    return answer