def solution(genres, plays):
    cnt = len(genres)
    
    dict = {}
    for i in range(cnt):
        if genres[i] not in dict:
            dict[genres[i]] = plays[i]
        else:
            dict[genres[i]] += plays[i]
    
    dict_sorted = sorted(dict.items(),key = lambda x : x[1], reverse= True)
    
    lst = {}
    for i in range(cnt):
        if genres[i] not in lst:
            lst[genres[i]] = [[plays[i],i]]
        else:
            lst[genres[i]].append([plays[i],i])
    
    for i in lst:
        lst[i].sort(key = lambda x : x[0],reverse=True)
    
    print(lst)
    ans = []
    for i in dict_sorted:
        for j in lst[i[0]][:2]:
            ans.append(j[1])
    
    return ans