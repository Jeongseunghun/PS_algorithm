from collections import deque

def solution(n, m, sx, sy, r, c, k):
    def convert(i):
        if i == 0:
            return 'd'
        elif i == 1:
            return 'l'
        elif i == 2:
            return 'r'
        elif i == 3:
            return 'u'
    
    def man(x1,y1):
        return abs(x1-(r-1)) + abs(y1-(c-1))
    
    #0: 아래(d), 1: 왼(l), 2: 오(r), 3: 위(u)
    dx = [1,0,0,-1]
    dy = [0,-1,1,0]
    
    if man(sx-1,sy-1) > k or (man(sx-1,sy-1) - k) % 2 != 0:
        return 'impossible'
    
    q = deque()
    q.append((sx-1,sy-1,0,''))
    
    while q:
        x,y,cnt,route = q.popleft()
        
        if x == r-1 and y == c-1 and cnt == k:
            return route
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                tmp = cnt+1
                if man(nx,ny) + tmp > k:
                    continue
                q.append((nx,ny,tmp,route+convert(i)))
                break

    return "impossible"