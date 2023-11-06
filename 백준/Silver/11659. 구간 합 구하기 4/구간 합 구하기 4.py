import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lst = list(map(int,input().split()))

sum_lst = [0]
total = 0
for i in range(N):
    total+=lst[i]
    sum_lst.append(total)

for i in range(M):
    s,e = map(int,input().split())
    print(sum_lst[e] - sum_lst[s-1])