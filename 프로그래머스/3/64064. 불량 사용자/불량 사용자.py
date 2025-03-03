from itertools import permutations

def solution(user_id,banned_id):
    ans = []
    
    def chk(lst,banned_id):
        for idx1, ban_id in enumerate(banned_id):
            if len(lst[idx1]) != len(ban_id):
                return False
            
            for idx2,j in enumerate(lst[idx1]):
                if '*' == ban_id[idx2]:
                    continue
                if j != ban_id[idx2]:
                    return False
        
        return True
    
    #모든 경우의 조합
    for lst in permutations(user_id,len(banned_id)):
        if not chk(lst,banned_id):
            continue
        else:
            lst = set(lst)
            if lst not in ans:
                ans.append(lst)

    return len(ans)