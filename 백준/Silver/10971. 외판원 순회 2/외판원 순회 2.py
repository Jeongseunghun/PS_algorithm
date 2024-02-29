N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

visited = [0] * N
m = 1e9

def dfs(cnt,s,cost):
    global m
    if cnt == N-1 and board[s][0] != 0:
        m = min(m,cost + board[s][0])
        return

    for i in range(N):
        if not visited[i] and board[s][i] != 0:
            visited[i] = 1
            dfs(cnt+1,i,cost+board[s][i])
            visited[i] = 0
    return

visited[0] = 1
dfs(0,0,0)

print(m)