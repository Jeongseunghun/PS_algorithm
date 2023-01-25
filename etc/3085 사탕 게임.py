from collections import deque

N = int(input())
lst = [list(input()) for i in range(N)]
maxcnt = 0

def check():
    global maxcnt
    for i in range(N):
        cnt = 1
        for j in range(1,N):
            if lst[i][j] == lst[i][j-1]:
                cnt+=1
                maxcnt = max(cnt,maxcnt)
            else:
                cnt=1
        cnt = 1
        for j in range(1,N):
            if lst[j][i] == lst[j-1][i]:
                cnt+=1
                maxcnt = max(cnt,maxcnt)
            else:
                cnt=1


for i in range(N):
    for j in range(N):
        if j+1 < N:
            lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
            check()
            lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
        if i+1 < N:
            lst[i][j], lst[i+1][j] = lst[i+1][j], lst[i][j]
            check()
            lst[i][j], lst[i+1][j] = lst[i+1][j], lst[i][j]
    
print(maxcnt)

    