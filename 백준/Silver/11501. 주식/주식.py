T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int,input().split()))
    stock.reverse()
    tmp = 0
    bene = 0
    for i in stock:
        if tmp > i:
            bene += (tmp - i)
        elif tmp <= i:
            tmp = i
    print(bene)