import copy

N,M = map(int,input().split())
space = []

#상우하좌
dx = [-1,0,1,0]
dy = [0,-1,0,1]

#1,2,3,4,5 방향
mode = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[0,3]],
    [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
    [[0,1,2,3]]
]

cctv=[]

for i in range(N):
    data = list(map(int,input().split()))
    space.append(data)
    for j in range(M):
        if data[j] in [1,2,3,4,5]:
            cctv.append([data[j],i,j])


#감시
def fill(space,mode,x,y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx>= N or ny>=M :
                break
            if space[nx][ny] == 6:
                break
            elif space[nx][ny] == 0:
                space[nx][ny] = -1

min_v = int(1e9)

#탐색
def dfs(depth, space):
    global min_v
    if depth == len(cctv):
        cnt = 0
        for i in range(N):
            cnt += space[i].count(0)
        min_v = min(min_v,cnt)
        return
    
    tmp = copy.deepcopy(space)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(tmp,i,x,y)
        dfs(depth+1,tmp)
        tmp = copy.deepcopy(space)
        
    
dfs(0,space)
print(min_v)   