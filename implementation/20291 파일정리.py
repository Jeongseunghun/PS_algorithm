n = int(input())

dic = {}

for i in range(n):
    a = list(input().split("."))[1]
    if a in dic:
        dic[a] +=1
    elif a not in dic:
        dic[a] = 1

res = list(dic)
res.sort()

for i in res:
    print(i, dic[i])


    



    