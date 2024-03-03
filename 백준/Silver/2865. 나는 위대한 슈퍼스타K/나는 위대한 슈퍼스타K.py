N,M,K = map(int,input().split())

contest = []
for i in range(M):
    tmp = list(map(float,input().split()))
    for j in range(0,N*2,2):
        lst = []
        lst.append(i)
        lst.append(int(tmp[j]))
        lst.append(float(tmp[j+1]))
        contest.append(lst)

contest.sort(key = lambda x : -x[2])

ans = [0] * N
cnt = 0
for g,i,s in contest:
    if ans[i-1] == 0:
        ans[i-1] = s
        cnt +=1
    if cnt == K:
        print(round(sum(ans),2))
        break