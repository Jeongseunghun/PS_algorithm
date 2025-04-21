from collections import deque
import math

def solution(n, k):
    #진수 변환
    def convert(num,digit):
        val = deque()
        while num >= k:
            val.appendleft(str(num % k))
            num //= k
        val.appendleft(str(num))
        return ''.join(list(val))
    
    #소수 판별
    def decimal(s):
        if s == '1':
            return False
        
        num = int(s)
        d = 2
        while d <= math.sqrt(num):
            if num % d == 0:
                return False
            d+=1
        else:
            return True
        
    answer = 0
    s = deque(convert(n,k))
    tmp = []
    while s:
        val = s.popleft()
        if val != '0':
            tmp.append(val)
        else:
            if len(tmp) == 0:
                continue
            flag = decimal(''.join(tmp))
            if flag:
                answer+=1
            tmp = []
    
    if tmp:
        flag = decimal(''.join(tmp))
        if flag:
            answer+=1
    
    return answer