from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for lst in permutations(dungeons, len(dungeons)):
        cnt = 0
        tmp_k = k
        for x,y in lst:
            if tmp_k >= x:
                tmp_k -= y
                cnt+=1
        answer = max(answer, cnt)
    
    return answer