N = int(input())
tree = list(map(int,input().split()))
r_node = int(input())

def dfs(v):
    tree[v] = -2
    for i in range(N):
        if tree[i] == v:
            dfs(i)


cnt = 0
dfs(r_node)

for i in range(N):
    if tree[i] != -2 and i not in tree:
        cnt+=1

print(cnt)