import sys
sys.setrecursionlimit(10 ** 8)

T = int(input())

def dfs(i):
    global ans
    visited[i] = True
    cycle.append(i)
    num = lst[i]
    
    if visited[num]:
        if num in cycle:
            ans += cycle[cycle.index(num):]
        return
    else:
        dfs(num)
    

for _ in range(T):
    n = int(input())
    lst = [0]+list(map(int,input().split()))
    ans = []
    visited = [False] * (n+1)
    
    for i in range(1,n+1):
        #방문 안했으면 dfs돌면서 사이클 체크
        if not visited[i]:
            cycle = []
            dfs(i)
            
    print(n-len(ans))