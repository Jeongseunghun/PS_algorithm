from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    
    for x,y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    q = deque([1])
    visited[1] = 1
    
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[x] + 1
    
    for i in visited:
        if i == max(visited):
            answer+=1
        
    return answer