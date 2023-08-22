x = input()

length = len(x)
min_num = "999999"
num = ""
used = [False] * length

def dfs(cnt):
    global min_num,num
    if cnt == length:
        if x < num:
            min_num = min(min_num,num)
        return

    for i in range(length):
        if used[i] == True:
            continue
        used[i] = True
        num += x[i]
        dfs(cnt+1)
        used[i] = False
        num = num[:-1]
        

dfs(0)

if min_num == "999999":
    min_num = 0
print(min_num)