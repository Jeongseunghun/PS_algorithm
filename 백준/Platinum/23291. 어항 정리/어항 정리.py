from collections import deque

N,K = map(int,input().split())
fishbowl = [deque(list(map(int,input().split())))]

#물고기 추가
def add_fish(fishbowl):
    min_val = min(fishbowl[0])
    for i in range(len(fishbowl[0])):
        if min_val == fishbowl[0][i]:
            fishbowl[0][i] += 1

#어항 쌓기
def build_bowl(fishbowl):
    #어항 첫번째를 빼고 두번째에 추가
    val = fishbowl[0].popleft()
    fishbowl.append(deque([val]))
    
def rotate_90(block):
    tmp = [[0] * len(block) for _ in range(len(block[0]))]
    for i in range(len(block[0])):
        for j in range(len(block)):
            tmp[i][j] = block[j][len(block[0])-1-i]
    return tmp
    
#어항 공중 부양 후 90도 회전 쌓기
def move_bowl(arr):
    while True:
        #어항 높이(len(arr)) > 바닥에 있는 개수(len(arr[0])) - 맨 위에 있는 개수(len(arr[-1]))면 멈추기
        if len(arr) > len(arr[0]) - len(arr[-1]):
            break
        blocks = []
        
        for i in range(len(arr)):
            tmp_q = deque()
            #맨 위의 어항 개수만큼 빼서 tmp_q에 집어넣기
            for _ in range(len(arr[-1])):
                tmp_q.append(arr[i].popleft())
                
            blocks.append(tmp_q)
        
        arr = [arr[0]]
        rotate = rotate_90(blocks)
        #돌린 어항 쌓아주기
        for i in rotate:
            arr.append(deque(i))

    return arr

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#물고기 조절
def adjust_fish(arr):
    board = [[0] * len(arr[x]) for x in range(len(arr))]
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(arr) and 0 <= ny < len(arr[nx]):
                    if arr[x][y] > arr[nx][ny]:
                        val = (arr[x][y] - arr[nx][ny]) // 5
                        if val >= 1:
                            board[x][y] -= val
                            board[nx][ny] += val
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] += board[i][j]

#어항 일렬 정렬
def flatten_bowl(arr):
    tmp = deque()
    #어항 박스 모양 세로로 이어붙이기
    for i in range(len(arr[-1])):
        for j in range(len(arr)):
            tmp.append(arr[j][i])
    #어항 나머지 이어붙이기
    for i in range(len(arr[-1]),len(arr[0])):
        tmp.append(arr[0][i])
    
    return [tmp] 
    
def rotate_180(arr):
    tmp = []
    for i in reversed(range(len(arr))):
        arr[i].reverse()
        tmp.append(arr[i])
    
    return tmp

#어항 쌓기(공중부양 다시)
def move_bowl2(arr):
    #왼쪽 N//2개를 tmp에 추가
    tmp = deque()
    for i in range(N//2):
        tmp.append(arr[0].popleft())
    #tmp 180도 회전
    rotate = rotate_180([tmp])
    #arr에 붙이기
    arr += rotate
    
    left = []
    #2번 반복
    for i in range(2):
        d = deque()
        #왼쪽 N//4개를 d에 추가
        for j in range(N//4):
            d.append(arr[i].popleft())
        left.append(d)
    rotated = rotate_180(left)
    arr += rotated
    
#어항 정리 횟수
cnt = 0
while True:
    if max(fishbowl[0]) - min(fishbowl[0]) <= K:
        print(cnt)
        break
    cnt += 1
    add_fish(fishbowl)
    build_bowl(fishbowl)
    fishbowl = move_bowl(fishbowl)
    adjust_fish(fishbowl)
    fishbowl = flatten_bowl(fishbowl)
    move_bowl2(fishbowl)
    adjust_fish(fishbowl)
    fishbowl = flatten_bowl(fishbowl)