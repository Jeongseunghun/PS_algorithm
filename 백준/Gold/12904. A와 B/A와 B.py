S = list(input())
T = list(input())

Flag = 0
while len(T)>0:
    if S == T:
        print(1)
        Flag = 1
        break
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T=T[::-1]

if Flag == 0:
    print(0)