N = int(input())

graph = [[0 for _ in range(101)] for _ in range(101)]


#방향(우상좌하)
dx = [1,0,-1,0]
dy = [0,-1,0,1]


for _ in range(N):
    x,y,d,g = map(int,input().split())
    graph[x][y] = 1
    
    route = [d]
    for i in range(g):
        tmp = []
        for j in range(len(route)):
            tmp.append((route[-j-1]+1) % 4)
        
        route.extend(tmp)
    
    for i in route:
        nx = x + dx[i]
        ny = y + dy[i]
        graph[nx][ny] = 1
        x = nx
        y = ny

ans = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
            ans+=1

print(ans)     
            
