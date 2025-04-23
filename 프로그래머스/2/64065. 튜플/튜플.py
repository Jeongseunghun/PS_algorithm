def solution(s):
    answer = []
    
    s = list(map(str,s.split("}")))
    
    lst = []
    for i in s:
        t = []
        tmp = ''
        for j in i:
            if j == ',' and tmp:
                t.append(int(tmp))
                tmp = ''
            elif j.isdigit():
                tmp += j
        if tmp:
            t.append(int(tmp))
            tmp = ''
        
        if t:
            lst.append(t)
    
    lst.sort(key = lambda x : len(x))
    
    for i in lst:
        for j in i:
            if j not in answer:
                answer.append(j)
        
    return answer