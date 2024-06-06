N,M = map(int,input().split())
lst = list(map(int,input().split()))
tmp = [0 for _ in range(N+1)]
for _ in range(M):
    a,b,k = map(int,input().split())
    tmp[a-1] +=k
    tmp[b] -= k

h = 0
for i in range(N):
    h += tmp[i]
    lst[i]+=h
print(*lst)