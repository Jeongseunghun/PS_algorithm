from collections import deque


def bfs():
    q = deque()
    q.append((hx,hy))
    while q:
        x,y = q.popleft()
        if abs(x-fx) + abs(y-fy) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                nx,ny = store[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    visited[i] = 1
                    q.append((nx,ny))
                    
    print('sad')
    return
            

t = int(input())
for i in range(t):
    n = int(input())
    hx, hy = map(int,input().split())
    store = []
    for j in range(n):
        x,y = map(int,input().split())
        store.append([x,y])
    fx,fy = map(int,input().split())
    visited = [0 for i in range((n+1))]
    bfs()


        
        