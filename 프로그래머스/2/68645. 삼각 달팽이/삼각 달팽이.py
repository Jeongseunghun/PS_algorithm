def solution(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1,2,3]
    
    lst = []
    for i in range(1,n+1):
        lst.append([0 for _ in range(i)])
    
    total = n * (n+1) // 2
    num = 1
    x,y = -1,0
    
    while n > 0:
        #아래
        for i in range(n):
            x+=1
            lst[x][y] = num
            num += 1
        n -= 1
        
        #옆
        for i in range(n):
            y+=1
            lst[x][y] = num
            num+=1
        n -= 1
        
        #위
        for i in range(n):
            x-=1
            y-=1
            lst[x][y] = num
            num+=1
        n-=1
        
    ans = []
    for i in lst:
        ans.extend(i)
    
    return ans