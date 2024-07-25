from itertools import permutations

T = int(input())
for _ in range(T):
    k = int(input())
    lst = []
    for _ in range(k):
        lst.append(input())
    tmp = []
    for x,y in permutations(lst,2):
        tmp.append(x+y)
    
    flag = False
    for i in tmp:
        if i == i[::-1]:
            flag= True
            print(i)
            break
    if flag == False:
        print(0)
            
                