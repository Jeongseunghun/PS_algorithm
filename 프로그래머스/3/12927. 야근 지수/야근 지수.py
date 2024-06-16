import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    ans = 0
    works = [-i for i in works]
    heapq.heapify(works)
    while n > 0:
        tmp = heapq.heappop(works)
        heapq.heappush(works,tmp+1)
        n-=1
    
    for i in works:
        ans+=i**2
    return ans