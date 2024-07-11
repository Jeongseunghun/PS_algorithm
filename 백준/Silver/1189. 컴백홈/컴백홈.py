dx = [0,0,-1,1]
dy = [1,-1,0,0]

R,C,K = map(int,input().split())
board = [list(input()) for _ in range(R)]
cnt = 0
def dfs(sx,sy,dis):
    global cnt
    if sx == 0 and sy == C-1 and dis == K:
        cnt+=1
    else:
        board[sx][sy] = 'T'
        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == '.':
                board[nx][ny] = 'T'
                dfs(nx,ny,dis+1)
                board[nx][ny] = '.'
                
dfs(R-1,0,1)
print(cnt)