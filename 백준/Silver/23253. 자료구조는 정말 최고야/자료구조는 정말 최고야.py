import sys
input = sys.stdin.readline

N,M = map(int,input().split())

flag = True
for _ in range(M):
    k = int(input())
    lst = list(map(int,input().split()))
    for i in range(1,k):
        if lst[i] > lst[i-1]:
            flag = False
            break
    if not flag:
        break

if flag:
    print('Yes')
else:
    print('No')
