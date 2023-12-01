N = input()
num = int(input())
cnt = 0
for i in range(num):
    s = input()
    tmp = s+s
    if N in tmp:
        cnt+=1
print(cnt)
    