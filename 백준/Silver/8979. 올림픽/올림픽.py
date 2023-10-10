N,K = map(int,input().split())
country = [list(map(int,input().split())) for _ in range(N)]
country = sorted(country,key = lambda x: (-x[1],-x[2],-x[3]))

idx = 0

for i in range(N):
    if country[i][0] == K:
        idx = i

for i in range(N):
    if country[idx][1:] == country[i][1:]:
        print(i+1)
        break