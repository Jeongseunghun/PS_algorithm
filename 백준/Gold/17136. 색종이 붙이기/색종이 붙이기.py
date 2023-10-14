board = [list(map(int,input().split())) for _ in range(10)]
#색종이 사용 갯수
paper = [0,0,0,0,0]

def dfs(x,y,cnt):
    global min_val
    
    #y좌표 넘어가면 끝
    if y >= 10:
        min_val = min(min_val,cnt)
        return
    
    #x좌표 넘어가면 다음 y좌표
    if x >= 10:
        dfs(0,y+1,cnt)
        return
    
    if board[x][y] == 1:
        #5종류 색종이 시행
        for k in range(5):
            #최대 5장까지 가능
            if paper[k] == 5:
                continue
            if x+k >= 10 or y+k >= 10:
                continue
            
            #0체크
            flag = False
            for i in range(x,x+k+1):
                for j in range(y,y+k+1):
                    #0이 있으면 멈춤
                    if board[i][j] == 0:
                        flag = True
                        break
                if flag:
                    break
            
            #다 1이면 색종이 한장 추가하고 0으로 바꿔주기
            if flag == False:
                for i in range(x,x+k+1):
                    for j in range(y,y+k+1):
                        board[i][j] = 0
                        
                paper[k] +=1
                dfs(x+k+1,y,cnt+1)
                paper[k] -=1
                
                for i in range(x,x+k+1):
                    for j in range(y,y+k+1):
                        board[i][j] = 1
    
    else:
        dfs(x+1,y,cnt)
                

min_val = 1e9
dfs(0,0,0)
if min_val == 1e9:
    print(-1)
else:
    print(min_val)