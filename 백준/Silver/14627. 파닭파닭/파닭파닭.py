S,C = map(int,input().split())
lst = []
for _ in range(S):
    L = int(input())
    lst.append(L)
    
s,e = 1, max(lst)

while s <= e:
    m = (s+e) // 2
    
    tmp = sum(i//m for i in lst)
    
    if tmp >= C:
        s = m+1
    else:
        e = m-1

ans = sum(lst) - e*C

print(ans)