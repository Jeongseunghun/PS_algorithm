from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    half = sum1+sum2 //2
    
    for i in range(300000):
        if sum1 == sum2:
            return i
        if sum1 > sum2:
            a=queue1.popleft()
            queue2.append(a)
            sum1-=a
            sum2+=a
        else:
            a=queue2.popleft()
            queue1.append(a)
            sum1+=a
            sum2-=a
            
            
    return -1
    