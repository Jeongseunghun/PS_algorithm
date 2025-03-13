from collections import Counter

def solution(weights):
    ans = 0
    
    weights = Counter(weights)
    
    for i in range(100,1001):
        if weights[i] > 0:
            ans += weights[i] * (weights[i]-1) // 2
            ans += weights[i] * (weights[i * 2 / 3])
            ans += weights[i] * (weights[i * 2 / 4])
            ans += weights[i] * (weights[i * 3 / 4])
        
    return ans