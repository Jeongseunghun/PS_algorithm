from itertools import combinations

N = int(input())
res = []
for i in range(1,11):
    for j in combinations(range(0,10),i):
        num = list(j)
        num.sort(reverse=True)
        res.append(int(''.join(map(str,num))))

res.sort()
if N >= len(res):
    print(-1)
else:
    print(res[N])