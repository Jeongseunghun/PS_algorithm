from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    
    dis = [-1 for _ in range(n+1)]
    dis[destination] = 0
    
    lst = [[] for _ in range(n+1)]
    
    q = deque()
    q.append(destination)

    for x,y in roads:
        lst[x].append(y)
        lst[y].append(x)
        
    while q:
        x = q.popleft()
        for i in lst[x]:
            if dis[i] == -1:
                q.append(i)
                dis[i] = dis[x] + 1
    
    for i in sources:
        answer.append(dis[i])

    return answer