def chk(num,s):
    if num > N:
        tmp = s.replace(" ","")
        if eval(tmp) == 0:
            print(s)
            return
        return
    
    chk(num+1,s+' '+str(num))
    chk(num+1,s+'+'+str(num))
    chk(num+1,s+'-'+str(num))

T = int(input())
for _ in range(T):
    N = int(input())
    ans = []
    chk(2,'1')
    print()