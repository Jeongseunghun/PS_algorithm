import sys
input = sys.stdin.readline

M, N = map(int,input().split())
lst = list(map(int,input().split()))

cnt = 0

s = 1
e = max(lst)

while s<=e:
    mid = (s+e) // 2
    total = 0
    for i in lst:
        total += i // mid
    if total >= M:
        s = mid + 1
        cnt = mid
    else:
        e = mid - 1

print(cnt)
    