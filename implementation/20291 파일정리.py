
n=int(input())
dic = {}

for i in range(n):
    a= input().split(".")[1]
    if a not in dic:
        dic[a] = 1
    else:
        dic[a] +=1

item = list(dic.keys())
item.sort()

for i in item:
    print(i,dic[i])



    