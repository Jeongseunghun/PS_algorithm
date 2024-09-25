def back(idx,s):
    global ans
    if idx == n:
        if int(s) <= int(B):
            ans = max(ans,int(s))
        return
    for i in range(n):
        if idx ==0 and A[i] == '0':
            continue
        
        if not chk[i]:
            chk[i] = True
            back(idx+1, s+A[i])
            chk[i] = False    
        
    
A,B = map(str,input().split())

n = len(A)
chk = [False] * n
ans= -1


back(0,'')

print(ans)