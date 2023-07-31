N = int(input())

room = [[0]*(N) for _ in range(N)]

students = []
    
#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(N*N):
    stu = list(map(int,input().split()))
    
    student_num = stu[0]
    love_num = stu[1:]
    
    students.append(stu)
    
    tmp = []
    
    for x in range(N):
        for y in range(N):
            
            if room[x][y] == 0 :
                #좋아하는 학생 수
                like_cnt = 0
                #비어있는 수
                empty_cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<N and 0<=ny<N:
                        if room[nx][ny] in love_num:
                            like_cnt += 1
                    
                        if room[nx][ny] == 0:
                            empty_cnt += 1
                tmp.append((like_cnt,empty_cnt,x,y))
    
    tmp = sorted(tmp, key = lambda x : (-x[0],-x[1],x[2],x[3]))
    
    room[tmp[0][2]][tmp[0][3]] = student_num
    
    
students.sort()

sum = 0
for x in range(N):
    for y in range(N):
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if (room[nx][ny] in students[room[x][y]-1][1:]):
                    cnt+=1
            
        if cnt != 0:
            sum += 10**(cnt-1)
print(sum)