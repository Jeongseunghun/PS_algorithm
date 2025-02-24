def solution(players, m, k):
    #증설 횟수
    ans = 0
    #[운영 중인 서버, 남은 운영 시간]
    current_server = []
    
    for p in players:
        tmp_server = []
        #운영 시간 감소
        for c in current_server:
            c[1] -= 1
            if c[1] > 0:
                tmp_server.append(c)
        
        current_server = tmp_server
        if len(current_server) < p//m:
            ans += p//m - len(current_server)
            #서버 증설
            for _ in range(p//m - len(current_server)):
                current_server.append([1,k])
        
        print(p, current_server)
        
    
    return ans