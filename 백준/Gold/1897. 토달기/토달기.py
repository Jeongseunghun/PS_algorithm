from collections import deque

def chk(w,t):
    tidx = 0
    widx = 0
    while widx < len(w):
        if w[widx] == t[tidx]:
            tidx += 1
        widx+=1
    if tidx == len(t):
        return True
    else:
        return False
    
    
def bfs(start):
    global res
    visited = []
    q = deque()
    q.append(start)
    visited.append(start)
    
    while q:
        t = q.popleft()
        for w in words:
            if w in visited or len(t)+1 != len(w):
                continue
            if w[1:] == t or t == w[:-1] or chk(w,t):
                q.append(w)
                visited.append(w)
                res = w

d,start = map(str,input().split())
d = int(d)
words = [input() for _ in range(d)]
res = start

bfs(start)
print(res)