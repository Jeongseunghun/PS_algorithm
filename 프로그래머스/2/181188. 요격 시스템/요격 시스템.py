def solution(targets):
    targets.sort(key = lambda x : (x[1]))
    standard = targets[0][1]-1
    ans = 1
    for t in range(1,len(targets)):
        if standard < targets[t][0]:
            ans += 1
            standard = targets[t][1] - 1
            print(standard)
            
    return ans