N,M = map(int,input().split())
board = [list(input()) for _ in range(N)]

#등차 리스트
tn = [i for i in range(-N,N)]
tm = [i for i in range(-M,M)]

ans = -1

def chk(s):
    s = int(s)
    return int(s**0.5) ** 2 == s

for x in range(N):
    for y in range(M):
        #등차
        for i in tn:
            for j in tm:
                tmp = ''
                id = x
                jd = y
                if not(i == 0 and j == 0):
                    while 0<= id < N and 0 <= jd < M:
                        tmp+= (board[id][jd])  
                        if chk(tmp):
                            ans = max(ans,int(tmp))
                        id+=i
                        jd+=j


print(ans)