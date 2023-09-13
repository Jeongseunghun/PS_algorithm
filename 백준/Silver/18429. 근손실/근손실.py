N,K = map(int,input().split())
kit = list(map(int,input().split()))
chk = [0] * N
cnt = 0

def dfs(depth,t):
    global cnt
    if t < 500:
        return
    if depth >= N:
        cnt+=1
        return
    for i in range(N):
        if chk[i] == 0:
            chk[i] = 1
            dfs(depth+1, t+kit[i]-K)
            chk[i] = 0

dfs(0,500)
print(cnt)