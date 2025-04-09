from itertools import combinations

#거리 구하기
def dis(x1,y1,x2,y2):
    return abs(x2-x1) + abs(y2-y1)

n,k = map(int,input().split())
home = []
for i in range(n):
    x,y = map(int,input().split())
    home.append([x,y])

candi = []
for i in combinations(home,k):
    candi.append(i)

ans = 1e9

for e in candi:
    max_dis = 0
    for [x1,y1] in home:
        min_dis = 1e9
        for [x2,y2] in e:
            min_dis = min(min_dis,dis(x1,y1,x2,y2))
        max_dis = max(max_dis,min_dis)
    ans = min(ans,max_dis)

print(ans)