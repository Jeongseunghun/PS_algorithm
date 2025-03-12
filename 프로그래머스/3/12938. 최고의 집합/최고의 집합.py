def solution(n, s):
    answer = []
    
    if s < n:
        return [-1]
    
    if s % n == 0:
        standard = s // n
        for i in range(n):
            answer.append(standard)
        answer.sort()
        return answer
    else:
        standard = s // n
        remain = s % n
        for i in range(n):
            if remain > 0:
                answer.append(standard+1)
                remain-=1
            else:
                answer.append(standard)
        
        answer.sort()
        return answer
        
    
    return [-1]