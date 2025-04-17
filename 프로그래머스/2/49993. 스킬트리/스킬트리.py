def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        tmp = ''
        for i in st:
            if i in skill:
                tmp+=i

        flag = True
        for i in range(len(tmp)):
            if tmp[i] != skill[i]:
                flag = False
                break
        if flag:
            answer+=1
            
    
    return answer