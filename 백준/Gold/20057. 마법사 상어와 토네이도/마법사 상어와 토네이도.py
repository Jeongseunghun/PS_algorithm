N = int(input())
sand = [list(map(int,input().split())) for _ in range(N)]
sx,sy= N//2, N//2

#방향별 비율
left = [(-2,0,0.02),(-1,0,0.07),(-1,-1,0.1),(-1,1,0.01),(0,-2,0.05),(1,-1,0.1),(1,0,0.07),(1,1,0.01),(2,0,0.02),(0,-1,0)]
right = [(x,-y,z) for x,y,z in left]
up = [(y,x,z) for x,y,z in left]
down = [(-y,x,z) for x,y,z in left]

rate = {'left':left, 'right':right, 'up':up, 'down':down}

#나간 모래
ans = 0


#모리 흩날림
def move(cnt,dx,dy,direction):
    global ans,sx,sy
    for _ in range(cnt + 1):
        sx,sy = sx+dx,sy+dy
        #범위 벗어나면 멈추기
        if sx < 0 or sy < 0:
            break
        
        total = 0
        for dx,dy,r in rate[direction]:
            nx = sx + dx
            ny = sy + dy
            #a
            if r == 0:
                s = sand[sx][sy] - total
            #그외 퍼지는 모래
            else:
                s = int(sand[sx][sy]*r)
            
            if 0 <= nx < N and 0<= ny < N:
                sand[nx][ny] += s
            else:
                ans += s
            total += s
            
        


for i in range(N):
    if i % 2 == 0:
        move(i,0,-1,'left')
        move(i,1,0,'down')
    else:
        move(i,0,1,'right')
        move(i,-1,0,'up')

print(ans)    