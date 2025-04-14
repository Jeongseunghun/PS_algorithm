from collections import deque

def solution(prices):
    prices = deque(prices)
    
    answer = []
    while prices:
        p = prices.popleft()
        t = 0
        for i in prices:
            t+=1
            if p > i:
                break
        answer.append(t)

    return answer