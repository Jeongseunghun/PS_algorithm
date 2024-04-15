N,H = map(int,input().split())

l = [0] * H

for i in range(N):
    h = int(input())
    if i % 2 == 0:
        l[H-h] += 1
    else:
        l[0] += 1
        l[h] -= 1

for i in range(1,H):
    l[i] += l[i-1]

cnt = 0
low = min(l)
for i in l:
    if i == low:
        cnt+=1

print(low,cnt)