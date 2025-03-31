def solution(scores):
    answer = 1
    #완호 점수
    wanx,wany = scores[0]
    
    scores.sort(key = lambda x : (-x[0],x[1]))
    
    m = scores[0][1]
    for i in range(len(scores)):
        if scores[i][0] > wanx and scores[i][1] > wany:
            return -1
        if m <= scores[i][1]:
            if scores[i][0] + scores[i][1] > wanx+wany:
                answer+=1
            m = scores[i][1]
        
    return answer