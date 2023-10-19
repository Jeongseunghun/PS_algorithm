N = int(input())
    
def dfs(n,start,end):
    if n == 1:
        print(start,end)
        return
    dfs(n-1,start,6-start-end)
    print(start,end)
    dfs(n-1,6-start-end,end)

print(2**N-1)
dfs(N,1,3)