N=int(input())

d = {'ChongChong'}

for i in range(1,N+1):
    a,b = input().split()
    
    if a in d:
        d.add(b)
    if b in d:
        d.add(a)

print(len(d))