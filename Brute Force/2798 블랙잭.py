from itertools import combinations

N,M = map(int,input().split())
num = list(map(int,input().split()))


a = list(combinations(num,3))
s = []
for i in a:
    s.append(sum(i))
    
s.sort()

for i in range(len(s)):
    res = s[i]
    if s[i] > M:
        res = s[i-1]
        break
    
print(res)