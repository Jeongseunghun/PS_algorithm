N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
#토네이도 시작
sx,sy = N//2,N//2

ans = 0

def cnt(sx,sy,direction):
    global ans
    
    if sy < 0:
        return
    
    total = 0
    for dx,dy,z in direction:
        nx = sx + dx
        ny = sy + dy
        # a일때
        if z == 0:
            sand = board[sx][sy] - total
        else:
            sand = int(board[sx][sy] * z)
            total += sand
        
        if 0 <= nx < N and 0 <= ny < N:
            board[nx][ny] += sand
        
        else:
            ans += sand




#좌하우상
dx = [0,1,0,-1]
dy = [-1,0,1,0]

#방향별 모래 비율
left = [(1,1,0.01),(-1,1,0.01),(1,0,0.07),(-1,0,0.07),(-1,-1,0.1),(1,-1,0.1),(2,0,0.02),(-2,0,0.02),(0,-2,0.05),(0,-1,0)]
right =[(x,-y,z) for x,y,z in left]
down = [(-y,x,z) for x,y,z in left]
up = [(y,x,z) for x,y,z in left]

#토네이도 회전 순서
dict = {0: left, 1: down, 2: right, 3:up}
t = 0
for i in range(2*N-1):
    d = i % 4
    if d == 0 or d == 2 :
        t += 1
    for _ in range(t):
        nx = sx + dx[d]
        ny = sy + dy[d]
        cnt(nx,ny,dict[d])
        sx,sy = nx,ny
        
print(ans)