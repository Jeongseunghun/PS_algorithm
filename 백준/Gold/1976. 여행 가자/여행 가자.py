def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

N = int(input())
M = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
city = list(map(int,input().split()))
parents = [i for i in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            union(i,j)
parents = [-1] + parents
s = parents[city[0]]
flag = True
for i in range(1,M):
    if parents[city[i]] != s:
        print("NO")
        flag = False
        break
    
if flag:
    print("YES")