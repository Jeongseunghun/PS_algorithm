def operator(num1,num2,oper):
    if oper == "+":
        return num1+num2;
    elif oper == "-":
        return num1-num2;
    else:
        return num1*num2;

def dfs(idx, val):
    global ans
    
    if idx == N -1:
        ans = max(ans,val)
        return
    
    if idx + 2 < N:
        val2 = operator(val, int(lst[idx+2]), lst[idx+1])
        dfs(idx+2,val2)
    
    if idx + 4 < N:
        val3 = operator(int(lst[idx+2]),int(lst[idx+4]),lst[idx+3])
        val2 = operator(val,val3,lst[idx+1])
        dfs(idx+4,val2)

N = int(input())
lst = list(input())
ans = -2**31

dfs(0,int(lst[0]))
print(ans)