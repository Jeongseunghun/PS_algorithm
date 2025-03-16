from itertools import combinations

def solution(relation):
    ans = 0
    
    N = len(relation)
    M = len(relation[0])
    
    lst = [i for i in range(M)]
    
    candi = []
    
    for i in range(1,N+1):
        for j in combinations(lst, i):
            tmp = []
            for r in relation:
                key = [r[c] for c in j]
                #중복 시 break
                if key in tmp:
                    break
                else:
                    tmp.append(key)
            else:
                for c in candi:
                    if set(c).issubset(set(j)):
                        break
                else:
                    candi.append(j)
            
    
    return len(candi)