from itertools import permutations

N,M = map(int,input().split())

lst = [i for i in range(1,N+1)]

tmp = []
for i in permutations(lst,M):
    print(*i)