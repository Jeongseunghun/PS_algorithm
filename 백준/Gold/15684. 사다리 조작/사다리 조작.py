N, M, H = map(int,input().split())

ladder = [[0]* (N) for _ in range(H)]
for i in range(M):
    x,y = map(int,input().split())
    ladder[x-1][y-1] = 1
    
def move():
    #사다리 N번 이동
    for i in range(N):
        num = i
        for j in range(H):
            #오른쪽 이동
            if ladder[j][num] == 1:
                num+=1
            #왼쪽 이동
            elif num>0 and ladder[j][num-1] == 1:
                num-=1
        if num != i:
            return False
    return True

def ladder_add(cnt,x,y):
    global ans
    # 사다리 번호 일치하면
    if move():
        ans = min(ans,cnt)
        return
    #3되면 종료
    elif cnt == 3 or ans <= cnt:
        return
    for i in range(x,H):
        if i == x:
            num = y
        else:
            num = 0
        for j in range(num, N-1):
            #오른쪽에 사다리가 존재하지 않을 경우
            if ladder[i][j] == 0 and ladder[i][j+1] == 0:
                if j > 0 and ladder[i][j-1]:
                    continue
                ladder[i][j] = True
                ladder_add(cnt+1,i,j+2)
                ladder[i][j] = False                

ans = 4
ladder_add(0,0,0)

print(ans if ans < 4 else -1)