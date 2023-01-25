N=int(input())
t=list(map(int,input().split(" ")))
m=0
t.sort()

if len(t)%2==0:
    for i in range(N//2):
        m=max(m,t[i] + t[N-1-i])
else:
    for i in range(N//2):
        m=max(m,t[i]+t[N-2-i])
    m=max(m,t[-1])
print(m)
