
import sys
input = sys.stdin.readline

bingo = dict()
for i in range(5):
    a=list(map(int,input().split()))
    for j in range(5):
        bingo[a[j]] = (i,j)
    

check = [[0]*5 for _ in range(5)]

call = 0
for _ in range(5):
    a=list(map(int,input().split()))
    for i in range(5):
        call +=1
        
        if a[i] in bingo:
            check[bingo[a[i]][0]][bingo[a[i]][1]] = 1
        
        bingo_cnt = 0
        for j in range(5):
            if sum(check[j]) ==5 :
                bingo_cnt +=1
            if sum([k[j] for k in check]) == 5:
                bingo_cnt +=1
        #대각선        
        if check[0][4] + check[1][3] + check[2][2] + check[3][1] + check[4][0] == 5:
            bingo_cnt += 1
        if check[0][0] + check[1][1] + check[2][2] + check[3][3] + check[4][4] == 5:
            bingo_cnt += 1
        
        #3빙고
        if bingo_cnt >= 3:
            print(call)
            sys.exit()
                
