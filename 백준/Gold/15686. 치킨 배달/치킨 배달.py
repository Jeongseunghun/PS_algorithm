from itertools import combinations

N,M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append([i,j])
        if city[i][j] == 1:
            house.append([i,j])

res = 999999

for c in combinations(chicken,M):
    tmp = 0
    for i in house:
        min_d = 99
        for j in range(len(c)):
            min_d = min(min_d, abs(c[j][0]-i[0]) + abs(c[j][1]-i[1]))
        tmp += min_d
    res = min(res,tmp)

print(res)          
            
