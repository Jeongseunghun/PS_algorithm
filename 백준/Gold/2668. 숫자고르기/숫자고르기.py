N = int(input())
#인덱스 1부터 매칭
two = [0]
for i in range(N):
    num = int(input())
    two.append(num)

ans = []
def dfs(v,start):
    visited[v] = True
    w = two[v]
    if not visited[w]:
        dfs(w,start)
    elif visited[w] and w == start:
        ans.append(w)
        
for i in range(1,N+1):
    visited = [False] * (N+1)
    dfs(i,i)
        
print(len(ans))
ans.sort()
for i in ans:
    print(i)
    