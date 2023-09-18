N = int(input())
#학생번호
board = [[0 for _ in range(N)] for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

#학생번호,좋아하는 학생리스트
def move(stu,love_lst):
    # 좋아하는 학생 수, 빈칸 수, x, y 저장
    tmp_lst = []
    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                #좋아하는 학생수
                love_cnt = 0
                #비어있는 칸
                empty_cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] in love_lst:
                            love_cnt+=1
                        if board[nx][ny] == 0:
                            empty_cnt+=1
                tmp_lst.append((love_cnt,empty_cnt,x,y))

    tmp_lst = sorted(tmp_lst,key = lambda x: (-x[0],-x[1],x[2],x[3]))

    l_cnt,e_cnt,x,y = tmp_lst[0]
    board[x][y] = stu


def survey(sum_lst):
    sum = 0
    for k in sum_lst:
        for x in range(N):
            for y in range(N):
                if board[x][y] == k[0]:
                    cnt = 0
                    for i in range(4):
                        nx = x+dx[i]
                        ny = y+dy[i]
                        if 0 <= nx < N and 0 <= ny < N:
                            if board[nx][ny] in k[1]:
                                cnt += 1
                    if cnt > 0:
                        sum+= 10**(cnt-1)

    return sum


sum_lst = []
for i in range(N**2):
    stu,num1,num2,num3,num4 = map(int,input().split())
    #좋아하는 학생 리스트 저장
    love_lst = [num1,num2,num3,num4]
    move(stu,love_lst)
    sum_lst.append((stu,love_lst))

print(survey(sum_lst))