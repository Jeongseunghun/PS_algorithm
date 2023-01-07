A=int(input())
T=int(input())
code = int(input())

arr = []
#회차
code_cnt = 0
bbun = 1
degi = 1

while True:
    code_cnt+=1
    turn = bbun
    for _ in range(2):
        arr.append((bbun,0))
        bbun+=1
        arr.append((degi,1))
        degi+=1 
    
    for _ in range(code_cnt+1):
        arr.append((bbun,0))
        bbun+=1
    
    for _ in range(code_cnt+1):
        arr.append((degi,1))
        degi+=1
    
    if turn < T <= bbun:
        print(arr.index((T,code)) % A)
        break
        
    
