def solution(people, limit):
    ans = 0
    
    people.sort()
    l,r = 0,len(people)-1
    
    while l <= r:
        if people[l] + people[r] <= limit:
            ans +=1
            l += 1
            r -= 1
        else:
            ans += 1
            r -= 1
    return ans