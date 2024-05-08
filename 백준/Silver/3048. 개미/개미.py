N1,N2 = map(int,input().split())
o1 = []
o2 = []
tmp1 = input()
tmp2 = input()
T = int(input())

for i in range(N1):
    o1.append([0,tmp1[i]])

for i in range(N2):
    o2.append([1,tmp2[i]])

ant = o1[::-1] + o2

ant2 = ant[:]
for i in range(T):
    for j in range(N1+N2-1):
        if ant[j][0] == 0 and ant[j+1][0] == 1:
            tmp = ant2[j]
            ant2[j] = ant2[j+1]
            ant2[j+1] = tmp
    ant = ant2[:]

ans = ''
for i in range(len(ant2)):
    ans += ant2[i][1]
print(ans)