from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(arr):
    visited = [[1] * 5 for _ in range(5)]
    
    for i in arr:
        visited[i[0]][i[1]] = 0
    q = deque([(arr[0])])
    visited[arr[0][0]][arr[0][1]] = 1
    chk = 1
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<5 and 0<=ny<5:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    chk += 1
                    q.append((nx,ny))
    if chk != 7:
        return False
    else:
        return True           
    
def dfs(depth,start,cnt):
    global res
    
    if cnt>= 4:
        return
    if depth == 7:
        if bfs(arr):
            res+=1
        return
    for i in range(start,25):
        x = i //5
        y = i % 5
        arr.append((x,y))
        dfs(depth+1,i+1,cnt+(board[x][y] == 'Y'))
        arr.pop()

board = [list(input()) for _ in range(5)]
arr = []
res = 0
dfs(0,0,0)

print(res)
