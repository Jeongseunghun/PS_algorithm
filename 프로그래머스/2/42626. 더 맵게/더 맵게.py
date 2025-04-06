import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while len(scoville) >= 2:
        if scoville[0] >= K:
            return answer
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville,a+2*b)
        answer+=1
    
    if scoville[0] >= K:
        return answer
    
    return -1