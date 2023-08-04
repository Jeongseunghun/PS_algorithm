import sys
input = sys.stdin.readline

N,K = map(int,input().split())
tem = list(map(int,input().split()))

max_tem = []
max_tem.append(sum(tem[:K]))
for i in range(N-K):
    max_tem.append(max_tem[i]-tem[i]+tem[K+i])
    

print(max(max_tem))
