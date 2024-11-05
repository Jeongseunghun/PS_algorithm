N = int(input())
A = []
B = []
C = []
D = []
for _ in range(N):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

dict = {}
for i in A:
    for j in B:
        v = i + j
        if v not in dict.keys():
            dict[v] = 1
        else:
            dict[v] += 1

ans = 0
for i in C:
    for j in D:
        v = -1 * (i+j)
        if v in dict.keys():
            ans += dict[v]

print(ans)
