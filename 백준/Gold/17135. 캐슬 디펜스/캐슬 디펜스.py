from itertools import combinations
import copy

#궁수 공격
def attack(lst):
    global tmp_enemy, tmp_board

    res = 0
    remove_lst = []
    # 궁수 좌표
    for ax, ay in lst:
        info = []
        # 적 좌표
        for ex, ey in tmp_enemy:
            dis = abs(ex - ax) + abs(ey - ay)
            if dis <= D:
                info.append([dis,ey,ex])
        if info:
            info.sort(key = lambda x : (x[0],x[1]))
            if [info[0][2],info[0][1]] not in remove_lst:
                remove_lst.append([info[0][2],info[0][1]])
    # print("remove_lst", remove_lst)
    # print("적 이전  ", tmp_enemy)
    for x,y in remove_lst:
        tmp_board[x][y] = 0
        tmp_enemy.remove([x,y])
        res += 1
    # print("적 이후  " ,tmp_enemy)
    # print("현재 res" ,res)
    return res

#적 아래로 이동
def move():
    global tmp_enemy,tmp_board
    # print("적 이동 전 ",tmp_enemy)
    
    new_enemy_lst = []
    for ex,ey in tmp_enemy:
        # 한칸씩 이동
        if ex < N - 1:  # 적이 맨 아래에 있는 경우 이동하지 않음
            new_enemy_lst.append([ex + 1, ey])
            
    tmp_enemy = new_enemy_lst
    # print("적 이동 ",tmp_enemy)
    tmp_board = [[0 for _ in range(M)] for _ in range(N)]
    for ex,ey in tmp_enemy:
        tmp_board[ex][ey] = 1

    flag = False
    for i in range(N):
        for j in range(M):
            if tmp_board[i][j] == 1:
                flag = True

    return flag


N,M,D = map(int,input().split())

#격자판
board = [list(map(int,input().split())) for _ in range(N)]

tmp = [[N,i] for i in range(M)]

#모든 3궁수 조합
archer_lst = []
for i in combinations(tmp,3):
    archer_lst.append(i)

#적 위치
enemy_lst = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            enemy_lst.append([i,j])

enemy_lst.sort()

ans = 0

#궁수 후보 lst
for lst in archer_lst:
    # print("궁수 좌표 " , lst)
    tmp_board = copy.deepcopy(board)
    tmp_enemy = copy.deepcopy(enemy_lst)
    res = 0

    #모든 적이 제외될 때까지
    while True:
        #공격 시작
        res += attack(lst)
        # print("공격 후 " ,tmp_board)
        #적 이동
        flag = move()
        if flag == False:
            break
        # print("움직인 후 " ,tmp_board)
        # print("--")
        
    ans = max(res,ans)
    # print("총 ans", ans)
    # print('-----------------------')
print(ans)