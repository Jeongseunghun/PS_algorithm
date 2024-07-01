import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))

s = [lst[0]]
for i in range(1,N):
    s.append(s[i-1]+lst[i])

M = int(input())
for _ in range(M):
    i,j = map(int,input().split())
    if i == 1:
        print(s[j-1])
    else:
        print(s[j-1]-s[i-2])