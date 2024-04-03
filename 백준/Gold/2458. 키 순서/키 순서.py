N,M = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(M)]

chk = [[] for _ in range(N+1)]
for x,y in lst:
    chk[x].append(y)
# 
# print(chk)

def dfs(num):
    global cnt,tmp

    if chk[num]:
        for i in chk[num]:
            if visited[i] == 0:
                l[tmp].append(i)
                l[i].append(tmp)
                visited[i] = 1
                dfs(i)
    return

ans = 0
l = [[] for _ in range(N+1)]

for num in range(1,N+1):
    tmp = num
    visited = [0 for _ in range(N+1)]
    visited[num] = 1
    l[num].append(num)
    dfs(num)

for i in l:
    if len(i) == N:
        ans+=1
#
# print(l)
# print("-----")
print(ans)