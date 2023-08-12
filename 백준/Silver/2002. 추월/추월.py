N = int(input())
dae = {}
young = []
#들어가는 순
for i in range(N):
    dae[input()] = i

#나오는 순
for i in range(N):
    young.append(input())

ans = 0

for i in range(N-1):
    now = dae[young[i]]
    for j in range(i+1,N):
        next = dae[young[j]]
        if next < now:
            ans+=1
            break

print(ans)