def solution(sticker):
    ans = 0
    
    if len(sticker) == 1:
        return sticker[0]
    
    #첫 번째부터
    dp1 = [0] + sticker[:-1]
    for i in range(2,len(sticker)):
        dp1[i] = max(dp1[i-1], dp1[i-2] + dp1[i])
    
    #두 번째부터
    dp2 = [0] + sticker[1:]
    for i in range(2,len(sticker)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + dp2[i])

    return max(dp1[-1],dp2[-1])