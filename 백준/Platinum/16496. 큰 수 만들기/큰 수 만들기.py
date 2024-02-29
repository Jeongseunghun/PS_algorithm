N = int(input())
lst = list(map(str,input().split()))

for i in range(N-1,0,-1):
    for j in range(i):
        A = lst[j]
        B = lst[j+1]
        AB = int(A+B)
        BA = int(B+A)
        if AB < BA:
            lst[j], lst[j+1] = lst[j+1], lst[j]

s = ''.join(lst)
if s[0] == '0':
    print(0)
else:
    print(s)