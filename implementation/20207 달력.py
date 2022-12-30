N = int(input())
cal = [0] * 366

for i in range(N):
    S,E = map(int,input().split())
    for j in range(S,E+1):
        cal[j] +=1

row = 0
col = 0
res = 0 

for i in range(366):
    if cal[i] !=0:
        row = max(row, cal[i])
        col+=1
    else:
        res += row * col
        row = 0
        col = 0
res += row * col        
print(res)
        
        
    
    
    


