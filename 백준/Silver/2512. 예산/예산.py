N = int(input())
lst = list(map(int,input().split()))
M = int(input())

def binary(lst):
    s = 0
    e = max(lst)
    while s <= e:
        m = (s+e) // 2
        cnt = 0
        #리스트 돌기
        for i in range(N):
            if lst[i] >= m:
                cnt += m 
            else:
                cnt += lst[i]
        
        if cnt <= M:
            s = m + 1
        else:
            e = m - 1
    
    return e

print(binary(lst))