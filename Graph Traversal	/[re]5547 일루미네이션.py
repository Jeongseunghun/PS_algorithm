W,H = map(int,input().split())
chart = [list(map(int,input().split())) for i in range(H)]
visited = [[0]*W for _ in range(H)]



def dfs(y,x):
    stack = [(y,x)]
    visited[y][x] = 1
    cnt = 0
    while stack:
        y,x = stack.pop()
        #짝수
        if y%2:
            di = [(-1,0),(-1,-1),(0,-1),(0,1),(1,0),(1,-1)]
        #홀수
        else:
            di = [(-1,0),(-1,1),(0,-1),(0,1),(1,0),(1,1)]
        for i,j in di:
            if 0<=y+i<H and 0<=x+j<W and not visited[y+i][x+j]:
                if chart[y+i][x+j]:
                    cnt+=1
                else:
                    visited[y+i][x+j] = 1
                    stack.append((y+i,x+j))
                    
    return cnt

total = 0
for y in [0,H-1]:
    for x in range(W):
        if chart[y][x]:
            total += 2
            if(y==0 and x==W-1) or (y==H-1 and x==0):
                total -= 1
        elif chart[y][x] == 0 and not visited[y][x]:
            total += dfs(y,x)

for y in range(H):
    for x in [0,W-1]:
        if chart[y][x]:
            if(x==0 and y%2) or (x==W-1 and y%2==0):
                total += 3
            else:
                total += 1
        elif chart[y][x] == 0 and not visited[y][x]:
            total += dfs(y,x)

print(total)
                
                 
            