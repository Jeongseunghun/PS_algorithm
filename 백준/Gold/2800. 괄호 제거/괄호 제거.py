from itertools import combinations

val = list(input())
ans = []
stack = []

res = set()

for i in range(len(val)):
    if val[i] == '(':
        ans.append(i)
    elif val[i] == ')':
        # "("" 인덱스값 , ")"" 인덱스값
        stack.append((ans.pop(),i))
   
for i in range(1,len(stack)+1):
    for com in combinations(stack,i):
        tmp = val[:]
        for x,y in com:
            tmp[x] = ''
            tmp[y] = ''
        res.add(''.join(tmp))
    
res = list(res)
res.sort()    

for i in res:
    print(i)
