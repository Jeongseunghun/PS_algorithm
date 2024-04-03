from collections import deque

gear = {}
for i in range(1,5):
    gear[i] = deque((map(int,input())))
T = int(input())

def rotate_right(gear_num,rot):
    if gear_num > 4 or gear[gear_num-1][2] == gear[gear_num][6]:
        return
    if gear[gear_num-1][2] != gear[gear_num][6]:
        rotate_right(gear_num+1,-rot)
        gear[gear_num].rotate(rot)
        
def rotate_left(gear_num,rot):
    if gear_num < 1 or gear[gear_num][2] == gear[gear_num+1][6]:
        return
    if gear[gear_num][2] != gear[gear_num+1][6]:
        rotate_left(gear_num-1,-rot)
        gear[gear_num].rotate(rot)


for _ in range(T):
    gear_num, rot = map(int,input().split())
    #입력 톱니 회전
    rotate_right(gear_num+1,-rot)
    rotate_left(gear_num-1,-rot)
    gear[gear_num].rotate(rot)


#점수 판별
cnt = 0  
for i in range(4):
    if gear[i+1][0] == 1:
        if i == 0:
            cnt+=1
        elif i == 1:
            cnt+=2
        elif i == 2:
            cnt+=4
        elif i == 3:
            cnt+=8

print(cnt)