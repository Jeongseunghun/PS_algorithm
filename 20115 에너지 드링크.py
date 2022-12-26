N=int(input())
E=[]
res=[]

for _ in range(N):
    E.append(int(input()))

E.sort()

while True:
    for i in range(len(E)):
        E[i]/2 E[-i]