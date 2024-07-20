N = int(input())
board = [list(input()) for _ in range(N)]

#머리 구하기
hx,hy = 0,0
flag = False
for i in range(N):
    for j in range(N):
        if board[i][j] == '*':
            hx = i
            hy = j
            flag = True
            break
    if flag:
        break
             
#심장
heartx,hearty = hx+1,hy

#왼쪽 팔
larm = 0
cnt = hearty
while True:
    cnt-=1
    if 0<=cnt and board[heartx][cnt] == '*':
        larm+=1
    else:
        break
    
#오른쪽 팔
rarm = 0
cnt = hearty
while True:
    cnt+=1
    if cnt<N and board[heartx][cnt] == '*':
        rarm+=1
    else:
        break

#허리
waist = 0
cnt = heartx
while True:
    cnt+=1
    if cnt<N and board[cnt][hearty] == '*':
        waist+=1
    else:
        break
    
#왼쪽 다리
lleg = 0
cnt = heartx + waist
while True:
    cnt+=1
    if cnt<N and board[cnt][hearty-1] == '*':
        lleg+=1
    else:
        break
#오른쪽 다리
rleg = 0
cnt = heartx + waist
while True:
    cnt+=1
    if cnt<N and board[cnt][hearty+1] == '*':
        rleg+=1
    else:
        break

print(heartx+1,hearty+1)
print(larm,rarm,waist,lleg,rleg)