T = int(input())
for _ in range(T):
    N = int(input())
    s = list(input())
    e = list(input())
    b_cnt = 0
    w_cnt = 0
    for i in range(N):
        if s[i] != e[i]:
            if s[i] == 'B':
                b_cnt+=1
            else:
                w_cnt+=1
    
    ans = 0
    
    while b_cnt > 0 and w_cnt > 0:
        b_cnt-=1
        w_cnt-=1
        ans+=1
    
    ans += b_cnt
    ans += w_cnt
    
    print(ans)