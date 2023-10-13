from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    lst = input()
    q = deque(lst[1:-1].split(","))
    if n == 0:
        q = deque()
    flag = True
    r = 0
    #정렬
    for i in p:
        if i == 'R':
            r+=1
        elif i == 'D':
            if len(q) == 0:
                print('error')
                flag = False
                break
            else:
                if r % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
    if flag == False:
        continue
    else:
        if r%2 == 0:
            print("[" + ','.join(q) + ']')
        else:
            q.reverse()
            print("[" + ','.join(q) + ']')
