from re import L


T = int(input())
for _ in range(T):
    n,d = map(int,input().split())
    #배열
    arr = [list(map(int,input().split())) for i in range(n)]
    
    #주대각선0,중간열1,부대각선2,중간행3
    tmp = [[],[],[],[]]
    
    for i in range(n):
        tmp[0].append(arr[i][i])
    
    for i in range(n):
        tmp[1].append(arr[i][int(n/2)])
    
    for i in range(n):
        tmp[2].append(arr[n-i-1][i])
    
    for i in range(n):
        tmp[3].append(arr[int(n/2)][i])
        
    #시계방향
    if d>0:
        for _ in range(d//45):
            temp = tmp[0]
            tmp[0] = tmp[3]
            tmp[3] = tmp[2]
            tmp[2] = list(reversed(tmp[1]))
            tmp[1] = temp
            
    #반시계방향
    else:
        for _ in range(abs(d)//45):
            temp = tmp[0]
            tmp[0] = tmp[1]
            tmp[1] = list(reversed(tmp[2]))
            tmp[2] = tmp[3]
            tmp[3] = temp
    
    
    for i in range(n):
        arr[i][i] = tmp[0][i]
        arr[i][int(n/2)] = tmp[1][i]
        arr[n-i-1][i] = tmp[2][i]
        arr[int(n/2)][i] = tmp[3][i]
        
    for i in range(n):
        print(*arr[i])

        