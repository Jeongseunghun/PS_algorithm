import sys
input = sys.stdin.readline

N,M = map(int,input().split())
road = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if road[i][j] > road[i][k] + road[k][j]:
                road[i][j] = road[i][k] + road[k][j]

for _ in range(M):
    a,b,c = map(int,input().split())
    if road[a-1][b-1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")
    