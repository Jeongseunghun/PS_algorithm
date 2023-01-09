from itertools import combinations

N,M= map(int,input().split())
no = [[False for _ in range(N)] for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    no[a-1][b-1] = True
    no[b-1][a-1] = True


res = 0

for i in combinations(range(N),3):
    if no[i[0]][i[1]] or no[i[0]][i[2]] or no[i[1]][i[2]]:
        continue
    res+=1

print(res)
    
    
    