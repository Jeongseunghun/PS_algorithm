N,M,K = list(map(int,input().split()))
T = 0
while True :
    N-=2
    M-=1
    if N<0 or M<0 or (N+M)<K:
        break
    T+=1
print(T)