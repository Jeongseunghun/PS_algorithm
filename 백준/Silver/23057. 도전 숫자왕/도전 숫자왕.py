from itertools import combinations

N = int(input())
lst = list(map(int,input().split()))

s = sum(lst)

tmp = []
for i in range(1,N+1):
    for x in combinations(lst,i):
        tmp.append(sum(x))

tmp = set(tmp)

print(s-len(tmp))