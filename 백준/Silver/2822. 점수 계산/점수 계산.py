s = []

for i in range(1,9):
    score = int(input())
    s.append(score)

res = sorted(s,reverse= True)

tmp = []
for i in res[:5]:
    tmp.append(s.index(i)+1)

print(sum(res[:5]))

tmp.sort()
print(*tmp)