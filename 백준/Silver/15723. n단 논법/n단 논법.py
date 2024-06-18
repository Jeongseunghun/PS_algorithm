def dfs(a,b):
    if a == b:
        return True
    for i in lst[a]:
        visited[i] = True
        if dfs(i,b):
            return True

N = int(input())
lst = [[] for _ in range(26)]
for _ in range(N):
    x,i,y = map(str,input().split())
    lst[ord(x)-97].append(ord(y) - 97)

M = int(input())
for _ in range(M):
    x,i,y = map(str,input().split())
    visited = [0 for _ in range(26)]
    ans = dfs(ord(x)-97,ord(y)-97)
    if ans:
        print("T")
    else:
        print("F")