N,M= list(map(int,input().split()))

while True:
    if min(N,M)<=4:
            print(min(N,M))
    elif min(N,M) ==5:
            print(min(N,M)-1)
    else:
        if N>M:
            print(M-2)
            
        elif N<=M:
            print(N-2)
    break