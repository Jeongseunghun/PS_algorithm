def solution(board, skill):
    answer = 0
    
    N = len(board)
    M = len(board[0])
    
    #누적합
    prefix = [[0 for _ in range(M+1)] for _ in range(N+1)]    
    
    for t, r1, c1, r2, c2, degree in skill:
        #적 공격
        if t == 1:
            s = -degree
        #아군 회복
        else:
            s = degree
        
        prefix[r1][c1] += s
        prefix[r1][c2+1] -= s
        prefix[r2+1][c1] -= s
        prefix[r2+1][c2+1] += s
            
    for i in range(N):
        for j in range(M):
            prefix[i][j+1] += prefix[i][j]
    for j in range(M):
        for i in range(N):
            prefix[i+1][j] += prefix[i][j]
    for i in range(N):
        for j in range(M):
            board[i][j] += prefix[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer