lst = list(map(int,input().split()))

if lst[0] == 1:
    if [i for i in range(1,9)] == lst:
        print('ascending')
    else:
        print('mixed')
elif lst[0] == 8:
    if [i for i in range(8,0,-1)] == lst:
        print('descending')
    else:
        print('mixed')
else:
    print('mixed')