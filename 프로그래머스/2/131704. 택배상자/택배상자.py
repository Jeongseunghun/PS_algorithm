def solution(order):
    ans = 0
    #보조 컨테이너
    subcon = []
    
    num = 0
    for i in range(1,len(order)+1):
        subcon.append(i)
        while subcon and subcon[-1] == order[num]:
            subcon.pop()
            num+=1
            ans+=1
        
    return ans