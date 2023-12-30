from collections import deque

n = int(input())
a = []
for _ in range(n):
    word = deque(input())
    Flag = False
    for i in a:
        if ''.join(list(word)) in i:
            Flag = True
            break
    if Flag:
        continue
    lst = []
    for i in range(len(word)):
        word.rotate(1)
        lst.append(''.join(list(word)))
    a.append(lst)
    

print(len(a))
        