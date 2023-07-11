n = int(input())
stack = []
tmp = []
flag = 0
cur = 1
for i in range(n):
    n = int(input())
    while cur <= n:
        stack.append(cur)
        tmp.append("+")
        cur+=1
    if stack[-1] == n:
        stack.pop()
        tmp.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in tmp:
        print(i)
            