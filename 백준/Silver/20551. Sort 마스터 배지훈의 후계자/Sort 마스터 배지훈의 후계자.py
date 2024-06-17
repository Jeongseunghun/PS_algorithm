from bisect import bisect_left
import sys

input = sys.stdin.readline

N,M = map(int,input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()
for _ in range(M):
    D = int(input())
    idx = bisect_left(lst,D)
    if idx >= N:
        print(-1)
    elif D == lst[idx]:
        print(idx)
    else:
        print(-1)