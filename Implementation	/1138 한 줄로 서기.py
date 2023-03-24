N = int(input())
lst = list(map(int,input().split()))

ans = [0 for _ in range(N)]

for i in range(N):
    cnt = 0
    for j in range(N):
        if lst[i] == cnt and ans[j] == 0:
            ans[j] = i+1
            break
        elif ans[j] == 0:
            cnt+=1
    

print(*ans)
    