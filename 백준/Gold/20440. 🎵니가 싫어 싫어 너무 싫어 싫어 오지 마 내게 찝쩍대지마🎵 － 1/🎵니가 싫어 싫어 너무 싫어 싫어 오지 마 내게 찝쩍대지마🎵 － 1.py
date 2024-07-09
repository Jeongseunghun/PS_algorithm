from collections import defaultdict

N = int(input())
lst = defaultdict(int)
for _ in range(N):
    s,e = map(int,input().split())
    lst[s] += 1
    lst[e] -= 1

max_time = 0
cnt = 0
em,xm = 0,0
flag = False
for i in sorted(lst.keys()):
    cnt += lst[i]
    if cnt > max_time:
        max_time = cnt
        em = i
        flag = True
    elif cnt < max_time and cnt - lst[i] == max_time and flag:
        xm = i
        flag = False
print(max_time)
print(em,xm)