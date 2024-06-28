N = int(input())
lst = []
for _ in range(N):
    d,w = map(int,input().split())
    lst.append((d,w))

ans = 0
visited = [False] * 1000
lst.sort(key = lambda x : x[1],reverse = True)
for i in range(N):
    a = lst[i][0]
    b = lst[i][1]
    for i in range(a-1,-1,-1):
        if visited[i] == False:
            visited[i] = True
            ans += b
            break

print(ans)
