# +, -, *10 +
def calc(ans):
    tmp = ans.replace(' ','')
    if eval(tmp) == 0:
        print(ans)

def chk(n,s):
    global res
    if n == N+1:
        calc(s)
        return
    chk(n+1,s+' '+str(n))
    chk(n+1,s+'+'+str(n))
    chk(n+1,s+'-'+str(n))

T = int(input())
for _ in range(T):
    N = int(input())
    
    res= []
    chk(2,'1')
    print()
    