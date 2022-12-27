N,K = map(int,input().split())
S = list(map(int,input().split()))
D = list(map(int,input().split()))

for i in range(K):
    P=[0]*N
    for j in range(N):
        P[D[j]-1] = S[j]
    S=P

print(*S) 
