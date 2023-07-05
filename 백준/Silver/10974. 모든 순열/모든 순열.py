from itertools import permutations

N = int(input())

arr = [i for i in range(1,N+1)]

res = list(permutations(arr,N))

for i in res:
    print(*i)