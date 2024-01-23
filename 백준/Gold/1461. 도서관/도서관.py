N,M = map(int,input().split())
loc = list(map(int,input().split()))

#음수 거리
m = []
#양수 거리
p = []

max_dis = 0
for i in loc:
    #최대 거리
    max_dis = max(abs(i),max_dis)
    if i > 0:
        p.append(i)
    else:
        m.append(i)
        
p.sort(reverse=True)
m.sort()

res = abs(max_dis)
for i in range(0,len(p),M):
    if p[i] != max_dis:
        res += abs(p[i])* 2

for i in range(0,len(m),M):
    if abs(m[i]) != max_dis:
        res += abs(m[i]) * 2
    
print(res)