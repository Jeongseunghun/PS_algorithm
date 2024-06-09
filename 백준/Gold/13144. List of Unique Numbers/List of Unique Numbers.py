N = int(input())
lst = list(map(int,input().split()))

l = 0
r = 0

visited = [0] * 100001
cnt = 0
while r < N and l <= r:
    if visited[lst[r]] == 0:
        visited[lst[r]] = 1
        cnt += r - l + 1
        r+=1
    else:
        visited[lst[l]] = 0
        l += 1

print(cnt)