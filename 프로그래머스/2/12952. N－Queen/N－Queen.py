def solution(n):
    def dfs(board,n,row):
        cnt = 0
        
        if n == row:
            return 1
        
        for col in range(n):
            board[row] = col
            
            for i in range(row):
                #세로로 겹칠 시
                if board[i] == board[row]:
                    break
                #대각선 겹칠 시
                if abs(board[i] - board[row]) == row-i:
                    break
            else:
                cnt += dfs(board,n,row+1)
        
        return cnt
    
    #index : 행, value : 열
    board = [0] * n
    
    return dfs(board,n,0)