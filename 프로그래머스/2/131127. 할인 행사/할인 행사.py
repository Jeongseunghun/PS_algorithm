from collections import Counter

def solution(want, number, discount):
    dict = {}
    for i in range(len(want)):
        dict[want[i]] = number[i]
    
    ans = 0
    
    for i in range(len(discount)-10+1):
        tmp = Counter(discount[i:i+10])
        cnt=0
        for j in tmp:
            if j not in dict:
                break
            if dict[j] == tmp[j]:
                cnt+=1
        if cnt == len(tmp):
            ans+=1
        
    return ans