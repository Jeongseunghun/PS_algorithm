def solution(stones, k):
    def bridge(val):
        
        cnt = 0
        
        for i in range(len(stones)):
            if stones[i] < val:
                cnt += 1
            elif stones[i] >= val:
                cnt = 0
            if cnt == k:
                return False
        return True
    
    ans = 1
    l = 1
    r = max(stones)
    
    while l <= r:
        mid = (l + r) // 2
        if bridge(mid):
            ans = max(ans,mid)
            l = mid + 1
        else:
            r = mid - 1
    
    return ans