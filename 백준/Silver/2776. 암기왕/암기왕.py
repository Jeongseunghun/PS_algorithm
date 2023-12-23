T = int(input())
for _ in range(T):
    N = int(input())
    lst = set(map(int,input().split()))
    M = int(input())
    note = list(map(int,input().split()))
    for i in note:
        if i in lst:
            print(1)
        else:
            print(0)
    