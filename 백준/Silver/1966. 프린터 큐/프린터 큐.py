from collections import deque

T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    doc = deque(list(map(int,input().split())))
    cnt = 0
    while doc:
        fast = max(doc)
        front = doc.popleft()
        M -= 1
        
        if fast == front:
            cnt+=1
            if M<0:
                print(cnt)
                break
        else:
            doc.append(front)
            if M < 0:
                M = len(doc) - 1
    