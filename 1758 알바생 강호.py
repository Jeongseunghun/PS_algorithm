N=int(input())
tip=0
a=[]

for _ in range(N):
    a.append(int(input()))

a.sort(reverse=True)

for i in range(len(a)):
    give=a[i]-i
    if give>0:
        tip+=give
    
    
print(tip)
