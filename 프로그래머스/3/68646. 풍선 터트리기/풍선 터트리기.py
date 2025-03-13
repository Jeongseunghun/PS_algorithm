#번호가 더 큰 풍선 터트리기

def solution(a):
    
    lst = [[True,True] for _ in range(len(a))]
    
    ans = 0
    m = a[0]
    for i in range(1,len(a)-1):
        if m < a[i]:
            lst[i][0] = False
        m = min(m,a[i])
    
    m = a[len(a)-1]
    for i in range(len(a)-1,-1,-1):
        if m < a[i]:
            lst[i][1] = False
        m = min(m,a[i])
        
    for i in lst:
        if not(i[0] == False and i[1] == False):
            ans+=1
    
    return ans