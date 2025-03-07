def solution(n, times):    
    l = 0
    r = n*max(times)
    
    ans = 0
    
    while l <= r:
        mid = (l+r) // 2
        num = 0
        for i in times: 
            num += mid //i
            if num >= n:
                break

        if num >= n:
            ans = mid
            r = mid-1
        else:
            l = mid+1

    
    return ans