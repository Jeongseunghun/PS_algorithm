def solution(diffs, times, limit):
    s = 1
    e = max(diffs)
    ans = max(diffs)
    while s <= e:
        level = (s+e) // 2
        
        total = 0
        
        for idx,i in enumerate(diffs):
            if diffs[idx] <= level:
                total += times[idx]
            elif diffs[idx] > level:
                wrong = diffs[idx] - level
                total += wrong * times[idx] + times[idx]
                if idx > 0:
                    total += wrong * times[idx-1]
                
        if total <= limit:
            e = level - 1
            ans = min(ans,level)
        else:
            s = level + 1
    
    return ans