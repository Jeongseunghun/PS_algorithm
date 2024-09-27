def calc(seq):
    global min_val, max_val
    seq = str(seq)
    res = int(seq[0])
    for i in range(1,len(seq),2):
        if seq[i] == '+':
            res+=int(seq[i+1])
        elif seq[i] == '-':
            res-=int(seq[i+1])
        elif seq[i] == '*':
            res*=int(seq[i+1])
    min_val = min(min_val,res)
    max_val = max(max_val,res)
    return min_val,max_val  
              
def dfs(sx,sy,dis):
    global val_lst
    if sx == N-1 and sy == N-1 and min_dis == len(dis):
        return val_lst.append(dis)
    for i in range(2):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            dfs(nx,ny,dis+board[nx][ny])
    

#오른쪽, 아래쪽
dx = [0,1]
dy = [1,0]

N = int(input())
board = [list(map(str,input().split())) for _ in range(N)]
val_lst = []

min_dis = 0
if N == 3:
    min_dis = 5
elif N == 5:
    min_dis = 9

dfs(0,0,board[0][0]) 

min_val = 1e9
max_val = -1e9

for i in val_lst:
    calc(i)

print(max_val,min_val)
