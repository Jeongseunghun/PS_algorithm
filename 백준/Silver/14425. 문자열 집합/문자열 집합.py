N,M = map(int,input().split())
S = [input() for _ in range(N)]

cnt = 0
for i in range(M):
    chk = input()
    if chk in S:
        cnt+=1
        
print(cnt)