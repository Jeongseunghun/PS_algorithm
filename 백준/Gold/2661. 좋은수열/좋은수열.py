N = int(input())

def chk(res,cnt):
    for i in range(1,cnt//2+1):
        if str(res)[cnt-i:] == str(res)[cnt-2*i:cnt-i]:
            return
        
    #개수 맞으면 출력
    if cnt == N:
        print(res)
        exit()
    #뒷자리 추가
    for i in range(1,4):
        tmp = res * 10 + i
        chk(tmp,cnt+1)

chk(0,0)