N = int(input())
cost = []
for i in range(N):
    tmp = list(map(int,input().split()))
    cost.append(tmp)
    
cost.sort()

total = [0] * N
for i in range(N):
    for j in range(i,N):
        profit = cost[i][0]-cost[j][1]
        if profit > 0:
            total[i] += profit

res = []
for i in range(N):
    if total[i] == max(total):
        res.append(cost[i][0])

if sum(total) == 0:
    print(0)
else:
    print(min(res))