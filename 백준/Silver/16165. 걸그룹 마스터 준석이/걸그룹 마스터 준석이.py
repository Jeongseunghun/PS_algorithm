N,M = map(int,input().split())
dict = {}
#멤버이름 : 팀이름
for _ in range(N):
    team = input()
    num = int(input())
    tmp = []
    for _ in range(num):
        tmp.append(input())
    tmp.sort()
    dict[team] = tmp
for _ in range(M):
    name = input()
    flag = int(input())
    if flag == 0:
        for i in dict[name]:
            print(i)
    else:
        for i in dict.keys():
            if name in dict[i]:
                print(i)