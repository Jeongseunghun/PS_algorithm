from itertools import combinations

tall = [int(input()) for _ in range(9)]

a= list(combinations(tall,7))

for i in a:
    if sum(i) ==100:
        a = sorted(i)
        for j in a:
            print(j)
        break
   