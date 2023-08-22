import copy

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

def move(dir):
    #상
    if dir == 0:
        for j in range(N):
            idx = 0
            #두번째 행 부터
            for i in range(1,N):
                if board[i][j] > 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    #해당 열 0행이 비어있으면 추가
                    if board[idx][j] == 0:
                        board[idx][j] = tmp
                    #같은 값 두 블럭 충돌 시 X2, idx 증가
                    elif board[idx][j] == tmp:
                        board[idx][j] = tmp * 2
                        idx += 1
                    #블럭이 있고 다른 값이면 idx 증가, 그 밑에 블록 옮김
                    else:
                        idx += 1
                        board[idx][j] = tmp              
    #하
    if dir == 1:
        for j in range(N):
            idx = N-1
            #마지막에서 두번째 행부터
            for i in range(N-2,-1,-1):
                if board[i][j] > 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[idx][j] == 0:
                        board[idx][j] = tmp
                    elif board[idx][j] == tmp:
                        board[idx][j] = tmp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[idx][j] = tmp
    #좌
    if dir == 2:
        for i in range(N):
            idx = 0
            for j in range(1,N):
                if board[i][j] > 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][idx] == 0:
                        board[i][idx] = tmp
                    elif board[i][idx] == tmp:
                        board[i][idx] = tmp * 2
                        idx += 1
                    else:
                        idx += 1
                        board[i][idx] = tmp
    #우
    if dir == 3:
        for i in range(N):
            idx = N-1
            for j in range(N-2,-1,-1):
                if board[i][j] > 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][idx] == 0:
                        board[i][idx] = tmp
                    elif board[i][idx] == tmp:
                        board[i][idx] = tmp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[i][idx] = tmp


def dfs(cnt):
    global board,ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, board[i][j])
        return
    
    tmp_board = copy.deepcopy(board)
    for i in range(4):
        move(i)
        dfs(cnt+1)
        board = copy.deepcopy(tmp_board)

ans = 0
dfs(0)
print(ans)
