def solution(genres, plays):
    answer = []
    dict = {}
    for idx,i in enumerate(genres):
        if i not in dict:
            dict[i] = plays[idx]
        else:
            dict[i] += plays[idx]
    
    dict = sorted(dict.items(),key = lambda x : -x[1])
    
    lst = []
    for idx,(g,p) in enumerate(zip(genres,plays)):
        lst.append([g,p,idx])
    
    lst.sort(key = lambda x : (-x[1],x[2]))
    
    for i in dict:
        cnt = 0
        for j in lst:
            if cnt >= 2:
                break
            elif j[0] == i[0]:
                cnt+=1
                answer.append(j[2])
                
    return answer