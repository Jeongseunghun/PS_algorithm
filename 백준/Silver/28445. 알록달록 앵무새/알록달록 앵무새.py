from itertools import permutations

d = list(map(str,input().split()))
t = list(map(str,input().split()))

ans = d+t
ans = list(set(ans))

res = []

for i in ans:
    res.append([i,i])

for x,y in permutations(ans,2):
    res.append([x,y])

res.sort(key = lambda x : (x[0],x[1]))

for x,y in res:
    print(x,y)