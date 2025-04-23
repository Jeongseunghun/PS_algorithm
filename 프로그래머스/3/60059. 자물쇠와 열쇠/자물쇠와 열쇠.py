def solution(key, lock):
    def chk(key_loc):
        #자물쇠의 홈 부분에 모두 맞는 지 체크
        for i in lock_loc:
            if i not in key_loc:
                return False
        
        #열쇠 돌기와 자물쇠 돌기가 자물쇠 영역 내에서 만나는 지 체크
        for i in key_loc:
            if i not in lock_loc:
                if 0 <= i[0] < N and 0 <= i[1] < N:
                    return False
        return True
    
    M = len(key)
    N = len(lock)
    
    #자물쇠(lock)의 홈 위치
    lock_loc = []
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                lock_loc.append([i,j])
    
    #4방향 회전
    for _ in range(4):
        key = list(zip(*key[::-1]))
        #열쇠(key)의 돌기 위치
        key_loc = []
        for i in range(M):
            for j in range(M):
                if key[i][j] == 1:
                    key_loc.append([i,j])
        
        for i in range(-M+1,N):
            for j in range(-M+1,N):
                tmp_key_loc = [[x+i,y+j] for x,y in key_loc]
                flag = chk(tmp_key_loc)
                if flag:
                    return True
    
    return False