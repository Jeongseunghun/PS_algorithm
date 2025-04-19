from itertools import combinations

def solution(places):
    answer = []
    for place in places:
        person = []
        wall = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    person.append([i,j])
                elif place[i][j] == 'X':
                    wall.append([i,j])
        
        flag = True
        for r,c in combinations(person,2):
            dis = abs(r[0]-c[0]) + abs(r[1]-c[1])
            
            if dis <= 2:
                #가로 일렬일 때 열 비교
                if r[0] == c[0] and place[r[0]][min(r[1],c[1])+1] != 'X':
                    flag = False
                #세로 일렬일 때 행 비교
                if r[1] == c[1] and place[min(r[0],c[0])+1][r[1]] != 'X':
                    flag = False
                #정대각선일 때 비교
                if r[1] < c[1] and r[0] < c[0] and not (place[r[0]+1][r[1]] == 'X' and place[r[0]][r[1]+1] == 'X'):
                    flag = False
                if r[1] > c[1] and r[0] > c[0] and not (place[c[0]+1][c[1]] == 'X' and place[c[0]][c[1]+1] == 'X'):
                    flag = False
                #역대각선일 때 비교
                if r[1] < c[1] and r[0] > c[0] and not (place[r[0]-1][r[1]] == 'X' and place[r[0]][r[1]+1] == 'X'):
                    flag = False
                if r[1] > c[1] and r[0] < c[0] and not (place[r[0]+1][r[1]] == 'X' and place[r[0]][r[1]-1] == 'X'):
                    flag = False
            
        if flag:
            answer.append(1)
        else:
            answer.append(0)
                
    return answer