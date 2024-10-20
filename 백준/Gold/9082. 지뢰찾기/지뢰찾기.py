T = int(input())
for _ in range(T):
    N = int(input())
    board = list(map(int,input()))
    mine = input()
    ans = 0
    for i in range(N):
        #첫 번째 지뢰
        if i == 0:
            if board[i] != 0 and board[i+1] != 0:
                board[i] -= 1
                board[i+1] -= 1
                ans+=1
        #마지막 지뢰
        elif i == N-1:
            if board[i] != 0 and board[i-1] != 0:
                board[i] -= 1
                board[i-1] -= 1
                ans+=1
        #중간 지뢰
        else:
            if board[i-1] != 0 and board[i] != 0 and board[i+1] != 0:
                board[i-1] -= 1
                board[i] -= 1
                board[i+1] -= 1
                ans += 1
    print(ans)
            
            
