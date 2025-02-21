def solution(n, t, m, p):
    
    #n진수 변환 함수
    def convert_n(num):
        T = '0123456789ABCDEF'
        q,r = divmod(num,n)
        if q == 0:
            return T[r]
        else:
            return convert_n(q) + T[r]
    
    ans = '0'
    #n진수로 바꾸기
    for num in range(1,t+1000000):
        tmp = convert_n(num)
        ans += tmp
    
    res = ''
    
    cnt = p-1
    while len(res) != t:
        res += ans[cnt]
        cnt+=m
        
    
    return res