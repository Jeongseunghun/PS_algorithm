from collections import deque

N,M = map(int,input().split())
blocks = [list(map(int,input().split())) for _ in range(N)]

#블록 그룹 찾기
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j,k,visited):
    tmp_blocks= []
    rainbow = []
    q = deque()
    cnt = 1
    rainbow_cnt = 0
    q.append((i,j))
    visited[i][j] = 1
    tmp_blocks.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                #색 동일, 검정X
                if (blocks[nx][ny] == k or blocks[nx][ny] == 0):
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    tmp_blocks.append((nx,ny))
                    cnt+=1
                    if blocks[nx][ny] == 0:
                        rainbow.append((nx,ny))
                        rainbow_cnt += 1
      
    for x,y in rainbow:
        visited[x][y] = 0
        
    return [cnt,rainbow_cnt,tmp_blocks]

#큰 블록 그룹 찾기, 기준 블록 선정
def biggest():
    visited = [[0 for _ in range(N)] for _ in range(N)]
    tmp_block = []
    for i in range(N):
        for j in range(N):
            if blocks[i][j] > 0 and visited[i][j] == 0:
                tmp = bfs(i,j,blocks[i][j],visited)
                if tmp[0] >= 2:
                    tmp_block.append(tmp)
                    
    tmp_block.sort(reverse=True)

    return tmp_block   

#큰 블록 그룹 제거 후 점수 계산
def score_cal(lst):
    global score
    
    for x,y in lst[2]:
        #빈칸은 -2
        blocks[x][y] = -2
         
    score += lst[0]**2

    return score
    
#중력 작용
def gravity():
    global blocks

    for i in range(N-2,-1,-1):
        for j in range(N):
            if blocks[i][j] > -1:
                r = i
                while True:
                    if 0 <= r+1 < N and blocks[r+1][j] == -2:
                        blocks[r+1][j] = blocks[r][j]
                        blocks[r][j] = -2
                        r+=1
                    else:
                        break

#반시계 회전
def rotate():
    global blocks

    tmp = [[] for _ in range(N)]
    for i in range(N-1,-1,-1):
        for j in range(N):
            tmp[abs(i-N)-1].append(blocks[j][i])

    blocks = tmp
    

score = 0
while True:
    tmp_block = biggest()
    if len(tmp_block) == 0:
        break
    score = score_cal(tmp_block[0])
    gravity()
    rotate()
    gravity()
print(score)