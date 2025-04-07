import heapq

def solution(n, works):
    answer = 0
    works = [-i for i in works]

    heapq.heapify(works)
    for i in range(n):
        a = heapq.heappop(works)
        if a < 0:
            heapq.heappush(works,a+1)
        else:
            heapq.heappush(works,0)
    
    for i in works:
        answer += i**2
        
    return answer