n= int(input())
a,b = map(int,input().split())
m = int(input())

chon = [[] for _ in range(n+1)]
visited = [False] * (n+1)
res =[]
for i in range(m):
    x,y = map(int,input().split())
    chon[x].append(y)
    chon[y].append(x)


def dfs(a, num):
    num+=1
    visited[a] = True
    
    if a == b:
        res.append(num)
    
    for i in chon[a]:
        if not visited[i]:
            dfs(i,num)
        

dfs(a,0)

if len(res) == 0:
    print(-1)
else:
    print(res[0]-1)
   