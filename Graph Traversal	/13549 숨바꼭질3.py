from collections import deque

N,K = map(int,input().split())

max_size = 100001
visited = [-1] * max_size
visited[N] = 0

q = deque()
q.append(N)

while q:
    cur = q.popleft()
    if cur == K:
        print(visited[K])
        break
    for next in [cur-1,cur+1,cur*2]:
        if 0 <= next < max_size:
            if visited[next] == -1 or visited[next] >= visited[cur] + 1:
                if next == cur*2:
                    visited[next] = visited[cur]
                else:
                    visited[next] = visited[cur] + 1
                
                q.append(next)
            


            
