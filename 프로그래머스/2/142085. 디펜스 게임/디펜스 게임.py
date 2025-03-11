import heapq

def solution(n, k, enemy):
    sum_enemy = 0
    
    ans = 0
    h = []
    heapq.heapify(h)
    
    for i in enemy:
        heapq.heappush(h,-i)
        sum_enemy += i
        if sum_enemy > n:
            if k == 0:
                break
            k-=1
            tmp = heapq.heappop(h)
            sum_enemy-= -tmp
        ans+=1
    
    return ans