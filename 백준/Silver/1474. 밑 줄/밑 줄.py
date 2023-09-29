N,M = map(int,input().split())
word = [input() for _ in range(N)]
d_len,r = divmod(M-sum(map(len,word)),N-1)
res = word[0]

for i in range(1,N):
    if word[i][0].islower() and r!=0 :
        r-=1
        res += '_' *(d_len+1) + word[i]
    elif i + r == N:
        r-=1
        res += '_' *(d_len+1) + word[i]
    else:
        res += '_'*(d_len) + word[i]

print(res)