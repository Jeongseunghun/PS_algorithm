N,M = map(int,input().split())
S = set()
for _ in range(N):
    d = input()
    S.add(d)

cnt = 0
for i in range(M):
    chk = input()
    if chk in S:
        cnt+=1
        
print(cnt)
    