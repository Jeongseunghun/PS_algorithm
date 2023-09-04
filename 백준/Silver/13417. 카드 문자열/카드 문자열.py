from collections import deque
T = int(input())

for tc in range(T):
    N = int(input())
    alpha = list(map(str,input().split()))
    tmp = deque(alpha[0])
    for i in range(1,len(alpha)):
        if tmp[0] >= alpha[i]:
            tmp.appendleft(alpha[i])
        else:
            tmp.append(alpha[i])

    print(''.join(tmp))