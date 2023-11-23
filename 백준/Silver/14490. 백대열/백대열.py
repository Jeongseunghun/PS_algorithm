def gcd(N,M):
    while N%M != 0:
        mod = M
        M = N % M
        N = mod
    return M

N,M = map(int,input().split(":"))
s = gcd(N,M)
print(N//s,":",M//s,sep="")