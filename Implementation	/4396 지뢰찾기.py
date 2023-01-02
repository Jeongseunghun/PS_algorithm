n= int(input())
bomb = []
for _ in range(n):
    bomb.append(list(input()))

open = []
for _ in range(n):
    open.append(list(input()))
    
flag = False

res = [['.' for _ in range(n)] for _ in range(n)]


#상 하 좌 우 좌상 좌하 우상 우하
dx=[-1,1,0,0,-1,1,-1,1]
dy=[0,0,-1,1,-1,-1,1,1]        
        
for i in range(n):
    for j in range(n):
        if open[i][j] =="x":
            if bomb[i][j] == '*':
                flag =True
            cnt=0
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if x>=0 and y>=0 and x<=n-1 and y<=n-1:
                    if bomb[x][y] == "*":
                        cnt+=1
            res[i][j] = str(cnt)

if flag:
    for i in range(n):
        for j in range(n):
            if bomb[i][j] == "*":
                res[i][j] = "*"

for i in range(n):
    print("".join(res[i]))
