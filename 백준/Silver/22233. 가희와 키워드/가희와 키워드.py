import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dict = {}

ans = 0
for _ in range(N):
    dict[input().rstrip()] = 1
    ans+=1

for _ in range(M):
    gh = set(input().rstrip().split(','))
    for i in gh:
        if i in dict and dict[i] >= 1:
            dict[i] -=1
            ans-=1
    print(ans)