from itertools import permutations

N = int(input())
item = ['1','2','3','4','5','6','7','8','9']

all = list(permutations(item,3))

for _ in range(N):
    predict,s,b= map(int,input().split())
    predict = list(str(predict))
    idx = 0
    for i in range(len(all)):
        strike = 0
        ball = 0
        i -= idx;
        for j in range(3):
            if predict[j] == all[i][j]:
                strike += 1
            elif predict[j] in all[i]:
                ball +=1
        
        if strike != s or ball != b:
            all.remove(all[i])
            idx +=1

print(len(all))
                
    
    



