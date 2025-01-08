import heapq

def solution(scoville, K):
    ans = 0
    heapq.heapify(scoville)
    while True:
        if scoville[0] >= K:
            return ans
        if len(scoville) >= 2:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville,a + 2 * b)
            ans+=1
        else:
            return -1

        
    
    if scoville[0] >= K:
        return ans
    else:
        return -1
