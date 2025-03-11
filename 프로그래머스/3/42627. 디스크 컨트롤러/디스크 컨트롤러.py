#대기 큐 = [작업의 번호, 작업의 요청 시각, 작업의 소요 시간]
#소요 시간 > 요청 시각 > 번호 작은 것
import heapq

def solution(jobs):
    #전체 반환 시간
    ans = 0
    #작업 완료 개수
    done = 0
    #대기 큐
    h = []
    #시작 시간
    start = -1
    #현재 시간
    t = 0
    
    while done < len(jobs):
        for s,l in jobs:
            if start < s <= t:
                #작업 소요시간, 작업 요청시간
                heapq.heappush(h,[l,s])
        
        if len(h) > 0:
            tmp = heapq.heappop(h)
            start = t
            t += tmp[0]
            ans += t - tmp[1]
            done += 1
        else:
            t += 1
    
    return ans // len(jobs)