def solution(routes):
    answer = 0
    
    cam = -30000
    
    routes.sort(key = lambda x : x[1])
    
    for s,e in routes:
        if cam < s:
            answer+=1
            cam = e

    
    return answer