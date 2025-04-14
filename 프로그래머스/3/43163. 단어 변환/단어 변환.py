from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = []
    
    def convert(w1,w2):
        cnt = 0
        for a,b in zip(w1,w2):
            if a != b:
                cnt+=1
        if cnt == 1:
            return True
    
    q = deque()
    q.append([begin,0])
    
    while q:
        word,cnt = q.popleft()
        if word == target:
            return cnt
        
        for w in words:
            if w not in visited and convert(word,w):
                visited.append(w)
                q.append([w,cnt+1])
    
    return 0