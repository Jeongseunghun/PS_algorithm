N,M = map(int,input().split())
A = list(map(int,input().split()))

s = 0
e = 1

ans = 0
tmp = A[s]

while e < N:
    if tmp + A[e] > M:
        tmp-=A[s]
        s+=1
    else:
        tmp+=A[e]
        e+=1
        if ans < tmp:
            ans = tmp

print(ans)