N,K = map(int,input().split())
lst = []
for i in range(1,N+1):
    if N % i == 0:
        lst.append(i)

lst.sort()
if len(lst) >=K:
    print(lst[K-1])
else:
    print(0)
        
    
