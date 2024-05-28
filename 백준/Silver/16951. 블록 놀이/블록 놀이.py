def chk(i):
    cnt = 0 
    for j in range(N):
        if j < i:
            if lst[j] != (lst[i] - (i-j)*K):
                cnt+=1
        elif j > i:
            if lst[j] != (lst[i] + (j-i)*K):
                cnt+=1
    return cnt

N,K = map(int,input().split())
lst = list(map(int,input().split()))

cnt = 1001

for i in range(N):
    if lst[i] > i*K:
        tmp = chk(i)
        cnt = min(cnt,tmp)
            
print(cnt)