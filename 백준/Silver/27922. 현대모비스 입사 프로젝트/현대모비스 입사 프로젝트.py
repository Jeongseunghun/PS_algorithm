n,k = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]

alst = sorted(lst,key = lambda x : -(x[0]+x[1]))
blst = sorted(lst,key = lambda x : -(x[0]+x[2]))
clst = sorted(lst,key = lambda x : -(x[1]+x[2]))

x = 0
y = 0
z = 0
for i in range(k):
    x += alst[i][0] + alst[i][1]
    y += blst[i][0] + blst[i][2]
    z += clst[i][1] + clst[i][2]

print(max(x,y,z))