def solution(n, stations, W):
    ans = 0
    
    #0~처음
    gap = (stations[0] - W - 1) // (W*2 + 1)

    if (stations[0] - W - 1) % (W*2 + 1) == 0:
        ans+=gap
    else:
        ans+=gap+1
    
    #처음~마지막
    for s in range(1,len(stations)):
        gap = (stations[s] - stations[s-1] - 2 * W - 1) // (W*2 + 1)
        if (stations[s] - stations[s-1] - 2 * W - 1) % (W*2 + 1) == 0:
            ans+=gap
        else:
            ans+=gap+1
    
    #마지막~N-1
    gap = (n - stations[-1] - W) // (W*2 + 1)
    if (n - stations[-1] - W) % (W*2 + 1) == 0:
        ans+=gap
    else:
        ans+=gap+1
    
    return ans