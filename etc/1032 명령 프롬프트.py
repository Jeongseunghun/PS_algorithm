from re import L


N=int(input())
b=[]

for i in range(N):
    b.append(input())

c=list(b[0])

for i in range(N):
    for j in range(len(c)):
        if c[j] == b[i][j]:
            continue
        else:
            c[j]="?"
            
print(''.join(c))