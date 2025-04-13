def chk(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False    
    
    if stack:
        return False
    else:
        return True

def seq(p):
    s = e = 0
    for idx,i in enumerate(p):
        if i == '(':
            s += 1
        elif i == ')':
            e += 1
        if s == e:        
            return p[:idx+1], p[idx+1:]

def solution(p):
    if p == "":
        return ""

    u,v = seq(p)
    
    #올바른 괄호 문자열이면
    if chk(u):
        return u + solution(v)
    else:
        s = ''
        for i in u[1:-1]:
            if i == '(':
                s += ')'
            else:
                s += '('
        
        return '(' + solution(v) + ')' + s
    
    return answer