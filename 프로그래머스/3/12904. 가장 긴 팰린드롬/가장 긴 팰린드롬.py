def solution(s):
    answer = s[0]
    
    def pal(l,r):
        tmp = ''
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                tmp = s[l:r+1]
            else:
                break
            l-=1
            r+=1
        
        return tmp
    
    for i in range(len(s)):
        #홀수
        res = pal(i,i)
        if len(answer) < len(res):
            answer = res
        
        #짝수
        res = pal(i,i+1)
        if len(answer) < len(res):
            answer = res
    
    return len(answer)