T = int(input())
for _ in range(T):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    lst.sort()
    top = 0
    cnt = 1
    for i in range(1,N):
        if lst[i][1] < lst[top][1]:
            top = i
            cnt += 1   
    print(cnt)