N = int(input())
A = list(map(int,input().split()))
plus,minus,multi,divi = map(int,input().split())

max_val = -1e9
min_val = 1e9

def dfs(i,arr):
    global plus,minus,multi,divi,max_val,min_val
    if i == N:
        max_val = max(max_val, arr)
        min_val = min(min_val, arr)
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, arr+A[i])
            plus +=1
        if minus > 0:
            minus -= 1
            dfs(i+1, arr-A[i])
            minus += 1
        if multi > 0:
            multi -= 1
            dfs(i+1, arr*A[i])
            multi += 1
        if divi > 0:
            divi -= 1
            dfs(i+1, int(arr / A[i]))
            divi += 1
        

dfs(1,A[0])

print(max_val)
print(min_val)