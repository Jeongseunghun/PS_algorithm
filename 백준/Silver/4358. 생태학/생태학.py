import sys

dic = {}
total = 0
while True:
    tree = sys.stdin.readline().rstrip()
    if tree == "":
        tree_len = len(dic)
        break
    total+=1
    if tree in dic:
        dic[tree] +=1
    elif tree not in dic:
        dic[tree] = 1

dic = dict(sorted(dic.items()))

for i in dic:
    a = dic[i]
    ans = (a/total * 100)
    
    print("%s %.4f" %(i,ans))