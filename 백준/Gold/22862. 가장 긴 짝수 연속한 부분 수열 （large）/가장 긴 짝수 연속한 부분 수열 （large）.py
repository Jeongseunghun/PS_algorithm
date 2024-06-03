N,K = map(int,input().split())
lst = list(map(int,input().split()))


l = 0
tmp = 0
cnt = 0
res = 0

for s in range(N):
    while l < N and cnt <= K:
        if lst[l] % 2 == 0:
            tmp+=1
        else:
            cnt +=1
        l+=1
        
        if s == 0 and l == N:
            res = tmp
            break
    
    if cnt == K+1:
        res = max(tmp,res)
    
    if lst[s] % 2 == 0:
        tmp-=1
    else:
        cnt-=1
        
print(res)
            