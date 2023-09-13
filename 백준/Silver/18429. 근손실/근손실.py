from itertools import permutations

N,K = map(int,input().split())
kit = list(map(int,input().split()))

tmp = []
for i in permutations(kit,len(kit)):
    tmp.append(i)

cnt = 0
for case in tmp:
    strength = 500
    flag = True
    for i in case:
        strength -= K
        strength += i
        if strength < 500:
            flag = False
            break
    if flag == True:
        cnt+=1

print(cnt)