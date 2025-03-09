#picks: [다이아몬드, 철, 돌]

def solution(picks, minerals):
    ans = 0
    
    #캘 수 있는 미네랄
    minerals = minerals[:sum(picks)*5+1]
    
    #최대 미네랄 50 // 5
    lst = [[0,0,0] for _ in range(10)]
    
    for idx, m in enumerate(minerals):
        if m == 'diamond':
            lst[idx//5][0] += 1  
        elif m == 'iron':
            lst[idx//5][1] += 1
        elif m == 'stone':
            lst[idx//5][2] += 1
    
    lst.sort(key = lambda x : (-x[0],-x[1],-x[2]))
    
    for a,b,c in lst:
        for i in range(3):
            if i == 0 and picks[0] > 0:
                picks[0] -= 1
                ans += a + b + c
                break
            elif i == 1 and picks[1] > 0:
                picks[1] -= 1
                ans += 5*a + b + c
                break
            elif i == 2 and picks[2] > 0:
                picks[2] -= 1
                ans += 25*a + 5*b + c
                break
    
    return ans