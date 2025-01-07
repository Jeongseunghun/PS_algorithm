from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([-numbers[0],0])
    q.append([numbers[0],0])
    
    while q:
        x,cnt = q.popleft()
        cnt+=1
        if cnt == len(numbers) and x == target:
            answer+=1
        if cnt < len(numbers):
            q.append([x+numbers[cnt],cnt])
            q.append([x-numbers[cnt],cnt])
        
    return answer