from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    point = len(weak)
    #원형 -> 선형
    weak = weak + [i+n for i in weak]
    
    #도와주는 친구 순서
    for lst in permutations(dist):
        #점검 시작 지점
        for i in range(point):
            tmp_weak = weak[i:i+point]
            current = weak[i]
            cnt = 0
            for j in lst:
                cnt += 1
                if cnt >= answer:
                    break
                current += j
                #끝까지 점검했으면 갱신
                if current >= tmp_weak[-1]:
                    answer = cnt
                    break
                else:
                    #다음 점검 위치 조정
                    for t in tmp_weak:
                        if t > current:
                            current = t
                            break
    
    if answer > len(dist):
        return -1
    else:
        return answer