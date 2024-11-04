import sys

N = int(input())
lst = list(map(int,input().split()))
lst.sort()
val = sys.maxsize

for i in range(N-2):
    s = i+1
    e = N-1
    while s < e:
        tmp = lst[i] + lst[s] + lst[e]
        if abs(tmp) < val:
            val = abs(tmp)
            res = [lst[i],lst[s],lst[e]]
        if tmp < 0:
            s += 1
        elif tmp > 0 :
            e -= 1
        else:
            break

print(res[0],res[1],res[2])