from collections import Counter

def solution(topping):
    answer = 0
    dict = Counter(topping)
    
    s = set()
    for i in topping:
        dict[i] -= 1
        if dict[i] == 0:
            del dict[i]
        s.add(i)
        if len(dict) == len(s):
            answer+=1
        
    
    return answer