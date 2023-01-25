a,b = map(int,input().split())

m = min(a,b)
lst = []

for i in range(1,m+1):
    if a%i == 0 and b%i == 0:
        lst.append(i)

min_cnt = max(lst) * (a//max(lst)) * (b//max(lst))
        
print(max(lst))
print(min_cnt)
    
    


